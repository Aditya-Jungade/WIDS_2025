from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class ResumeAnalyzer():
    """ResumeAnalyzer crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools

    llm_gemini2 = LLM(
        model = "google/gemini-2.0-flash-lite", 
        temperature = 0.1, 
        max_tokens = 2000
    )

    llm_gemini = LLM(
        model = "google/gemini-2.0-flash", 
        temperature = 0.5, 
        max_tokens = 2000
    )

    llm_groq = LLM(
        model = "groq/llama-3.2-90b-text-preview", 
        temperature = 0.1, 
        max_tokens = 2000
    )


    @agent
    def specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['specialist'],
            llm = self.llm_gemini2,  # type: ignore[index]
            verbose=True
        )
    
    @agent
    def expert(self) -> Agent:
        return Agent(
            config=self.agents_config['expert'], 
            llm = self.llm_groq, # type: ignore[index]
            verbose=True
        )    
    
    @agent
    def recruiter(self) -> Agent:
        return Agent(
            config=self.agents_config['recruiter'], 
            llm = self.llm_gemini, # type: ignore[index]
            verbose=True
        )    



    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task

    @task
    def ats_optimization_task(self) -> Task:
        return Task(
            config=self.tasks_config['ats_optimization_task'], # type: ignore[index]
            # output_file='report.md'
        )

    @task
    def technical_evaluation_task(self) -> Task:
        return Task(
            config=self.tasks_config['technical_evaluation_task'], # type: ignore[index]
            # output_file='report.md'
        )

    @task
    def recruiter_screening_task(self) -> Task:
        return Task(
            config=self.tasks_config['recruiter_screening_task'], # type: ignore[index]
            output_file='final_candidate_review.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the ResumeAnalyzer crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
