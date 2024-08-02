# Hello Memory

## Guide

### 1 Langchain Memory demostration

![](https://python.langchain.com/v0.2/assets/images/message_history-4c13b8b9363beb4621d605bf6b5a34b4.png)

#### llama3.1 on ollama

```sh
ollama list
NAME             ID           SIZE
llama3.1:latest  62757c860e01 4.7 GB
```

#### run

```sh
source lc_env/bin/activate
python langchain_memory.py
```

### 2 Autogen

#### llama3.1 on ollama with litellm

```sh
source ag_env/bin/activate
litellm --model ollama_chat/llama3.1
```

#### run demo

```sh
source lc_env/bin/activate
python autugen_memory.py
```

### 3 Llamaindex

<https://docs.llamaindex.ai/en/stable/module_guides/storing/chat_stores/>

### 4 crewai

<https://docs.crewai.com/core-concepts/Memory/>

## Frameworks Installation

### Ollama

<https://github.com/ollama/ollama>

### Langchain v0.2

- `langchain-core`: Base abstractions and LangChain Expression Language.
- `langchain-community`: Third party integrations.
  - Partner packages (e.g. langchain-openai, langchain-anthropic, etc.): Some integrations have been further split into their own lightweight packages that only depend on langchain-core.
- `langchain`: Chains, agents, and retrieval strategies that make up an application's cognitive architecture.
- LangGraph: Build robust and stateful multi-actor applications with LLMs by modeling steps as edges and nodes in a graph. Integrates smoothly with LangChain, but can be used without it.
- LangSmith: A developer platform that lets you debug, test, evaluate, and monitor LLM applications.

```sh
python3 -m venv lc_env
source lc_env/bin/activate

pip install --upgrade pip
pip install langchain-core langchain langchain-community langgraph langsmith
pip install -qU langchain_ollama
```

### litellm

### Augogen

```sh
python3 -m venv ag_env
source ag_env/bin/activate

pip install --upgrade pip
pip install pyautogen
pip install "litellm[proxy]"
```
