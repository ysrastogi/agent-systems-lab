# Agent Systems Lab 🧪

Welcome to the **Agent Systems Lab**, an open-ended playground for building, training, and benchmarking various AI agent architectures. This repository serves as a systematic sandbox for exploring how differently structured agents think, act, and solve complex tasks.

---

## 🎯 Project Goals

The objective of this lab is to move beyond "vibes-based" development by implementing and stress-testing the most effective agentic patterns. We aim to answer:
*   *Which architecture is best for complex multi-step reasoning?*
*   *How does self-reflection impact hallucination rates?*
*   *What is the tradeoff between reasoning steps and latency?*

---

## 🏗️ Architecture Playground: Roadmap

We are systematically exploring the following architectures. Each has its own directory in `architectures/`:
Future Architectures:
    - [ ] ReAct
    - [ ] Planner-Executor
    - [ ] Reflection/Critic
    - [ ] Memory-Augmented
    - [ ] Swarm


## 🔬 Benchmark Tasks

Each architecture is pitted against three primary "Hard Tasks":

1.  **Research Assistant** 📚: Synthesizing deep reports on nuanced technical topics (e.g., Vector DB tradeoffs).
    - *Metrics:* Depth, Accuracy, Hallucination Rate.
2.  **Code Debugger** 💻: Fixing algorithmic bugs that require deep tracing.
    - *Metrics:* Pass/Fail, Success Rate, Execution Cost.
3.  **Data Analyst** 📊: Extracting numerical insights from raw, unstructured data.
    - *Metrics:* Correctness, Reliability, Reasoning Clarity.

---

## 🛠️ Repository Structure

```text
agent-systems-lab/
├── core/                   # Shared primitives (Base Agent, Runner, Tool Registry)
├── tasks/                  # Task definitions & benchmarks
├── architectures/          # Modular implementations of agent loops
├── runs/                   # Versioned JSON logs (Goldmine for analysis)
├── evals/                  # Metric dashboards & comparisons
├── experiments/            # Scratch space for "messy" innovative ideas
└── main.py                 # The experimental entry point
```

## 🚀 Get Running

1.  **Run current experiments**:
    ```bash
    python main.py
    ```
2.  **Inspect performance**: Look at `evals/results.md` for a summary or drill into `runs/` for the step-by-step thinking of the agent.
3.  **Contribute**: Fork an architecture, tweak the prompt or logic, and compare it against the baseline in `evals/`.
