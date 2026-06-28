import json
from pathlib import Path

ROOT = Path(r"C:/Users/Alexa/Desktop/SandBox")
PROJECTS = ROOT / 'projects'
TEMPLATES = Path(r"C:/Users/Alexa/AppData/Local/hermes/skills/development/vscode-workspace-configurator/templates")

# helper
def load_json(p: Path):
    if not p.exists():
        return None
    try:
        return json.loads(p.read_text(encoding='utf-8'))
    except Exception as e:
        print(f'ERROR loading {p}: {e}')
        return None

def write_json(p: Path, data):
    p.write_text(json.dumps(data, indent=2), encoding='utf-8')
    print(f'WROTE {p}')

# Required edits per user confirmation (A)
add_launch = ['Django-Scrapy-Selenium','docs','Python-projects','selenium_webdriver','xamehi','youtube-downloader']
add_bun_to = ['Banking']
merge_dual = ['rhixecompany-comics']
add_devprod_tasks = ['ecom','rhixecompany-comics','xamehi']

# load templates
tpl_next = load_json(TEMPLATES / 'settings-nextjs.json') or {}
tpl_django = load_json(TEMPLATES / 'settings-django.json') or {}
tpl_node = load_json(TEMPLATES / 'settings-node.json') or {}

# launch snippets
django_launch = {
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Django: Runserver",
      "type": "debugpy",
      "request": "launch",
      "program": "${workspaceFolder}/manage.py",
      "args": ["runserver"],
      "django": True,
      "justMyCode": True
    }
  ]
}

next_launch = {
  "version": "0.2.0",
  "configurations": [
    {
      "command": "npm run dev",
      "name": "Next.js: Dev Server",
      "request": "launch",
      "type": "node-terminal"
    }
  ]
}

bun_launch_conf = {
  "name": "Bun: Current File",
  "type": "node",
  "request": "launch",
  "runtimeExecutable": "bun",
  "program": "${file}",
  "console": "integratedTerminal"
}

node_launch_conf = {
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Node.js: Current File",
      "type": "node",
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal"
    },
    {
      "name": "npm start",
      "type": "node",
      "request": "launch",
      "runtimeExecutable": "npm",
      "runtimeArgs": ["start"],
      "console": "integratedTerminal"
    }
  ]
}

# tasks templates
dev_task_node = {"command":"npm run dev","label":"Dev","type":"shell","group":"build"}
build_task_node = {"command":"npm run build","label":"Build","type":"shell","group":"build"}

dev_task_django = {"command":"python manage.py runserver","label":"Runserver","type":"shell","group":"build"}
build_task_django = {"command":"python manage.py collectstatic --noinput && python manage.py migrate","label":"Build: collectstatic+migrate","type":"shell","group":"build"}

# iterate repos
changes = []
for repo_name in sorted([p.name for p in PROJECTS.iterdir() if p.is_dir()]):
    repo = PROJECTS / repo_name
    vscode = repo / '.vscode'
    if not vscode.exists():
        print(f'SKIP {repo_name} no .vscode')
        continue
    # Ensure launch.json exists or has snippet
    launch = vscode / 'launch.json'
    settings = vscode / 'settings.json'
    tasks = vscode / 'tasks.json'
    # load current
    cur_launch = load_json(launch)
    cur_settings = load_json(settings) or {}
    cur_tasks = load_json(tasks) or {"version":"2.0.0","tasks":[]}

    # 1) add launch where requested
    if repo_name in add_launch:
        # pick template by stack detection
        pkg = repo / 'package.json'
        req = repo / 'requirements.txt'
        manage = repo / 'manage.py'
        if pkg.exists():
            # node/next
            # create Node/Next launch depending on package
            j = load_json(pkg)
            deps = ' '.join(list(j.get('dependencies',{}).keys())+list(j.get('devDependencies',{}).keys())).lower() if j else ''
            if 'next' in deps:
                # ensure next launch present
                if not cur_launch:
                    write_json(launch, next_launch)
                    changes.append(f'{repo_name}: added Next.js launch.json')
                else:
                    # merge configs if not present
                    existing_names = [c.get('name') for c in cur_launch.get('configurations',[])]
                    for cfg in next_launch['configurations']:
                        if cfg.get('name') not in existing_names:
                            cur_launch.setdefault('configurations',[]).append(cfg)
                            changes.append(f'{repo_name}: appended Next.js launch config')
                    write_json(launch, cur_launch)
            else:
                # generic node
                if not cur_launch:
                    write_json(launch, node_launch_conf)
                    changes.append(f'{repo_name}: added Node launch.json')
                else:
                    existing_names = [c.get('name') for c in cur_launch.get('configurations',[])]
                    for cfg in node_launch_conf.get('configurations',[]):
                        if cfg.get('name') not in existing_names:
                            cur_launch.setdefault('configurations',[]).append(cfg)
                            changes.append(f'{repo_name}: appended Node launch config {cfg.get("name")}')
                    write_json(launch, cur_launch)
        elif manage.exists() or (req.exists() and 'django' in req.read_text(encoding='utf-8').lower()):
            # django
            if not cur_launch:
                write_json(launch, django_launch)
                changes.append(f'{repo_name}: added Django launch.json')
            else:
                existing_names = [c.get('name') for c in cur_launch.get('configurations',[])]
                for cfg in django_launch.get('configurations',[]):
                    if cfg.get('name') not in existing_names:
                        cur_launch.setdefault('configurations',[]).append(cfg)
                        changes.append(f'{repo_name}: appended Django launch config')
                write_json(launch, cur_launch)
        else:
            # unknown -> add node launch by default
            if not cur_launch:
                write_json(launch, node_launch_conf)
                changes.append(f'{repo_name}: added default Node launch.json (unknown stack)')
            else:
                existing_names = [c.get('name') for c in cur_launch.get('configurations',[])]
                for cfg in node_launch_conf.get('configurations',[]):
                    if cfg.get('name') not in existing_names:
                        cur_launch.setdefault('configurations',[]).append(cfg)
                        changes.append(f'{repo_name}: appended default Node launch config')
                write_json(launch, cur_launch)

    # 2) add bun launch config for Banking
    if repo_name in add_bun_to:
        if not launch.exists():
            # create minimal with bun config
            launch_obj = {"version":"0.2.0","configurations":[bun_launch_conf]}
            write_json(launch, launch_obj)
            changes.append(f'{repo_name}: created launch.json with Bun config')
        else:
            cur_launch = load_json(launch) or {"version":"0.2.0","configurations":[]}
            names = [c.get('name') for c in cur_launch.get('configurations',[])]
            if bun_launch_conf.get('name') not in names:
                cur_launch.setdefault('configurations',[]).append(bun_launch_conf)
                write_json(launch, cur_launch)
                changes.append(f'{repo_name}: appended Bun launch config')

    # 3) merge dual stack for rhixecompany-comics
    if repo_name in merge_dual:
        # ensure settings.json has JS/TS language blocks from tpl_next
        modified = False
        # tpl_next contains language blocks like [javascript], etc.
        for k,v in tpl_next.items():
            if k.startswith('['):
                if k not in cur_settings:
                    cur_settings[k] = v
                    modified = True
        if modified:
            write_json(settings, cur_settings)
            changes.append(f'{repo_name}: merged Next.js language blocks into settings.json')
        # ensure launch has both django and next
        if not launch.exists():
            combined = {"version":"0.2.0","configurations":[]}
            combined['configurations'].extend(django_launch['configurations'])
            combined['configurations'].extend(next_launch['configurations'])
            write_json(launch, combined)
            changes.append(f'{repo_name}: wrote combined launch.json (Django+Next)')
        else:
            cur_launch = load_json(launch) or {"version":"0.2.0","configurations":[]}
            names = [c.get('name') for c in cur_launch.get('configurations',[])]
            for cfg in django_launch['configurations'] + next_launch['configurations']:
                if cfg.get('name') not in names:
                    cur_launch.setdefault('configurations',[]).append(cfg)
                    changes.append(f'{repo_name}: appended {cfg.get("name")} to launch.json')
            write_json(launch, cur_launch)

    # 4) add dev/prod tasks for specific repos
    if repo_name in add_devprod_tasks:
        cur_tasks = load_json(tasks) or {"version":"2.0.0","tasks":[]}
        existing_labels = [t.get('label') for t in cur_tasks.get('tasks',[])]
        # choose tasks based on stack
        pkg = repo / 'package.json'
        if pkg.exists():
            # JS project
            if 'Dev' not in existing_labels:
                cur_tasks.setdefault('tasks',[]).append(dev_task_node)
                changes.append(f'{repo_name}: added Dev task to tasks.json')
            if 'Build' not in existing_labels:
                cur_tasks.setdefault('tasks',[]).append(build_task_node)
                changes.append(f'{repo_name}: added Build task to tasks.json')
        else:
            # django
            if 'Runserver' not in existing_labels:
                cur_tasks.setdefault('tasks',[]).append(dev_task_django)
                changes.append(f'{repo_name}: added Runserver task to tasks.json')
            if 'Build: collectstatic+migrate' not in existing_labels:
                cur_tasks.setdefault('tasks',[]).append(build_task_django)
                changes.append(f'{repo_name}: added Build task to tasks.json')
        write_json(tasks, cur_tasks)

print('\nSUMMARY OF CHANGES:')
for c in changes:
    print('- ', c)

if not changes:
    print('No changes were necessary.')
