import json
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import ConfigurableFieldSpec
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

llama31 = ChatOllama(
    model="llama3.1",
)

gemma2 = ChatOllama(
    model="gemma2",
)

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

runnable = prompt | llama31

store = {}

# https://api.python.langchain.com/en/latest/community_api_reference.html#module-langchain_community.chat_message_histories


def get_session_history(user_id: str, session_id: str) -> BaseChatMessageHistory:
    key = user_id + "-" + session_id
    if key not in store:
        store[key] = ChatMessageHistory()
    return store[key]


with_message_history = RunnableWithMessageHistory(
    runnable,
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
