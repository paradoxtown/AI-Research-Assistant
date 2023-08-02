from agent import prompts, llm_utils
from config import Config

CFG = Config()

def english_polishing(content):
    prompt = prompts.generate_english_polishing_prompt(content)
    messages = [{
        "role": "user",
        "content": prompt,
    }]
    
    yield from llm_utils.llm_stream_response(
        model=CFG.fast_llm_model,
        messages=messages)
