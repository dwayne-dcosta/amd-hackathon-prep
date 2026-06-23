# 🛡️ Enterprise Token-Efficient Routing Hub
**Track 1 Optimization Panel - Deployed on AMD Developer Cloud & Fireworks AI Infrastructure**

## 💡 Project Overview
An automated, containerized hybrid routing agent engineered to solve the commercial scalability and cost limitations of enterprise LLM deployments. By sitting between a zero-cost local inference node and high-performance remote AMD Instinct GPU clusters via Fireworks AI managed endpoints, the engine intelligently delegates incoming tasks based on real-time token footprint metrics and semantic reasoning triggers.


## 📊 Strategic Value Proposition & Business Model
* **The Problem**: Relying entirely on heavy cloud APIs introduces unsustainable corporate cost scaling, token budget waste, and unmanaged latency spikes.
* **The Solution**: A modular routing gateway that maximizes hardware efficiency, providing strict budget guardrails while guaranteeing 100% reasoning accuracy.
* **Market Scope (TAM/SAM)**: Targeted at enterprise software architectures deploying production-grade conversational agents, automated data parsing, and continuous code optimization pipelines.

---

## 🛠️ Technology Stack & Architecture
* **Core Engine**: Python 3.11, Tiktoken (`cl100k_base` tokenizer layout)
* **Frontend Dashboard**: Streamlit (Native eye-friendly Dark-Mode Framework)
* **Container Layer**: Docker (Multi-stage lightweight Linux configuration)
* **Target Compute Infrastructure**: AMD Instinct MI300X Hardware Nodes & Fireworks AI Managed Endpoints

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
