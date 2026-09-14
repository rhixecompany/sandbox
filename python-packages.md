# python-packages.md — Workspace Python dependency inventory

> Generated: 2026-09-11 | Scope: SandBox root + `projects/*` requirements*.txt + pyproject.toml | Manager: pip + uv

## Summary

| Metric                   | Count |
| ------------------------ | ----- |
| Total dependency entries | 501   |
| Unique packages          | 289   |
| Source files             | 15    |

## Top 15 source files (by dependency count)

| Source                                                | Dependencies |
| ----------------------------------------------------- | ------------ |
| `root`                                                | 274          |
| `projects\ecom`                                       | 62           |
| `projects\Python-projects`                            | 41           |
| `projects\profile`                                    | 23           |
| `projects\cookiecutter-django-tailwind`               | 20           |
| `projects\rhixecompany-comics\backend`                | 19           |
| `projects\xamehi.tv`                                  | 18           |
| `projects\Banking`                                    | 14           |
| `packages\openrouter-client-py`                       | 7            |
| `projects\mcp-servers\python`                         | 6            |
| `projects\Banking\.claude\skills\slack-gif-creator`   | 4            |
| `projects\Django-Scrapy-Selenium`                     | 4            |
| `projects\rhixe_scans`                                | 4            |
| `projects\cookiecutter-django-tailwind\docs`          | 3            |
| `projects\Banking\.claude\skills\mcp-builder\scripts` | 2            |

## Full dependency list (unique packages, alphabetical)

| Package                         | Spec                                        | Sources                                                                                                                                               |
| ------------------------------- | ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Django`                        | `*, >=5.0,<5.2`                             | `projects\profile`, `projects\rhixecompany-comics\backend`, `projects\xamehi.tv`                                                                      |
| `Pillow`                        | `*, >=10.0,<11.0`                           | `projects\profile`, `projects\rhixecompany-comics\backend`                                                                                            |
| `PyDictionary`                  | `==2.0.1`                                   | `projects\Python-projects`, `root`                                                                                                                    |
| `PyGithub`                      | `==2.3.0`                                   | `projects\cookiecutter-django-tailwind`, `root`                                                                                                       |
| `agent-client-protocol`         | `==0.9.0`                                   | `root`                                                                                                                                                |
| `aiofile`                       | `==3.12.3`                                  | `root`                                                                                                                                                |
| `aiohappyeyeballs`              | `==2.7.1`                                   | `root`                                                                                                                                                |
| `aiohttp`                       | `==3.14.3`                                  | `root`                                                                                                                                                |
| `aiosignal`                     | `==1.4.0`                                   | `root`                                                                                                                                                |
| `annotated-doc`                 | `==0.0.5`                                   | `root`                                                                                                                                                |
| `annotated-types`               | `==0.8.0`                                   | `root`                                                                                                                                                |
| `anthropic`                     | `==0.87.0, >=0.39.0`                        | `projects\Banking\.claude\skills\mcp-builder\scripts`, `root`                                                                                         |
| `anyio`                         | `==4.14.2`                                  | `root`                                                                                                                                                |
| `appdirs`                       | `==1.4.4`                                   | `projects\ecom`, `root`                                                                                                                               |
| `asgiref`                       | `==3.2.10`                                  | `projects\ecom`, `root`                                                                                                                               |
| `ast-serialize`                 | `==0.8.0`                                   | `root`                                                                                                                                                |
| `astroid`                       | `==2.4.2`                                   | `projects\ecom`, `root`                                                                                                                               |
| `attrs`                         | `==26.1.0`                                  | `root`                                                                                                                                                |
| `audioop-lts`                   | `==0.2.2`                                   | `root`                                                                                                                                                |
| `authlib`                       | `==1.7.2`                                   | `root`                                                                                                                                                |
| `authors`                       | `*`                                         | `packages\openrouter-client-py`                                                                                                                       |
| `autopep8`                      | `==1.5.4`                                   | `projects\ecom`, `root`                                                                                                                               |
| `av`                            | `==18.0.0`                                  | `root`                                                                                                                                                |
| `beartype`                      | `==0.22.9`                                  | `root`                                                                                                                                                |
| `beautifulsoup4`                | `==4.13.3`                                  | `projects\Python-projects`, `root`                                                                                                                    |
| `binaryornot`                   | `==0.4.4`                                   | `projects\cookiecutter-django-tailwind`, `root`                                                                                                       |
| `black`                         | `==25.1.0`                                  | `projects\Python-projects`, `root`                                                                                                                    |
| `blinker`                       | `==1.9.0`                                   | `root`                                                                                                                                                |
| `boto3`                         | `==1.14.31, ==1.42.89`                      | `projects\ecom`, `root`                                                                                                                               |
| `botocore`                      | `==1.17.31, ==1.42.97`                      | `projects\ecom`, `root`                                                                                                                               |
| `brotlicffi`                    | `==1.2.0.1`                                 | `root`                                                                                                                                                |
| `bs4`                           | `==0.0.2`                                   | `projects\Python-projects`, `root`                                                                                                                    |
| `cachelib`                      | `==0.1`                                     | `projects\ecom`, `root`                                                                                                                               |
| `cachetools`                    | `==7.1.7`                                   | `root`                                                                                                                                                |
| `caio`                          | `==0.12.2`                                  | `root`                                                                                                                                                |
| `celery`                        | `>=5.3,<6.0`                                | `projects\rhixecompany-comics\backend`, `root`                                                                                                        |
| `certifi`                       | `==2020.4.5.1, ==2025.1.31, ==2026.5.20`    | `projects\Python-projects`, `projects\ecom`, `root`                                                                                                   |
| `cffi`                          | `==2.1.1`                                   | `root`                                                                                                                                                |
| `cfgv`                          | `==3.5.0`                                   | `projects\Banking`, `root`                                                                                                                            |
| `chardet`                       | `==3.0.4`                                   | `projects\ecom`, `root`                                                                                                                               |
| `charset-normalizer`            | `==3.4.1, ==3.5.1`                          | `projects\Python-projects`, `root`                                                                                                                    |
| `click`                         | `==7.1.2, ==8.1.8, ==8.4.2`                 | `projects\Python-projects`, `projects\ecom`, `root`                                                                                                   |
| `colorama`                      | `==0.4.4, ==0.4.6`                          | `projects\Python-projects`, `projects\ecom`, `root`                                                                                                   |
| `concurrent-log-handler`        | `==0.9.29`                                  | `root`                                                                                                                                                |
| `contourpy`                     | `==1.3.1, ==1.3.3`                          | `projects\Python-projects`, `root`                                                                                                                    |
| `cookiecutter`                  | `==2.6.0`                                   | `projects\cookiecutter-django-tailwind`, `root`                                                                                                       |
| `coverage`                      | `==7.6.10`                                  | `projects\Python-projects`, `root`                                                                                                                    |
| `credentials`                   | `==1.1`                                     | `projects\Python-projects`, `root`                                                                                                                    |
| `croniter`                      | `==6.0.0`                                   | `root`                                                                                                                                                |
| `cryptography`                  | `==50.0.0`                                  | `root`                                                                                                                                                |
| `cs50`                          | `==5.0.4`                                   | `projects\ecom`, `root`                                                                                                                               |
| `cspell`                        | `==0.0.1a1`                                 | `root`                                                                                                                                                |
| `ctranslate2`                   | `==4.8.1`                                   | `root`                                                                                                                                                |
| `cycler`                        | `==0.12.1`                                  | `projects\Python-projects`, `root`                                                                                                                    |
| `cyclopts`                      | `==4.23.0`                                  | `root`                                                                                                                                                |
| `davey`                         | `==0.1.6`                                   | `root`                                                                                                                                                |
| `debugpy`                       | `==1.8.20`                                  | `root`                                                                                                                                                |
| `defusedxml`                    | `==0.7.1`                                   | `root`                                                                                                                                                |
| `dependencies`                  | `*`                                         | `packages\openrouter-client-py`, `projects\mcp-servers\python`                                                                                        |
| `dependency-injector`           | `==4.49.1`                                  | `root`                                                                                                                                                |
| `description`                   | `*`                                         | `packages\openrouter-client-py`, `projects\mcp-servers\python`                                                                                        |
| `discord-py`                    | `==2.7.1`                                   | `root`                                                                                                                                                |
| `distlib`                       | `==0.3.1, ==0.4.0, ==0.4.3`                 | `projects\Banking`, `projects\ecom`, `root`                                                                                                           |
| `distro`                        | `==1.9.0`                                   | `root`                                                                                                                                                |
| `dj-database-url`               | `*`                                         | `projects\xamehi.tv`                                                                                                                                  |
| `django`                        | `==3.1.14, >=5.0,<5.2`                      | `projects\ecom`, `root`                                                                                                                               |
| `django-allauth`                | `*`                                         | `projects\xamehi.tv`                                                                                                                                  |
| `django-ckeditor`               | `*, ==6.3.2`                                | `projects\ecom`, `projects\profile`, `root`                                                                                                           |
| `django-cors-headers`           | `*, ==3.11.0, >=4.3,<5.0`                   | `projects\ecom`, `projects\rhixecompany-comics\backend`, `projects\xamehi.tv`, `root`                                                                 |
| `django-crispy-forms`           | `*, ==1.14.0`                               | `projects\ecom`, `projects\profile`, `root`                                                                                                           |
| `django-environ`                | `*`                                         | `projects\profile`                                                                                                                                    |
| `django-filter`                 | `*, ==21.1, >=24.1,<25.0`                   | `projects\ecom`, `projects\profile`, `projects\rhixecompany-comics\backend`, `projects\xamehi.tv`, `root`                                             |
| `django-js-asset`               | `*, ==2.0.0`                                | `projects\ecom`, `projects\profile`, `projects\xamehi.tv`, `root`                                                                                     |
| `django-storages`               | `*, ==1.12.3`                               | `projects\ecom`, `projects\profile`, `projects\xamehi.tv`, `root`                                                                                     |
| `django-upgrade`                | `==1.20.0`                                  | `projects\cookiecutter-django-tailwind`, `root`                                                                                                       |
| `djangorestframework`           | `*, ==3.13.1, >=3.15,<4.0`                  | `projects\ecom`, `projects\rhixecompany-comics\backend`, `projects\xamehi.tv`, `root`                                                                 |
| `djangorestframework-simplejwt` | `*, ==5.2.0, >=5.3,<6.0`                    | `projects\ecom`, `projects\rhixecompany-comics\backend`, `projects\xamehi.tv`, `root`                                                                 |
| `djlint`                        | `==1.34.1`                                  | `projects\cookiecutter-django-tailwind`, `root`                                                                                                       |
| `dnspython`                     | `==2.8.0`                                   | `root`                                                                                                                                                |
| `docstring-parser`              | `==0.18.0`                                  | `root`                                                                                                                                                |
| `docutils`                      | `*, ==0.15.2`                               | `projects\ecom`, `projects\profile`, `root`                                                                                                           |
| `drf-spectacular`               | `>=0.27,<1.0`                               | `projects\rhixecompany-comics\backend`, `root`                                                                                                        |
| `edge-tts`                      | `==7.2.7`                                   | `root`                                                                                                                                                |
| `email-validator`               | `==2.3.0`                                   | `root`                                                                                                                                                |
| `environ`                       | `==1.0`                                     | `projects\Python-projects`, `root`                                                                                                                    |
| `exceptiongroup`                | `==1.3.1`                                   | `root`                                                                                                                                                |
| `fastapi`                       | `==0.141.1`                                 | `root`                                                                                                                                                |
| `faster-whisper`                | `==1.2.1`                                   | `root`                                                                                                                                                |
| `fastmcp`                       | `==2.10.6`                                  | `root`                                                                                                                                                |
| `fastmcp-slim`                  | `==3.4.7`                                   | `root`                                                                                                                                                |
| `filelock`                      | `==3.0.12, ==3.29.0, ==3.32.2`              | `projects\Banking`, `projects\ecom`, `root`                                                                                                           |
| `fire`                          | `==0.7.1`                                   | `root`                                                                                                                                                |
| `firecrawl-anydoc`              | `==0.2.4`                                   | `root`                                                                                                                                                |
| `flask`                         | `==1.1.4, ==3.1.3`                          | `projects\ecom`, `root`                                                                                                                               |
| `flask-session`                 | `==0.4.0`                                   | `projects\ecom`, `root`                                                                                                                               |
| `flatbuffers`                   | `==25.12.19`                                | `root`                                                                                                                                                |
| `fonttools`                     | `==4.56.0, ==4.63.0`                        | `projects\Python-projects`, `root`                                                                                                                    |
| `frozenlist`                    | `==1.8.0`                                   | `root`                                                                                                                                                |
| `fsspec`                        | `==2026.7.0`                                | `root`                                                                                                                                                |
| `futures`                       | `==3.0.5`                                   | `projects\Python-projects`, `root`                                                                                                                    |
| `git-filter-repo`               | `==2.47.0`                                  | `root`                                                                                                                                                |
| `gitpython`                     | `==3.1.43`                                  | `projects\cookiecutter-django-tailwind`, `root`                                                                                                       |
| `google-api-core`               | `==2.34.0`                                  | `root`                                                                                                                                                |
| `google-api-python-client`      | `==2.194.0`                                 | `root`                                                                                                                                                |
| `google-auth`                   | `==2.55.1`                                  | `root`                                                                                                                                                |
| `google-auth-httplib2`          | `==0.3.1`                                   | `root`                                                                                                                                                |
| `google-auth-oauthlib`          | `==1.3.1`                                   | `root`                                                                                                                                                |
| `googleapis-common-protos`      | `==1.75.1`                                  | `root`                                                                                                                                                |
| `goslate`                       | `==1.5.4`                                   | `projects\Python-projects`, `root`                                                                                                                    |
| `greenlet`                      | `==1.1.2`                                   | `projects\ecom`, `root`                                                                                                                               |
| `griffelib`                     | `==2.2.0`                                   | `root`                                                                                                                                                |
| `gunicorn`                      | `*, ==20.1.0, >=22.0,<23.0`                 | `projects\ecom`, `projects\profile`, `projects\rhixecompany-comics\backend`, `projects\xamehi.tv`, `root`                                             |
| `h11`                           | `==0.16.0`                                  | `root`                                                                                                                                                |
| `hf-xet`                        | `==1.6.0`                                   | `root`                                                                                                                                                |
| `honcho-ai`                     | `==2.2.0`                                   | `root`                                                                                                                                                |
| `httpcore`                      | `==1.0.9`                                   | `root`                                                                                                                                                |
| `httpcore2`                     | `==2.7.0`                                   | `root`                                                                                                                                                |
| `httplib2`                      | `==0.32.0`                                  | `root`                                                                                                                                                |
| `httptools`                     | `==0.8.0`                                   | `root`                                                                                                                                                |
| `httpx`                         | `==0.28.1`                                  | `root`                                                                                                                                                |
| `httpx-sse`                     | `==0.4.3`                                   | `root`                                                                                                                                                |
| `httpx2`                        | `==2.7.0`                                   | `root`                                                                                                                                                |
| `huggingface-hub`               | `==1.24.0`                                  | `root`                                                                                                                                                |
| `identify`                      | `==2.6.19`                                  | `projects\Banking`, `root`                                                                                                                            |
| `idna`                          | `==2.9, ==3.10, ==3.19`                     | `projects\Python-projects`, `projects\ecom`, `root`                                                                                                   |
| `imageio`                       | `>=2.31.0`                                  | `projects\Banking\.claude\skills\slack-gif-creator`                                                                                                   |
| `imageio-ffmpeg`                | `>=0.4.9`                                   | `projects\Banking\.claude\skills\slack-gif-creator`                                                                                                   |
| `iniconfig`                     | `==2.3.0`                                   | `root`                                                                                                                                                |
| `install`                       | `==1.3.3`                                   | `projects\ecom`, `root`                                                                                                                               |
| `isort`                         | `==5.6.4`                                   | `projects\ecom`, `root`                                                                                                                               |
| `itsdangerous`                  | `==1.1.0, ==2.2.0`                          | `projects\ecom`, `root`                                                                                                                               |
| `jaraco-classes`                | `==3.4.0`                                   | `root`                                                                                                                                                |
| `jaraco-context`                | `==6.1.2`                                   | `root`                                                                                                                                                |
| `jaraco-functools`              | `==4.6.0`                                   | `root`                                                                                                                                                |
| `jinja2`                        | `==2.11.3, ==3.1.4, ==3.1.6`                | `projects\cookiecutter-django-tailwind`, `projects\ecom`, `root`                                                                                      |
| `jiter`                         | `==0.16.0`                                  | `root`                                                                                                                                                |
| `jmespath`                      | `*, ==0.10.0, ==1.1.0`                      | `projects\ecom`, `projects\profile`, `root`                                                                                                           |
| `joserfc`                       | `==1.7.4`                                   | `root`                                                                                                                                                |
| `joystick`                      | `==0.3.8`                                   | `root`                                                                                                                                                |
| `jsonref`                       | `==1.1.0`                                   | `root`                                                                                                                                                |
| `jsonschema`                    | `==4.26.0`                                  | `root`                                                                                                                                                |
| `jsonschema-path`               | `==0.5.0`                                   | `root`                                                                                                                                                |
| `jsonschema-specifications`     | `==2025.9.1`                                | `root`                                                                                                                                                |
| `keyring`                       | `==25.7.0`                                  | `root`                                                                                                                                                |
| `kiwisolver`                    | `==1.4.8, ==1.5.0`                          | `projects\Python-projects`, `root`                                                                                                                    |
| `lazy-object-proxy`             | `==1.4.3`                                   | `projects\ecom`, `root`                                                                                                                               |
| `librt`                         | `==0.15.0`                                  | `root`                                                                                                                                                |
| `markdown`                      | `==3.10.2`                                  | `root`                                                                                                                                                |
| `markdown-it-py`                | `==4.2.0`                                   | `root`                                                                                                                                                |
| `markupsafe`                    | `==1.1.1, ==3.0.3`                          | `projects\ecom`, `root`                                                                                                                               |
| `matplotlib`                    | `==3.10.1, ==3.11.1`                        | `projects\Python-projects`, `root`                                                                                                                    |
| `mccabe`                        | `==0.6.1`                                   | `projects\ecom`, `root`                                                                                                                               |
| `mcp`                           | `==2.0.0, >=1.1.0`                          | `projects\Banking\.claude\skills\mcp-builder\scripts`, `root`                                                                                         |
| `mcp-types`                     | `==2.0.0`                                   | `root`                                                                                                                                                |
| `mdurl`                         | `==0.1.2`                                   | `root`                                                                                                                                                |
| `microsoft-teams-api`           | `==2.0.13.4`                                | `root`                                                                                                                                                |
| `microsoft-teams-apps`          | `==2.0.13.4`                                | `root`                                                                                                                                                |
| `microsoft-teams-cards`         | `==2.0.13.4`                                | `root`                                                                                                                                                |
| `microsoft-teams-common`        | `==2.0.13.4`                                | `root`                                                                                                                                                |
| `more-itertools`                | `==11.1.0`                                  | `root`                                                                                                                                                |
| `msal`                          | `==1.37.0`                                  | `root`                                                                                                                                                |
| `multidict`                     | `==6.7.1`                                   | `root`                                                                                                                                                |
| `mypy`                          | `*, ==1.15.0, ==2.3.0`                      | `projects\Banking`, `projects\Django-Scrapy-Selenium`, `projects\Python-projects`, `projects\cookiecutter-django-tailwind`, `projects\ecom` (+5 more) |
| `mypy-extensions`               | `==1.0.0, ==1.1.0`                          | `projects\Python-projects`, `root`                                                                                                                    |
| `myst-parser`                   | `==3.0.1`                                   | `projects\cookiecutter-django-tailwind\docs`, `root`                                                                                                  |
| `name`                          | `*`                                         | `packages\openrouter-client-py`, `projects\mcp-servers\python`                                                                                        |
| `nemo-relay`                    | `==0.8.4`                                   | `root`                                                                                                                                                |
| `nodeenv`                       | `==1.10.0`                                  | `projects\Banking`, `root`                                                                                                                            |
| `numpy`                         | `==2.2.4, ==2.4.3, >=1.24.0`                | `projects\Banking\.claude\skills\slack-gif-creator`, `projects\Python-projects`, `root`                                                               |
| `oauthlib`                      | `==3.3.1`                                   | `root`                                                                                                                                                |
| `ollama`                        | `==0.6.2`                                   | `root`                                                                                                                                                |
| `onnxruntime`                   | `==1.28.0`                                  | `root`                                                                                                                                                |
| `openai`                        | `==2.24.0`                                  | `root`                                                                                                                                                |
| `openapi-pydantic`              | `==0.5.1`                                   | `root`                                                                                                                                                |
| `opencv-python`                 | `==4.11.0.86`                               | `projects\Python-projects`, `root`                                                                                                                    |
| `openrouter`                    | `>=1.0.0`                                   | `root`                                                                                                                                                |
| `opentelemetry-api`             | `==1.44.0`                                  | `root`                                                                                                                                                |
| `packaging`                     | `==24.2, ==26.0`                            | `projects\Python-projects`, `root`                                                                                                                    |
| `pathable`                      | `==0.6.0`                                   | `root`                                                                                                                                                |
| `pathspec`                      | `==1.1.1`                                   | `root`                                                                                                                                                |
| `pillow`                        | `*, ==12.3.0, >=10.0.0...`                  | `projects\Banking\.claude\skills\slack-gif-creator`, `projects\Python-projects`, `projects\ecom`, `projects\xamehi.tv`, `root`                        |
| `pip`                           | `==26.1.1, ==26.2.1`                        | `projects\Banking`, `root`                                                                                                                            |
| `platformdirs`                  | `==4.11.0, ==4.9.6`                         | `projects\Banking`, `root`                                                                                                                            |
| `pluggy`                        | `==1.6.0`                                   | `root`                                                                                                                                                |
| `portalocker`                   | `==4.1.0`                                   | `root`                                                                                                                                                |
| `pre-commit`                    | `*, ==3.8.0, ==4.2.0...`                    | `projects\Banking`, `projects\Django-Scrapy-Selenium`, `projects\Python-projects`, `projects\cookiecutter-django-tailwind`, `projects\ecom` (+5 more) |
| `prompt-toolkit`                | `==3.0.52`                                  | `root`                                                                                                                                                |
| `propcache`                     | `==0.5.2`                                   | `root`                                                                                                                                                |
| `proto-plus`                    | `==1.28.3`                                  | `root`                                                                                                                                                |
| `protobuf`                      | `==7.36.0`                                  | `root`                                                                                                                                                |
| `psutil`                        | `==7.2.2`                                   | `root`                                                                                                                                                |
| `psycopg2-binary`               | `*, ==2.9.3, >=2.9,<3.0`                    | `projects\ecom`, `projects\profile`, `projects\rhixecompany-comics\backend`, `projects\xamehi.tv`, `root`                                             |
| `py-key-value-aio`              | `==0.4.5`                                   | `root`                                                                                                                                                |
| `pyasn1`                        | `==0.6.4`                                   | `root`                                                                                                                                                |
| `pyasn1-modules`                | `==0.4.2`                                   | `root`                                                                                                                                                |
| `pycodestyle`                   | `==2.8.0`                                   | `projects\ecom`, `root`                                                                                                                               |
| `pycparser`                     | `==3.0`                                     | `root`                                                                                                                                                |
| `pydantic`                      | `==2.13.4`                                  | `root`                                                                                                                                                |
| `pydantic-core`                 | `==2.46.4`                                  | `root`                                                                                                                                                |
| `pydantic-settings`             | `==2.15.0`                                  | `root`                                                                                                                                                |
| `pygame`                        | `==2.6.1`                                   | `root`                                                                                                                                                |
| `pygments`                      | `==2.21.0`                                  | `root`                                                                                                                                                |
| `pyjwt`                         | `==2.13.0, ==2.3.0`                         | `projects\ecom`, `root`                                                                                                                               |
| `pylint`                        | `==2.6.2`                                   | `projects\ecom`, `root`                                                                                                                               |
| `pynacl`                        | `==1.6.2`                                   | `root`                                                                                                                                                |
| `pyparsing`                     | `==3.2.1, ==3.3.2`                          | `projects\Python-projects`, `root`                                                                                                                    |
| `pyperclip`                     | `==1.11.0`                                  | `root`                                                                                                                                                |
| `pyright`                       | `==1.1.414`                                 | `root`                                                                                                                                                |
| `pytest`                        | `==8.3.2, ==8.3.5, ==9.1.1`                 | `projects\Python-projects`, `projects\cookiecutter-django-tailwind`, `root`                                                                           |
| `pytest-asyncio`                | `==1.3.0`                                   | `root`                                                                                                                                                |
| `pytest-cookies`                | `==0.7.0`                                   | `projects\cookiecutter-django-tailwind`, `root`                                                                                                       |
| `pytest-instafail`              | `==0.5.0`                                   | `projects\cookiecutter-django-tailwind`, `root`                                                                                                       |
| `pytest-xdist`                  | `==3.6.1`                                   | `projects\cookiecutter-django-tailwind`, `root`                                                                                                       |
| `python-dateutil`               | `*, ==2.8.1, ==2.9.0.post0`                 | `projects\Python-projects`, `projects\ecom`, `projects\profile`, `root`                                                                               |
| `python-discovery`              | `==1.3.0, ==1.5.1`                          | `projects\Banking`, `root`                                                                                                                            |
| `python-dotenv`                 | `==0.20.0, ==1.2.2, >=1.0,<2.0`             | `projects\ecom`, `projects\rhixecompany-comics\backend`, `root`                                                                                       |
| `python-multipart`              | `==0.0.32`                                  | `root`                                                                                                                                                |
| `python-telegram-bot`           | `==22.8`                                    | `root`                                                                                                                                                |
| `pytz`                          | `*, ==2022.1, ==2026.3.post1`               | `projects\ecom`, `projects\profile`, `root`                                                                                                           |
| `pywin32`                       | `==311`                                     | `root`                                                                                                                                                |
| `pywin32-ctypes`                | `==0.2.3`                                   | `root`                                                                                                                                                |
| `pywinpty`                      | `==2.0.15`                                  | `root`                                                                                                                                                |
| `pyyaml`                        | `==6.0.1, ==6.0.3`                          | `projects\Banking`, `projects\cookiecutter-django-tailwind`, `root`                                                                                   |
| `qrcode`                        | `==8.0`                                     | `projects\Python-projects`, `root`                                                                                                                    |
| `readme`                        | `*`                                         | `projects\mcp-servers\python`                                                                                                                         |
| `redis`                         | `>=5.0,<6.0`                                | `projects\rhixecompany-comics\backend`, `root`                                                                                                        |
| `referencing`                   | `==0.37.0`                                  | `root`                                                                                                                                                |
| `requests`                      | `==2.25.1, ==2.32.3, ==2.33.0`              | `projects\Python-projects`, `projects\cookiecutter-django-tailwind`, `projects\ecom`, `root`                                                          |
| `requests-oauthlib`             | `==2.0.0`                                   | `root`                                                                                                                                                |
| `requires-python`               | `*`                                         | `packages\openrouter-client-py`, `projects\mcp-servers\python`                                                                                        |
| `rich`                          | `==14.3.3`                                  | `root`                                                                                                                                                |
| `rich-rst`                      | `==2.1.0`                                   | `root`                                                                                                                                                |
| `rpds-py`                       | `==2026.6.3`                                | `root`                                                                                                                                                |
| `ruamel-yaml`                   | `==0.18.17`                                 | `root`                                                                                                                                                |
| `ruamel-yaml-clib`              | `==0.2.15`                                  | `root`                                                                                                                                                |
| `ruff`                          | `==0.11.2, ==0.15.10, ==0.5.5`              | `projects\Python-projects`, `projects\cookiecutter-django-tailwind`, `root`                                                                           |
| `s3transfer`                    | `*, ==0.16.1, ==0.3.7`                      | `projects\ecom`, `projects\profile`, `root`                                                                                                           |
| `schedule`                      | `==1.2.2`                                   | `projects\Python-projects`, `root`                                                                                                                    |
| `scrapy`                        | `>=2.11,<3.0`                               | `projects\rhixecompany-comics\backend`, `root`                                                                                                        |
| `selenium`                      | `>=4.20,<5.0`                               | `projects\rhixecompany-comics\backend`, `root`                                                                                                        |
| `setuptools`                    | `==62.6.0, ==83.0.0`                        | `projects\ecom`, `root`                                                                                                                               |
| `sh`                            | `==2.0.7, ==2.0.7; sys_platform != "win32"` | `projects\cookiecutter-django-tailwind`, `root`                                                                                                       |
| `simple-term-menu`              | `==1.6.6`                                   | `root`                                                                                                                                                |
| `six`                           | `*, ==1.16.0, ==1.17.0`                     | `projects\Python-projects`, `projects\ecom`, `projects\profile`, `root`                                                                               |
| `slack-bolt`                    | `==1.30.0`                                  | `root`                                                                                                                                                |
| `slack-sdk`                     | `==3.43.0`                                  | `root`                                                                                                                                                |
| `sniffio`                       | `==1.3.1`                                   | `root`                                                                                                                                                |
| `snowballstemmer`               | `==3.1.1`                                   | `root`                                                                                                                                                |
| `socksio`                       | `==1.0.0`                                   | `root`                                                                                                                                                |
| `sounddevice`                   | `==0.5.5`                                   | `root`                                                                                                                                                |
| `soupsieve`                     | `==2.6`                                     | `projects\Python-projects`, `root`                                                                                                                    |
| `sphinx`                        | `==7.4.7`                                   | `projects\cookiecutter-django-tailwind\docs`, `root`                                                                                                  |
| `sphinx-rtd-theme`              | `==2.0.0`                                   | `projects\cookiecutter-django-tailwind\docs`, `root`                                                                                                  |
| `sqlalchemy`                    | `==1.4.37`                                  | `projects\ecom`, `root`                                                                                                                               |
| `sqlparse`                      | `*, ==0.3.1`                                | `projects\ecom`, `projects\profile`, `root`                                                                                                           |
| `sse-starlette`                 | `==3.4.8`                                   | `root`                                                                                                                                                |
| `starlette`                     | `==1.6.0`                                   | `root`                                                                                                                                                |
| `tabulate`                      | `==0.10.0`                                  | `root`                                                                                                                                                |
| `tenacity`                      | `==9.1.4`                                   | `root`                                                                                                                                                |
| `termcolor`                     | `==1.1.0, ==3.3.0`                          | `projects\ecom`, `root`                                                                                                                               |
| `test`                          | `*`                                         | `packages\openrouter-client-py`                                                                                                                       |
| `tokenizers`                    | `==0.23.1`                                  | `root`                                                                                                                                                |
| `toml`                          | `==0.10.2`                                  | `projects\ecom`, `root`                                                                                                                               |
| `tornado`                       | `==6.5.8`                                   | `root`                                                                                                                                                |
| `tox`                           | `==4.16.0`                                  | `projects\cookiecutter-django-tailwind`, `root`                                                                                                       |
| `tqdm`                          | `==4.70.0`                                  | `root`                                                                                                                                                |
| `truststore`                    | `==0.10.4`                                  | `root`                                                                                                                                                |
| `ty`                            | `==0.0.21`                                  | `root`                                                                                                                                                |
| `types-PyYAML`                  | `*, ==6.0.12.20260724`                      | `projects\Banking`, `projects\Django-Scrapy-Selenium`, `projects\Python-projects`, `projects\cookiecutter-django-tailwind`, `projects\ecom` (+5 more) |
| `types-python-dateutil`         | `==2.9.0.20260807`                          | `root`                                                                                                                                                |
| `types-requests`                | `*, ==2.33.0.20260712`                      | `projects\Banking`, `projects\Django-Scrapy-Selenium`, `projects\Python-projects`, `projects\cookiecutter-django-tailwind`, `projects\ecom` (+5 more) |
| `typing-extensions`             | `==4.16.0`                                  | `root`                                                                                                                                                |
| `typing-inspection`             | `==0.4.4`                                   | `root`                                                                                                                                                |
| `typing_extensions`             | `==4.12.2`                                  | `projects\Python-projects`, `root`                                                                                                                    |
| `tzdata`                        | `==2025.3`                                  | `root`                                                                                                                                                |
| `uncalled-for`                  | `==0.4.0`                                   | `root`                                                                                                                                                |
| `uritemplate`                   | `==4.2.0`                                   | `root`                                                                                                                                                |
| `urllib3`                       | `*, ==1.25.9, ==2.3.0...`                   | `projects\Python-projects`, `projects\ecom`, `projects\profile`, `root`                                                                               |
| `uvicorn`                       | `==0.52.4`                                  | `root`                                                                                                                                                |
| `version`                       | `*`                                         | `packages\openrouter-client-py`, `projects\mcp-servers\python`                                                                                        |
| `virtualenv`                    | `*, ==20.2.1, ==21.3.1...`                  | `projects\Banking`, `projects\ecom`, `projects\xamehi.tv`, `root`                                                                                     |
| `watchfiles`                    | `==1.2.0`                                   | `root`                                                                                                                                                |
| `wcwidth`                       | `==0.8.2`                                   | `root`                                                                                                                                                |
| `websockets`                    | `==15.0.1`                                  | `root`                                                                                                                                                |
| `werkzeug`                      | `==0.15.4, ==3.1.8`                         | `projects\ecom`, `root`                                                                                                                               |
| `whitenoise`                    | `*, ==5.1.0, >=6.6,<7.0`                    | `projects\ecom`, `projects\profile`, `projects\rhixecompany-comics\backend`, `projects\xamehi.tv`, `root`                                             |
| `wrapt`                         | `==1.14.1`                                  | `projects\ecom`, `root`                                                                                                                               |
| `yarl`                          | `==1.24.5`                                  | `root`                                                                                                                                                |
| `youtube-transcript-api`        | `==1.2.4`                                   | `root`                                                                                                                                                |

## Per-source breakdown

### `packages\openrouter-client-py` (7 deps)

| Package           | Spec |
| ----------------- | ---- |
| `authors`         | `*`  |
| `dependencies`    | `*`  |
| `description`     | `*`  |
| `name`            | `*`  |
| `requires-python` | `*`  |
| `test`            | `*`  |
| `version`         | `*`  |

### `projects\Banking` (14 deps)

| Package            | Spec       |
| ------------------ | ---------- |
| `cfgv`             | `==3.5.0`  |
| `distlib`          | `==0.4.0`  |
| `filelock`         | `==3.29.0` |
| `identify`         | `==2.6.19` |
| `mypy`             | `*`        |
| `nodeenv`          | `==1.10.0` |
| `pip`              | `==26.1.1` |
| `platformdirs`     | `==4.9.6`  |
| `pre-commit`       | `==4.6.0`  |
| `python-discovery` | `==1.3.0`  |
| `pyyaml`           | `==6.0.3`  |
| `types-PyYAML`     | `*`        |
| `types-requests`   | `*`        |
| `virtualenv`       | `==21.3.1` |

### `projects\Banking\.claude\skills\mcp-builder\scripts` (2 deps)

| Package     | Spec       |
| ----------- | ---------- |
| `anthropic` | `>=0.39.0` |
| `mcp`       | `>=1.1.0`  |

### `projects\Banking\.claude\skills\slack-gif-creator` (4 deps)

| Package          | Spec       |
| ---------------- | ---------- |
| `imageio`        | `>=2.31.0` |
| `imageio-ffmpeg` | `>=0.4.9`  |
| `numpy`          | `>=1.24.0` |
| `pillow`         | `>=10.0.0` |

### `projects\Django-Scrapy-Selenium` (4 deps)

| Package          | Spec |
| ---------------- | ---- |
| `mypy`           | `*`  |
| `pre-commit`     | `*`  |
| `types-PyYAML`   | `*`  |
| `types-requests` | `*`  |

### `projects\Python-projects` (39 deps)

| Package              | Spec            |
| -------------------- | --------------- |
| `PyDictionary`       | `==2.0.1`       |
| `beautifulsoup4`     | `==4.13.3`      |
| `black`              | `==25.1.0`      |
| `bs4`                | `==0.0.2`       |
| `certifi`            | `==2025.1.31`   |
| `charset-normalizer` | `==3.4.1`       |
| `click`              | `==8.1.8`       |
| `colorama`           | `==0.4.6`       |
| `contourpy`          | `==1.3.1`       |
| `coverage`           | `==7.6.10`      |
| `credentials`        | `==1.1`         |
| `cycler`             | `==0.12.1`      |
| `environ`            | `==1.0`         |
| `fonttools`          | `==4.56.0`      |
| `futures`            | `==3.0.5`       |
| `goslate`            | `==1.5.4`       |
| `idna`               | `==3.10`        |
| `kiwisolver`         | `==1.4.8`       |
| `matplotlib`         | `==3.10.1`      |
| `mypy`               | `==1.15.0`      |
| `mypy-extensions`    | `==1.0.0`       |
| `numpy`              | `==2.2.4`       |
| `opencv-python`      | `==4.11.0.86`   |
| `packaging`          | `==24.2`        |
| `pillow`             | `>=12.3.0`      |
| `pre-commit`         | `==4.2.0`       |
| `pyparsing`          | `==3.2.1`       |
| `pytest`             | `==8.3.5`       |
| `python-dateutil`    | `==2.9.0.post0` |
| `qrcode`             | `==8.0`         |
| `requests`           | `==2.32.3`      |
| `ruff`               | `==0.11.2`      |
| `schedule`           | `==1.2.2`       |
| `six`                | `==1.17.0`      |
| `soupsieve`          | `==2.6`         |
| `types-PyYAML`       | `*`             |
| `types-requests`     | `*`             |
| `typing_extensions`  | `==4.12.2`      |
| `urllib3`            | `==2.3.0`       |

### `projects\cookiecutter-django-tailwind` (20 deps)

| Package            | Spec                               |
| ------------------ | ---------------------------------- |
| `PyGithub`         | `==2.3.0`                          |
| `binaryornot`      | `==0.4.4`                          |
| `cookiecutter`     | `==2.6.0`                          |
| `django-upgrade`   | `==1.20.0`                         |
| `djlint`           | `==1.34.1`                         |
| `gitpython`        | `==3.1.43`                         |
| `jinja2`           | `==3.1.4`                          |
| `mypy`             | `*`                                |
| `pre-commit`       | `==3.8.0`                          |
| `pytest`           | `==8.3.2`                          |
| `pytest-cookies`   | `==0.7.0`                          |
| `pytest-instafail` | `==0.5.0`                          |
| `pytest-xdist`     | `==3.6.1`                          |
| `pyyaml`           | `==6.0.1`                          |
| `requests`         | `==2.32.3`                         |
| `ruff`             | `==0.5.5`                          |
| `sh`               | `==2.0.7; sys_platform != "win32"` |
| `tox`              | `==4.16.0`                         |
| `types-PyYAML`     | `*`                                |
| `types-requests`   | `*`                                |

### `projects\cookiecutter-django-tailwind\docs` (3 deps)

| Package            | Spec      |
| ------------------ | --------- |
| `myst-parser`      | `==3.0.1` |
| `sphinx`           | `==7.4.7` |
| `sphinx-rtd-theme` | `==2.0.0` |

### `projects\ecom` (62 deps)

| Package                         | Spec           |
| ------------------------------- | -------------- |
| `appdirs`                       | `==1.4.4`      |
| `asgiref`                       | `==3.2.10`     |
| `astroid`                       | `==2.4.2`      |
| `autopep8`                      | `==1.5.4`      |
| `boto3`                         | `==1.14.31`    |
| `botocore`                      | `==1.17.31`    |
| `cachelib`                      | `==0.1`        |
| `certifi`                       | `==2020.4.5.1` |
| `chardet`                       | `==3.0.4`      |
| `click`                         | `==7.1.2`      |
| `colorama`                      | `==0.4.4`      |
| `cs50`                          | `==5.0.4`      |
| `distlib`                       | `==0.3.1`      |
| `django`                        | `==3.1.14`     |
| `django-ckeditor`               | `==6.3.2`      |
| `django-cors-headers`           | `==3.11.0`     |
| `django-crispy-forms`           | `==1.14.0`     |
| `django-filter`                 | `==21.1`       |
| `django-js-asset`               | `==2.0.0`      |
| `django-storages`               | `==1.12.3`     |
| `djangorestframework`           | `==3.13.1`     |
| `djangorestframework-simplejwt` | `==5.2.0`      |
| `docutils`                      | `==0.15.2`     |
| `filelock`                      | `==3.0.12`     |
| `flask`                         | `==1.1.4`      |
| `flask-session`                 | `==0.4.0`      |
| `greenlet`                      | `==1.1.2`      |
| `gunicorn`                      | `==20.1.0`     |
| `idna`                          | `==2.9`        |
| `install`                       | `==1.3.3`      |
| `isort`                         | `==5.6.4`      |
| `itsdangerous`                  | `==1.1.0`      |
| `jinja2`                        | `==2.11.3`     |
| `jmespath`                      | `==0.10.0`     |
| `lazy-object-proxy`             | `==1.4.3`      |
| `markupsafe`                    | `==1.1.1`      |
| `mccabe`                        | `==0.6.1`      |
| `mypy`                          | `*`            |
| `pillow`                        | `>=12.3.0`     |
| `pre-commit`                    | `*`            |
| `psycopg2-binary`               | `==2.9.3`      |
| `pycodestyle`                   | `==2.8.0`      |
| `pyjwt`                         | `==2.3.0`      |
| `pylint`                        | `==2.6.2`      |
| `python-dateutil`               | `==2.8.1`      |
| `python-dotenv`                 | `==0.20.0`     |
| `pytz`                          | `==2022.1`     |
| `requests`                      | `==2.25.1`     |
| `s3transfer`                    | `==0.3.7`      |
| `setuptools`                    | `==62.6.0`     |
| `six`                           | `==1.16.0`     |
| `sqlalchemy`                    | `==1.4.37`     |
| `sqlparse`                      | `==0.3.1`      |
| `termcolor`                     | `==1.1.0`      |
| `toml`                          | `==0.10.2`     |
| `types-PyYAML`                  | `*`            |
| `types-requests`                | `*`            |
| `urllib3`                       | `==1.25.9`     |
| `virtualenv`                    | `==20.2.1`     |
| `werkzeug`                      | `==0.15.4`     |
| `whitenoise`                    | `==5.1.0`      |
| `wrapt`                         | `==1.14.1`     |

### `projects\mcp-servers\python` (6 deps)

| Package           | Spec |
| ----------------- | ---- |
| `dependencies`    | `*`  |
| `description`     | `*`  |
| `name`            | `*`  |
| `readme`          | `*`  |
| `requires-python` | `*`  |
| `version`         | `*`  |

### `projects\profile` (23 deps)

| Package               | Spec |
| --------------------- | ---- |
| `Django`              | `*`  |
| `Pillow`              | `*`  |
| `django-ckeditor`     | `*`  |
| `django-crispy-forms` | `*`  |
| `django-environ`      | `*`  |
| `django-filter`       | `*`  |
| `django-js-asset`     | `*`  |
| `django-storages`     | `*`  |
| `docutils`            | `*`  |
| `gunicorn`            | `*`  |
| `jmespath`            | `*`  |
| `mypy`                | `*`  |
| `pre-commit`          | `*`  |
| `psycopg2-binary`     | `*`  |
| `python-dateutil`     | `*`  |
| `pytz`                | `*`  |
| `s3transfer`          | `*`  |
| `six`                 | `*`  |
| `sqlparse`            | `*`  |
| `types-PyYAML`        | `*`  |
| `types-requests`      | `*`  |
| `urllib3`             | `*`  |
| `whitenoise`          | `*`  |

### `projects\rhixe_scans` (4 deps)

| Package          | Spec |
| ---------------- | ---- |
| `mypy`           | `*`  |
| `pre-commit`     | `*`  |
| `types-PyYAML`   | `*`  |
| `types-requests` | `*`  |

### `projects\rhixecompany-comics\backend` (19 deps)

| Package                         | Spec           |
| ------------------------------- | -------------- |
| `Django`                        | `>=5.0,<5.2`   |
| `Pillow`                        | `>=10.0,<11.0` |
| `celery`                        | `>=5.3,<6.0`   |
| `django-cors-headers`           | `>=4.3,<5.0`   |
| `django-filter`                 | `>=24.1,<25.0` |
| `djangorestframework`           | `>=3.15,<4.0`  |
| `djangorestframework-simplejwt` | `>=5.3,<6.0`   |
| `drf-spectacular`               | `>=0.27,<1.0`  |
| `gunicorn`                      | `>=22.0,<23.0` |
| `mypy`                          | `*`            |
| `pre-commit`                    | `*`            |
| `psycopg2-binary`               | `>=2.9,<3.0`   |
| `python-dotenv`                 | `>=1.0,<2.0`   |
| `redis`                         | `>=5.0,<6.0`   |
| `scrapy`                        | `>=2.11,<3.0`  |
| `selenium`                      | `>=4.20,<5.0`  |
| `types-PyYAML`                  | `*`            |
| `types-requests`                | `*`            |
| `whitenoise`                    | `>=6.6,<7.0`   |

### `projects\xamehi.tv` (18 deps)

| Package                         | Spec |
| ------------------------------- | ---- |
| `Django`                        | `*`  |
| `dj-database-url`               | `*`  |
| `django-allauth`                | `*`  |
| `django-cors-headers`           | `*`  |
| `django-filter`                 | `*`  |
| `django-js-asset`               | `*`  |
| `django-storages`               | `*`  |
| `djangorestframework`           | `*`  |
| `djangorestframework-simplejwt` | `*`  |
| `gunicorn`                      | `*`  |
| `mypy`                          | `*`  |
| `pillow`                        | `*`  |
| `pre-commit`                    | `*`  |
| `psycopg2-binary`               | `*`  |
| `types-PyYAML`                  | `*`  |
| `types-requests`                | `*`  |
| `virtualenv`                    | `*`  |
| `whitenoise`                    | `*`  |

### `root` (274 deps)

| Package                         | Spec                |
| ------------------------------- | ------------------- |
| `PyDictionary`                  | `==2.0.1`           |
| `PyGithub`                      | `==2.3.0`           |
| `agent-client-protocol`         | `==0.9.0`           |
| `aiofile`                       | `==3.12.3`          |
| `aiohappyeyeballs`              | `==2.7.1`           |
| `aiohttp`                       | `==3.14.3`          |
| `aiosignal`                     | `==1.4.0`           |
| `annotated-doc`                 | `==0.0.5`           |
| `annotated-types`               | `==0.8.0`           |
| `anthropic`                     | `==0.87.0`          |
| `anyio`                         | `==4.14.2`          |
| `appdirs`                       | `==1.4.4`           |
| `asgiref`                       | `==3.2.10`          |
| `ast-serialize`                 | `==0.8.0`           |
| `astroid`                       | `==2.4.2`           |
| `attrs`                         | `==26.1.0`          |
| `audioop-lts`                   | `==0.2.2`           |
| `authlib`                       | `==1.7.2`           |
| `autopep8`                      | `==1.5.4`           |
| `av`                            | `==18.0.0`          |
| `beartype`                      | `==0.22.9`          |
| `beautifulsoup4`                | `==4.13.3`          |
| `binaryornot`                   | `==0.4.4`           |
| `black`                         | `==25.1.0`          |
| `blinker`                       | `==1.9.0`           |
| `boto3`                         | `==1.42.89`         |
| `botocore`                      | `==1.42.97`         |
| `brotlicffi`                    | `==1.2.0.1`         |
| `bs4`                           | `==0.0.2`           |
| `cachelib`                      | `==0.1`             |
| `cachetools`                    | `==7.1.7`           |
| `caio`                          | `==0.12.2`          |
| `celery`                        | `>=5.3,<6.0`        |
| `certifi`                       | `==2026.5.20`       |
| `cffi`                          | `==2.1.1`           |
| `cfgv`                          | `==3.5.0`           |
| `chardet`                       | `==3.0.4`           |
| `charset-normalizer`            | `==3.5.1`           |
| `click`                         | `==8.4.2`           |
| `colorama`                      | `==0.4.6`           |
| `concurrent-log-handler`        | `==0.9.29`          |
| `contourpy`                     | `==1.3.3`           |
| `cookiecutter`                  | `==2.6.0`           |
| `coverage`                      | `==7.6.10`          |
| `credentials`                   | `==1.1`             |
| `croniter`                      | `==6.0.0`           |
| `cryptography`                  | `==50.0.0`          |
| `cs50`                          | `==5.0.4`           |
| `cspell`                        | `==0.0.1a1`         |
| `ctranslate2`                   | `==4.8.1`           |
| `cycler`                        | `==0.12.1`          |
| `cyclopts`                      | `==4.23.0`          |
| `davey`                         | `==0.1.6`           |
| `debugpy`                       | `==1.8.20`          |
| `defusedxml`                    | `==0.7.1`           |
| `dependency-injector`           | `==4.49.1`          |
| `discord-py`                    | `==2.7.1`           |
| `distlib`                       | `==0.4.3`           |
| `distro`                        | `==1.9.0`           |
| `django`                        | `>=5.0,<5.2`        |
| `django-ckeditor`               | `==6.3.2`           |
| `django-cors-headers`           | `>=4.3,<5.0`        |
| `django-crispy-forms`           | `==1.14.0`          |
| `django-filter`                 | `>=24.1,<25.0`      |
| `django-js-asset`               | `==2.0.0`           |
| `django-storages`               | `==1.12.3`          |
| `django-upgrade`                | `==1.20.0`          |
| `djangorestframework`           | `>=3.15,<4.0`       |
| `djangorestframework-simplejwt` | `>=5.3,<6.0`        |
| `djlint`                        | `==1.34.1`          |
| `dnspython`                     | `==2.8.0`           |
| `docstring-parser`              | `==0.18.0`          |
| `docutils`                      | `==0.15.2`          |
| `drf-spectacular`               | `>=0.27,<1.0`       |
| `edge-tts`                      | `==7.2.7`           |
| `email-validator`               | `==2.3.0`           |
| `environ`                       | `==1.0`             |
| `exceptiongroup`                | `==1.3.1`           |
| `fastapi`                       | `==0.141.1`         |
| `faster-whisper`                | `==1.2.1`           |
| `fastmcp`                       | `==2.10.6`          |
| `fastmcp-slim`                  | `==3.4.7`           |
| `filelock`                      | `==3.32.2`          |
| `fire`                          | `==0.7.1`           |
| `firecrawl-anydoc`              | `==0.2.4`           |
| `flask`                         | `==3.1.3`           |
| `flask-session`                 | `==0.4.0`           |
| `flatbuffers`                   | `==25.12.19`        |
| `fonttools`                     | `==4.63.0`          |
| `frozenlist`                    | `==1.8.0`           |
| `fsspec`                        | `==2026.7.0`        |
| `futures`                       | `==3.0.5`           |
| `git-filter-repo`               | `==2.47.0`          |
| `gitpython`                     | `==3.1.43`          |
| `google-api-core`               | `==2.34.0`          |
| `google-api-python-client`      | `==2.194.0`         |
| `google-auth`                   | `==2.55.1`          |
| `google-auth-httplib2`          | `==0.3.1`           |
| `google-auth-oauthlib`          | `==1.3.1`           |
| `googleapis-common-protos`      | `==1.75.1`          |
| `goslate`                       | `==1.5.4`           |
| `greenlet`                      | `==1.1.2`           |
| `griffelib`                     | `==2.2.0`           |
| `gunicorn`                      | `>=22.0,<23.0`      |
| `h11`                           | `==0.16.0`          |
| `hf-xet`                        | `==1.6.0`           |
| `honcho-ai`                     | `==2.2.0`           |
| `httpcore`                      | `==1.0.9`           |
| `httpcore2`                     | `==2.7.0`           |
| `httplib2`                      | `==0.32.0`          |
| `httptools`                     | `==0.8.0`           |
| `httpx`                         | `==0.28.1`          |
| `httpx-sse`                     | `==0.4.3`           |
| `httpx2`                        | `==2.7.0`           |
| `huggingface-hub`               | `==1.24.0`          |
| `identify`                      | `==2.6.19`          |
| `idna`                          | `==3.19`            |
| `iniconfig`                     | `==2.3.0`           |
| `install`                       | `==1.3.3`           |
| `isort`                         | `==5.6.4`           |
| `itsdangerous`                  | `==2.2.0`           |
| `jaraco-classes`                | `==3.4.0`           |
| `jaraco-context`                | `==6.1.2`           |
| `jaraco-functools`              | `==4.6.0`           |
| `jinja2`                        | `==3.1.6`           |
| `jiter`                         | `==0.16.0`          |
| `jmespath`                      | `==1.1.0`           |
| `joserfc`                       | `==1.7.4`           |
| `joystick`                      | `==0.3.8`           |
| `jsonref`                       | `==1.1.0`           |
| `jsonschema`                    | `==4.26.0`          |
| `jsonschema-path`               | `==0.5.0`           |
| `jsonschema-specifications`     | `==2025.9.1`        |
| `keyring`                       | `==25.7.0`          |
| `kiwisolver`                    | `==1.5.0`           |
| `lazy-object-proxy`             | `==1.4.3`           |
| `librt`                         | `==0.15.0`          |
| `markdown`                      | `==3.10.2`          |
| `markdown-it-py`                | `==4.2.0`           |
| `markupsafe`                    | `==3.0.3`           |
| `matplotlib`                    | `==3.11.1`          |
| `mccabe`                        | `==0.6.1`           |
| `mcp`                           | `==2.0.0`           |
| `mcp-types`                     | `==2.0.0`           |
| `mdurl`                         | `==0.1.2`           |
| `microsoft-teams-api`           | `==2.0.13.4`        |
| `microsoft-teams-apps`          | `==2.0.13.4`        |
| `microsoft-teams-cards`         | `==2.0.13.4`        |
| `microsoft-teams-common`        | `==2.0.13.4`        |
| `more-itertools`                | `==11.1.0`          |
| `msal`                          | `==1.37.0`          |
| `multidict`                     | `==6.7.1`           |
| `mypy`                          | `==2.3.0`           |
| `mypy-extensions`               | `==1.1.0`           |
| `myst-parser`                   | `==3.0.1`           |
| `nemo-relay`                    | `==0.8.4`           |
| `nodeenv`                       | `==1.10.0`          |
| `numpy`                         | `==2.4.3`           |
| `oauthlib`                      | `==3.3.1`           |
| `ollama`                        | `==0.6.2`           |
| `onnxruntime`                   | `==1.28.0`          |
| `openai`                        | `==2.24.0`          |
| `openapi-pydantic`              | `==0.5.1`           |
| `opencv-python`                 | `==4.11.0.86`       |
| `openrouter`                    | `>=1.0.0`           |
| `opentelemetry-api`             | `==1.44.0`          |
| `packaging`                     | `==26.0`            |
| `pathable`                      | `==0.6.0`           |
| `pathspec`                      | `==1.1.1`           |
| `pillow`                        | `==12.3.0`          |
| `pip`                           | `==26.2.1`          |
| `platformdirs`                  | `==4.11.0`          |
| `pluggy`                        | `==1.6.0`           |
| `portalocker`                   | `==4.1.0`           |
| `pre-commit`                    | `==4.6.1`           |
| `prompt-toolkit`                | `==3.0.52`          |
| `propcache`                     | `==0.5.2`           |
| `proto-plus`                    | `==1.28.3`          |
| `protobuf`                      | `==7.36.0`          |
| `psutil`                        | `==7.2.2`           |
| `psycopg2-binary`               | `==2.9.3`           |
| `py-key-value-aio`              | `==0.4.5`           |
| `pyasn1`                        | `==0.6.4`           |
| `pyasn1-modules`                | `==0.4.2`           |
| `pycodestyle`                   | `==2.8.0`           |
| `pycparser`                     | `==3.0`             |
| `pydantic`                      | `==2.13.4`          |
| `pydantic-core`                 | `==2.46.4`          |
| `pydantic-settings`             | `==2.15.0`          |
| `pygame`                        | `==2.6.1`           |
| `pygments`                      | `==2.21.0`          |
| `pyjwt`                         | `==2.13.0`          |
| `pylint`                        | `==2.6.2`           |
| `pynacl`                        | `==1.6.2`           |
| `pyparsing`                     | `==3.3.2`           |
| `pyperclip`                     | `==1.11.0`          |
| `pyright`                       | `==1.1.414`         |
| `pytest`                        | `==9.1.1`           |
| `pytest-asyncio`                | `==1.3.0`           |
| `pytest-cookies`                | `==0.7.0`           |
| `pytest-instafail`              | `==0.5.0`           |
| `pytest-xdist`                  | `==3.6.1`           |
| `python-dateutil`               | `==2.9.0.post0`     |
| `python-discovery`              | `==1.5.1`           |
| `python-dotenv`                 | `==1.2.2`           |
| `python-multipart`              | `==0.0.32`          |
| `python-telegram-bot`           | `==22.8`            |
| `pytz`                          | `==2026.3.post1`    |
| `pywin32`                       | `==311`             |
| `pywin32-ctypes`                | `==0.2.3`           |
| `pywinpty`                      | `==2.0.15`          |
| `pyyaml`                        | `==6.0.3`           |
| `qrcode`                        | `==8.0`             |
| `redis`                         | `>=5.0,<6.0`        |
| `referencing`                   | `==0.37.0`          |
| `requests`                      | `==2.33.0`          |
| `requests-oauthlib`             | `==2.0.0`           |
| `rich`                          | `==14.3.3`          |
| `rich-rst`                      | `==2.1.0`           |
| `rpds-py`                       | `==2026.6.3`        |
| `ruamel-yaml`                   | `==0.18.17`         |
| `ruamel-yaml-clib`              | `==0.2.15`          |
| `ruff`                          | `==0.15.10`         |
| `s3transfer`                    | `==0.16.1`          |
| `schedule`                      | `==1.2.2`           |
| `scrapy`                        | `>=2.11,<3.0`       |
| `selenium`                      | `>=4.20,<5.0`       |
| `setuptools`                    | `==83.0.0`          |
| `sh`                            | `==2.0.7`           |
| `simple-term-menu`              | `==1.6.6`           |
| `six`                           | `==1.17.0`          |
| `slack-bolt`                    | `==1.30.0`          |
| `slack-sdk`                     | `==3.43.0`          |
| `sniffio`                       | `==1.3.1`           |
| `snowballstemmer`               | `==3.1.1`           |
| `socksio`                       | `==1.0.0`           |
| `sounddevice`                   | `==0.5.5`           |
| `soupsieve`                     | `==2.6`             |
| `sphinx`                        | `==7.4.7`           |
| `sphinx-rtd-theme`              | `==2.0.0`           |
| `sqlalchemy`                    | `==1.4.37`          |
| `sqlparse`                      | `==0.3.1`           |
| `sse-starlette`                 | `==3.4.8`           |
| `starlette`                     | `==1.6.0`           |
| `tabulate`                      | `==0.10.0`          |
| `tenacity`                      | `==9.1.4`           |
| `termcolor`                     | `==3.3.0`           |
| `tokenizers`                    | `==0.23.1`          |
| `toml`                          | `==0.10.2`          |
| `tornado`                       | `==6.5.8`           |
| `tox`                           | `==4.16.0`          |
| `tqdm`                          | `==4.70.0`          |
| `truststore`                    | `==0.10.4`          |
| `ty`                            | `==0.0.21`          |
| `types-PyYAML`                  | `==6.0.12.20260724` |
| `types-python-dateutil`         | `==2.9.0.20260807`  |
| `types-requests`                | `==2.33.0.20260712` |
| `typing-extensions`             | `==4.16.0`          |
| `typing-inspection`             | `==0.4.4`           |
| `typing_extensions`             | `==4.12.2`          |
| `tzdata`                        | `==2025.3`          |
| `uncalled-for`                  | `==0.4.0`           |
| `uritemplate`                   | `==4.2.0`           |
| `urllib3`                       | `==2.7.0`           |
| `uvicorn`                       | `==0.52.4`          |
| `virtualenv`                    | `==21.7.1`          |
| `watchfiles`                    | `==1.2.0`           |
| `wcwidth`                       | `==0.8.2`           |
| `websockets`                    | `==15.0.1`          |
| `werkzeug`                      | `==3.1.8`           |
| `whitenoise`                    | `>=6.6,<7.0`        |
| `wrapt`                         | `==1.14.1`          |
| `yarl`                          | `==1.24.5`          |
| `youtube-transcript-api`        | `==1.2.4`           |
