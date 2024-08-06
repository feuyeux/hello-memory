# Hello Memory

## 1 Langchain Memory demostration

![message history](message_history.png)

### 1.1 Langchain & Ollama Installation

#### Ollama

<https://github.com/ollama/ollama>

#### Langchain v0.2

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
pip install langchain-core langchain langchain-community
# pip installlanggraph langsmith
pip install -qU langchain_ollama
```

### 1.2 llama3.1 on ollama

<https://ollama.com/library>

```sh
ollama list
NAME             ID           SIZE
llama3.1:latest  62757c860e01 4.7 GB
```

### 1.3 run

```sh
source lc_env/bin/activate
python langchain_memory.py
```

### 1.4 output

#### 1.4.1 gemma2

```sh
[id] run-76e65c2d-75ba-4ff1-bc39-a943a56dd813-0
[content] Bonjour Bob !Enchanté de faire ta connaissance.  
[response_metadata] {
    "created_at": "2024-08-03T11:58:32.6524729Z",
    "done": true,
    "done_reason": "stop",
    "eval_count": 13,
    "eval_duration": 718158000,
    "load_duration": 5976973700,
    "message": {
        "content": "",
        "role": "assistant"
    },
    "model": "gemma2",
    "prompt_eval_count": 31,
    "prompt_eval_duration": 76641000,
    "total_duration": 6776227700
}
[usage_metadata] {
    "input_tokens": 31,
    "output_tokens": 13,
    "total_tokens": 44
}

[id] run-400361cb-e618-4bd7-9755-d963ce7bb729-0
[content] Votre nom est Bob. 😊
[response_metadata] {
    "created_at": "2024-08-03T11:58:33.6709248Z",
    "done": true,
    "done_reason": "stop",
    "eval_count": 9,
    "eval_duration": 465788000,
    "load_duration": 22591100,
    "message": {
        "content": "",
        "role": "assistant"
    },
    "model": "gemma2",
    "prompt_eval_count": 57,
    "prompt_eval_duration": 78038000,
    "total_duration": 570082600
}
[usage_metadata] {
    "input_tokens": 57,
    "output_tokens": 9,
    "total_tokens": 66
}
```

#### 1.4.2 llama3.1

```sh
[id] run-4c80216f-dda0-4e08-9b8c-cec66c89b223-0
[content] Bonjour, Bob! Enchanté! Comment ça va aujourd'hui? (Hello, Bob! Nice to meet you! How are you today?)
[response_metadata] {
    "created_at": "2024-08-03T11:59:12.8925514Z",
    "done": true,
    "done_reason": "stop",
    "eval_count": 30,
    "eval_duration": 692782000,
    "load_duration": 2272843200,
    "message": {
        "content": "",
        "role": "assistant"
    },
    "model": "llama3.1",
    "prompt_eval_count": 35,
    "prompt_eval_duration": 36290000,
    "total_duration": 3005458200
}
[usage_metadata] {
    "input_tokens": 35,
    "output_tokens": 30,
    "total_tokens": 65
}

[id] run-c5f20332-fef3-4061-b22e-5a463ca50725-0
[content] Ton nom est... Bob! (Your name is... Bob!)
[response_metadata] {
    "created_at": "2024-08-03T11:59:13.6900852Z",
    "done": true,
    "done_reason": "stop",
    "eval_count": 14,
    "eval_duration": 313995000,
    "load_duration": 12513600,
    "message": {
        "content": "",
        "role": "assistant"
    },
    "model": "llama3.1",
    "prompt_eval_count": 79,
    "prompt_eval_duration": 28343000,
    "total_duration": 358870100
}
[usage_metadata] {
    "input_tokens": 79,
    "output_tokens": 14,
    "total_tokens": 93
}
```

## 2 Autogen

### 2.1 Autogen & litellm Installation

```sh
python3 -m venv ag_env
source ag_env/bin/activate

pip install --upgrade pip
pip install pyautogen "litellm[proxy]"
```

### 2.2 run litellm (llama3.1 on ollama)

```sh
source ag_env/bin/activate
litellm --model ollama_chat/llama3.1
```

### 2.3 run demo

```sh
source lc_env/bin/activate
python autugen_memory.py
```

## 3 Llamaindex

<https://docs.llamaindex.ai/en/stable/examples/agent/memory/composable_memory/>

### 3.1 llama-index Installation

```sh
python3 -m venv li_env
source ag_env/bin/activate

pip install --upgrade pip
pip install llama-index llama-index-llms-ollama llama-index-embeddings-ollama
```

### 3.2 run vectorMemory

```sh
source lc_env/bin/activate
python llamaindex_memory.py
```

## 4 crewai

<https://docs.crewai.com/core-concepts/Memory/>

### 4.0 Memory System Components

| Component             | Description                                                  |
| :-------------------- | :----------------------------------------------------------- |
| **Short-Term Memory** | Temporarily stores recent interactions and outcomes, enabling agents to recall and utilize information relevant to their current context during the current executions. |
| **Long-Term Memory**  | Preserves valuable insights and learnings from past executions, allowing agents to build and refine their knowledge over time. So Agents can remember what they did right and wrong across multiple executions |
| **Entity Memory**     | Captures and organizes information about entities (people, places, concepts) encountered during tasks, facilitating deeper understanding and relationship mapping. |
| **Contextual Memory** | Maintains the context of interactions by combining `ShortTermMemory`, `LongTermMemory`, and `EntityMemory`, aiding in the coherence and relevance of agent responses over a sequence of tasks or a conversation. |

#### How Memory Systems Empower Agents

1. **Contextual Awareness**: With short-term and contextual memory, agents gain the ability to maintain context over a conversation or task sequence, leading to more coherent and relevant responses.
2. **Experience Accumulation**: Long-term memory allows agents to accumulate experiences, learning from past actions to improve future decision-making and problem-solving.
3. **Entity Understanding**: By maintaining entity memory, agents can recognize and remember key entities, enhancing their ability to process and interact with complex information.

### 4.1 crewai Installation

```sh
python3 -m venv crew_env
source crew_env/bin/activate

pip install --upgrade pip
pip install 'crewai[tools]'
pip install -U langchain-huggingface
```

### 4.2 run crewai

<https://www.youtube.com/watch?v=-hHplC_gcSE>

```sh
python crewai_memory.py
```

```sh
How does bird fly?
```

## 5 memary

```sh
pip install virtualenv 
virtualenv mm_venv --python=3.11.9

source mm_venv/bin/activate
pip install --upgrade pip

pip install memary
pip install -r requirements.txt
```
