import os
import autogen
from autogen.agentchat.contrib.capabilities import transform_messages, transforms

os.environ['AUTOGEN_USE_DOCKER'] = 'no'
llm_config = {
    "config_list": [
        {
            "model": "NotRequired",  # Loaded with LiteLLM command
            "api_key": "NotRequired",  # Not needed
            "base_url": "http://localhost:4000"  # Your LiteLLM URL
        }
    ],
    "cache_seed": None  # Turns off caching, useful for testing different models
}

# Define your agent; the user proxy and an assistant
assistant = autogen.AssistantAgent(
    "assistant",
    llm_config=llm_config,
)
user_proxy = autogen.UserProxyAgent(
    "user_proxy",
    human_input_mode="NEVER",
    is_termination_msg=lambda x: "TERMINATE" in x.get("content", ""),
    max_consecutive_auto_reply=10,
)

context_handling = transform_messages.TransformMessages(
    transforms=[
        transforms.MessageHistoryLimiter(max_messages=10),
        transforms.MessageTokenLimiter(max_tokens=1000, max_tokens_per_message=50, min_tokens=500),
    ]
)
context_handling.add_to_agent(assistant)


def tasting(assistant: autogen.ConversableAgent, user_proxy: autogen.UserProxyAgent):
    for _ in range(1000):
        # define a fake, very long messages
        assitant_msg = {"role": "assistant", "content": "test " * 1000}
        user_msg = {"role": "user", "content": ""}

        assistant.send(assitant_msg, user_proxy, request_reply=False, silent=True)
        user_proxy.send(user_msg, assistant, request_reply=False, silent=True)

    try:
        user_proxy.initiate_chat(assistant, message="plot and save a graph of x^2 from -10 to 10", clear_history=False)
    except Exception as e:
        print(f"Encountered an error with the base assistant: \n{e}")


tasting(assistant, user_proxy)
