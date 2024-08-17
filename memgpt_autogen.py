import autogen
import openai
from memgpt.autogen.memgpt_agent import create_autogen_memgpt_agent
import os

os.environ['AUTOGEN_USE_DOCKER'] = 'no'
config_list = [
    {
        "api_key": "sk-12345",
        "api_base": "http://localhost:1234/v1",
        "api_type": "open_ai",

    }
]

openai.api_key = "sk-12345"
openai.api_base = "http://localhost:1234/v1"

llm_config = {"config_list": config_list, "seed": 44,
              "request_timeout": 600, "temperature": 0.7}

# The user agent
user_proxy = autogen.UserProxyAgent(
    name="User_proxy",
    system_message="A human admin.",
    code_execution_config={"last_n_messages": 2, "work_dir": "groupchat"},
    human_input_mode="NEVER"
)

# The agent playing the role of the product manager (PM)
ProdManager = autogen.AssistantAgent(
    name="Product_manager",
    system_message="Creative in software product ideas.",
    llm_config=llm_config
)

use_memgpt = True

if not use_memgpt:
    print("Using AutoGen Coder")
    coder = autogen.AssistantAgent(
        name="Coder",
        system_message=f"I am a 10x engineer, trained in Python. I was the first engineer at Microsoft "
        f"(which I make sure to tell everyone I work with).\n"
        f"You are participating in a group chat with a user ({
            user_proxy.name}) "
        f"and a product manager ({ProdManager.name}).",
        llm_config=llm_config,
    )
#
else:
    print("Using MemGPT Coder")
    agent_config = dict(
        name="MemGPT_coder",
        persona="I am an engineer, trained in Python",
        human=f"You are participating in a group chat with a user ({
            user_proxy.name}) and a product manager ({ProdManager.name}).",
        llm_config=llm_config,
    )
    coder = create_autogen_memgpt_agent(
        agent_config=agent_config
    )

# Initialize the group chat between the user and two LLM agents (PM and coder)
groupchat = autogen.GroupChat(
    agents=[user_proxy, ProdManager, coder], messages=[], max_round=2)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)

# Begin the group chat with a message from the user
user_proxy.initiate_chat(
    manager,
    message="develop a SaaS solution designed to streamline and enhance supply chain management for businesses.that's it."
)
