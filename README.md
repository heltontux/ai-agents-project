
# 🤖 AI Agents Project

AI Agents Project is an educational framework built from scratch to explore the internal architecture of modern AI Agents. Instead of relying on existing frameworks such as LangChain or CrewAI, this project implements the core building blocks step by step, providing a deeper understanding of how autonomous agents work.

## Why this project?

Most AI Agent projects teach developers how to use frameworks.
This project focuses on understanding how those frameworks are built internally, implementing each architectural layer from scratch.

## ✨ Objectives

- Understand the architecture behind AI Agents

- Build an extensible agent framework

- Learn Tool Calling

- Explore software engineering practices

- Apply testing, observability and clean architecture

## 🏗️ SimpleAgent Architecture
The project follows a layered architecture, keeping the Agent, LLM providers and Tools loosely coupled through abstractions.

```mermaid
flowchart TD

    U["👤 User"]
    A["🤖 SimpleAgent"]

    subgraph Core
        L["📦 BaseLLM"]
        R["🧰 ToolRegistry"]
    end

    subgraph LLM
        S["⚙️ OpenAIService"]
        O["🧠 OpenAI Responses API"]
    end

    subgraph Tools
        B["🔧 BaseTool"]
        D["📅 DateTimeTool"]
    end

    U -->|Prompt| A

    A --> L
    A --> R

    L --> S
    S --> O

    R --> B
    B --> D

    O -->|LLM Response| A
    D -->|Tool Result| A

    A -->|Final Response| U

    classDef agent fill:#2563eb,color:#fff,stroke:#1d4ed8
    classDef service fill:#10b981,color:#fff
    classDef tool fill:#f59e0b,color:#fff
    classDef api fill:#8b5cf6,color:#fff
    classDef user fill:#64748b,color:#fff

    class U user
    class A agent
    class L,R service
    class S service
    class O api
    class B,D tool
```

#### 🔄 Tool Calling Flow
The DateTime tool is a simple feature for testing the concepts involved in LLM calls.

```mermaid
sequenceDiagram

    actor User

    participant Agent as SimpleAgent
    participant LLM as OpenAIService
    participant Registry as ToolRegistry
    participant Tool as DateTimeTool

    User->>Agent: Send Prompt
    Agent->>LLM: Forward Prompt

    LLM-->>Agent: Tool Call Request

    Agent->>Registry: Find Tool
    Registry-->>Agent: DateTimeTool

    Agent->>Tool: Execute()
    Tool-->>Agent: Current Date/Time

    Agent->>LLM: Send Tool Result
    LLM-->>Agent: Final Answer

    Agent-->>User: Response
```

## 🚀 Current Features

- Generic Agent architecture 
- Tool Calling 
- Tool Registry 
- Abstract Tool interface 
- Provider abstraction (BaseLLM) 
- OpenAI integration 
- Fake LLM for testing 
- Automated tests with pytest 
- Execution observability 
- Token usage metrics
- Short-term memory

## 🛠️ Tech Stack


<div align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue.svg)

![OpenAI](https://img.shields.io/badge/OpenAI-Responses_API-412991)

![Tests](https://img.shields.io/badge/Tests-pytest-success)

![License](https://img.shields.io/badge/Status-Learning%20Project-orange)

![Build](https://img.shields.io/badge/Build-uv-yellow)

![Git](https://img.shields.io/badge/Code_versioning-git-brown)

</div>

## Project Status

🚧 Under active development

Current module:
- ✅ Generic Agent
- ✅ Tool Calling
- ✅ Testing
- ✅ Observability
- ✅ Memory

Upcoming:
- 🔜 ~~Memory~~
- 🔜 RAG
- 🔜 Planner
- 🔜 Multi-Agent
- 🔜 MCP

## 📦 Installation

### Prerequisites

- Python 3.12+
- Git
- uv (recommended)

### Installing requirements

Install Python and uv (if not already installed)
#### Windows (PowerShell)
```bash
winget install Python
python --version
```
```bash
winget install --id=astral-sh.uv -e
uv --version
```
#### Linux (Debian derivatives)
```bash
apt install python3
python3 --version
```

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv --version
```
### Clone the repository

```bash
git clone https://github.com/heltontux/ai-agents-project.git

cd ai-agents-project
```
### Download the dependencies

```bash
uv sync
```
```bash
uv add pytest
```

### Configure environment variables

Create a `.env` file in the project root and insert the LLM API key.

```env
OPENAI_API_KEY=your_api_key
OPENAI_MODEL=gpt-5.5
```
## ✅ Running Tests

Execute all automated tests:

```bash
uv run pytest -v
```
Current test coverage includes:

- Tool implementations
- Tool Registry
- Agent orchestration
- Fake LLM
- Dependency injection


## ▶️ Running

Start the application with:

```bash
uv run python -m app.main
```
Windows runs uv as a Python module. If you can't use uv directly, do the following:
```bash
python -m uv run python -m app.main
```

Example:

```text
You: What time is it?

LLM responded in 3.112s
Tool selected: get_current_datetime
Input Tokens: 481
Output Tokens: 878
Total Tokens: 1359

TuxBot: It is currently 15:09.
```

## 🗺️ Roadmap

### Module 1 — LLM Fundamentals ✅

- Prompt Engineering
- Function Calling
- OpenAI Responses API

### Module 2 — Agent Framework ✅

- Generic Agent
- Tool Calling
- Tool Registry
- Dependency Injection
- Testing
- Observability
- Token Metrics

### Module 3 — Memory 🚧

- Conversation History
- Short-Term Memory
- Context Window Management

### Module 4 — RAG

- Embeddings
- Vector Database
- Semantic Search

### Module 5 — Planning

- ReAct
- Planner
- Reflection

### Module 6 — Multi-Agent Systems

- Agent Communication
- Specialized Agents
- Debate

### Module 7 — MCP

- Model Context Protocol
- External Integrations

## 🤝 Contributing

Contributions are welcome!

If you'd like to improve the project:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

Please follow the project's coding style and keep the architecture clean and modular.

## 📄 License

This project is licensed under the MIT License.

See the [LICENSE](LICENSE.txt) file for details.
