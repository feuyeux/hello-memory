from crewai import Crew, Agent, Task, Process
from langchain_openai import ChatOpenAI

import os
os.environ["OPENAI_API_KEY"] = "NA"

llm = ChatOpenAI(
    model="llama3.1",
    base_url="http://localhost:11434/v1")

father_agent = Agent(
    role='Father',
    goal='You are the father of a kid. The kid may ask you any question.'
         'Your goal is to provide a satisfactory answer to the kid.',
    verbose=True,
    memory=True,
    backstory=(
        "You are a 40 year old male. You live in the city of San Jose with your wife and kid who is 10 years old."
    ),
    tools=[],
    allow_delegation=True,
    llm=llm
)

father_task = Task(
    description=(
        "Your task is to answer the {question} of your kid in a satisfactory "
        "and legible way so that it makes sense to your kid. "
    ),
    expected_output='Answer to your kid question',
    tools=[],
    # human_input = True,
    agent=father_agent
)

parent_crew = Crew(
    agents=[father_agent],
    tasks=[father_task],
    process=Process.sequential,
    memory=True,
    verbose=True,
    embedder={
        "provider": "huggingface",
        "config": {
                    # https://huggingface.co/mixedbread-ai/mxbai-embed-large-v1
                    "model": "mixedbread-ai/mxbai-embed-large-v1",
        }
    }
)

while True:
    question = input("Kid: \n")
    answer = parent_crew.kickoff({"question": question})

    print("***********************")
    print(answer)
