from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import FileReadTool
from tools.model import Placeholder
from tools.custom_tool import TemplateDocTool

@CrewBase
class draft_crew:
    """MultiAgentLegalDraftAutomation crew"""

    @agent
    def legal_selection_specialist(self) -> Agent:
        return Agent(
            config=self.agents_config['legal_selection_specialist'],
            tools=[],
        )

    @agent
    def legal_drafter(self) -> Agent:
        return Agent(
            config=self.agents_config['legal_drafter'],
            tools=[],
            output_parser=Placeholder.from_text,
            output_pydantic=Placeholder,
        )

    @agent
    def report_compiler(self) -> Agent:
        return Agent(
            config=self.agents_config['report_compiler'],
            tools=[TemplateDocTool()],
        )


    @task
    def selection_task(self) -> Task:
        return Task(
            config=self.tasks_config['selection_task'],
            tools=[],
        )

    @task
    def legal_drafting_task(self) -> Task:
        return Task(
            config=self.tasks_config['legal_drafting_task'],
            tools=[],
        )

    @task
    def report_compilation_task(self) -> Task:
        return Task(
            config=self.tasks_config['report_compilation_task'],
            tools=[TemplateDocTool()],
        )


    @crew
    def crew(self) -> Crew:
        """Creates the MultiAgentLegalDraftAutomation crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
