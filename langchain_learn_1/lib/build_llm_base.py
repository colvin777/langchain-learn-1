import asyncio
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from typing import Any
from langchain.callbacks import LangChainTracer
from langsmith import Client


def getModelBuilder(spec={"type": "llm", "provider": "openai"}, options: Any= {}):
    # Set up LangSmith tracer

    # client = Client(apiUrl="https://api.smith.langchain.com", apiKey="@me.secrets.LANGSMITH")
    # tracer = LangChainTracer(client=client)
    # callbacks = [tracer] if options is None or options.get("verbose", True) else []

    if spec == {"type": "llm", "provider": "openai"}:
        return  OpenAI(**options)
    elif spec == {"type": "chat", "provider": "openai"}:
        return  ChatOpenAI(**options)
    elif spec == {"type": "embedding", "provider": "openai"}:
        return  OpenAIEmbeddings(**options)



builder = getModelBuilder();
model = builder("Tell me a famous saying");
# print(builder.call("Tell me a famous saying"))
