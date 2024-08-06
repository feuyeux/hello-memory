import json

from langchain.chains.llm import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, HumanMessagePromptTemplate
from langchain_core.runnables import ConfigurableFieldSpec
from langchain_community.chat_message_histories import ChatMessageHistory, FileChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

llama31 = ChatOllama(
    model="llama3.1",
)

gemma2 = ChatOllama(
    model="gemma2",
)

# choose the model to use
llm = llama31

#
# print("==== LangChain Memory TESTING ====")
# prompt = ChatPromptTemplate.from_messages([
#     MessagesPlaceholder(variable_name='chat_history'),
#     HumanMessagePromptTemplate.from_template('{question}')
# ])
# memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
# memory_chain = LLMChain(llm=llm, memory=memory, prompt=prompt)
# round1 = memory_chain.predict(question="hi im bob!")
# print("round1", round1)
# round2 = memory_chain.predict(question="whats my name?")
# print("round2", round2)

#
print("==== LangChain History TESTING ====")
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You're an assistant who speaks in {language}. Respond in 20 words or fewer",
        ),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}"),
    ]
)

history_chain = prompt | llm

store = {}


def get_session_history(user_id: str, session_id: str) -> BaseChatMessageHistory:
    key = user_id + "-" + session_id
    if key not in store:
        # store[key] = ChatMessageHistory()
        store[key] = FileChatMessageHistory(".chat_history.json")
    return store[key]


with_message_history = RunnableWithMessageHistory(
    history_chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history",
    history_factory_config=[
        ConfigurableFieldSpec(
            id="user_id",
            annotation=str,
            name="User ID",
            description="Unique identifier for the user.",
            default="",
            is_shared=True,
        ),
        ConfigurableFieldSpec(
            id="session_id",
            annotation=str,
            name="Conversation ID",
            description="Unique identifier for the conversation.",
            default="",
            is_shared=True,
        ),
    ],
)

#
round1 = with_message_history.invoke(
    {
        "language": "french", "input": "hi im bob!"
    },
    config={"configurable": {"user_id": "han", "session_id": "2718281828"}}
)
metadata = json.dumps(round1.response_metadata, indent=4, sort_keys=True)
usage_metadata = json.dumps(round1.usage_metadata, indent=4, sort_keys=True)
print("[id]", round1.id)
print("[content]", round1.content)
print("[response_metadata]", metadata)
print("[usage_metadata]", usage_metadata)
#
round2 = with_message_history.invoke(
    {
        "language": "french", "input": "whats my name?"
    },
    config={"configurable": {"user_id": "han", "session_id": "2718281828"}}
)
metadata = json.dumps(round2.response_metadata, indent=4, sort_keys=True)
usage_metadata = json.dumps(round2.usage_metadata, indent=4, sort_keys=True)
print("[id]", round2.id)
print("[content]", round2.content)
print("[response_metadata]", metadata)
print("[usage_metadata]", usage_metadata)
