from crewai import Agent
from crewai_tools import SerperDevTool
from langchain_openai import ChatOpenAI
from langchain_huggingface import HuggingFaceEmbeddings
from crewai import Crew, Process, Task
import os

search_tool = SerperDevTool()

os.environ["OPENAI_API_KEY"] = "NA"

llm = ChatOpenAI(
    model="llama3.1",
    base_url="http://localhost:11434/v1")

researcher = Agent(
    llm=llm,
    role='Senior Researcher',
    goal='Discover latest trends in {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "Driven by curiosity, you're at the forefront of"
        "innovation, eager to explore and share knowledge that could change"
        "the world."
    ),
    tools=[search_tool],
    allow_delegation=True
)

writer = Agent(
    llm=llm,
    role='Writer agent',
    goal='Narrate contents to know more about {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools=[search_tool],
    allow_delegation=False
)

research_task = Task(
    description=(
        "Identify the next big trend in {topic}."
        "Focus on identifying pros and cons and the overall narrative."
        "Your final report should clearly articulate the key points,"
        "its market opportunities, and potential risks."
    ),
    expected_output='A comprehensive 3 paragraphs long report on the latest AI trends.',
    tools=[search_tool],
    agent=researcher,
)

write_task = Task(
    description=(
        "Compose an insightful article on {topic}."
        "Focus on the latest trends and how it's impacting the industry."
        "This article should be easy to understand, engaging, and positive."
    ),
    expected_output='A 4 paragraph article on {topic} advancements formatted as markdown.',
    tools=[search_tool],
    agent=writer,
    async_execution=False,
    output_file='new-blog-post.md'
)

crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task],
    process=Process.sequential,  # Optional: Sequential task execution is default
    memory=True,
    embedder={
        "provider": "huggingface",
        "config": {
            # https://huggingface.co/mixedbread-ai/mxbai-embed-large-v1
            "model": "mixedbread-ai/mxbai-embed-large-v1",
        }
    },
    cache=True,
    max_rpm=100,
    share_crew=True
)

result = crew.kickoff(inputs={'topic': 'AI in healthcare'})
print(result)
