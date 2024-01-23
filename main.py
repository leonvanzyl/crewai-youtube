from dotenv import load_dotenv
load_dotenv()

from crewai import Agent, Task, Crew
from langchain.tools import DuckDuckGoSearchRun

search_tool = DuckDuckGoSearchRun()

# Team Members
researcher = Agent(
    role="Senior Research Analyst",
    goal='Uncover cutting-edge developments in AI and data science',
    backstory="""You work at a leading tech think tank.
    Your expertise lies in identifying emerging trends.
    You have a knack for dissecting complex data and presenting
    actionable insights.""",
    verbose=True,
    allow_delegation=False,
    tools=[search_tool]
)

writer = Agent(
  role='Tech Content Strategist',
  goal='Craft compelling content on tech advancements',
  backstory="""You are a renowned Content Strategist, known for
  your insightful and engaging articles.
  You transform complex concepts into compelling narratives.""",
  verbose=True,
  allow_delegation=False,
)

# Tasks
task1 = Task(
  description="""Conduct a comprehensive analysis of the latest advancements in AI in 2024.
  Identify key trends, breakthrough technologies, and potential industry impacts.
  Your final answer MUST be a full analysis report""",
  agent=researcher
)

task2 = Task(
  description="""Using the insights provided, develop an engaging blog
  post that highlights the most significant AI advancements.
  Your post should be informative yet accessible, catering to a tech-savvy audience.
  Make it sound cool, avoid complex words so it doesn't sound like AI.
  Your final answer MUST be the full blog post of at least 4 paragraphs.""",
  agent=writer
)

# Create Crew
crew = Crew(
    agents=[researcher, writer],
    tasks=[task1, task2],
    verbose=2
)

# Start work!
result = crew.kickoff()
print(result)