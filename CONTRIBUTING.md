# Contributing to Instinct Gate 🤝

First off, thank you for taking the time to contribute! Instinct Gate thrives as an open-source, enterprise-ready microservice because of developers like you. 

By contributing to this repository, you help make LLM deployments more cost-effective, token-aware, and performant for everyone.

---

## 📜 Code of Conduct & Governance
As the creator and lead maintainer of this project, I retain final structural oversight. To maintain elite software quality, ensure your modifications align with our architectural standards before opening a Pull Request (PR). All approved contributions will be legally released under this project's master open-source license.

---

## ⚙️ Core Engineering Standards

To prevent codebase degradation and protect our highly optimized, lightweight runtime footprints, all submissions must respect these five structural invariants:

1. **Decoupled Architecture:** Keep new third-party model connectors, routing heuristic algorithms, and analytics dashboards modular. They must remain isolated from the main container gateway entrypoint (`app.py`).
2. **Forced Absolute Pathing:** Never use relative pathing sequences (`./output`) for file I/O operations. To survive strict sandboxed cloud volume-mounts, always anchor data persistence processes using Python's absolute directory resolution (`os.path.abspath`).
3. **Stream Flushing Integrity:** When writing data payload buffers to disk storage, always trigger manual memory flushes (`f.flush()`) and system synchronization calls (`os.fsync(f.fileno())`) to guarantee zero data loss upon container exit.
4. **Dual-Input Fallback Support:** Any changes to the main execution block must preserve both input ingestion tracks: reading arrays natively from `/input/tasks.json` or falling back cleanly to command-line string array parsing (`sys.argv`).
5. **No Layer Bloat:** Keep dependencies tight. Check your `requirements.txt` changes carefully to maintain our tiny, rapid-deployment multi-architecture container layer sizes.

---

## 🧪 Mandatory Local Verification Matrix

Before opening a Pull Request, you **must** verify your container execution integrity locally by mocking our production sandbox infrastructure volume mounts. 

Follow these steps to run a local simulation check:

### 1. Structure Your Mock Directories
Create temporary local test directories on your development workstation:
```bash
mkdir -p test_input test_output
```

### 2. Create a Mock `tasks.json` Payload
Place a standard batch file inside your input folder (`test_input/tasks.json`) matching the platform's multi-task evaluation array:
```json
[
  {"task_id": "T01", "prompt": "Verify system integration performance bounds."},
  {"task_id": "T02", "prompt": "Run rapid edge routing calculation."}
]
```

### 3. Execute the Docker Sandbox Harness
Compile your branch changes and boot up the container, forcing it to interact with your mock folders:
```bash
# Build your local development layers
docker build -t instinct-gate-dev .

# Run the localized volume mount check
docker run --rm \
  -v \$(pwd)/test_input:/input \
  -v \$(pwd)/test_output:/output \
  instinct-gate-dev
```

### 4. Assert Output Schema Compliance
Open your generated `test_output/results.json` file and verify that your changes output the exact dictionary validation keys required by the evaluation schema:

```json
[
  {
    "task_id": "T01",
    "answer": "REMOTE_PREMIUM",
    "route": "REMOTE_PREMIUM",
    "tokens": 7,
    "estimated_cost": 0.00000105,
    "reasoning": "Routed successfully via Instinct Gate."
  },
  {
    "task_id": "T02",
    "answer": "LOCAL_CHEAP",
    "route": "LOCAL_CHEAP",
    "tokens": 4,
    "estimated_cost": 0.0,
    "reasoning": "Routed successfully via Instinct Gate."
  }
]
```
*Your PR description must include a copy of your successful local schema test logs to be considered for a merge.*

---

## 🚀 How to Submit a Pull Request

1. **Fork the Repository** and create a feature branch off of the `main` branch:
   ```bash
   git checkout -b feature/your-awesome-upgrade
   ```
2. **Commit your changes** using clean, descriptive engineering messages.
3. **Push to your fork** and open a **Pull Request** targeting our `main` branch.
4. Participate actively in the code review discussion!

Thank you for building the future of token-efficient infrastructure with Instinct Gate! 🚀
