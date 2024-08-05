from llama_index.llms.ollama import Ollama
from llama_index.core.tools import FunctionTool
from llama_index.core.agent import FunctionCallingAgentWorker
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.core.memory import (
    VectorMemory,
    SimpleComposableMemory,
    ChatMemoryBuffer,
)

import nest_asyncio

nest_asyncio.apply()

llm = Ollama(model="llama3.1:latest", request_timeout=120.0)

ollama_embedding = OllamaEmbedding(
    model_name="llama3",
    base_url="http://localhost:11434",
    ollama_additional_kwargs={"mirostat": 0},
)

vector_memory = VectorMemory.from_defaults(
    vector_store=None,  # leave as None to use default in-memory vector store
    embed_model=ollama_embedding,
    retriever_kwargs={"similarity_top_k": 2},
)

chat_memory_buffer = ChatMemoryBuffer.from_defaults()

composable_memory = SimpleComposableMemory.from_defaults(
    primary_memory=chat_memory_buffer,
    secondary_memory_sources=[vector_memory],
)


def multiply(a: int, b: int) -> int:
    """Multiply two integers and returns the result integer"""
    return a * b


def mystery(a: int, b: int) -> int:
    """Mystery function on two numbers"""
    return a**2 - b**2


multiply_tool = FunctionTool.from_defaults(fn=multiply)
mystery_tool = FunctionTool.from_defaults(fn=mystery)

agent_worker = FunctionCallingAgentWorker.from_tools(
    [multiply_tool, mystery_tool], llm=llm, verbose=True
)
agent_with_memory = agent_worker.as_agent(memory=composable_memory)

agent_with_memory.chat("What is the mystery function on 5 and 6?")
agent_with_memory.chat("What happens if you multiply 2 and 3?")

agent_with_memory.chat(
    "What was the output of the mystery function on 5 and 6 again? Don't recompute."
)
agent_with_memory.chat(
    "What was the output of the multiply function on 2 and 3 again? Don't recompute."
)
