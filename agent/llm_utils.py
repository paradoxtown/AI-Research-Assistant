from __future__ import annotations
from config import Config
import openai

CFG = Config()

openai.api_key = CFG.openai_api_key
openai.api_base = CFG.openai_api_base

from typing import Optional

def llm_response(model, 
             messages, 
             temperature: float = CFG.temperature,
             max_tokens: Optional[int] = None):
    return openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
        ).choices[0].message["content"]


def llm_stream_response(model, 
                        messages, 
                        temperature: float = CFG.temperature, 
                        max_tokens: Optional[int] = None):
    response = ""
    for chunk in openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            stream=True,
    ):
        content = chunk["choices"][0].get("delta", {}).get("content")
        if content is not None:
            response += content
            yield response
