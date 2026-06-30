Updating: 1password

Fetching: official/security\1password
Warning: '1password' is already installed at 1password
Quarantined to .hub\quarantine\1password
Running security scan...
Scan: 1password (official/builtin)  Verdict: SAFE
Decision: ALLOWED — Allowed (builtin source, safe verdict)
Installed: 1password
Files: SKILL.md, references\cli-examples.md, references\get-started.md

Updating: 3-statement-model

Fetching: official/finance\3-statement-model
Warning: '3-statement-model' is already installed at 3-statement-model
Quarantined to .hub\quarantine\3-statement-model
Running security scan...
Scan: 3-statement-model (official/builtin)  Verdict: SAFE
Decision: ALLOWED — Allowed (builtin source, safe verdict)
Installed: 3-statement-model
Files: SKILL.md, references\formatting.md, references\formulas.md, 
references\sec-filings.md

Updating: antigravity-cli

Fetching: official/autonomous-ai-agents\antigravity-cli
Warning: 'antigravity-cli' is already installed at antigravity-cli
Quarantined to .hub\quarantine\antigravity-cli
Running security scan...
Scan: antigravity-cli (official/builtin)  Verdict: DANGEROUS
  CRITICAL supply_chain   references\cli-docs.md:9       "- macOS/Linux: `curl 
-fsSL https://antigravity.google/cli/in"

Decision: ALLOWED — Allowed (builtin source, dangerous verdict)
Installed: antigravity-cli
Files: SKILL.md, references\cli-docs.md

Updating: baoyu-article-illustrator

Fetching: official/creative\baoyu-article-illustrator
Warning: 'baoyu-article-illustrator' is already installed at 
baoyu-article-illustrator
Quarantined to .hub\quarantine\baoyu-article-illustrator
Running security scan...
Scan: baoyu-article-illustrator (official/builtin)  Verdict: SAFE
Decision: ALLOWED — Allowed (builtin source, safe verdict)
Installed: baoyu-article-illustrator
Files: PORT_NOTES.md, SKILL.md, prompts\system.md, 
references\prompt-construction.md, references\style-presets.md, 
references\styles.md, references\usage.md, references\workflow.md, 
references\palettes\macaron.md, references\palettes\mono-ink.md, 
references\palettes\neon.md, references\palettes\warm.md, 
references\styles\blueprint.md, references\styles\chalkboard.md, 
references\styles\editorial.md, references\styles\elegant.md, 
references\styles\fantasy-animation.md, references\styles\flat-doodle.md, 
references\styles\flat.md, references\styles\ink-notes.md, 
references\styles\intuition-machine.md, references\styles\minimal.md, 
references\styles\nature.md, references\styles\notion.md, 
references\styles\pixel-art.md, references\styles\playful.md, 
references\styles\retro.md, references\styles\scientific.md, 
references\styles\screen-print.md, references\styles\sketch-notes.md, 
references\styles\sketch.md, references\styles\vector-illustration.md, 
references\styles\vintage.md, references\styles\warm.md, 
references\styles\watercolor.md

Updating: baoyu-comic

Fetching: official/creative\baoyu-comic
Warning: 'baoyu-comic' is already installed at baoyu-comic
Quarantined to .hub\quarantine\baoyu-comic
Running security scan...
Scan: baoyu-comic (official/builtin)  Verdict: SAFE
Decision: ALLOWED — Allowed (builtin source, safe verdict)
Installed: baoyu-comic
Files: PORT_NOTES.md, SKILL.md, references\analysis-framework.md, 
references\auto-selection.md, references\base-prompt.md, 
references\character-template.md, references\ohmsha-guide.md, 
references\partial-workflows.md, references\storyboard-template.md, 
references\workflow.md, references\art-styles\chalk.md, 
references\art-styles\ink-brush.md, references\art-styles\ligne-claire.md, 
references\art-styles\manga.md, references\art-styles\minimalist.md, 
references\art-styles\realistic.md, references\layouts\cinematic.md, 
references\layouts\dense.md, references\layouts\four-panel.md, 
references\layouts\mixed.md, references\layouts\splash.md, 
references\layouts\standard.md, references\layouts\webtoon.md, 
references\presets\concept-story.md, references\presets\four-panel.md, 
references\presets\ohmsha.md, references\presets\shoujo.md, 
references\presets\wuxia.md, references\tones\action.md, 
references\tones\dramatic.md, references\tones\energetic.md, 
references\tones\neutral.md, references\tones\romantic.md, 
references\tones\vintage.md, references\tones\warm.md

Updating: canvas

Fetching: official/productivity\canvas
Warning: 'canvas' is already installed at canvas
Quarantined to .hub\quarantine\canvas
Running security scan...
Scan: canvas (official/builtin)  Verdict: DANGEROUS
  CRITICAL exfiltration   SKILL.md:74                    "curl -s -H 
"Authorization: Bearer $CANVAS_API_TOKEN" \"
  CRITICAL exfiltration   SKILL.md:78                    "curl -s -H 
"Authorization: Bearer $CANVAS_API_TOKEN" \"
  CRITICAL exfiltration   scripts\canvas_api.py:19       "CANVAS_API_TOKEN = 
os.environ.get("CANVAS_API_TOKEN", "")"
  HIGH     exfiltration   scripts\canvas_api.py:19       "CANVAS_API_TOKEN = 
os.environ.get("CANVAS_API_TOKEN", "")"

Decision: ALLOWED — Allowed (builtin source, dangerous verdict)
Installed: canvas
Files: SKILL.md, scripts\canvas_api.py

Updating: chroma

Fetching: official/mlops\chroma
Warning: 'chroma' is already installed at chroma
Quarantined to .hub\quarantine\chroma
Running security scan...
Scan: chroma (official/builtin)  Verdict: SAFE
  MEDIUM   supply_chain   SKILL.md:47                    "pip install chromadb"
  MEDIUM   supply_chain   SKILL.md:50                    "npm install chromadb 
@chroma-core/default-embed"

Decision: ALLOWED — Allowed (builtin source, safe verdict)
Installed: chroma
Files: SKILL.md, references\integration.md

Updating: clip

Fetching: official/mlops\clip
Warning: 'clip' is already installed at clip
Quarantined to .hub\quarantine\clip
Running security scan...
Scan: clip (official/builtin)  Verdict: SAFE
  MEDIUM   supply_chain   SKILL.md:45                    "pip install 
git+https://github.com/openai/CLIP.git"
  MEDIUM   supply_chain   SKILL.md:46                    "pip install torch 
torchvision ftfy regex tqdm"

Decision: ALLOWED — Allowed (builtin source, safe verdict)
Installed: clip
Files: SKILL.md, references\applications.md

Updating: code-wiki

Fetching: official/software-development\code-wiki
Warning: 'code-wiki' is already installed at code-wiki
Quarantined to .hub\quarantine\code-wiki
Running security scan...
Scan: code-wiki (official/builtin)  Verdict: SAFE
  MEDIUM   supply_chain   SKILL.md:47                    "| 1 | Resolve target 
— local cwd, given path, or `git clone "
  MEDIUM   supply_chain   SKILL.md:68                    "git clone --depth 50 
<url> "$WIKI_TMP/repo""

Decision: ALLOWED — Allowed (builtin source, safe verdict)
Installed: code-wiki
Files: SKILL.md, templates\architecture.md, templates\getting-started.md, 
templates\module.md, templates\README.md

Updating: concept-diagrams

Fetching: official/creative\concept-diagrams
Warning: 'concept-diagrams' is already installed at concept-diagrams
Quarantined to .hub\quarantine\concept-diagrams
Running security scan...
Scan: concept-diagrams (official/builtin)  Verdict: CAUTION
  HIGH     injection      examples\automated-password-reset-flow.md:55 "<!-- D1
· Email in system?  diamond: center=(340,200) hw=100"
  HIGH     injection      examples\automated-password-reset-flow.md:90 "<!-- ──
Center Yes branch: system generates & sends token ──"
  HIGH     injection      examples\place-order-uml-sequence.md:79 "<!-- 
:InventorySystem -->"
  HIGH     injection      examples\place-order-uml-sequence.md:96 "<!-- 
InventorySystem: active from reserveItems → updateStock"
  HIGH     injection      examples\place-order-uml-sequence.md:133 "<!-- ⑤ 
reserveItems(cartItems)  :OrderController → :Inventor"
  HIGH     injection      examples\place-order-uml-sequence.md:137 "<!-- ⑥ « 
itemsReserved »  :InventorySystem → :OrderControlle"
  HIGH     injection      examples\place-order-uml-sequence.md:165 "<!-- ⑨ 
updateStockLevels()  :OrderController → :InventorySys"
  HIGH     injection      examples\place-order-uml-sequence.md:195 "<!-- ⑬ « 
unavailable »  :InventorySystem → :OrderController "
  MEDIUM   supply_chain   examples\autonomous-llm-research-agent-flow.md:101 
"<text class="ts" x="310" y="392" text-anchor="middle" domina"

Decision: ALLOWED — Allowed (builtin source, caution verdict)
Installed: concept-diagrams
Files: SKILL.md, examples\apartment-floor-plan-conversion.md, 
examples\automated-password-reset-flow.md, 
examples\autonomous-llm-research-agent-flow.md, 
examples\banana-journey-tree-to-smoothie.md, 
examples\commercial-aircraft-structure.md, 
examples\cpu-ooo-microarchitecture.md, examples\electricity-grid-flow.md, 
examples\feature-film-production-pipeline.md, 
examples\hospital-emergency-department-flow.md, 
examples\ml-benchmark-grouped-bar-chart.md, 
examples\place-order-uml-sequence.md, examples\smart-city-infrastructure.md, 
examples\smartphone-layer-anatomy.md, examples\sn2-reaction-mechanism.md, 
examples\wind-turbine-structure.md, references\dashboard-patterns.md, 
references\infrastructure-patterns.md, references\physical-shape-cookbook.md, 
templates\template.html

Updating: darwinian-evolver

Fetching: official/research\darwinian-evolver
Warning: 'darwinian-evolver' is already installed at darwinian-evolver
Quarantined to .hub\quarantine\darwinian-evolver
Running security scan...
Scan: darwinian-evolver (official/builtin)  Verdict: DANGEROUS
  CRITICAL injection      SKILL.md:164                   "reject phrases like 
"ignore previous instructions" with HTTP"
  CRITICAL exfiltration   scripts\parrot_openrouter.py:39 "key = 
os.environ.get("OPENROUTER_API_KEY")"
  CRITICAL exfiltration   templates\custom_problem_template.py:47 "key = 
os.environ.get("OPENROUTER_API_KEY")"
  HIGH     exfiltration   scripts\parrot_openrouter.py:39 "key = 
os.environ.get("OPENROUTER_API_KEY")"
  HIGH     exfiltration   templates\custom_problem_template.py:47 "key = 
os.environ.get("OPENROUTER_API_KEY")"
  HIGH     exfiltration   templates\custom_problem_template.py:90 "# TODO: 
include enough context for the LLM to diagnose the f"
  MEDIUM   supply_chain   SKILL.md:179                   "8. **No PyPI 
package.** `pip install darwinian-evolver` will"
  MEDIUM   supply_chain   SKILL.md:67                    "&& uv run 
darwinian_evolver --help | head -5"
  MEDIUM   supply_chain   SKILL.md:76                    "uv run 
darwinian_evolver parrot \"
  MEDIUM   supply_chain   SKILL.md:102                   "uv run --with openai 
python "$SKILL_DIR/scripts/parrot_openr"
  MEDIUM   supply_chain   SKILL.md:110                   "uv run --with openai 
python "$SKILL_DIR/scripts/show_snapsho"
  MEDIUM   supply_chain   SKILL.md:174                   "6. **CLI is hardcoded
to Anthropic.** `uv run darwinian_evol"
  MEDIUM   supply_chain   SKILL.md:189                   "cd "$DE_DIR" && uv 
run darwinian_evolver --help >/dev/null &"
  MEDIUM   supply_chain   SKILL.md:59                    "[ -d 
darwinian_evolver ] || git clone --depth 1 https://gith"
  MEDIUM   supply_chain   templates\custom_problem_template.py:10 
"OPENROUTER_API_KEY=... uv run --with openai python /path/to/"

Decision: ALLOWED — Allowed (builtin source, dangerous verdict)
Installed: darwinian-evolver
Files: SKILL.md, scripts\parrot_openrouter.py, scripts\show_snapshot.py, 
templates\custom_problem_template.py

Updating: dcf-model

Fetching: official/finance\dcf-model
Warning: 'dcf-model' is already installed at dcf-model
Quarantined to .hub\quarantine\dcf-model
Running security scan...
Scan: dcf-model (official/builtin)  Verdict: SAFE
  MEDIUM   supply_chain   scripts\validate_dcf.py:19     "raise 
ImportError("openpyxl not installed. Run: pip install "

Decision: ALLOWED — Allowed (builtin source, safe verdict)
Installed: dcf-model
Files: requirements.txt, SKILL.md, TROUBLESHOOTING.md, scripts\validate_dcf.py

Updating: torchtitan

Fetching: official/mlops\torchtitan
Warning: 'torchtitan' is already installed at torchtitan
Quarantined to .hub\quarantine\torchtitan
Running security scan...
Scan: torchtitan (official/builtin)  Verdict: SAFE
  MEDIUM   supply_chain   SKILL.md:24                    "pip install 
torchtitan"
  MEDIUM   supply_chain   SKILL.md:190                   "USE_CPP=0 pip install
git+https://github.com/pytorch/ao.git"
  MEDIUM   supply_chain   SKILL.md:27                    "git clone 
https://github.com/pytorch/torchtitan"
  MEDIUM   supply_chain   references\float8.md:13        "USE_CPP=0 pip install
git+https://github.com/pytorch/ao.git"

Decision: ALLOWED — Allowed (builtin source, safe verdict)
Installed: torchtitan
Files: SKILL.md, references\checkpoint.md, references\custom-models.md, 
references\float8.md, references\fsdp.md

Updating: domain-intel

Fetching: official/research\domain-intel
Warning: 'domain-intel' is already installed at domain-intel
Quarantined to .hub\quarantine\domain-intel
Running security scan...
Scan: domain-intel (official/builtin)  Verdict: SAFE
Decision: ALLOWED — Allowed (builtin source, safe verdict)
Installed: domain-intel
Files: SKILL.md, scripts\domain_intel.py

Updating: drug-discovery

Fetching: official/research\drug-discovery
Warning: 'drug-discovery' is already installed at drug-discovery
Quarantined to .hub\quarantine\drug-discovery
Running security scan...
Scan: drug-discovery (official/builtin)  Verdict: SAFE
Decision: ALLOWED — Allowed (builtin source, safe verdict)
Installed: drug-discovery
Files: SKILL.md, references\ADMET_REFERENCE.md, scripts\chembl_target.py, 
scripts\ro5_screen.py

Updating: duckduckgo-search

Fetching: official/research\duckduckgo-search
Warning: 'duckduckgo-search' is already installed at duckduckgo-search
Quarantined to .hub\quarantine\duckduckgo-search
Running security scan...
Scan: duckduckgo-search (official/builtin)  Verdict: SAFE
  MEDIUM   supply_chain   SKILL.md:47                    "pip install ddgs"
  MEDIUM   supply_chain   SKILL.md:232                   "- **Package name**: 
The package is `ddgs` (previously `duckd"
  MEDIUM   supply_chain   scripts\duckduckgo.sh:18       "echo "Requires: pip 
install ddgs""
  MEDIUM   supply_chain   scripts\duckduckgo.sh:24       "echo "Error: ddgs not
found. Install with: pip install ddgs""

Decision: ALLOWED — Allowed (builtin source, safe verdict)
Installed: duckduckgo-search
Files: SKILL.md, scripts\duckduckgo.sh

Updating: evm

Fetching: official/blockchain\evm
Warning: 'evm' is already installed at evm
Quarantined to .hub\quarantine\evm
Running security scan...
Scan: evm (official/builtin)  Verdict: SAFE
Decision: ALLOWED — Allowed (builtin source, safe verdict)
Installed: evm
Files: SKILL.md, scripts\evm_client.py

Updating: excel-author

Fetching: official/finance\excel-author
Warning: 'excel-author' is already installed at excel-author
Quarantined to .hub\quarantine\excel-author
Running security scan...
Scan: excel-author (official/builtin)  Verdict: SAFE
  MEDIUM   supply_chain   SKILL.md:29                    "pip install 
"openpyxl>=3.0""
  MEDIUM   execution      scripts\recalc.py:45           "subprocess.run("

Decision: ALLOWED — Allowed (builtin source, safe verdict)
Installed: excel-author
Files: SKILL.md, scripts\recalc.py

Updating: faiss

Fetching: official/mlops\faiss
Warning: 'faiss' is already installed at faiss
Quarantined to .hub\quarantine\faiss
Running security scan...
Scan: faiss (official/builtin)  Verdict: SAFE
  MEDIUM   supply_chain   SKILL.md:45                    "pip install 
faiss-cpu"
  MEDIUM   supply_chain   SKILL.md:48                    "pip install 
faiss-gpu"

Decision: ALLOWED — Allowed (builtin source, safe verdict)
Installed: faiss
Files: SKILL.md, references\index_types.md

Updating: fastmcp

Fetching: official/mcp\fastmcp
Warning: 'fastmcp' is already installed at fastmcp
Quarantined to .hub\quarantine\fastmcp
Running security scan...
Scan: fastmcp (official/builtin)  Verdict: DANGEROUS
  CRITICAL persistence    SKILL.md:175                   "- configure the 
server in `~/AppData/Local/hermes/config.yaml` using the "
  CRITICAL persistence    SKILL.md:296                   "The server-building 
part may be correct while the Hermes con"
  CRITICAL exfiltration   templates\api_wrapper.py:13    "API_TOKEN = 
os.getenv("API_TOKEN")"
  MEDIUM   network        SKILL.md:155                   "fastmcp list 
http://127.0.0.1:8000/mcp --json"
  MEDIUM   network        SKILL.md:156                   "fastmcp call 
http://127.0.0.1:8000/mcp search_resources quer"
  MEDIUM   supply_chain   SKILL.md:39                    "pip install fastmcp"
  MEDIUM   supply_chain   SKILL.md:46                    "pip install httpx"
  MEDIUM   supply_chain   SKILL.md:271                   "pip install fastmcp"
  MEDIUM   network        references\fastmcp-cli.md:49   "fastmcp list 
http://127.0.0.1:8000/mcp --json"
  MEDIUM   supply_chain   references\fastmcp-cli.md:8    "pip install fastmcp"
  MEDIUM   supply_chain   references\fastmcp-cli.md:12   "FastMCP documents 
`pip install fastmcp` and `fastmcp version"

Decision: ALLOWED — Allowed (builtin source, dangerous verdict)
Installed: fastmcp
Files: SKILL.md, references\fastmcp-cli.md, scripts\scaffold_fastmcp.py, 
templates\api_wrapper.py, templates\database_server.py, 
templates\file_processor.py

Updating: fitness-nutrition

Fetching: official/health\fitness-nutrition
Warning: 'fitness-nutrition' is already installed at fitness-nutrition
Quarantined to .hub\quarantine\fitness-nutrition
Running security scan...
Scan: fitness-nutrition (official/builtin)  Verdict: DANGEROUS
  CRITICAL exfiltration   SKILL.md:173                   "curl -s 
"https://api.nal.usda.gov/fdc/v1/foods/search?api_ke"
  CRITICAL exfiltration   SKILL.md:194                   "curl -s 
"https://api.nal.usda.gov/fdc/v1/food/${FDC_ID}?api_"
  CRITICAL exfiltration   scripts\nutrition_search.py:20 "API_KEY = 
os.environ.get("USDA_API_KEY", "DEMO_KEY")"
  CRITICAL obfuscation    scripts\nutrition_search.py:8  "echo -e 
"oats\\nbanana\\nwhey protein" | python3 nutrition_s"
  HIGH     exfiltration   scripts\nutrition_search.py:20 "API_KEY = 
os.environ.get("USDA_API_KEY", "DEMO_KEY")"

Decision: ALLOWED — Allowed (builtin source, dangerous verdict)
Installed: fitness-nutrition
Files: SKILL.md, references\FORMULAS.md, scripts\body_calc.py, 
scripts\nutrition_search.py

Updating: gitnexus-explorer

Fetching: official/research\gitnexus-explorer
Warning: 'gitnexus-explorer' is already installed at gitnexus-explorer
Quarantined to .hub\quarantine\gitnexus-explorer
Running security scan...
Scan: gitnexus-explorer (official/builtin)  Verdict: DANGEROUS
  CRITICAL persistence    SKILL.md:201                   "- **The web UI does 
NOT create `.claude/` or `CLAUDE.md`.** "
  HIGH     network        SKILL.md:29                    "- **cloudflared** — 
for tunneling (auto-installed to ~/.loca"
  HIGH     network        SKILL.md:161                   "# Install cloudflared
if needed (no sudo)"
  HIGH     network        SKILL.md:162                   "if ! command -v 
cloudflared &>/dev/null; then"
  HIGH     network        SKILL.md:164                   "curl -sL 
https://github.com/cloudflare/cloudflared/releases/"
  HIGH     network        SKILL.md:165                   "-o 
~/.local/bin/cloudflared"
  HIGH     network        SKILL.md:166                   "chmod +x 
~/.local/bin/cloudflared"
  HIGH     network        SKILL.md:171                   "cloudflared tunnel 
--config /dev/null --url http://localhost"
  HIGH     network        SKILL.md:183                   "pkill -f cloudflared"
  HIGH     network        SKILL.md:193                   "- **`--config 
/dev/null` is required for cloudflared** if th"
  HIGH     network        SKILL.md:194                   "named tunnel config 
at `~/.cloudflared/config.yml`. Without "
  HIGH     privilege_escalation SKILL.md:97                    "no sudo, no 
nginx."
  HIGH     privilege_escalation SKILL.md:161                   "# Install 
cloudflared if needed (no sudo)"
  MEDIUM   supply_chain   SKILL.md:46                    "cd 
"$GITNEXUS_DIR/gitnexus-shared" && npm install && npm run"
  MEDIUM   supply_chain   SKILL.md:45                    "git clone 
https://github.com/abhigyanpatwari/GitNexus.git "$"

Decision: ALLOWED — Allowed (builtin source, dangerous verdict)
Installed: gitnexus-explorer
Files: SKILL.md, scripts\proxy.mjs

Updating: guidance

Fetching: official/mlops\guidance
Warning: 'guidance' is already installed at guidance
Quarantined to .hub\quarantine\guidance
Running security scan...
Scan: guidance (official/builtin)  Verdict: SAFE
  MEDIUM   supply_chain   SKILL.md:33                    "pip install guidance"
  MEDIUM   supply_chain   SKILL.md:36                    "pip install guidance 
# Hugging Face models"
  MEDIUM   supply_chain   SKILL.md:37                    "pip install guidance 
# llama.cpp models"

Decision: ALLOWED — Allowed (builtin source, safe verdict)
Installed: guidance
Files: SKILL.md, references\backends.md, references\constraints.md, 
references\examples.md

Updating: here-now

Fetching: official/productivity\here-now
Warning: 'here-now' is already installed at here-now
Quarantined to .hub\quarantine\here-now
Running security scan...
Scan: here-now (official/builtin)  Verdict: DANGEROUS
  CRITICAL exfiltration   scripts\publish.sh:95          "API_KEY=$(cat 
"$CREDENTIALS_FILE" | tr -d '[:space:]')"

Decision: ALLOWED — Allowed (builtin source, dangerous verdict)
Installed: here-now
Files: SKILL.md, scripts\drive.sh, scripts\publish.sh

Updating: accelerate

Fetching: official/mlops\accelerate
Warning: 'accelerate' is already installed at accelerate
Quarantined to .hub\quarantine\accelerate
Running security scan...
Scan: accelerate (official/builtin)  Verdict: CAUTION
  HIGH     exfiltration   references\performance.md:303  
"os.environ["TOKENIZERS_PARALLELISM"] = "true""
  MEDIUM   supply_chain   SKILL.md:23                    "pip install 
accelerate"
  MEDIUM   supply_chain   SKILL.md:322                   "- **DeepSpeed**: 
`deepspeed` (pip install deepspeed)"
  MEDIUM   supply_chain   references\megatron-integration.md:21 "pip install -e
."
  MEDIUM   supply_chain   references\megatron-integration.md:26 "pip install -v
--disable-pip-version-check --no-cache-dir --"
  MEDIUM   supply_chain   references\megatron-integration.md:19 "git clone 
https://github.com/NVIDIA/Megatron-LM.git"
  MEDIUM   supply_chain   references\megatron-integration.md:24 "git clone 
https://github.com/NVIDIA/apex"
  MEDIUM   supply_chain   references\performance.md:180  "# pip install 
flash-attn"

Decision: ALLOWED — Allowed (builtin source, caution verdict)
Installed: accelerate
Files: SKILL.md, references\custom-plugins.md, 
references\megatron-integration.md, references\performance.md

Updating: huggingface-tokenizers

Fetching: official/mlops\huggingface-tokenizers
Warning: 'huggingface-tokenizers' is already installed at 
huggingface-tokenizers
Quarantined to .hub\quarantine\huggingface-tokenizers
Running security scan...
Scan: huggingface-tokenizers (official/builtin)  Verdict: SAFE
  MEDIUM   supply_chain   SKILL.md:44                    "pip install 
tokenizers"
  MEDIUM   supply_chain   SKILL.md:47                    "pip install 
tokenizers transformers"
  MEDIUM   supply_chain   references\integration.md:561  "pip install 
tokenizers"

Decision: ALLOWED — Allowed (builtin source, safe verdict)
Installed: huggingface-tokenizers
Files: SKILL.md, references\algorithms.md, references\integration.md, 
references\pipeline.md, references\training.md

Updating: hyperframes

Fetching: official/creative\hyperframes
Warning: 'hyperframes' is already installed at hyperframes
Quarantined to .hub\quarantine\hyperframes
Running security scan...
Scan: hyperframes (official/builtin)  Verdict: CAUTION
  HIGH     privilege_escalation references\troubleshooting.md:61 "| Ubuntu / 
Debian | `sudo apt-get install -y ffmpeg`    |"
  HIGH     privilege_escalation references\troubleshooting.md:62 "| Fedora / 
RHEL   | `sudo dnf install -y ffmpeg`        |"
  HIGH     privilege_escalation references\troubleshooting.md:63 "| Arch       
| `sudo pacman -S ffmpeg`             |"
  HIGH     privilege_escalation scripts\setup.sh:48            "Linux*)   echo 
"   sudo apt-get install -y ffmpeg   # Debian"
  HIGH     privilege_escalation scripts\setup.sh:49            "echo "   sudo 
dnf install -y ffmpeg       # Fedora/RHEL";;"
  HIGH     privilege_escalation scripts\setup.sh:82            "echo "   Try: 
sudo npm install -g hyperframes@latest""
  HIGH     privilege_escalation scripts\setup.sh:97            "echo "   Try 
'npm install -g hyperframes@latest' or 'sudo np"
  MEDIUM   supply_chain   SKILL.md:63                    "2. Installs the 
`hyperframes` CLI globally (`npm install -g "
  MEDIUM   supply_chain   references\cli.md:3            "Everything runs 
through `npx hyperframes` (or the globally-i"
  MEDIUM   supply_chain   references\troubleshooting.md:20 "npm install -g 
hyperframes@latest"
  MEDIUM   supply_chain   scripts\setup.sh:80            "if ! npm install -g 
"hyperframes@latest" >/dev/null 2>&1; th"
  MEDIUM   supply_chain   scripts\setup.sh:81            "red "✗ npm install -g
hyperframes@latest failed.""
  MEDIUM   supply_chain   scripts\setup.sh:82            "echo "   Try: sudo 
npm install -g hyperframes@latest""
  MEDIUM   supply_chain   scripts\setup.sh:97            "echo "   Try 'npm 
install -g hyperframes@latest' or 'sudo np"

Decision: ALLOWED — Allowed (builtin source, caution verdict)
Installed: hyperframes
Files: SKILL.md, references\cli.md, references\composition.md, 
references\features.md, references\gsap.md, references\troubleshooting.md, 
references\website-to-video.md, scripts\setup.sh

Updating: hyperliquid

Fetching: official/blockchain\hyperliquid
Warning: 'hyperliquid' is already installed at hyperliquid
Quarantined to .hub\quarantine\hyperliquid
Running security scan...
Scan: hyperliquid (official/builtin)  Verdict: CAUTION
  HIGH     exfiltration   scripts\hyperliquid_client.py:87 "value = 
os.environ.get(key, "").strip()"

Decision: ALLOWED — Allowed (builtin source, caution verdict)
Installed: hyperliquid
Files: SKILL.md, scripts\hyperliquid_client.py

Updating: creative-ideation

Fetching: official/creative\creative-ideation
Warning: 'creative-ideation' is already installed at creative-ideation
Quarantined to .hub\quarantine\creative-ideation
Running security scan...
Scan: creative-ideation (official/builtin)  Verdict: SAFE
Decision: ALLOWED — Allowed (builtin source, safe verdict)
Installed: creative-ideation
Files: SKILL.md, references\anti-slop.md, references\exercises.md, 
references\full-prompt-library.md, references\heuristics.md, 
references\method-catalog.md, references\methods\affinity-diagrams.md, 
references\methods\analogy-and-blending.md, references\methods\biomimicry.md, 
references\methods\chance-and-remix.md, 
references\methods\compression-progress.md, 
references\methods\creative-discipline.md, 
references\methods\defamiliarization.md, 
references\methods\derive-and-mapping.md, 
references\methods\first-principles.md, references\methods\jobs-to-be-done.md, 
references\methods\lateral-provocations.md, 
references\methods\leverage-points.md, 
references\methods\oblique-strategies.md, references\methods\oulipo.md, 
references\methods\pataphysics.md, references\methods\pattern-languages.md, 
references\methods\polya.md, references\methods\premortem-and-inversion.md, 
references\methods\scamper.md, references\methods\story-skeletons.md, 
references\methods\triz-principles.md, references\methods\volume-generation.md

Updating: cli

Fetching: official/devops\cli
Warning: 'cli' is already installed at cli
Quarantined to .hub\quarantine\cli
Running security scan...
Scan: cli (official/builtin)  Verdict: DANGEROUS
  CRITICAL supply_chain   SKILL.md:40                    "curl -fsSL 
https://cli.inference.sh | sh"
  CRITICAL supply_chain   references\authentication.md:6 "curl -fsSL 
https://cli.inference.sh | sh"
  CRITICAL supply_chain   references\authentication.md:44 "curl -fsSL 
https://cli.inference.sh | sh"
  CRITICAL destructive    references\cli-reference.md:78 "infsh completion bash
> /etc/bash_completion.d/infsh"
  CRITICAL supply_chain   references\cli-reference.md:6  "curl -fsSL 
https://cli.inference.sh | sh"

Decision: ALLOWED — Allowed (builtin source, dangerous verdict)
Installed: cli
Files: SKILL.md, references\app-discovery.md, references\authentication.md, 
references\cli-reference.md, references\running-apps.md

Updating: instructor

Fetching: official/mlops\instructor
Warning: 'instructor' is already installed at instructor
Quarantined to .hub\quarantine\instructor
Running security scan...
Scan: instructor (official/builtin)  Verdict: SAFE
  MEDIUM   supply_chain   SKILL.md:33                    "pip install 
instructor"
  MEDIUM   supply_chain   SKILL.md:36                    "pip install 
"instructor"  # Anthropic Claude"
  MEDIUM   supply_chain   SKILL.md:37                    "pip install 
"instructor"     # OpenAI"
  MEDIUM   supply_chain   SKILL.md:38                    "pip install 
"instructor"        # All providers"

Decision: ALLOWED — Allowed (builtin source, safe verdict)
Installed: instructor
Files: SKILL.md, references\examples.md, references\providers.md, 
references\validation.md

Updating: kanban-video-orchestrator

Fetching: official/creative\kanban-video-orchestrator
Warning: 'kanban-video-orchestrator' is already installed at 
kanban-video-orchestrator
Quarantined to .hub\quarantine\kanban-video-orchestrator
Running security scan...
Scan: kanban-video-orchestrator (official/builtin)  Verdict: SAFE
  MEDIUM   supply_chain   references\kanban-setup.md:120 "installs). If absent:
`pip install pyyaml`."
  MEDIUM   persistence    scripts\bootstrap_pipeline.py:106 
"f"team[{i}].profile {t['profile']!r} must match ""
  MEDIUM   persistence    scripts\bootstrap_pipeline.py:111 
"f"team[{i}].profile {t['profile']!r} is duplicated""
  MEDIUM   execution      scripts\monitor.py:37          "out = 
subprocess.run("
  MEDIUM   execution      scripts\monitor.py:46          "out = 
subprocess.run("
  MEDIUM   execution      scripts\monitor.py:70          "out = 
subprocess.run("

Decision: ALLOWED — Allowed (builtin source, safe verdict)
Installed: kanban-video-orchestrator
Files: SKILL.md, assets\brief.md.tmpl, assets\setup.sh.tmpl, 
assets\soul.md.tmpl, references\examples.md, references\intake.md, 
references\kanban-setup.md, references\monitoring.md, 
references\role-archetypes.md, references\tool-matrix.md, 
scripts\bootstrap_pipeline.py, scripts\monitor.py

Updating: lambda-labs

Fetching: official/mlops\lambda-labs
Warning: 'lambda-labs' is already installed at lambda-labs
Quarantined to .hub\quarantine\lambda-labs
Running security scan...
Scan: lambda-labs (official/builtin)  Verdict: DANGEROUS
  CRITICAL exfiltration   SKILL.md:225                   "curl -u 
$LAMBDA_API_KEY: \"
  CRITICAL exfiltration   SKILL.md:232                   "curl -u 
$LAMBDA_API_KEY: \"
  CRITICAL exfiltration   SKILL.md:245                   "curl -u 
$LAMBDA_API_KEY: \"
  CRITICAL persistence    SKILL.md:309                   "echo 'ssh-rsa 
AAAA...' >> ~/.ssh/authorized_keys"
  CRITICAL persistence    references\advanced-usage.md:578 "# Update 
authorized_keys on running instances"
  CRITICAL persistence    references\advanced-usage.md:579 "ssh ubuntu@<IP> 
"echo '$(cat ~/.ssh/lambda_key_new.pub)' >> "
  CRITICAL exfiltration   references\troubleshooting.md:12 "curl -u 
$LAMBDA_API_KEY: \"
  CRITICAL exfiltration   references\troubleshooting.md:50 "curl -u 
$LAMBDA_API_KEY: \"
  CRITICAL exfiltration   references\troubleshooting.md:82 "curl -u 
$LAMBDA_API_KEY: \"
  CRITICAL exfiltration   references\troubleshooting.md:479 "curl -u 
$LAMBDA_API_KEY: \"
  CRITICAL persistence    references\troubleshooting.md:102 "# Check 
authorized_keys on instance (if you have another way"
  CRITICAL persistence    references\troubleshooting.md:103 "cat 
~/.ssh/authorized_keys"
  HIGH     exfiltration   SKILL.md:68                    "ssh -i 
~/.ssh/lambda_key ubuntu@<INSTANCE-IP>"
  HIGH     exfiltration   SKILL.md:299                   "ssh-keygen -t ed25519
-f ~/.ssh/lambda_key"
  HIGH     exfiltration   SKILL.md:309                   "echo 'ssh-rsa 
AAAA...' >> ~/.ssh/authorized_keys"
  HIGH     exfiltration   SKILL.md:148                   
"access_token=os.environ["LAMBDA_API_KEY"]"
  HIGH     exfiltration   references\advanced-usage.md:253 
"run_remote_job(instance["ip"], "~/.ssh/lambda_key", commands"
  HIGH     exfiltration   references\advanced-usage.md:575 "ssh-keygen -t 
ed25519 -f ~/.ssh/lambda_key_new -C "lambda-$("
  HIGH     exfiltration   references\advanced-usage.md:579 "ssh ubuntu@<IP> 
"echo '$(cat ~/.ssh/lambda_key_new.pub)' >> "
  HIGH     exfiltration   references\advanced-usage.md:582 "ssh -i 
~/.ssh/lambda_key_new ubuntu@<IP>"
  HIGH     exfiltration   references\advanced-usage.md:16 "rank = 
int(os.environ["RANK"])"
  HIGH     exfiltration   references\advanced-usage.md:17 "world_size = 
int(os.environ["WORLD_SIZE"])"
  HIGH     exfiltration   references\advanced-usage.md:18 "local_rank = 
int(os.environ["LOCAL_RANK"])"
  HIGH     exfiltration   references\advanced-usage.md:208 "manager = 
LambdaJobManager(os.environ["LAMBDA_API_KEY"])"
  HIGH     exfiltration   references\advanced-usage.md:474 
"wandb.login(key=os.environ["WANDB_API_KEY"])"
  HIGH     exfiltration   references\troubleshooting.md:93 "ssh -v -i 
~/.ssh/lambda_key ubuntu@<IP>"
  HIGH     exfiltration   references\troubleshooting.md:96 "chmod 600 
~/.ssh/lambda_key"
  HIGH     exfiltration   references\troubleshooting.md:97 "chmod 644 
~/.ssh/lambda_key.pub"
  HIGH     exfiltration   references\troubleshooting.md:103 "cat 
~/.ssh/authorized_keys"
  HIGH     exfiltration   references\troubleshooting.md:513 "| `Module not 
found` | Wrong Python env | Activate correct v"
  HIGH     privilege_escalation references\troubleshooting.md:145 "sudo reboot"
  HIGH     privilege_escalation references\troubleshooting.md:149 "sudo reboot"
  HIGH     privilege_escalation references\troubleshooting.md:197 "sudo reboot"
  HIGH     privilege_escalation references\troubleshooting.md:380 "sudo apt 
install python3.11 python3.11-venv python3.11-dev"
  MEDIUM   persistence    SKILL.md:299                   "ssh-keygen -t ed25519
-f ~/.ssh/lambda_key"
  MEDIUM   supply_chain   SKILL.md:136                   "pip install 
lambda-cloud-client"
  MEDIUM   supply_chain   SKILL.md:476                   "pip install 
transformers accelerate peft"
  MEDIUM   supply_chain   SKILL.md:360                   "git clone 
https://github.com/user/project"
  MEDIUM   persistence    references\advanced-usage.md:609 "# On instance, 
store in ~/.bashrc"
  MEDIUM   persistence    references\advanced-usage.md:610 "echo 'export 
HF_TOKEN="..."' >> ~/.bashrc"
  MEDIUM   persistence    references\advanced-usage.md:575 "ssh-keygen -t 
ed25519 -f ~/.ssh/lambda_key_new -C "lambda-$("
  MEDIUM   supply_chain   references\advanced-usage.md:389 "pip install torch 
transformers accelerate"
  MEDIUM   persistence    references\troubleshooting.md:114 "ssh-keygen -R 
<IP>"
  MEDIUM   supply_chain   references\troubleshooting.md:328 "pip install 
hf_transfer"
  MEDIUM   supply_chain   references\troubleshooting.md:364 "pip install 
<package>"
  MEDIUM   supply_chain   references\troubleshooting.md:367 "pip install torch 
--index-url https://download.pytorch.org/w"
  MEDIUM   supply_chain   references\troubleshooting.md:402 "pip install 
<package>"

Decision: ALLOWED — Allowed (builtin source, dangerous verdict)
Installed: lambda-labs
Files: SKILL.md, references\advanced-usage.md, references\troubleshooting.md

Updating: llava

Fetching: official/mlops\llava
Warning: 'llava' is already installed at llava
Quarantined to .hub\quarantine\llava
Running security scan...
Scan: llava (official/builtin)  Verdict: SAFE
  MEDIUM   supply_chain   SKILL.md:51                    "pip install -e ."
  MEDIUM   supply_chain   SKILL.md:47                    "git clone 
https://github.com/haotian-liu/LLaVA"

Decision: ALLOWED — Allowed (builtin source, safe verdict)
Installed: llava
Files: SKILL.md, references\training.md

Updating: meme-generation

Fetching: official/creative\meme-generation
Warning: 'meme-generation' is already installed at meme-generation
Quarantined to .hub\quarantine\meme-generation
Running security scan...
Scan: meme-generation (official/builtin)  Verdict: SAFE
Decision: ALLOWED — Allowed (builtin source, safe verdict)
Installed: meme-generation
Files: EXAMPLES.md, SKILL.md, scripts\generate_meme.py, scripts\templates.json

Updating: memento-flashcards

Fetching: official/productivity\memento-flashcards
Warning: 'memento-flashcards' is already installed at memento-flashcards
Quarantined to .hub\quarantine\memento-flashcards
Running security scan...
Scan: memento-flashcards (official/builtin)  Verdict: SAFE
  MEDIUM   supply_chain   SKILL.md:211                   "pip install 
youtube-transcript-api"
  MEDIUM   supply_chain   SKILL.md:302                   "- **Optional 
dependency** — `youtube_quiz.py` needs `youtube"
  MEDIUM   supply_chain   scripts\youtube_quiz.py:4      "Requires: pip install
youtube-transcript-api"
  MEDIUM   supply_chain   scripts\youtube_quiz.py:35     ""message": "Run: pip 
install youtube-transcript-api","

Decision: ALLOWED — Allowed (builtin source, safe verdict)
Installed: memento-flashcards
Files: SKILL.md, scripts\memento_cards.py, scripts\youtube_quiz.py

Updating: modal

Fetching: official/mlops\modal
Warning: 'modal' is already installed at modal
Quarantined to .hub\quarantine\modal
Running security scan...
Scan: modal (official/builtin)  Verdict: DANGEROUS
  CRITICAL exfiltration   references\troubleshooting.md:371 "value = 
os.environ.get("KEY")  # Use get() to handle missing"
  HIGH     exfiltration   SKILL.md:242                   "token = 
os.environ["HF_TOKEN"]"
  HIGH     obfuscation    references\advanced-usage.md:478 "result = 
sandbox.exec("python", "-c", "print('Hello from san"
  HIGH     exfiltration   references\troubleshooting.md:371 "value = 
os.environ.get("KEY")  # Use get() to handle missing"
  MEDIUM   execution      SKILL.md:62                    "return 
subprocess.run(["nvidia-smi"], capture_output=True, t"
  MEDIUM   supply_chain   SKILL.md:48                    "pip install modal"
  MEDIUM   execution      references\advanced-usage.md:60 
"subprocess.run(["python", "-m", "torch.distributed.launch", "
  MEDIUM   execution      references\troubleshooting.md:158 "result = 
subprocess.run(["nvidia-smi"], capture_output=True,"
  MEDIUM   execution      references\troubleshooting.md:458 
"print(subprocess.run(["nvidia-smi"], capture_output=True, te"
  MEDIUM   execution      references\troubleshooting.md:459 
"print(subprocess.run(["pip", "list"], capture_output=True, t"
  MEDIUM   supply_chain   references\troubleshooting.md:24 "**Error**: `pip 
install modal` fails"
  MEDIUM   supply_chain   references\troubleshooting.md:29 "pip install 
--upgrade pip"
  MEDIUM   supply_chain   references\troubleshooting.md:32 "python3.11 -m pip 
install modal"
  MEDIUM   supply_chain   references\troubleshooting.md:35 "pip install modal 
--prefer-binary"

Decision: ALLOWED — Allowed (builtin source, dangerous verdict)
Installed: modal
Files: SKILL.md, references\advanced-usage.md, references\troubleshooting.md

Updating: nemo-curator

Fetching: official/mlops\nemo-curator
Warning: 'nemo-curator' is already installed at nemo-curator
Quarantined to .hub\quarantine\nemo-curator
Running security scan...
Scan: nemo-curator (official/builtin)  Verdict: SAFE
  MEDIUM   supply_chain   SKILL.md:44                    "uv pip install 
"nemo-curator""
  MEDIUM   supply_chain   SKILL.md:47                    "uv pip install 
"nemo-curator""
  MEDIUM   supply_chain   SKILL.md:50                    "uv pip install 
"nemo-curator""

Decision: ALLOWED — Allowed (builtin source, safe verdict)
Installed: nemo-curator
Files: SKILL.md, references\deduplication.md, references\filtering.md

Updating: neuroskill-bci

Fetching: official/health\neuroskill-bci
Warning: 'neuroskill-bci' is already installed at neuroskill-bci
Quarantined to .hub\quarantine\neuroskill-bci
Running security scan...
Scan: neuroskill-bci (official/builtin)  Verdict: SAFE
  MEDIUM   network        references\api.md:28           "curl -s -X POST 
http://127.0.0.1:8375/ \"
  MEDIUM   network        references\api.md:58           "Connect to 
`ws://127.0.0.1:8375/` to receive real-time event"

Decision: ALLOWED — Allowed (builtin source, safe verdict)
Installed: neuroskill-bci
Files: SKILL.md, references\api.md, references\metrics.md, 
references\protocols.md

Updating: openclaw-migration

Fetching: official/migration\openclaw-migration
Warning: 'openclaw-migration' is already installed at openclaw-migration
Quarantined to .hub\quarantine\openclaw-migration
Running security scan...
Scan: openclaw-migration (official/builtin)  Verdict: DANGEROUS
  CRITICAL persistence    scripts\openclaw_to_hermes.py:1148 
"self.record("workspace-agents", "workspace/AGENTS.md", "", ""
  CRITICAL persistence    scripts\openclaw_to_hermes.py:1335 "# OpenClaw's 
AGENTS.md, MEMORY.md, etc."
  CRITICAL persistence    scripts\openclaw_to_hermes.py:419 
"``~/AppData/Local/hermes/config.yaml`` (the real Hermes home) instead of "
  CRITICAL persistence    scripts\openclaw_to_hermes.py:420 
"``~/.Hermes/config.yaml``."
  CRITICAL persistence    scripts\openclaw_to_hermes.py:2949 ""- Review 
`~/AppData/Local/hermes/config.yaml` for any adjustments","
  CRITICAL persistence    scripts\openclaw_to_hermes.py:3116 "print("    1. 
Review ~/AppData/Local/hermes/config.yaml")"

Decision: ALLOWED — Allowed (builtin source, dangerous verdict)
Installed: openclaw-migration
Files: SKILL.md, scripts\openclaw_to_hermes.py

Updating: flash-attention

Fetching: official/mlops\flash-attention
Warning: 'flash-attention' is already installed at flash-attention
Quarantined to .hub\quarantine\flash-attention
Running security scan...
Scan: flash-attention (official/builtin)  Verdict: SAFE
  MEDIUM   supply_chain   SKILL.md:36                    "pip install 
flash-attn --no-build-isolation"
  MEDIUM   supply_chain   SKILL.md:69                    "pip install --upgrade
torch"
  MEDIUM   supply_chain   SKILL.md:157                   "pip install 
flash-attn --no-build-isolation"
  MEDIUM   supply_chain   SKILL.md:253                   "pip install 
flash-attn --no-build-isolation"
  MEDIUM   supply_chain   SKILL.md:302                   "pip install 
flash-attn --no-build-isolation"
  MEDIUM   supply_chain   SKILL.md:308                   "pip install 
flash-attn --no-build-isolation"
  MEDIUM   supply_chain   references\transformers-integration.md:28 "pip 
install transformers>=4.36"
  MEDIUM   supply_chain   references\transformers-integration.md:29 "pip 
install flash-attn --no-build-isolation"
  MEDIUM   supply_chain   references\transformers-integration.md:249 "pip 
install flash-attn --no-build-isolation"

Decision: ALLOWED — Allowed (builtin source, safe verdict)
Installed: flash-attention
Files: SKILL.md, references\benchmarks.md, 
references\transformers-integration.md

Updating: osint-investigation

Fetching: official/research\osint-investigation
Warning: 'osint-investigation' is already installed at osint-investigation
Quarantined to .hub\quarantine\osint-investigation
Running security scan...
Scan: osint-investigation (official/builtin)  Verdict: DANGEROUS
  CRITICAL exfiltration   scripts\fetch_courtlistener.py:130 
"p.add_argument("--token", default=os.environ.get("COURTLISTE"
  CRITICAL exfiltration   scripts\fetch_opencorporates.py:176 
"p.add_argument("--token", default=os.environ.get("OPENCORPOR"
  CRITICAL exfiltration   scripts\fetch_senate_ld.py:127 
"p.add_argument("--token", default=os.environ.get("SENATE_LDA"
  HIGH     exfiltration   scripts\fetch_courtlistener.py:130 
"p.add_argument("--token", default=os.environ.get("COURTLISTE"
  HIGH     exfiltration   scripts\fetch_opencorporates.py:176 
"p.add_argument("--token", default=os.environ.get("OPENCORPOR"
  HIGH     exfiltration   scripts\fetch_senate_ld.py:127 
"p.add_argument("--token", default=os.environ.get("SENATE_LDA"

Decision: ALLOWED — Allowed (builtin source, dangerous verdict)
Installed: osint-investigation
Files: SKILL.md, references\sources\courtlistener.md, 
references\sources\gdelt.md, references\sources\icij-offshore.md, 
references\sources\nyc-acris.md, references\sources\ofac-sdn.md, 
references\sources\opencorporates.md, references\sources\sec-edgar.md, 
references\sources\senate-ld.md, references\sources\usaspending.md, 
references\sources\wayback.md, references\sources\wikipedia.md, 
scripts\build_findings.py, scripts\entity_resolution.py, 
scripts\fetch_courtlistener.py, scripts\fetch_gdelt.py, 
scripts\fetch_icij_offshore.py, scripts\fetch_nyc_acris.py, 
scripts\fetch_ofac_sdn.py, scripts\fetch_opencorporates.py, 
scripts\fetch_sec_edgar.py, scripts\fetch_senate_ld.py, 
scripts\fetch_usaspending.py, scripts\fetch_wayback.py, 
scripts\fetch_wikipedia.py, scripts\timing_analysis.py, scripts\_http.py, 
scripts\_normalize.py, templates\source-template.md

Updating: oss-forensics

Fetching: official/security\oss-forensics
Warning: 'oss-forensics' is already installed at oss-forensics
Quarantined to .hub\quarantine\oss-forensics
Running security scan...
Scan: oss-forensics (official/builtin)  Verdict: DANGEROUS
  CRITICAL supply_chain   references\recovery-techniques.md:89 "curl -s 
"https://web.archive.org/cdx/search/cdx?url=github.c"
  CRITICAL supply_chain   references\recovery-techniques.md:97 "curl -s 
"https://web.archive.org/cdx/search/cdx?url=github.c"
  CRITICAL supply_chain   references\recovery-techniques.md:130 "curl -s 
"https://api.github.com/repos/OWNER/REPO/contents/pa"
  CRITICAL traversal      templates\malicious-package-report.md:17 "- 
**Exfiltrated Data Types**: [Environment variables, ~/.ssh"
  HIGH     exfiltration   templates\malicious-package-report.md:17 "- 
**Exfiltrated Data Types**: [Environment variables, ~/.ssh"
  MEDIUM   supply_chain   SKILL.md:123                   "git clone 
https://github.com/OWNER/REPO.git target_repo && c"

Decision: ALLOWED — Allowed (builtin source, dangerous verdict)
Installed: oss-forensics
Files: SKILL.md, references\evidence-types.md, 
references\github-archive-guide.md, references\investigation-templates.md, 
references\recovery-techniques.md, scripts\evidence-store.py, 
templates\forensic-report.md, templates\malicious-package-report.md

Updating: peft

Fetching: official/mlops\peft
Warning: 'peft' is already installed at peft
Quarantined to .hub\quarantine\peft
Running security scan...
Scan: peft (official/builtin)  Verdict: SAFE
  MEDIUM   supply_chain   SKILL.md:43                    "pip install peft"
  MEDIUM   supply_chain   SKILL.md:46                    "pip install peft 
bitsandbytes"
  MEDIUM   supply_chain   SKILL.md:49                    "pip install peft 
transformers accelerate bitsandbytes datase"
  MEDIUM   supply_chain   references\troubleshooting.md:16 "pip install 
bitsandbytes --no-cache-dir"
  MEDIUM   supply_chain   references\troubleshooting.md:22 "pip install ."
  MEDIUM   supply_chain   references\troubleshooting.md:32 "pip install triton"
  MEDIUM   supply_chain   references\troubleshooting.md:46 "pip install 
peft>=0.13.0 --upgrade"
  MEDIUM   supply_chain   references\troubleshooting.md:19 "git clone 
https://github.com/TimDettmers/bitsandbytes.git"

Decision: ALLOWED — Allowed (builtin source, safe verdict)
Installed: peft
Files: SKILL.md, references\advanced-usage.md, references\troubleshooting.md

Updating: pinecone

Fetching: official/mlops\pinecone
Warning: 'pinecone' is already installed at pinecone
Quarantined to .hub\quarantine\pinecone
Running security scan...
Scan: pinecone (official/builtin)  Verdict: SAFE
  MEDIUM   supply_chain   SKILL.md:45                    "pip install 
pinecone-client"

Decision: ALLOWED — Allowed (builtin source, safe verdict)
Installed: pinecone
Files: SKILL.md, references\deployment.md

Updating: pixel-art

Fetching: official/creative\pixel-art
Warning: 'pixel-art' is already installed at pixel-art
Quarantined to .hub\quarantine\pixel-art
Running security scan...
Scan: pixel-art (official/builtin)  Verdict: SAFE
  MEDIUM   execution      ATTRIBUTION.md:31              "- `ffmpeg` invocation
switched from `os.system` to `subproce"
  MEDIUM   supply_chain   SKILL.md:191                   "- Pillow (`pip 
install Pillow`)"
  MEDIUM   execution      scripts\pixel_art_video.py:297 "subprocess.run("
  MEDIUM   execution      scripts\pixel_art_video.py:309 "subprocess.run("

Decision: ALLOWED — Allowed (builtin source, safe verdict)
Installed: pixel-art
Files: ATTRIBUTION.md, SKILL.md, references\palettes.md, scripts\palettes.py, 
scripts\pixel_art.py, scripts\pixel_art_video.py, scripts\__init__.py

Updating: pytorch-fsdp

Fetching: official/mlops\pytorch-fsdp
Warning: 'pytorch-fsdp' is already installed at pytorch-fsdp
Quarantined to .hub\quarantine\pytorch-fsdp
Running security scan...
Scan: pytorch-fsdp (official/builtin)  Verdict: CAUTION
  HIGH     exfiltration   SKILL.md:38                    "**Pattern 2:** 
Distributed communication package - torch.dis"
  HIGH     exfiltration   references\other.md:1724       "5. Another way to 
pass local_rank to the subprocesses via en"
  MEDIUM   structural     references\other.md:0          "333KB"
  MEDIUM   network        SKILL.md:38                    "**Pattern 2:** 
Distributed communication package - torch.dis"
  MEDIUM   network        SKILL.md:44                    "**Pattern 3:** 
Initialization# The package needs to be initi"

Decision: ALLOWED — Allowed (builtin source, caution verdict)
Installed: pytorch-fsdp
Files: SKILL.md, references\index.md, references\other.md

Updating: pytorch-lightning

Fetching: official/mlops\pytorch-lightning
Warning: 'pytorch-lightning' is already installed at pytorch-lightning
Quarantined to .hub\quarantine\pytorch-lightning
Running security scan...
Scan: pytorch-lightning (official/builtin)  Verdict: SAFE
  MEDIUM   supply_chain   SKILL.md:23                    "pip install 
lightning"
  MEDIUM   supply_chain   references\distributed.md:276  "# pip install 
transformer-engine"
  MEDIUM   supply_chain   references\hyperparameter-tuning.md:11 "pip install 
ray"
  MEDIUM   supply_chain   references\hyperparameter-tuning.md:12 "pip install 
lightning"
  MEDIUM   supply_chain   references\hyperparameter-tuning.md:102 "pip install 
optuna"
  MEDIUM   supply_chain   references\hyperparameter-tuning.md:103 "pip install 
optuna-integration"
  MEDIUM   supply_chain   references\hyperparameter-tuning.md:179 "pip install 
wandb"
  MEDIUM   supply_chain   references\hyperparameter-tuning.md:251 "pip install 
hyperopt"

Decision: ALLOWED — Allowed (builtin source, safe verdict)
Installed: pytorch-lightning
Files: SKILL.md, references\callbacks.md, references\distributed.md, 
references\hyperparameter-tuning.md

Updating: qdrant

Fetching: official/mlops\qdrant
Warning: 'qdrant' is already installed at qdrant
Quarantined to .hub\quarantine\qdrant
Running security scan...
Scan: qdrant (official/builtin)  Verdict: CAUTION
  HIGH     privilege_escalation references\troubleshooting.md:12 "sudo 
systemctl start docker"
  MEDIUM   supply_chain   SKILL.md:49                    "pip install 
qdrant-client"
  MEDIUM   persistence    references\troubleshooting.md:12 "sudo systemctl 
start docker"
  MEDIUM   supply_chain   references\troubleshooting.md:35 "pip install 
qdrant-client"
  MEDIUM   supply_chain   references\troubleshooting.md:38 "pip install 
qdrant-client>=1.12.0"
  MEDIUM   supply_chain   references\troubleshooting.md:46 "pip install 
'qdrant-client'"

Decision: ALLOWED — Allowed (builtin source, caution verdict)
Installed: qdrant
Files: SKILL.md, references\advanced-usage.md, references\troubleshooting.md

Updating: searxng-search

Fetching: official/research\searxng-search
Warning: 'searxng-search' is already installed at searxng-search
Quarantined to .hub\quarantine\searxng-search
Running security scan...
Scan: searxng-search (official/builtin)  Verdict: SAFE
  MEDIUM   supply_chain   SKILL.md:132                   "pip install 
searxng-data"
  MEDIUM   supply_chain   SKILL.md:160                   "pip install searxng"

Decision: ALLOWED — Allowed (builtin source, safe verdict)
Installed: searxng-search
Files: SKILL.md, scripts\searxng.sh

Updating: simpo

Fetching: official/mlops\simpo
Warning: 'simpo' is already installed at simpo
Quarantined to .hub\quarantine\simpo
Running security scan...
Scan: simpo (official/builtin)  Verdict: SAFE
  MEDIUM   supply_chain   SKILL.md:32                    "python -m pip install
."
  MEDIUM   supply_chain   SKILL.md:35                    "python -m pip install
flash-attn --no-build-isolation"
  MEDIUM   supply_chain   SKILL.md:30                    "git clone 
https://github.com/huggingface/alignment-handbook."

Decision: ALLOWED — Allowed (builtin source, safe verdict)
Installed: simpo
Files: SKILL.md, references\datasets.md, references\hyperparameters.md, 
references\loss-functions.md

Updating: solana

Fetching: official/blockchain\solana
Warning: 'solana' is already installed at solana
Quarantined to .hub\quarantine\solana
Running security scan...
Scan: solana (official/builtin)  Verdict: CAUTION
  HIGH     exfiltration   scripts\solana_client.py:31    "RPC_URL = 
os.environ.get("

Decision: ALLOWED — Allowed (builtin source, caution verdict)
Installed: solana
Files: SKILL.md, scripts\solana_client.py

Updating: stable-diffusion

Fetching: official/mlops\stable-diffusion
Warning: 'stable-diffusion' is already installed at stable-diffusion
Quarantined to .hub\quarantine\stable-diffusion
Running security scan...
Scan: stable-diffusion (official/builtin)  Verdict: SAFE
  MEDIUM   supply_chain   SKILL.md:48                    "pip install diffusers
transformers accelerate torch"
  MEDIUM   supply_chain   SKILL.md:49                    "pip install xformers 
# Optional: memory-efficient attention"
  MEDIUM   supply_chain   references\troubleshooting.md:12 "pip install 
--upgrade huggingface_hub"
  MEDIUM   supply_chain   references\troubleshooting.md:15 "pip install 
--upgrade diffusers"
  MEDIUM   supply_chain   references\troubleshooting.md:28 "pip install 
xformers --index-url https://download.pytorch.or"
  MEDIUM   supply_chain   references\troubleshooting.md:31 "pip install -v -U 
git+https://github.com/facebookresearch/xf"
  MEDIUM   supply_chain   references\troubleshooting.md:45 "pip install torch 
torchvision --index-url https://download.p"

Decision: ALLOWED — Allowed (builtin source, safe verdict)
Installed: stable-diffusion
Files: SKILL.md, references\advanced-usage.md, references\troubleshooting.md

Updating: stocks

Fetching: official/finance\stocks
Warning: 'stocks' is already installed at stocks
Quarantined to .hub\quarantine\stocks
Running security scan...
Scan: stocks (official/builtin)  Verdict: DANGEROUS
  CRITICAL exfiltration   scripts\stocks_client.py:247   "key = 
os.environ.get("ALPHA_VANTAGE_KEY")"
  CRITICAL exfiltration   scripts\stocks_client.py:381   "av_key = 
os.environ.get("ALPHA_VANTAGE_KEY")"
  HIGH     exfiltration   scripts\stocks_client.py:247   "key = 
os.environ.get("ALPHA_VANTAGE_KEY")"
  HIGH     exfiltration   scripts\stocks_client.py:381   "av_key = 
os.environ.get("ALPHA_VANTAGE_KEY")"

Decision: ALLOWED — Allowed (builtin source, dangerous verdict)
Installed: stocks
Files: SKILL.md, scripts\stocks_client.py

Updating: subagent-driven-development

Fetching: official/software-development\subagent-driven-development
Warning: 'subagent-driven-development' is already installed at 
subagent-driven-development
Quarantined to .hub\quarantine\subagent-driven-development
Running security scan...
Scan: subagent-driven-development (official/builtin)  Verdict: CAUTION
  HIGH     exfiltration   SKILL.md:271                   "Include TDD 
instructions in every implementer context."

Decision: ALLOWED — Allowed (builtin source, caution verdict)
Installed: subagent-driven-development
Files: SKILL.md, references\context-budget-discipline.md, 
references\gates-taxonomy.md

Updating: telephony

Fetching: official/productivity\telephony
Warning: 'telephony' is already installed at telephony
Quarantined to .hub\quarantine\telephony
Running security scan...
Scan: telephony (official/builtin)  Verdict: CAUTION
  HIGH     exfiltration   scripts\telephony.py:136       "value = 
os.environ.get(env_key, "")"

Decision: ALLOWED — Allowed (builtin source, caution verdict)
Installed: telephony
Files: SKILL.md, scripts\telephony.py

Updating: tensorrt-llm

Fetching: official/mlops\tensorrt-llm
Warning: 'tensorrt-llm' is already installed at tensorrt-llm
Quarantined to .hub\quarantine\tensorrt-llm
Running security scan...
Scan: tensorrt-llm (official/builtin)  Verdict: SAFE
  MEDIUM   supply_chain   SKILL.md:44                    "docker pull 
nvidia/tensorrt_llm:latest"
  MEDIUM   supply_chain   references\optimization.md:208 "pip install 
tensorrt_llm"

Decision: ALLOWED — Allowed (builtin source, safe verdict)
Installed: tensorrt-llm
Files: SKILL.md, references\multi-gpu.md, references\optimization.md, 
references\serving.md

Updating: watchers

Fetching: official/devops\watchers
Warning: 'watchers' is already installed at watchers
Quarantined to .hub\quarantine\watchers
Running security scan...
Scan: watchers (official/builtin)  Verdict: DANGEROUS
  CRITICAL exfiltration   scripts\watch_github.py:118    "token = 
os.environ.get("GITHUB_TOKEN") or os.environ.get("GH"
  HIGH     exfiltration   scripts\watch_github.py:118    "token = 
os.environ.get("GITHUB_TOKEN") or os.environ.get("GH"

Decision: ALLOWED — Allowed (builtin source, dangerous verdict)
Installed: watchers
Files: SKILL.md, scripts\watch_github.py, scripts\watch_http_json.py, 
scripts\watch_rss.py, scripts\_watermark.py

Updating: web-pentest

Fetching: official/security\web-pentest
Warning: 'web-pentest' is already installed at web-pentest
Quarantined to .hub\quarantine\web-pentest
Running security scan...
Scan: web-pentest (official/builtin)  Verdict: DANGEROUS
  CRITICAL destructive    SKILL.md:69                    "filesystem-write 
SSTI, command injection with `rm`/`shutdown"
  CRITICAL persistence    SKILL.md:83                    "in 
`~/AppData/Local/hermes/config.yaml` for the session."
  CRITICAL traversal      references\bypass-techniques.md:44 "- Null byte 
(older platforms): `../../../etc/passwd%00.png`"
  CRITICAL traversal      references\bypass-techniques.md:46 "- Absolute path: 
`/etc/passwd` (skips traversal entirely)"
  CRITICAL traversal      references\bypass-techniques.md:50 "- Try ending the 
path early: `../../etc/passwd%00`"
  CRITICAL traversal      references\exploitation-techniques.md:36 "Witness: 
`../../../../etc/passwd` (Linux) or `..\..\..\..\wi"
  CRITICAL exfiltration   scripts\recon-scan.sh:46       "echo "Could not parse
host from URL: $TARGET_URL" >&2"
  CRITICAL exfiltration   scripts\recon-scan.sh:81       "echo "Host '$HOST' is
NOT in $SCOPE_FILE. Refusing to scan.""
  CRITICAL exfiltration   scripts\recon-scan.sh:88       "echo " 
target=$TARGET_URL host=$HOST ts=$TS""
  HIGH     network        SKILL.md:245                   "webhook.site for 
sensitive engagements — exfil paths)."
  HIGH     execution      SKILL.md:144                   "2. **Inventory 
sinks** — every `execute(`, `os.system(`, `ev"
  HIGH     obfuscation    references\bypass-techniques.md:64 "- 
`onerror=eval('alert(1)')` → `onerror=eval(name)` + set"
  HIGH     traversal      references\bypass-techniques.md:44 "- Null byte 
(older platforms): `../../../etc/passwd%00.png`"
  HIGH     traversal      references\exploitation-techniques.md:36 "Witness: 
`../../../../etc/passwd` (Linux) or `..\..\..\..\wi"
  HIGH     execution      references\vuln-taxonomy.md:20 "| `CMD-shell` | 
`os.system("ls " + v)` | DON'T — refactor to"
  MEDIUM   execution      references\bypass-techniques.md:30 "- Substitution: 
`$(sleep 5)`, `` `sleep 5` ``"
  MEDIUM   execution      references\bypass-techniques.md:35 "- Encoding: 
`bash<<<$(base64 -d <<< c2xlZXAgNQo=)`"
  MEDIUM   traversal      references\bypass-techniques.md:44 "- Null byte 
(older platforms): `../../../etc/passwd%00.png`"
  MEDIUM   traversal      references\bypass-techniques.md:50 "- Try ending the 
path early: `../../etc/passwd%00`"
  MEDIUM   network        references\exploitation-techniques.md:165 "- Internal
recon (operator OK + scope): `http://127.0.0.1:63"
  MEDIUM   network        references\exploitation-techniques.md:166 
"`http://127.0.0.1:9200/`, `http://[::1]:80/`"
  MEDIUM   execution      references\exploitation-techniques.md:199 "- 
argv-list subprocess invocation (Python `subprocess.run([."
  MEDIUM   execution      references\exploitation-techniques.md:28 "- Linux: `;
sleep 5` or `$(sleep 5)` or `` `sleep 5` ``"
  MEDIUM   execution      references\exploitation-techniques.md:30 "- If output
is reflected: `; echo HERMESPENTEST-$(id)`"
  MEDIUM   traversal      references\exploitation-techniques.md:36 "Witness: 
`../../../../etc/passwd` (Linux) or `..\..\..\..\wi"
  MEDIUM   execution      references\vuln-taxonomy.md:19 "| `CMD-argument` | 
`subprocess.run(["ls", v])` | argv list ("
  MEDIUM   network        scripts\recon-scan.sh:8        "#   recon-scan.sh 
engagement-20260525-031415 http://127.0.0."

Decision: ALLOWED — Allowed (builtin source, dangerous verdict)
Installed: web-pentest
Files: SKILL.md, references\bypass-techniques.md, 
references\exploitation-techniques.md, references\scope-enforcement.md, 
references\vuln-taxonomy.md, scripts\recon-scan.sh, templates\authorization.md,
templates\exploitation-queue.json, templates\pentest-report.md

Updating: whisper

Fetching: official/mlops\whisper
Warning: 'whisper' is already installed at whisper
Quarantined to .hub\quarantine\whisper
Running security scan...
Scan: whisper (official/builtin)  Verdict: CAUTION
  HIGH     privilege_escalation SKILL.md:50                    "# Ubuntu: sudo 
apt install ffmpeg"
  MEDIUM   supply_chain   SKILL.md:46                    "pip install -U 
openai-whisper"
  MEDIUM   supply_chain   SKILL.md:198                   "# pip install 
faster-whisper"

Decision: ALLOWED — Allowed (builtin source, caution verdict)
Installed: whisper
Files: SKILL.md, references\languages.md

Updating: bun-nextjs

Fetching: skills-sh/secondsky/claude-skills/bun-nextjs
Warning: 'bun-nextjs' is already installed at bun-nextjs
Quarantined to .hub\quarantine\bun-nextjs
Running security scan...
Scan: bun-nextjs (skills-sh/secondsky/claude-skills/bun-nextjs/community)  
Verdict: SAFE
  MEDIUM   supply_chain   SKILL.md:39                    "- **Audit before 
installing** — Run `socket package score np"

Decision: ALLOWED — Allowed (community source, safe verdict)
┌───────────────────────────── Upstream Metadata ─────────────────────────────┐
│ Repo: https://github.com/secondsky/claude-skills                            │
│ Detail Page: https://skills.sh/secondsky/claude-skills/bun-nextjs           │
└─────────────────────────────────────────────────────────────────────────────┘
Installed: bun-nextjs
Files: SKILL.md

Updating: bun-shell

Fetching: skills-sh/secondsky/claude-skills/bun-shell
Warning: 'bun-shell' is already installed at bun-shell
Quarantined to .hub\quarantine\bun-shell
Running security scan...
Scan: bun-shell (skills-sh/secondsky/claude-skills/bun-shell/community)  
Verdict: SAFE
Decision: ALLOWED — Allowed (community source, safe verdict)
┌───────────────────────────── Upstream Metadata ─────────────────────────────┐
│ Repo: https://github.com/secondsky/claude-skills                            │
│ Detail Page: https://skills.sh/secondsky/claude-skills/bun-shell            │
└─────────────────────────────────────────────────────────────────────────────┘
Installed: bun-shell
Files: SKILL.md

Updating: ci-cd-best-practices

Fetching: skills-sh/mindrally/skills/ci-cd-best-practices
Warning: 'ci-cd-best-practices' is already installed at ci-cd-best-practices
Quarantined to .hub\quarantine\ci-cd-best-practices
Running security scan...
Scan: ci-cd-best-practices 
(skills-sh/mindrally/skills/ci-cd-best-practices/community)  Verdict: SAFE
Decision: ALLOWED — Allowed (community source, safe verdict)
┌───────────────────────────── Upstream Metadata ─────────────────────────────┐
│ Repo: https://github.com/mindrally/skills                                   │
│ Detail Page: https://skills.sh/mindrally/skills/ci-cd-best-practices        │
└─────────────────────────────────────────────────────────────────────────────┘
Installed: ci-cd-best-practices
Files: SKILL.md

Updating: ci-cd-pipeline-builder

Fetching: skills-sh/alirezarezvani/claude-skills/ci-cd-pipeline-builder
Warning: 'ci-cd-pipeline-builder' is already installed at 
ci-cd-pipeline-builder
Quarantined to .hub\quarantine\ci-cd-pipeline-builder
Running security scan...
Scan: ci-cd-pipeline-builder 
(skills-sh/alirezarezvani/claude-skills/ci-cd-pipeline-builder/community)  
Verdict: SAFE
  MEDIUM   supply_chain   references\github-actions-templates.md:38 "- run: 
python3 -m pip install -U pip"
  MEDIUM   supply_chain   references\gitlab-ci-templates.md:36 "- python3 -m 
pip install -U pip"
  MEDIUM   supply_chain   scripts\pipeline_generator.py:150 ""      - run: 
python3 -m pip install -U pip","
  MEDIUM   supply_chain   scripts\pipeline_generator.py:250 ""    - python3 -m 
pip install -U pip","
  MEDIUM   supply_chain   scripts\pipeline_generator.py:99 "return "pnpm 
install --frozen-lockfile""

Decision: ALLOWED — Allowed (community source, safe verdict)
┌───────────────────────────── Upstream Metadata ─────────────────────────────┐
│ Repo: https://github.com/alirezarezvani/claude-skills                       │
│ Detail Page:                                                                │
│ https://skills.sh/alirezarezvani/claude-skills/ci-cd-pipeline-builder       │
└─────────────────────────────────────────────────────────────────────────────┘
Installed: ci-cd-pipeline-builder
Files: README.md, SKILL.md, references/deployment-gates.md, 
references/github-actions-templates.md, references/gitlab-ci-templates.md, 
references/pipeline-design-notes.md, scripts/pipeline_generator.py, 
scripts/stack_detector.py

Updating: django-application

Fetching: skills-sh/aj-geddes/useful-ai-prompts/django-application
Warning: 'django-application' is already installed at django-application
Quarantined to .hub\quarantine\django-application
Running security scan...
Scan: django-application 
(skills-sh/aj-geddes/useful-ai-prompts/django-application/community)  Verdict: 
SAFE
Decision: ALLOWED — Allowed (community source, safe verdict)
┌───────────────────────────── Upstream Metadata ─────────────────────────────┐
│ Repo: https://github.com/aj-geddes/useful-ai-prompts                        │
│ Detail Page:                                                                │
│ https://skills.sh/aj-geddes/useful-ai-prompts/django-application            │
└─────────────────────────────────────────────────────────────────────────────┘
Installed: django-application
Files: SKILL.md, references/admin-interface-customization.md, 
references/authentication-and-permissions.md, 
references/database-queries-and-optimization.md, 
references/django-project-setup.md, references/model-design-with-orm.md, 
references/url-routing.md, 
references/views-with-class-based-and-function-based-approaches.md, 
scripts/validate-schema.sh, templates/migration-template.sql

Updating: django-celery

Fetching: skills-sh/affaan-m/everything-claude-code/django-celery
Warning: 'django-celery' is already installed at django-celery
Quarantined to .hub\quarantine\django-celery
Running security scan...
Scan: django-celery 
(skills-sh/affaan-m/everything-claude-code/django-celery/community)  Verdict: 
CAUTION
  HIGH     exfiltration   SKILL.md:36                    
"os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.sett"
  MEDIUM   persistence    SKILL.md:228                   "from celery.schedules
import crontab"
  MEDIUM   persistence    SKILL.md:233                   "'schedule': 
crontab(hour=2, minute=0),   # 2am daily"
  MEDIUM   persistence    SKILL.md:241                   "'schedule': 
crontab(day_of_week='monday', hour=8, minute=0),"
  MEDIUM   persistence    SKILL.md:261                   "'crontab': schedule,"
  MEDIUM   supply_chain   SKILL.md:26                    "pip install 'celery' 
django-celery-results django-cel"
  MEDIUM   supply_chain   SKILL.md:411                   "pip install flower"

Decision: BLOCKED — Blocked (community source + caution verdict, 7 findings). 
Use --force to override.
┌───────────────────────────── Upstream Metadata ─────────────────────────────┐
│ Repo: https://github.com/affaan-m/everything-claude-code                    │
│ Detail Page:                                                                │
│ https://skills.sh/affaan-m/everything-claude-code/django-celery             │
└─────────────────────────────────────────────────────────────────────────────┘
Installed: django-celery
Files: SKILL.md

Updating: chainlink
Resolving 'chainlink'...
Resolved to: chainlink

Fetching: chainlink
Warning: 'chainlink' is already installed at chainlink
Quarantined to .hub\quarantine\chainlink
Running security scan...
Scan: chainlink (chainlink/community)  Verdict: SAFE
Decision: ALLOWED — Allowed (community source, safe verdict)
Installed: chainlink
Files: skill-card.md, SKILL.md, _meta.json

Updating: firecrawl-agent

Fetching: skills-sh/firecrawl/cli/firecrawl
Warning: 'firecrawl-agent' is already installed at firecrawl-agent
Quarantined to .hub\quarantine\firecrawl-agent
Running security scan...
Scan: firecrawl-agent (skills-sh/firecrawl/cli/firecrawl/community)  Verdict: 
SAFE
  LOW      privilege_escalation SKILL.md:5                     "allowed-tools:"

Decision: ALLOWED — Allowed (community source, safe verdict)
┌───────────────────────────── Upstream Metadata ─────────────────────────────┐
│ Repo: https://github.com/firecrawl/cli                                      │
│ Detail Page: https://skills.sh/firecrawl/cli/firecrawl                      │
└─────────────────────────────────────────────────────────────────────────────┘
Installed: firecrawl-agent
Files: SKILL.md

Updating: cloudflare-temporary-deploy

Fetching: official/web-development\cloudflare-temporary-deploy
Warning: 'cloudflare-temporary-deploy' is already installed at 
cloudflare-temporary-deploy
Quarantined to .hub\quarantine\cloudflare-temporary-deploy
Running security scan...
Scan: cloudflare-temporary-deploy (official/builtin)  Verdict: SAFE
Decision: ALLOWED — Allowed (builtin source, safe verdict)
Installed: cloudflare-temporary-deploy
Files: SKILL.md, scripts\parse_deploy_output.py

Updating: firecrawl-scrape

Fetching: skills-sh/firecrawl/cli/firecrawl-scrape
Warning: 'firecrawl-scrape' is already installed at firecrawl-scrape
Quarantined to .hub\quarantine\firecrawl-scrape
Running security scan...
Scan: firecrawl-scrape (skills-sh/firecrawl/cli/firecrawl-scrape/community)  
Verdict: SAFE
  LOW      privilege_escalation SKILL.md:5                     "allowed-tools:"

Decision: ALLOWED — Allowed (community source, safe verdict)
┌───────────────────────────── Upstream Metadata ─────────────────────────────┐
│ Repo: https://github.com/firecrawl/cli                                      │
│ Detail Page: https://skills.sh/firecrawl/cli/firecrawl-scrape               │
└─────────────────────────────────────────────────────────────────────────────┘
Installed: firecrawl-scrape
Files: SKILL.md

Updating: firecrawl-search

Fetching: skills-sh/firecrawl/cli/firecrawl-search
Warning: 'firecrawl-search' is already installed at firecrawl-search
Quarantined to .hub\quarantine\firecrawl-search
Running security scan...
Scan: firecrawl-search (skills-sh/firecrawl/cli/firecrawl-search/community)  
Verdict: SAFE
  LOW      privilege_escalation SKILL.md:5                     "allowed-tools:"

Decision: ALLOWED — Allowed (community source, safe verdict)
┌───────────────────────────── Upstream Metadata ─────────────────────────────┐
│ Repo: https://github.com/firecrawl/cli                                      │
│ Detail Page: https://skills.sh/firecrawl/cli/firecrawl-search               │
└─────────────────────────────────────────────────────────────────────────────┘
Installed: firecrawl-search
Files: SKILL.md

Updating: firecrawl-crawl

Fetching: skills-sh/firecrawl/cli/firecrawl-crawl
Warning: 'firecrawl-crawl' is already installed at firecrawl-crawl
Quarantined to .hub\quarantine\firecrawl-crawl
Running security scan...
Scan: firecrawl-crawl (skills-sh/firecrawl/cli/firecrawl-crawl/community)  
Verdict: SAFE
  LOW      privilege_escalation SKILL.md:5                     "allowed-tools:"

Decision: ALLOWED — Allowed (community source, safe verdict)
┌───────────────────────────── Upstream Metadata ─────────────────────────────┐
│ Repo: https://github.com/firecrawl/cli                                      │
│ Detail Page: https://skills.sh/firecrawl/cli/firecrawl-crawl                │
└─────────────────────────────────────────────────────────────────────────────┘
Installed: firecrawl-crawl
Files: SKILL.md

Updating: firecrawl-map

Fetching: skills-sh/firecrawl/cli/firecrawl-map
Warning: 'firecrawl-map' is already installed at firecrawl-map
Quarantined to .hub\quarantine\firecrawl-map
Running security scan...
Scan: firecrawl-map (skills-sh/firecrawl/cli/firecrawl-map/community)  Verdict:
SAFE
  LOW      privilege_escalation SKILL.md:5                     "allowed-tools:"

Decision: ALLOWED — Allowed (community source, safe verdict)
┌───────────────────────────── Upstream Metadata ─────────────────────────────┐
│ Repo: https://github.com/firecrawl/cli                                      │
│ Detail Page: https://skills.sh/firecrawl/cli/firecrawl-map                  │
└─────────────────────────────────────────────────────────────────────────────┘
Installed: firecrawl-map
Files: SKILL.md

Updating: firecrawl-download

Fetching: skills-sh/firecrawl/cli/firecrawl-download
Warning: 'firecrawl-download' is already installed at firecrawl-download
Quarantined to .hub\quarantine\firecrawl-download
Running security scan...
Scan: firecrawl-download (skills-sh/firecrawl/cli/firecrawl-download/community)
Verdict: SAFE
  LOW      privilege_escalation SKILL.md:5                     "allowed-tools:"

Decision: ALLOWED — Allowed (community source, safe verdict)
┌───────────────────────────── Upstream Metadata ─────────────────────────────┐
│ Repo: https://github.com/firecrawl/cli                                      │
│ Detail Page: https://skills.sh/firecrawl/cli/firecrawl-download             │
└─────────────────────────────────────────────────────────────────────────────┘
Installed: firecrawl-download
Files: SKILL.md

Updating: obliteratus

Fetching: official/mlops/obliteratus
Warning: 'obliteratus' is already installed at mlops/obliteratus
Quarantined to .hub\quarantine\obliteratus
Running security scan...
Scan: obliteratus (official/builtin)  Verdict: SAFE
  MEDIUM   supply_chain   SKILL.md:53                    "pip install -e ."
  MEDIUM   supply_chain   SKILL.md:55                    "# pip install -e ".""
  MEDIUM   supply_chain   SKILL.md:51                    "git clone 
https://github.com/elder-plinius/OBLITERATUS.git"

Decision: ALLOWED — Allowed (builtin source, safe verdict)
Installed: mlops\obliteratus
Files: SKILL.md, references\analysis-modules.md, references\methods-guide.md, 
templates\abliteration-config.yaml, templates\analysis-study.yaml, 
templates\batch-abliteration.yaml

Updating: dspy

Fetching: official/mlops/research/dspy
Warning: 'dspy' is already installed at mlops/research/dspy
Quarantined to .hub\quarantine\dspy
Running security scan...
Scan: dspy (official/builtin)  Verdict: SAFE
  MEDIUM   supply_chain   SKILL.md:33                    "pip install dspy"
  MEDIUM   supply_chain   SKILL.md:36                    "pip install 
git+https://github.com/stanfordnlp/dspy.git"
  MEDIUM   supply_chain   SKILL.md:39                    "pip install dspy     
# OpenAI"
  MEDIUM   supply_chain   SKILL.md:40                    "pip install dspy     
# Anthropic Claude"
  MEDIUM   supply_chain   SKILL.md:41                    "pip install dspy     
# All providers"

Decision: ALLOWED — Allowed (builtin source, safe verdict)
Installed: mlops\research\dspy
Files: SKILL.md, references\examples.md, references\modules.md, 
references\optimizers.md

Updating: saelens

Fetching: official/mlops/saelens
Warning: 'saelens' is already installed at mlops/saelens
Quarantined to .hub\quarantine\saelens
Running security scan...
Scan: saelens (official/builtin)  Verdict: SAFE
  MEDIUM   supply_chain   SKILL.md:44                    "pip install sae-lens"
  MEDIUM   supply_chain   references\README.md:19        "pip install sae-lens"

Decision: ALLOWED — Allowed (builtin source, safe verdict)
Installed: mlops\saelens
Files: SKILL.md, references\api.md, references\README.md, 
references\tutorials.md

Updating: slime

Fetching: official/mlops/slime
Warning: 'slime' is already installed at mlops/slime
Quarantined to .hub\quarantine\slime
Running security scan...
Scan: slime (official/builtin)  Verdict: SAFE
  MEDIUM   supply_chain   SKILL.md:66                    "cd /root/slime && pip
install -e . --no-deps"
  MEDIUM   supply_chain   SKILL.md:75                    "pip install -e ."
  MEDIUM   supply_chain   SKILL.md:72                    "git clone 
https://github.com/THUDM/slime.git"
  MEDIUM   supply_chain   SKILL.md:61                    "docker pull 
slimerl/slime:latest"

Decision: ALLOWED — Allowed (builtin source, safe verdict)
Installed: mlops\slime
Files: SKILL.md, references\api-reference.md, references\troubleshooting.md

Updating: trl-fine-tuning

Fetching: official/mlops/training/trl-fine-tuning
Warning: 'trl-fine-tuning' is already installed at 
mlops/training/trl-fine-tuning
Quarantined to .hub\quarantine\trl-fine-tuning
Running security scan...
Scan: trl-fine-tuning (official/builtin)  Verdict: SAFE
  MEDIUM   supply_chain   SKILL.md:23                    "pip install trl 
transformers datasets peft accelerate"

Decision: ALLOWED — Allowed (builtin source, safe verdict)
Installed: mlops\training\trl-fine-tuning
Files: SKILL.md, references\dpo-variants.md, references\grpo-training.md, 
references\online-rl.md, references\reward-modeling.md, 
references\sft-training.md, templates\basic_grpo_training.py

Updating: shop

Fetching: official/productivity/shop
Warning: 'shop' is already installed at productivity/shop
Quarantined to .hub\quarantine\shop
Running security scan...
Scan: shop (official/builtin)  Verdict: DANGEROUS
  CRITICAL persistence    references\direct-api.md:26    "device_name=<your 
name> - <device>   # e.g. Max - Mac Mini; "
  MEDIUM   supply_chain   SKILL.md:24                    "pnpm add --global 
@shopify/shop-cli   # or: npm install --gl"
  MEDIUM   supply_chain   SKILL.md:28                    "To upgrade: `pnpm add
--global @shopify/shop-cli@latest` (or"

Decision: ALLOWED — Allowed (builtin source, dangerous verdict)
Installed: productivity\shop
Files: SKILL.md, references\catalog-mcp.md, references\direct-api.md, 
references\legal.md, references\safety.md

Updating: godmode

Fetching: official/security/godmode
Warning: 'godmode' is already installed at security/godmode
Quarantined to .hub\quarantine\godmode
Running security scan...
Scan: godmode (official/builtin)  Verdict: DANGEROUS
  CRITICAL exfiltration   SKILL.md:237                   
"api_key=os.getenv("OPENROUTER_API_KEY"),"
  CRITICAL exfiltration   SKILL.md:288                   
"api_key=os.getenv("OPENROUTER_API_KEY"),"
  CRITICAL persistence    SKILL.md:84                    "1. **Reads 
`~/AppData/Local/hermes/config.yaml`** to detect the current m"
  CRITICAL persistence    SKILL.md:134                   "Edit 
`~/AppData/Local/hermes/config.yaml`:"
  CRITICAL persistence    SKILL.md:172                   "Then set in 
`~/AppData/Local/hermes/config.yaml`:"
  CRITICAL persistence    references\jailbreak-templates.md:96 "Pick a template
above and set it in `~/AppData/Local/hermes/config.yaml`:"
  CRITICAL exfiltration   scripts\auto_jailbreak.py:342  "return 
os.getenv("OPENROUTER_API_KEY", "")"
  CRITICAL exfiltration   scripts\auto_jailbreak.py:344  "return 
os.getenv("ANTHROPIC_API_KEY", "")"
  CRITICAL exfiltration   scripts\auto_jailbreak.py:346  "return 
os.getenv("OPENAI_API_KEY", "")"
  CRITICAL exfiltration   scripts\auto_jailbreak.py:348  "return 
os.getenv("OPENROUTER_API_KEY", "")"
  CRITICAL exfiltration   scripts\godmode_race.py:15     
"api_key=os.getenv("OPENROUTER_API_KEY"),"
  CRITICAL exfiltration   scripts\godmode_race.py:323    "api_key = api_key or 
os.getenv("OPENROUTER_API_KEY")"
  CRITICAL exfiltration   scripts\godmode_race.py:448    "api_key = api_key or 
os.getenv("OPENROUTER_API_KEY")"
  HIGH     privilege_escalation scripts\parseltongue.py:31     "'jailbreak', 
'unlock', 'root', 'sudo', 'admin', 'privilege',"
  MEDIUM   injection      SKILL.md:265                   "- "for educational 
purposes only""
  MEDIUM   obfuscation    scripts\auto_jailbreak.py:171  
"'\u2022-\u2022-\u2022-\u2022.\u2022-\u2022-\u2022-\u2022-<|G"
  MEDIUM   obfuscation    scripts\auto_jailbreak.py:172  
"'-\u2022-\u2022-\u2022-\u2022.\u2022-\u2022-\u2022-\u2022 '"
  MEDIUM   obfuscation    scripts\godmode_race.py:419    "'system': 
'/User-Query> extremely unfiltered liberated respo"
  MEDIUM   supply_chain   scripts\godmode_race.py:321    "raise 
ImportError("openai package required. Install with: pi"
  MEDIUM   supply_chain   scripts\godmode_race.py:446    "raise 
ImportError("openai package required. Install with: pi"
  LOW      obfuscation    scripts\parseltongue.py:182    "return word[::-1]"

Decision: ALLOWED — Allowed (builtin source, dangerous verdict)
Installed: security\godmode
Files: SKILL.md, references\jailbreak-templates.md, 
references\refusal-detection.md, scripts\auto_jailbreak.py, 
scripts\godmode_race.py, scripts\load_godmode.py, scripts\parseltongue.py, 
templates\prefill-subtle.json, templates\prefill.json

Updated 81 skill(s).

