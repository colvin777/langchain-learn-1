from typing import List
from openai import Completion, Embedding, Moderation


def completion(prompt: str | list, options = {}) -> str:
    res = Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        **options
    )
    return res.choices[0].text

def embed(input, model="text-embedding-ada-002", **kwargs):
    data = Embedding.create(model=model, input=input, **kwargs)
    return data

def modr(input):
    return Moderation.create(input)