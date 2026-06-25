<?php

namespace McpServer\Tools;

use MCP\Server\Tool\BaseTool;
use MCP\Server\Tool\Attribute\ToolParameter;

/**
 * GreetTool — returns a personalised greeting.
 *
 * Parameters:
 *   name (string, required) — the person or entity to greet.
 *   style (string, optional) — one of "friendly", "formal", "shout".
 */
class GreetTool extends BaseTool
{
    public function __construct()
    {
        parent::__construct(
            name: 'greet',
            description: 'Generate a personalised greeting message.',
            parameters: [
                new ToolParameter(
                    name: 'name',
                    type: 'string',
                    description: 'The name of the person or entity to greet',
                    required: true,
                ),
                new ToolParameter(
                    name: 'style',
                    type: 'string',
                    description: 'Greeting style: friendly, formal, or shout',
                    required: false,
                    default: 'friendly',
                ),
            ],
        );
    }

    /**
     * Execute the greet tool.
     *
     * @param  array<string, mixed>  $arguments
     * @return string
     */
    public function execute(array $arguments): string
    {
        $name  = $arguments['name'];
        $style = $arguments['style'] ?? 'friendly';

        return match ($style) {
            'formal'  => "Greetings, {$name}. It is a pleasure to make your acquaintance.",
            'shout'   => "HELLO {$name}! HOW ARE YOU TODAY?",
            default   => "Hey {$name}! Hope you're having a great day 👋",
        };
    }
}
