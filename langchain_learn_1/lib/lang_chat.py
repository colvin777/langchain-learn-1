from langchain.schema import SystemMessage, HumanMessage
from build_llm_base import getModelBuilder
builder = getModelBuilder({
    "type": "chat",
    "provider": "openai",
  })
messages=[
    SystemMessage(content=
      "You are a helpful assistant that translates English to Chinese."),
     HumanMessage(content="Translate: I love programming.")
  ]
res=builder(messages)
print(res)


from langchain.globals import set_llm_cache

from langchain.docstore.document import Document
docs = [Document(page_content=t) for t in texts[:3]]
from langchain.chains.summarize import load_summarize_chain

chain = load_summarize_chain(llm, chain_type="map_reduce", reduce_llm=no_cache_llm)
chain.run(docs)