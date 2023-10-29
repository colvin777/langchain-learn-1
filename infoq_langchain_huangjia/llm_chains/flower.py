from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains import SequentialChain
from pydantic import BaseModel, Field
from langchain.output_parsers import PydanticOutputParser


class FlowerDescription(BaseModel):
    flower_type: str = Field(description="鲜花的种类")
    price: int = Field(description="鲜花的价格")
    description: str = Field(description="鲜花的描述文案")
    reason: str = Field(description="为什么要这样写这个文案")


output_parser = PydanticOutputParser(pydantic_object=FlowerDescription)

flowers = ["玫瑰", "百合", "康乃馨"]
prices = ["50", "30", "20"]

template = """您是一位专业的鲜花店文案撰写员。
对于售价为 {price} 元的 {flower} ，您能提供一个吸引人的简短中文描述吗？
{format_instructions}
"""

prompt = PromptTemplate(input_variables=["price", "flower"], template=template,
                        partial_variables={"format_instructions": output_parser.get_format_instructions()})
llm = OpenAI(temperature=.7)

des_chain = LLMChain(llm=llm, prompt=prompt, output_parser=output_parser)

for flower, price in zip(flowers, prices):
    res = des_chain({"price": price, "flower": flower})
    print(res)
