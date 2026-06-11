/**
 * Dependency Graph System for Seed Orchestration
 * Manages explicit dependency declarations, validates graphs, and provides topological ordering
 * @module dependency-graph
 */

import { logger } from "./logger";

import type {
  DependencyGraph,
  DependencyGraphNode,
  DependencyValidationError,
  DependencyValidationResult,
  SeederMetadata,
} from "./types";

/**
 * Builds and validates dependency graphs for seeders
 * Detects circular dependencies and topologically sorts entities
 */
export class DependencyGraphBuilder {
  private seeders: Map<string, SeederMetadata>;

  constructor(seeders: Map<string, SeederMetadata>) {
    this.seeders = seeders;
  }

  /**
   * Build dependency graph from seeder metadata
   * Returns graph and any validation errors
   */
  build(): { errors: DependencyValidationError[]; graph: DependencyGraph | null } {
    const errors: DependencyValidationError[] = [];

    // Validate all dependencies exist
    for (const [entityName, metadata] of this.seeders) {
      for (const dependency of metadata.dependencies) {
        if (!this.seeders.has(dependency)) {
          errors.push({
            type: "missing-dependency",
            entity: entityName,
            message: `Entity "${entityName}" depends on "${dependency}" which is not registered`,
            affectedEntities: [entityName],
          });
        }
      }
    }

    if (errors.length > 0) {
      return { graph: null, errors };
    }

    // Build nodes and edges
    const nodes = new Map<string, DependencyGraphNode>();
    const edges = new Map<string, Set<string>>();

    for (const [entityName, metadata] of this.seeders) {
      nodes.set(entityName, {
        metadata,
        dependents: [],
      });
      edges.set(entityName, new Set(metadata.dependencies));
    }

    // Build reverse edges (dependents)
    for (const [entityName, dependencies] of edges) {
      for (const dep of dependencies) {
        const depNode = nodes.get(dep);
        if (depNode) {
          depNode.dependents.push(entityName);
        }
      }
    }

    // Check for circular dependencies
    const circularErrors = this.detectCycles(edges);
    if (circularErrors.length > 0) {
      return { graph: null, errors: circularErrors };
    }

    // Topological sort
    const ordered = this.topologicalSort(edges);

    const graph: DependencyGraph = {
      nodes,
      edges,
      ordered,
    };

    return { graph, errors: [] };
  }

  /**
   * Validate dependency graph for issues
   */
  validate(graph: DependencyGraph): DependencyValidationResult {
    const errors: DependencyValidationError[] = [];
    const warnings: string[] = [];

    // Check for orphaned nodes
    for (const entityName of graph.ordered) {
      const node = graph.nodes.get(entityName);
      if (!node) {
        errors.push({
          type: "invalid-metadata",
          entity: entityName,
          message: `Entity "${entityName}" in sorted order has no metadata`,
        });
      }
    }

    // Check for missing nodes in sorted order
    if (graph.ordered.length !== graph.nodes.size) {
      warnings.push(`Graph has ${graph.nodes.size} nodes but ${graph.ordered.length} are sorted`);
    }

    // Warn about optional-only dependencies
    for (const [entityName, node] of graph.nodes) {
      if (node.metadata.isOptional && node.dependents.length > 0) {
        warnings.push(`Optional entity "${entityName}" has ${node.dependents.length} dependents`);
      }
    }

    return {
      valid: errors.length === 0,
      errors,
      warnings,
    };
  }

  /**
   * Detect circular dependencies using DFS
   */
  private detectCycles(edges: Map<string, Set<string>>): DependencyValidationError[] {
    const visited = new Set<string>();
    const rec = new Set<string>();
    const errors: DependencyValidationError[] = [];

    const dfs = (node: string, path: string[]): void => {
      visited.add(node);
      rec.add(node);
      path.push(node);

      const dependencies = edges.get(node) || new Set();
      for (const dep of dependencies) {
        if (!visited.has(dep)) {
          dfs(dep, path);
        } else if (rec.has(dep)) {
          // Found cycle
          const cycleStart = path.indexOf(dep);
          const cycle = path.slice(cycleStart);
          cycle.push(dep);

          errors.push({
            type: "circular",
            entity: node,
            message: `Circular dependency detected: ${cycle.join(" -> ")}`,
            affectedEntities: cycle,
          });
        }
      }

      rec.delete(node);
      path.pop();
    };

    for (const node of edges.keys()) {
      if (!visited.has(node)) {
        dfs(node, []);
      }
    }

    return errors;
  }

  /**
   * Topologically sort entities using Kahn's algorithm
   * Respects priority for entities at same dependency level
   */
  private topologicalSort(edges: Map<string, Set<string>>): string[] {
    // Calculate in-degree: number of dependencies for each entity
    // Entities with 0 dependencies should be processed first
    const inDegree = new Map<string, number>();
    for (const [entity, dependencies] of edges) {
      inDegree.set(entity, dependencies.size);
    }

    // Build reverse edges (dependents) for efficient lookup
    const dependents = new Map<string, Set<string>>();
    for (const [entity] of edges) {
      dependents.set(entity, new Set());
    }
    for (const [entity, dependencies] of edges) {
      for (const dep of dependencies) {
        const depDependents = dependents.get(dep);
        if (depDependents) {
          depDependents.add(entity);
        }
      }
    }

    // Start with nodes that have no dependencies (in-degree = 0)
    const queue: string[] = [];
    const metadata = new Map(this.seeders);

    for (const [entity, degree] of inDegree) {
      if (degree === 0) {
        queue.push(entity);
      }
    }

    // Sort by priority (lower priority number = higher priority)
    queue.sort((a, b) => {
      const aPriority = metadata.get(a)?.priority ?? 5;
      const bPriority = metadata.get(b)?.priority ?? 5;
      return aPriority - bPriority;
    });

    const sorted: string[] = [];

    while (queue.length > 0) {
      // Use priority queue: take highest priority (lowest number)
      queue.sort((a, b) => {
        const aPriority = metadata.get(a)?.priority ?? 5;
        const bPriority = metadata.get(b)?.priority ?? 5;
        return aPriority - bPriority;
      });

      const current = queue.shift();
      if (!current) break;

      sorted.push(current);

      // Process all entities that depended on current (using dependents map)
      const currentDependents = dependents.get(current) || new Set();
      for (const dependent of currentDependents) {
        // Decrement in-degree
        const newDegree = (inDegree.get(dependent) || 0) - 1;
        inDegree.set(dependent, newDegree);

        // If in-degree is 0, add to queue
        if (newDegree === 0) {
          queue.push(dependent);
        }
      }
    }

    // Verify all nodes were processed
    if (sorted.length !== edges.size) {
      logger.warn(`Topological sort incomplete: ${sorted.length}/${edges.size} entities sorted`);
    }

    return sorted;
  }

  /**
   * Generate Mermaid diagram for dependency visualization
   */
  generateMermaidDiagram(graph: DependencyGraph): string {
    let mermaid = "graph TD\n";

    // Add nodes with descriptions
    for (const [entityName, node] of graph.nodes) {
      const desc = node.metadata.description.split("\n")[0];
      const sanitized = entityName.charAt(0).toUpperCase() + entityName.slice(1);
      mermaid += `  ${entityName}["${sanitized}<br/>${desc}"]\n`;
    }

    // Add edges (dependencies)
    for (const [entityName, dependencies] of graph.edges) {
      for (const dep of dependencies) {
        mermaid += `  ${entityName} --> ${dep}\n`;
      }
    }

    // Add legend
    mermaid += "\n  style Legend fill:#f9f,stroke:#333,stroke-width:2px\n";

    return mermaid;
  }

  /**
   * Generate ASCII graph representation
   */
  generateASCIIGraph(graph: DependencyGraph): string {
    const lines: string[] = [];
    lines.push("Dependency Graph:");
    lines.push("================\n");

    // Group by dependency depth
    const depths = new Map<string, number>();
    const visited = new Set<string>();

    const calculateDepth = (entity: string, currentDepth: number): void => {
      if (visited.has(entity)) return;
      visited.add(entity);
      depths.set(entity, Math.max(depths.get(entity) ?? 0, currentDepth));

      const dependencies = graph.edges.get(entity) || new Set();
      for (const dep of dependencies) {
        calculateDepth(dep, currentDepth + 1);
      }
    };

    for (const entity of graph.ordered) {
      calculateDepth(entity, 0);
    }

    // Group by depth
    const byDepth = new Map<number, string[]>();
    for (const [entity, depth] of depths) {
      if (!byDepth.has(depth)) {
        byDepth.set(depth, []);
      }
      byDepth.get(depth)!.push(entity);
    }

    // Print by level
    const maxDepth = Math.max(...depths.values());
    for (let d = 0; d <= maxDepth; d++) {
      const entities = byDepth.get(d) || [];
      if (entities.length > 0) {
        lines.push(`Level ${d}: ${entities.join(", ")}`);
      }
    }

    return lines.join("\n");
  }
}

/**
 * Orchestrates seeding with full dependency graph support
 */
export class DependencyGraphValidator {
  /**
   * Validate complete seeding plan
   */
  static validateSeedingPlan(
    graph: DependencyGraph,
    entitiesToSeed: string[]
  ): {
    errors: string[];
    orderedActual: string[];
    valid: boolean;
    warnings: string[];
  } {
    const errors: string[] = [];
    const warnings: string[] = [];

    // Check all requested entities exist
    for (const entity of entitiesToSeed) {
      if (!graph.nodes.has(entity)) {
        errors.push(`Requested entity "${entity}" not found in dependency graph`);
      }
    }

    if (errors.length > 0) {
      return { valid: false, errors, warnings, orderedActual: [] };
    }

    // Find minimum set including all dependencies
    const toSeed = new Set(entitiesToSeed);
    const addDependencies = (entity: string): void => {
      const deps = graph.edges.get(entity);
      if (deps) {
        for (const dep of deps) {
          if (!toSeed.has(dep)) {
            toSeed.add(dep);
            addDependencies(dep);
          }
        }
      }
    };

    for (const entity of entitiesToSeed) {
      addDependencies(entity);
    }

    if (toSeed.size > entitiesToSeed.length) {
      const added = Array.from(toSeed)
        .filter((e) => !entitiesToSeed.includes(e))
        .join(", ");
      warnings.push(`Added ${toSeed.size - entitiesToSeed.length} dependencies: ${added}`);
    }

    // Get ordered subset
    const orderedActual = graph.ordered.filter((e) => toSeed.has(e));

    return {
      valid: true,
      errors: [],
      warnings,
      orderedActual,
    };
  }
}
