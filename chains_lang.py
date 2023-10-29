from langchain.llms import OpenAI
from langchain.schema import Document
from langchain.chains import StuffDocumentsChain, LLMChain

docs = [ Document(page_content = "Harrison went to Harvard.", metadata={}),
 Document(page_content="Ankush went to Princeton.",  metadata={} )
]

document_prompt = PromptTemplate(
    input_variables=["page_content"],
    template="{page_content}"
)
document_variable_name = "context"
llm = OpenAI()
# The prompt here should take as an input variable the
# `document_variable_name`
prompt = PromptTemplate.from_template(
    "Summarize this content: {context}"
)
llm_chain = LLMChain(llm=llm, prompt=prompt)
chain = StuffDocumentsChain(
    llm_chain=llm_chain,
    document_prompt=document_prompt,
    document_variable_name=document_variable_name
)

# Suppose we have a single-input chain that takes a 'question' string:
await chain.arun("What's the temperature in Boise, Idaho?")
# -> "The temperature in Boise is..."

# Suppose we have a multi-input chain that takes a 'question' string
# and 'context' string:
question = "What's the temperature in Boise, Idaho?"
context = "Weather report for Boise, Idaho on 07/03/23..."
await chain.arun(question=question, context=context)
# -> "The temperature in Boise is..."