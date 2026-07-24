<p align="center">
  <img src="Instinct-Gate-icon-clean-remove-bg.png" width="500" alt="Instinct Gate Logo"/>
</p>

# 🛡️ Instinct Gate: Enterprise Token-Efficient Routing Hub
**Multi-Architecture Optimization Panel & AI Governance Enforcement Gateway**  
*Deployed on AMD Developer Cloud Architecture & Fireworks AI Infrastructure*

[![Release Version](https://shields.io)](https://github.com)
[![Compliance Framework](https://shields.io)](config/compliance_policy.json)

---

## 🏛️ Project & Governance Overview
Instinct Gate is an institutional-grade, containerized AI infrastructure gateway engineered to enforce **data lifecycle governance, resource allocation bounds, and automated safety fallback routing** right at the network boundary [INDEX]. 

By sitting between local, alignment-tuned open-source inference nodes running on your **AMD hardware runtime** and high-performance remote cloud clusters via Fireworks AI managed endpoints, the engine intelligently delegates incoming tasks based on real-time token footprint metrics, semantic reasoning triggers, and hardcoded compliance policies [INDEX].

Instead of presenting an abstract AI wrapper app, Instinct Gate converts theoretical AI alignment principles—such as **UNESCO Ethics Guidelines** and **EU AI Act mandates**—into infrastructure-enforced software layers suitable for fellowships (like SPAR, One League, and AIAF) and enterprise software architectures alike [INDEX].

---

## 🏛️ Core Alignment Frameworks Enforced

1. **Controlled Data Lifecycles (UNESCO AI Guidelines Art. 21):** Enforces strict temporal boundaries on data retention using an automated, cryptographic data-purging engine that scrubs log caches the second they cross corporate storage policies [INDEX].
2. **System Robustness & Fail-Safe Redundancy (EU AI Act Title III):** Provides dynamic safety interceptors [INDEX]. If a prompt triggers content moderation alerts or downstream API failures occur, the gateway instantly routes traffic to an alignment-tuned model running locally on your hardware runtime [INDEX].
3. **Observability & Auditing Ledger (Accountability Principle):** Outputs real-time JSON infrastructure telemetry (including token throughput, calculation outlays, and budget circuit breaker states) to feed persistent analytical dashboards [INDEX].

---

## 📊 Strategic Value Proposition & Business Model
* **The Problem**: Relying entirely on heavy cloud APIs introduces unsustainable corporate cost scaling, token budget waste, and unmanaged latency spikes.
* **The Solution**: A modular routing gateway that maximizes hardware efficiency, providing strict budget guardrails while guaranteeing 100% reasoning accuracy.
* **Market Scope (TAM/SAM)**: Targeted at enterprise software architectures deploying production-grade conversational agents, automated data parsing, and continuous code optimization pipelines.

---

## 📂 Production-Grade Repository Topology

```text
instinct-gate/
├── config/                  # Immutable Governance Policy Configuration
│   └── compliance_policy.json # Hardcoded data boundaries & safety limits
├── src/                     # Core Routing, Optimization, & Enforcement Engine
│   ├── app.py               # Main System Gateway Core Entrypoint
│   ├── compliance_engine.py # Asynchronous 60-Day Data Purging Module
│   ├── safety_router.py     # Dynamic Fallback & Safety Interceptor Routing
│   ├── rate_limiter.py      # Sliding-Window Log Engine Matrix
│   ├── budget_guard.py      # Accumulator Loop & Spending Circuit Breaker
│   ├── cache_manager.py     # Sub-Millisecond Route Serialization Cache
│   └── judge_simulation.py  # Advanced Stress-Testing Benchmarking Suite
└── telemetry/               # Logic Feeding Real-Time Audit Metrics
    └── 1_Dashboard.py       # Live Visualization Analytics Canvas Engine
```

---

## 🚀 Local Deployment & Verification

### Prerequisites
Ensure you have Docker Desktop running on your host machine.

### 1. Build the Isolated Container
Execute this command in your terminal to compile the container image using the optimized registry mirror:
```bash
docker build -t amd-router-test .
```

### 2. Launch the Web Interface
Boot the container and map the internal web server network port directly to your local machine browser layout:
```bash
docker run --rm -p 8501:8501 amd-router-test
```

Once initialized, navigate to `http://localhost:8501` in your web browser to interact with the real-time dynamic dashboard.

---

## 🛠️ Local Verification & Development Deployment

Instinct Gate is fully containerized and strictly adheres to the official AMD Hackathon Track 1 execution runtime contract. The container operating architecture is completely stateless, dynamic, and free of hardcoded variables.

### 📦 1. Multi-Architecture Container Registry Ingestion
Instinct Gate is compiled natively into a cross-platform, multi-architecture container manifest. The single image tag automatically pulls the correct architecture matching your target deployment node, supporting enterprise cloud clusters, Apple Silicon hardware, and localized edge devices simultaneously.

* **Supported Platforms:** Intel Cloud (`linux/amd64`), Apple Silicon / Mobile (`linux/arm64`), and Legacy Desktop (`linux/386` x86).

Pull the production layers from the GitHub Container Registry using the unified tag:
```bash
docker pull ghcr.io/dwayne-dcosta/instinct-gate:latest
```

### 🚢 2. Running Local Grader Pipeline Simulation
To simulate the automated grading harness evaluation locally, mount your task input/output directories and pass the required environment configuration variables at runtime:

```bash
docker run --rm \
  -v \$(pwd)/input:/input \
  -v \$(pwd)/output:/output \
  -e FIREWORKS_API_KEY="your_api_key_here" \
  -e FIREWORKS_BASE_URL="https://fireworks.ai" \
  -e ALLOWED_MODELS="minimax-m3,gemma-4-31b-it" \
  ghcr.io/dwayne-dcosta/instinct-gate:latest
```

### 📋 3. Input / Output Data Contract Enforcement
* **Ingestion Portal:** Reads structured array strings sequentially from `/input/tasks.json` matching the `[{"task_id": "...", "prompt": "..."}]` schema layout.
* **Egress Mapping:** Outputs valid, machine-parsable JSON matching the required schema to `/output/results.json` before signaling execution complete via a clean exit code (`exit 0`).

---

## 🔑 Configuration & API Keys

To run this application, you must provide your API keys for your local routing matrix and remote Fireworks AI serverless inference clusters.

### Local Development
Create a Streamlit secrets file at `.streamlit/secrets.toml` in your root directory and inject your credentials using the following structure:

```toml
# .streamlit/secrets.toml
FIREWORKS_API_KEY = "your_fireworks_ai_api_key_here"
LOCAL_EDGE_ENDPOINT = "your_local_inference_node_key_here"
```

### Cloud Deployment (Streamlit Community Cloud)
If running on the Streamlit Cloud hub ecosystem, navigate straight to your App Dashboard -> **Settings** -> **Secrets**, and paste the exact same TOML parameters into the cloud configuration canvas workspace panel.


