import os
import json
from llm_call import IntelligenceEngine
from utils.logger import logger
from concurrent.futures import ThreadPoolExecutor
from typing import Dict, List


class ChainWorkflow:
    def __init__(self, prompts: list[str], system_prompt: str = ""):
        self.prompts = prompts
        self.engine = IntelligenceEngine(api_key=os.getenv("ANTHROPIC_API_KEY"), 
                                system_prompt=system_prompt)
    
    def run(self, query: str) -> str:
        result = query
        
        for i, prompt in enumerate(self.prompts, start=1):
            logger.info(f"Running prompt {i} of {len(self.prompts)}")
            logger.info(f"Prompt: {prompt}")
            result = self.engine.call(result)
            logger.info(f"Result: {result[:100]}...")
            logger.info(f"--------------------------------")
        return result


class ParallelWorkflow:
    def __init__(self, instruction: str, system_prompt: str = "", num_threads: int = 10):
        self.instruction = instruction
        self.engine = IntelligenceEngine(api_key=os.getenv("ANTHROPIC_API_KEY"), 
                                system_prompt=system_prompt)
        self.num_threads = num_threads
    
    def run(self, inputs: list[str]) -> list[str]:
        with ThreadPoolExecutor(max_workers=self.num_threads) as executor:
            futures = [executor.submit(self.engine.call, f"{self.instruction}<input>{x}</input>") for x in inputs]
            results = [future.result() for future in futures]
        return results

Route = Dict[str, str]

class RoutingWorkflow:
    def __init__(self, selection_prompt: str, routes: List[Route], 
                system_prompt: str = "", num_threads: int = 10):
        self.selection_prompt = selection_prompt
        self.routes = routes
        self.engine = IntelligenceEngine(api_key=os.getenv("ANTHROPIC_API_KEY"), 
                                system_prompt=system_prompt)
        self.num_threads = num_threads

    def _select_route(self, query: str) -> str:
        response = self.engine.call(f"{self.selection_prompt}<options>{self.routes.keys()}</options><query>{query}</query>")
        return response
    
    def _execute_route(self, route: str, query: str) -> str:
        prompt = self.routes[route]
        return self.engine.call(f"{prompt}<query>{query}</query>")


    def run(self, query: str) -> str:
        route = self._select_route(query)
        return self._execute_route(route, query)