# Description: Research assistant class that handles the research process for a given question.

# libraries
import json
from actions.google_search import get_urls, scrape_text
from processing.text import \
    write_to_file, \
    read_txt_files
from agent.llm_utils import llm_response, llm_stream_response
from config import Config
from agent import prompts
import os
import string

CFG = Config()


class ResearchAgent:
    def __init__(self, question, agent):
        """ Initializes the research assistant with the given question.
            Args: question (str): The question to research
            Returns: None
        """

        self.question = question
        self.agent = agent
        self.visited_urls = set()
        self.search_summary = ""
        self.directory_name = ''.join(c for c in question if c.isascii() and c not in string.punctuation)[:100]
        self.dir_path = os.path.dirname(f"./outputs/{self.directory_name}/")

    async def call_agent(self, action):
        messages = [{
            "role": "system",
            "content": prompts.generate_agent_role_prompt(self.agent),
        }, {
            "role": "user",
            "content": action,
        }]
        return llm_response(
                    model=CFG.fast_llm_model,
                    messages=messages,
                )

    def call_agent_stream(self, action):
        messages = [{
            "role": "system",
            "content": prompts.generate_agent_role_prompt(self.agent),
        }, {
            "role": "user",
            "content": action,
        }]
        yield from llm_stream_response(
                model=CFG.fast_llm_model,
                messages=messages
            )

    async def create_search_queries(self):
        """ Creates the search queries for the given question.
        Args: None
        Returns: list[str]: The search queries for the given question
        """
        result = await self.call_agent(prompts.generate_search_queries_prompt(self.question))
        return json.loads(result) if type(result) != str else result.strip("[]").replace('"', '').split("] [")

    async def async_search(self, query):
        """ Runs the async search for the given query.
        Args: query (str): The query to run the async search for
        Returns: list[str]: The async search for the given query
        """
        urls = get_urls(query)
        max_search_result = 5

        responses = []
        for url in urls[:max_search_result]:
            content = scrape_text(url['link'])
            content = content[:min(4000, len(content))]
            responses.append(f"Resource: {url}, Content: {content}")
        return responses

    async def run_search_summary(self, query):
        """ Runs the search summary for the given query.
        Args: query (str): The query to run the search summary for
        Returns: str: The search summary for the given query
        """

        responses = await self.async_search(query)

        result = "\n----------------\n".join(responses)
        query = hash(query)
        os.makedirs(os.path.dirname(f"./outputs/{self.directory_name}/research-{query}.txt"), exist_ok=True)
        write_to_file(f"./outputs/{self.directory_name}/research-{query}.txt", result)
        return result

    async def search_online(self):
        """ Conducts the research for the given question.
        Args: None
        Returns: str: The research for the given question
        """

        self.search_summary = read_txt_files(self.dir_path) if os.path.isdir(self.dir_path) else ""
        
        if not self.search_summary:
            search_queries = await self.create_search_queries()
            for query in search_queries:
                research_result = await self.run_search_summary(query)
                self.search_summary += f"{research_result}\n================\n"

        return self.search_summary

    async def create_concepts(self):
        """ Creates the concepts for the given question.
        Args: None
        Returns: list[str]: The concepts for the given question
        """
        result = self.call_agent(prompts.generate_concepts_prompt(self.question, self.search_summary))

        return json.loads(result)

    def write_report(self, report_type):
        """ Writes the report for the given question.
        Args: None
        Returns: str: The report for the given question
        """
        report_type_func = prompts.get_report_by_type(report_type)
        
        yield from self.call_agent_stream(report_type_func(self.question, self.search_summary))

    async def write_lessons(self):
        """ Writes lessons on essential concepts of the research.
        Args: None
        Returns: None
        """
        concepts = await self.create_concepts()
        for concept in concepts:
            answer = await self.call_agent(prompts.generate_lesson_prompt(concept))
            write_md_to_pdf("Lesson", self.directory_name, answer)
