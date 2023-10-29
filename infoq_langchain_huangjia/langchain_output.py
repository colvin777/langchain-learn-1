from langchain.llms import OpenAI

model = OpenAI(model_name='text-davinci-003')

import pandas as pd

df = pd.DataFrame(columns=["flower_type", "price", "description", "reason"])

flowers = ["玫瑰", "百合", "康乃馨"]
prices = ["50", "30", "20"]

from pydantic import BaseModel, Field


class FlowerDescription(BaseModel):
    flower_type: str = Field(description="鲜花的种类")
    price: int = Field(description="鲜花的价格")
    description: str = Field(description="鲜花的描述文案")
    reason: str = Field(description="为什么要这样写这个文案")


from langchain.output_parsers import PydanticOutputParser

output_parser = PydanticOutputParser(pydantic_object=FlowerDescription)

format_instructions = output_parser.get_format_instructions()

# print(format_instructions)

"""
{
  "properties": {
    "flower_type": {
      "description": "\u9c9c\u82b1\u7684\u79cd\u7c7b",
      "title": "Flower Type",
      "type": "string"
    },
    "price": {
      "description": "\u9c9c\u82b1\u7684\u4ef7\u683c",
      "title": "Price",
      "type": "integer"
    },
    "description": {
      "description": "\u9c9c\u82b1\u7684\u63cf\u8ff0\u6587\u6848",
      "title": "Description",
      "type": "string"
    },
    "reason": {
      "description": "\u4e3a\u4ec0\u4e48\u8981\u8fd9\u6837\u5199\u8fd9\u4e2a\u6587\u6848",
      "title": "Reason",
      "type": "string"
    }
  },
  "required": [
    "flower_type",
    "price",
    "description",
    "reason"
  ]
}
"""

from langchain.prompts import PromptTemplate

template = """您是一位专业的鲜花店文案撰写员。
对于售价为 {price} 元的 {flower} ，您能提供一个吸引人的简短中文描述吗？
{format_instructions}"""

prompt1 = PromptTemplate(
    template=template,
    input_variables=['flower', 'price'],
    partial_variables={"format_instructions": format_instructions}
)

# print(prompt1)
# print('--------------------------------------------------------------------')
prompt = PromptTemplate.from_template(template, partial_variables={"format_instructions": format_instructions})

# print(prompt)


for flower, price in zip(flowers, prices):
    input = prompt.format(flower=flower, price=price)

    print(input)
    print('--------------------------------------------------------------------')

    output = model(input)
    parsed_output = output_parser.parse(output)
    parsed_output_dict = parsed_output.model_dump()  # 将Pydantic格式转换为字典
    # 将解析后的输出添加到DataFrame中
    df.loc[len(df)] = parsed_output.model_dump()
# 打印字典
print("输出的数据：", df.to_dict(orient='records'))
