from typing import List
import openai


def chat(prompt: str | list, options = {}) -> str:
    messages = prompt if isinstance(prompt, list) else [{ "role": "user", "content": prompt }]
    result = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        **options
    )
    message = result.choices[0].message
    return message.function_call if hasattr(message, "function_call") else message.content

