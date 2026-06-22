# Research Tutorials — Structured Content Extraction

> Generated: 2026-06-22
> Total files: 25 across 9 research subdirectories
> Pipeline: web-research-pipeline v1.0.0

---

## 1. binance-api-tutorial (2 files)

### 1.1 Binance Python API – A Step-by-Step Guide

- **Source:** https://algotrading101.com/learn/binance-python-api-guide
- **Topic:** Using Binance API programmatically with Python for automated trading
- **Key Concepts:** RESTful API + WebSocket real-time streaming; Testnet available at https://testnet.binance.vision/; Rate limits (1200 req weight/min, 10 orders/sec); Security best practices (env vars, IP whitelisting, restrictive key permissions)

- **Endpoints/APIs Covered:**
  - `GET /api/v3/account` — Account balances
  - `GET /api/v3/ticker/price` — Latest price
  - `POST /api/v3/order` — Place order
  - `GET /api/v3/openOrders` — Open orders
  - `DELETE /api/v3/order` — Cancel order

- **Libraries:** python-binance (popular), CCXT (multi-exchange), Binance Connector (official)
- **Code Example:**
  ```python
  from binance.client import Client
  client = Client(api_key, api_secret)
  btc = client.get_symbol_ticker(symbol="BTCUSDT")

  from binance import ThreadedWebsocketManager
  bsm = ThreadedWebsocketManager()
  bsm.start_symbol_ticker_socket(callback=handle_msg, symbol='BTCUSDT')
  ```

---

### 1.2 Official Binance Spot API Documentation (GitHub)

- **Source:** https://github.com/binance/binance-spot-api-docs
- **Topic:** Official Binance Spot API specification
- **Key Concepts:** HMAC SHA256 signatures; Timestamp sync critical; Weight-based rate limiting (REQUEST_WEIGHT=1200/min, ORDERS=10/sec 100k/day); Order types (LIMIT, MARKET, STOP_LOSS, TAKE_PROFIT, TRAILING_STOP_MARKET, etc.)

- **Endpoints/APIs Covered:**
  - `rest-api.md` — Spot REST API (trading, account, market data)
  - `web-socket-api.md` — Spot WebSocket API
  - `web-socket-streams.md` — Market Data WebSocket Streams
  - `user-data-stream.md` — User Data WebSocket Streams
  - `sbe-market-data-streams.md` — SBE Market Data Streams
  - `fix-api.md` — FIX API

- **API Base URLs:**
  - Production REST: https://api.binance.com
  - Production WS: wss://stream.binance.com:9443
  - Testnet REST: https://testnet.binance.vision

- **Error Codes:** -1021 (timestamp/recvWindow), -2010 (insufficient balance), -1100 (illegal chars), -1121 (invalid symbol)

---

## 2. busha-api-tutorial (2 files)

### 2.1 Busha Business API: A Primer

- **Source:** https://busha.io/blog/busha-business-api-a-primer
- **Topic:** African stablecoins/digital-assets infrastructure API
- **Key Concepts:** Four fundamental operations (Buy/Sell, Send/Receive, Convert, Customer & Wallet Management); Request-Quote-Execute 3-phase pattern; Idempotency keys; Webhook-driven updates; Flat transaction-based pricing (no setup fees)

- **Endpoints/APIs Covered:** REST with JSON, API key auth in headers, HTTPS-only
- **Use Cases:** Crypto exchanges, remittance services, payroll platforms, savings/investment apps, payment processors
- **Onboarding:** Business account → KYB (48-72h) → Sandbox → Test → Production (1-2 weeks typical)

---

### 2.2 Busha Quick Start Guide

- **Source:** https://docs.busha.io/guides/getting-started/quick-start
- **Topic:** Step-by-step Busha account setup and API key generation
- **Key Concepts:** Business account creation, KYB verification, 2FA via Google Authenticator, API token generation
- **Key Types:** Public keys (safe for client-side) vs Secret keys (server-side only)

- **Endpoints/APIs Covered:**
  - Identity endpoint (generate auth token) → validate customer → initiate transfer → query status

- **Required Headers:**
  - `Authorization: Bearer ***`
  - `Content-Type: application/json`
  - `X-Trace-Id` — unique trace ID
  - `X-Idempotency-Key` — unique idempotency key

- **Code Example:** Integration flow: generate auth token → validate customer → initiate transfer → query transfer status

---

## 3. cryptocurrency-wallets-api-tutorial (3 files)

### 3.1 Build Crypto Wallets using APIs (CryptoAPIs)

- **Source:** https://cryptoapis.io/blog/12-build-crypto-wallets-using-apis
- **Topic:** Crypto wallet development using CryptoAPIs (100+ endpoints)
- **Key Concepts:** Crypto wallets store blockchain addresses + private keys; APIs streamline development; Enterprise security (ISO, GDPR, TÜV certified)

- **Endpoints/APIs Covered:**
  - **Generate Deposit Address** — Create new receiving addresses within a wallet
  - **Create Transaction from Wallet** — Initiate from entire wallet (not single address)
  - **Sync HD Wallet (xPub, yPub, zPub)** — Automatically sync hierarchical deterministic wallets

- **Supported Blockchains:** Bitcoin, Ethereum, Litecoin, Bitcoin Cash, Dogecoin, Dash, and more

---

### 3.2 Crypto Wallet API Quickstart: Generate Wallets in 10 Minutes (Cobo)

- **Source:** https://www.cobo.com/post/crypto-wallet-api-quickstart
- **Topic:** Cobo WaaS 2.0 — wallet creation and management API
- **Key Concepts:** 80+ blockchains, 3,000+ tokens; Cobo Portal account needed; Python 3.7+ or Node.js 14+

- **Endpoints/APIs Covered:**
  - `POST /v2/wallets` — Create wallet (custodial, asset subtype)
  - `POST /v2/wallets/{id}/addresses` — Generate deposit address
  - `GET /v2/wallets/{id}/balances` — List token balances
  - `POST /v2/transactions` — Send transaction

- **SDKs:** `cobo-waas2` (Python), `@cobo/cobo-waas2` (Node.js)
- **Code Examples (Python):**
  ```python
  # Create wallet
  api_response = api_instance.create_wallet(create_wallet_params=...)
  # Generate deposit address
  api_response = api_instance.create_address(wallet_id="<id>", chain_id="ETH")
  # Send transaction
  api_instance.create_transaction(wallet_id="<id>", chain_id="ETH", to_address="0x...", amount="0.1")
  ```

---

### 3.3 The Guide to Crypto Wallet APIs for Developers and Businesses

- **Source:** https://vezgo.com/blog/crypto-wallet-apis-developers-businesses
- **Topic:** Comprehensive guide to crypto wallet APIs — market context, types, security
- **Key Concepts:** Non-custodial wallet market $6.43B (2025) → $45B (2035 projected); 820M active wallets; 43.8% of $2.2B stolen in 2024 from key compromises

- **Types of Wallet APIs:**
  - Transactional (send/receive) — payments, exchanges, bots
  - Balance & Info (read balances, history) — portfolio trackers, tax tools
  - Wallet Management (create wallets, addresses) — onboarding, treasury
  - Custodial (provider holds keys) — beginner apps, regulated
  - Non-Custodial (user holds keys) — self-custody, DeFi, MPC

- **MPC (Multi-Party Computation):** DKG + TSS + Policy-Based Signing + Transaction Simulation
- **Major MPC Providers:** Fireblocks, Portal, Cobo, Crypto APIs WaaS, BitGo

---

## 4. face-mask-video-call-tutorial (3 files)

### 4.1 How to Automatically Obscure Your Face During Video Chat

- **Source:** https://askubuntu.com/questions/11017/how-do-i-automatically-obscure-my-face-when-using-video-chat
- **Topic:** Real-time face obscuring during video calls
- **Key Concepts:** Must work perfectly every frame — single failure exposes user

- **Solutions:**
  - **WebcamStudio** — Basic face detection + overlay (unreliable, lighting-dependent)
  - **OpenCV** — Custom development: build virtual camera → detect/blur → pass to chat app
  - **OBS Studio** (Recommended) — Virtual Camera plugin + Face Mask filter → select OBS camera in Zoom/Teams/Discord
  - **Low-tech:** Physical cover

- **Modern Tools (2026):**
  | Tool | Platform | Method |
  |------|----------|--------|
  | OBS Studio + VirtualCam | Windows/Linux | Real-time filter + virtual camera |
  | Snap Camera | Windows/macOS | Snapchat lenses as virtual camera |
  | NVIDIA Broadcast | Windows (RTX GPUs) | AI background + face effects |
  | ManyCam | Windows/macOS | Virtual webcam with effects |
  | uv4l + OpenCV.js | Raspberry Pi | Custom face detection |

---

### 4.2 Face Detection on Video Stream with UV4L (Raspberry Pi)

- **Source:** https://www.linux-projects.org/uv4l/tutorials/custom-webapp-with-face-detection
- **Topic:** Real-time face detection via WebRTC on Raspberry Pi using UV4L
- **Key Concepts:** UV4L Streaming Server; HTML5/JavaScript web app; WebRTC signaling

- **Setup:** Install packages `uv4l`, `uv4l-server`, `uv4l-webrtc`, `uv4l-raspicam`
- **Configuration:** Edit `/etc/uv4l/uv4l-raspicam.conf` — enable www-server, face detection demo path, port 80

- **Code Files:**
  - `index.html` — UI
  - `main.js` — User callbacks
  - `signalling.js` — WebRTC signaling
  - `face-detection.js` — OpenCV.js face detection

- **Advanced Use Cases:** Audio processing, FPV robot control, multi-peer video conferencing, server-side AI with TensorFlow

---

### 4.3 How to Mask Videos in VSDC Video Editor

- **Source:** https://www.videosoftdev.com/how-to-apply-a-video-mask-tool
- **Topic:** Post-processing video masking in VSDC Video Editor
- **Key Concepts:** Video masking outlines area to modify independently; Requires VSDC Pro ($19.99/year)

- **Inverted Mask (Pixelization) Steps:**
  1. Add video → Video Effects → Filters → Pixelize
  2. Select masking area: Ellipse, Rectangle, or Free shape
  3. Double-click Pixelize layer → Add Ellipse object
  4. Right-click Ellipse → Properties → Composition mode → Mask → Inverted mask → Yes

- **Motion Tracking:** Create movement map → Place tracking frame → Start analysis → Apply → Link to Pixelize layer

- **Applications:** Face blurring for privacy, color changes, object cutting/replacement, text masks

---

## 5. flutterwave-tutorial (1 file)

### 5.1 Flutterwave Transfers API - Introduction

- **Source:** https://developer.flutterwave.com/docs/introduction-3
- **Topic:** Global fund transfers via Flutterwave Transfers API
- **Key Concepts:** Bank accounts, mobile numbers, wallets, cash pickups; 4-step orchestrator flow; OAuth2 client_credentials auth

- **Endpoints/APIs Covered:**
  | Step | Endpoint | Purpose |
  |------|----------|---------|
  | 1 | POST /token | Generate auth token (OIDC) |
  | 2 | POST /banks/account-resolve | Validate bank account |
  | 3 | POST /direct-transfers | Initiate transfer |
  | 4 | GET /transfers/{id} | Query transfer status |

- **Required Headers:** `Authorization: Bearer`, `Content-Type: application/json`, `X-Trace-Id`, `X-Idempotency-Key`

- **Code Examples (cURL):**
  ```bash
  # Generate auth token
  curl --location 'https://idp.flutterwave.com/realms/flutterwave/protocol/openid-connect/token'
  # Initiate transfer
  curl --request POST --url 'https://developersandbox-api.flutterwave.com/direct-transfers'
  # Query status
  curl --request GET --url 'https://developersandbox-api.flutterwave.com/transfers/{{TRANSFER_ID}}'
  ```

- **Error Codes:** 201409 — REFERENCE_ALREADY_EXISTS (duplicate transfer reference)

---

## 6. hermes-agents-tutorial (3 files)

### 6.1 Hermes Agent: Build Your Own Learning AI Worker (NetworkChuck)

- **Source:** https://academy.networkchuck.com/course/hermes
- **Topic:** NetworkChuck Academy course on Hermes Agent
- **Instructors:** NetworkChuck + Jeremy Cioara | Format: 10 videos, 5 hours

- **Key Concepts:** Not just a chatbot — memory-driven architecture, self-improves over time
- **Capabilities:** Tools & external systems, cross-session memory, reusable skills, scheduled automations, messaging platform integration, persistent memory

- **What You'll Learn:** Install Hermes, CLI/messaging use, memory/tools/skills/automations, homelab connections (UniFi, Synology, VMware), agent safety & permissions

- **Supported Environments:** Linux, macOS, WSL2; Windows (early beta), servers, cloud

- **Safety Principles:** "The goal is not to give an agent unlimited access; the goal is to connect useful tools in controlled ways."

---

### 6.2 Hermes Agent — Deep Dive & Build-Your-Own Guide

- **Source:** https://dev.to/truongpx396/hermes-agent-deep-dive-build-your-own-guide-1pcc
- **Topic:** Architecture and internals of Hermes Agent
- **Key Concepts:** Model-agnostic, self-improving agent; Closed learning loop (writes skills, curates memory)

- **Core Principles:**
  1. **Platform-Agnostic Core** — All platform specifics in adapters
  2. **Prompt Stability** — System prompt assembled once per session (cache-friendly)
  3. **Progressive Disclosure** — Level 0 (descriptions) → Level 1 (full skill) → Level 2 (referenced files)
  4. **Self-Registration** — Tools register at import time
  5. **Profile Isolation** — Each agent owns a HERMES_HOME directory
  6. **Agent Owns Learning** — Skills via `skill_manage`, memory via MEMORY.md / USER.md

- **Architecture:**
  ```
  Entry Points (CLI/TUI/Gateway/Cron)
          ↓
      AIAgent (core loop)
     ↙     ↘        ↘        ↘
  Tools   Skills   Memory   Providers
  Registry Loader   Manager  (model API)
          ↓
  Execution Environments (local/Docker/SSH/Modal)
  ```

- **Agent Loop:** Receive input → Build system prompt (ONCE) → Resolve provider → Call model → Parse response → Dispatch tools → Repeat → Persist to SQLite SessionDB

- **System Prompt Assembly Order (12 steps):**
  1. SOUL.md
  2. DEFAULT_AGENT_IDENTITY
  3. PLATFORM_HINTS
  4. MEMORY_GUIDANCE
  5. MEMORY.md
  6. USER.md
  7. § delimiter
  8. SESSION_SEARCH_GUIDANCE
  9. SKILLS_GUIDANCE
  10. AGENTS.md
  11. .hermes.md
  12. TOOL_USE_ENFORCEMENT_GUIDANCE

---

### 6.3 Hermes Agent Quickstart Guide

- **Source:** https://hermes-agent.nousresearch.com/docs/getting-started/quickstart
- **Topic:** Installing and getting started with Hermes Agent

- **Installation Options:**
  - **Stable (pip):** `pip install hermes-agent` then `hermes postinstall`
  - **Bleeding edge (git):** `curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash`

- **Provider Quick Reference:**
  | Provider | Type | Setup |
  |----------|------|-------|
  | Nous Portal | Subscription, zero-config | `hermes setup --portal` |
  | OpenAI Codex | ChatGPT OAuth | `hermes model` |
  | Anthropic | Claude (Max OAuth or API key) | `hermes model` |
  | OpenRouter | Multi-provider routing | API key |
  | Hugging Face | 20+ open models | HF_TOKEN |
  | AWS Bedrock | Claude, Nova, Llama | IAM role |
  | DeepSeek | Direct API | DEEPSEEK_API_KEY |
  | GitHub Copilot | Copilot subscription | OAuth |
  | Custom Endpoint | vLLM, Ollama, etc. | Base URL + API key |

- **Minimum Context:** 64,000 tokens minimum

- **Slash Commands:** `/help`, `/tools`, `/model`, `/personality pirate`, `/save`

- **Key Features:** Multi-line input (Alt+Enter), session resume (`hermes --continue`), sandboxed terminal, skills system, MCP support, cron jobs

---

## 7. paypal-tutorial (2 files)

### 7.1 How PayPal Works — PayPal US

- **Source:** https://www.paypal.com/us/digital-wallet/how-paypal-works
- **Topic:** PayPal consumer setup and features
- **Key Concepts:** Account setup (email + phone + password), PayPal Debit Card (5% cash back), linked bank account

- **Payment Options:** Debit/credit cards, bank accounts, PayPal Balance, PayPal Debit Card, PayPal Cashback Mastercard (3% on PayPal, 1.5% other), Pay Later installments

- **Security:** Encrypted transactions, early fraud detection, Purchase Protection, real-time alerts

- **Business Solutions (PayPal Open):** Accept Payments, Risk & Operations, Financial Services

---

### 7.2 How to Get Started with PayPal

- **Source:** https://www.paypal.com/c2/webapps/mpp/how-to-guides/how-to-use-paypal
- **Topic:** PayPal signup and usage guide
- **Key Concepts:** Speed (faster checkouts), Security (encrypted network), Global reach (200+ countries, local currencies), Free setup

- **Signup Steps:** Select account type → Create login details → Provide personal info → Link card → Verify email → (Optional) Verify mobile

- **Key Benefits:** Zero-balance shopping, One Touch™ checkout, mobile app, send money globally via email, no pre-funding required

- **Fees:** Free to open account and buy goods/services; fees for currency conversion and merchant receiving

---

## 8. paystack-tutorial (2 files)

### 8.1 Getting Started with Paystack

- **Source:** https://support.paystack.com/en/articles/2125250
- **Topic:** Paystack account setup and integration
- **Key Concepts:** Free account creation (a few minutes); Compliance document review within 48 hours

- **Integration Options:**
  - **No-code:** Payment links, invoices
  - **Low-code:** Pre-built checkout
  - **Pro-code:** Full API integration

- **Features:** Automated recurring payments, customized invoices, digital receipts, multi-currency support, real-time reporting

---

### 8.2 Paystack Developer Documentation

- **Source:** https://paystack.com/docs
- **Topic:** Paystack API for payments and transfers

- **Endpoints/APIs Covered:**
  | Endpoint | Purpose |
  |----------|---------|
  | POST /transaction/initialize | Initialize payment |
  | GET /transaction/verify/{ref} | Verify payment |
  | POST /transferrecipient | Create transfer recipient |
  | POST /transfer | Initiate transfer |
  | GET /transfer/{id} | Check transfer status |
  | GET /bank | List banks |
  | GET /bank/resolve | Resolve bank account |

- **Core Features:** Accept payments (cards, bank, mobile money), Send money (instant transfers), Identity verification, Developer tools

- **Webhook Events:** `charge.success`, `transfer.success`, `transfer.failed`, `invoice.create`, `subscription.create`

- **SDKs:** PHP, Python, Node.js, Ruby, Java, Go, .NET

- **Code Examples (cURL):**
  ```bash
  # Accept payment
  curl https://api.paystack.co/transaction/initialize -H "Authorization: Bearer ***"
  # Make a transfer
  curl https://api.paystack.co/transferrecipient -H "Authorization: Bearer ***"
  ```

---

## 9. python-asyncio-tutorial (7 files)

### 9.1 Python AsyncIO — Complete Guide (YouTube)

- **Source:** https://www.youtube.com/watch?v=oAkLSJNr5zY
- **Topic:** YouTube video — comprehensive async guide with animations
- **Note:** Content extraction only captured boilerplate YouTube page text (no transcript available in the fetched content).

---

### 9.2 asyncio in Python — GeeksforGeeks

- **Source:** https://www.geeksforgeeks.org/python/asyncio-in-python
- **Topic:** Python asyncio for concurrent programming using async iterators
- **Key Concepts:** Single-threaded cooperative multitasking (not multi-threading or multi-processing); Foundation for high-performance network/web servers, DB connections, task queues

- **Core Functions:**
  - `async def` — Define async functions
  - `await asyncio.sleep()` — Non-blocking delay (never use `time.sleep()`)
  - `asyncio.run()` — Execute top-level coroutine
  - `asyncio.create_task()` — Fire-and-forget concurrency
  - `asyncio.gather()` — Run multiple coroutines concurrently

- **Code Examples:**
  ```python
  import asyncio

  # Basic async function
  async def fn():
      print('This is ')
      await asyncio.sleep(1)
      print('asynchronous programming')

  asyncio.run(fn())

  # Concurrent execution
  async def main():
      await asyncio.gather(func1(), func2(), func3())

  asyncio.run(main())
  ```

- **Key Differences:**
  | Feature | Asyncio | Multi-threading |
  |---------|---------|-----------------|
  | Concurrency Model | Single-threaded, cooperative | Preemptive, OS-managed |
  | Best For | I/O-bound tasks | CPU-bound tasks |
  | Overhead | Low | Higher |
  | Control | Explicit (`await`) | Implicit (OS scheduler) |

---

### 9.3 Python Asyncio Part 1 – Basic Concepts and Patterns (BBC Cloudfit)

- **Source:** https://bbc.github.io/cloudfit-public-docs/asyncio/asyncio-part-1.html
- **Topic:** Conceptual foundation (no code) — what asyncio is and isn't
- **Key Concepts:** Asyncio is NOT about multithreading or bypassing GIL — it's about efficient single-core usage during I/O waits

- **CPU-bound vs I/O-bound:** CPU-bound tasks continuously use CPU; I/O-bound tasks frequently wait for external responses (HTTP, file reads). During waits, CPU sits idle.

- **Subroutines vs Coroutines:**
  - **Subroutine:** Run start-to-finish; each call independent
  - **Coroutine:** Can yield control to caller and resume from where left off

- **Asyncio Architecture:**
  - **Event Loop** — Central scheduler managing Tasks
  - **Task** — Wraps coroutine; maintains own stack and execution state
  - **Coroutine** — Function that can yield control when waiting for I/O

- **Execution Model:**
  1. Only one Task executes at a time
  2. When Task hits I/O wait, it yields control to Event Loop
  3. Event Loop pauses that Task and wakes another ready Task
  4. When I/O completes, original Task resumes from where it left off

- **Critical:** Event Loop cannot forcibly interrupt — control transferred only when coroutine explicitly yields (`await`)

---

### 9.4 Python AsyncIO Explained in 9 Minutes — YouTube (NeuralNine)

- **Source:** https://www.youtube.com/watch?v=q_yk3oV14hE
- **Topic:** Quick asyncio overview — 3 concurrency approaches in Python

- **3 Approaches:**
  - **Multiprocessing** — Best for CPU-bound tasks (bypasses GIL)
  - **Multi-threading** — Limited by GIL; useful when async not supported
  - **AsyncIO** — Ideal for I/O-bound tasks; single thread + event loop

- **Core Patterns:**
  - `async def` — Define coroutines (pausable/resumable)
  - `asyncio.run(main())` — Start event loop
  - `asyncio.gather()` — Run multiple coroutines concurrently
  - `asyncio.create_task()` — Background task (await later)
  - `asyncio.wait(..., return_when=FIRST_COMPLETED)` — Fine-grained control
  - `asyncio.wait_for(coro, timeout=2)` — Timeouts

- **Code Examples:**
  ```python
  async def io_task(name, delay, iterations):
      for i in range(iterations):
          print(f"{name} - Iteration {i}")
          await asyncio.sleep(delay)

  # Concurrent
  await asyncio.gather(io_task("A", 1, 5), io_task("B", 2, 3))

  # Background task
  task = asyncio.create_task(background_task())
  await task

  # Timeout
  try:
      result = await asyncio.wait_for(long_operation(), timeout=2)
  except asyncio.TimeoutError:
      print("Took too long!")
  ```

- **Performance:** Sequential = ~11s → Concurrent = ~4.5s (for 3 tasks)

---

### 9.5 Asyncio in Python — Full Tutorial (Tech With Tim / YouTube)

- **Source:** https://www.youtube.com/watch?v=Qb9s3UiMSTA
- **Topic:** Comprehensive asyncio tutorial for Python 3.11+
- **Key Concepts:** Event loop (central hub managing tasks), Coroutines (defined with `async def`, must be awaited or wrapped in task)

- **Core Components:**
  1. **Event Loop** — Manages and distributes async tasks
  2. **Coroutines** — `async def` functions; calling returns coroutine object (does NOT execute until awaited)
  3. **Tasks** — `asyncio.create_task(coro())` for concurrent execution
  4. **Futures** — Low-level promise of a future result (rarely used directly)
  5. **Synchronization Primitives**

- **Task Management:**
  - `asyncio.create_task()` — Schedule coroutine for concurrent execution
  - `asyncio.gather()` — Run multiple concurrently, returns results in order (poor error handling — does NOT cancel others on failure)
  - `asyncio.TaskGroup` (Python 3.11+) — Preferred; auto-cancels others on failure via async context manager

- **Synchronization Primitives:**
  - **Lock** — Ensures only one coroutine accesses critical section
  - **Semaphore** — Limits access to N concurrent coroutines (throttling)
  - **Event** — Boolean flag for synchronization (wait/set)

- **Code Examples:**
  ```python
  # TaskGroup (Python 3.11+)
  async with asyncio.TaskGroup() as tg:
      task1 = tg.create_task(fetch_data(1, 2))
      task2 = tg.create_task(fetch_data(2, 3))

  # Lock
  async with lock:
      await asyncio.sleep(1)

  # Semaphore (limit to 2 concurrent)
  sem = asyncio.Semaphore(2)
  async with sem:
      await asyncio.sleep(1)
  ```

---

### 9.6 Introduction to asyncio in Python — Patrick's Software Blog

- **Source:** https://www.patricksoftwareblog.com/introduction_to_asyncio_in_python.html
- **Topic:** Practical asyncio with httpx, API calls, Semaphore throttling
- **Code Repo:** https://gitlab.com/patkennedy79/asyncio_example

- **Key Concepts:** Concurrency via 3 approaches (Processes → CPU-bound, Threads → GIL-limited, asyncio → I/O-bound); Coroutines can suspend/resume

- **Execution Patterns:**
  - **Sequential** `await` — adds up wait times (e.g., 3s + 4s + 5s = 12s)
  - **`asyncio.gather()`** — Runs concurrently, returns all results at once (~5s for above)
  - **`asyncio.as_completed()`** — Processes results as they become available (real-time output)

- **Practical Example:** Fetching user data from ReqRes API (`https://reqres.in/api/users/{id}`)
  ```python
  async def get_user_data(client: httpx.AsyncClient, index: int) -> str:
      response = await client.get(f'https://reqres.in/api/users/{index}', timeout=2.0)
      ...
  ```

- **Performance Comparison:**
  | Approach | Time |
  |----------|------|
  | Async (`as_completed`) | 0.24s |
  | Synchronous | 1.80s |
  | **Speedup** | **~7.5x** |

- **Semaphore for Rate Limiting:**
  ```python
  semaphore = asyncio.Semaphore(5)  # Max 5 concurrent
  async with semaphore:
      response = await client.get(...)
  ```

---

### 9.7 Python's asyncio: A Hands-On Walkthrough — Real Python

- **Source:** https://realpython.com/async-io-python
- **Topic:** Comprehensive async I/O walkthrough — the definitive reference
- **Key Concepts:** Single-threaded, single-process cooperative multitasking; NOT threading or multiprocessing

- **Chess Analogy (Miguel Grinberg):** Synchronous = one game at a time (12h). Asynchronous = move between tables (1h). Same person, same number of moves — just less idle time.

- **Core Building Blocks:**
  - **Awaitable objects** — most often coroutines
  - **Event loop** — schedules and executes coroutines
  - **Coroutines** — functions that can suspend and resume

- **`async`/`await` Syntax:**
  | Construct | Purpose |
  |---|---|
  | `async def` | Defines a coroutine function |
  | `await` | Suspends execution until awaited result returns; yields to event loop |
  | `async for` | Iterates over async iterator |
  | `async with` | Async context manager |

- **Rules:** `await` only inside `async def`; `yield from` inside `async def` → SyntaxError

- **Performance Comparison (count example):**
  - Synchronous (`time.sleep`): ~6.03 seconds (blocking)
  - Asynchronous (`asyncio.sleep` + gather): ~2.00 seconds (non-blocking)

- **Event Loop Details:**
  - `asyncio.run()` — Recommended way to start loop in modern Python
  - `asyncio.get_running_loop()` — Returns running loop instance
  - Pluggable implementations: `SelectorEventLoop` (Unix), `ProactorEventLoop` (Windows), `uvloop` (third-party, faster)

- **Calling coroutines:** Calling returns coroutine object — does NOT execute:
  ```python
  >>> routine = main()
  >>> routine
  <coroutine object main at 0x1027a6150>
  >>> asyncio.run(routine)
  ```

- **asyncio REPL:** `python -m asyncio` → use `await` directly at top level

- **Common Patterns:**
  - **Coroutine Chaining** — One coroutine awaits another, passes result to the next
  - **Async context managers** — `async with httpx.AsyncClient() as client:`
  - **Async iterators** — `async for` loops
  - **Queues** — `asyncio.Queue` for producer/consumer patterns
  - **Semaphores** — Rate limiting
  - **Callbacks + Futures** — Low-level control

---

## Summary Statistics

| Subdirectory | File Count | Primary Topics |
|---|---|---|
| binance-api-tutorial | 2 | Binance trading API, REST/WebSocket, spot trading |
| busha-api-tutorial | 2 | African stablecoin infrastructure, KYB, quote-execute flow |
| cryptocurrency-wallets-api-tutorial | 3 | Wallet APIs (CryptoAPIs, Cobo), MPC, HD wallets |
| face-mask-video-call-tutorial | 3 | Face masking/obscuring, OBS, UV4L, VSDC editor |
| flutterwave-tutorial | 1 | Global transfers API, OAuth2, 4-step flow |
| hermes-agents-tutorial | 3 | Hermes Agent installation, architecture, deep dive |
| paypal-tutorial | 2 | PayPal consumer setup, signup, features, security |
| paystack-tutorial | 2 | Paystack payments API, transfers, webhooks, SDKs |
| python-asyncio-tutorial | 7 | Python asyncio concepts, event loop, tasks, gather, semaphore, httpx |
| **Total** | **25** | |

---
