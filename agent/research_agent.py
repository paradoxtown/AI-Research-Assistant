import json
from actions.duck_search import duckduckgo_search
from processing.text import read_txt_files
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

    def call_agent(self, action):
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

    def create_search_queries(self):
        """ Creates the search queries for the given question.
        Args: None
        Returns: list[str]: The search queries for the given question
        """
        result = self.call_agent(prompts.generate_search_queries_prompt(self.question))
        return json.loads(result)

    def search_single_query(self, query):
        """ Runs the async search for the given query.
        Args: query (str): The query to run the async search for
        Returns: list[str]: The async search for the given query
        """
        return duckduckgo_search(query, max_search_result=3)

    def run_search_summary(self, query):
        """ Runs the search summary for the given query.
        Args: query (str): The query to run the search summary for
        Returns: str: The search summary for the given query
        """

        responses = self.search_single_query(query)
        
        print(f"Searching for {query}")
        query = hash(query)
        file_path = f"./outputs/{self.directory_name}/research-{query}.txt"
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as f:
            json.dump(responses, f)
            print(f"Saved {query} to {file_path}")
        return responses

    def search_online(self):
        """ Conducts the search for the given question.
        Args: None
        Returns: str: The search results for the given question
        """

        self.search_summary = read_txt_files(self.dir_path) if os.path.isdir(self.dir_path) else ""
        
        if not self.search_summary:
            search_queries = self.create_search_queries()
            for _, query in search_queries.items():
                search_result = self.run_search_summary(query)
                self.search_summary += f"=Query=:\n{query}\n=Search Result=:\n{search_result}\n================\n"

        return self.search_summary

    def write_report(self, report_type):
        """ Writes the report for the given question.
        Args: None
        Returns: str: The report for the given question
        """
        yield "Searching online..."

        report_type_func = prompts.get_report_by_type(report_type)
        
        yield from self.call_agent_stream(report_type_func(self.question, self.search_online()))
