from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains.router.llm_router import LLMRouterChain, RouterOutputParser
from langchain.chains.router.multi_prompt import MULTI_PROMPT_ROUTER_TEMPLATE as RounterTemplate
from langchain.chains import ConversationChain
from langchain.chains import MultiPromptChain


# 构建两个场景的模板
flower_care_template = """你是一个经验丰富的园丁，擅长解答关于养花育花的问题。 
                            下面是需要你来回答的问题: 
                            {input}"""

flower_deco_template = """你是一位网红插花大师，擅长解答关于鲜花装饰的问题。 
                            下面是需要你来回答的问题: 
                            {input}"""

# 构建提示信息
prompt_infos = [
    {
        "key": "flower_care",
        "description": "适合回答关于鲜花护理的问题",
        "template": flower_care_template,
    },
    {
        "key": "flower_decoration",
        "description": "适合回答关于鲜花装饰的问题",
        "template": flower_deco_template,
    }
]
chain_map = {}
llm = OpenAI()
for info in prompt_infos:
    prompt = PromptTemplate(template=info['template'],
                            input_variables=["input"])
    # print("目标提示：\n", prompt)
    chain = LLMChain(llm=llm, prompt=prompt, verbose=True)
    chain_map[info["key"]] = chain

destinations = [f"{p['key']}: {p['description']}" for p in prompt_infos]
# destinations1 = [p['key']+": " + p['description'] for p in prompt_infos]
# print(destinations)

router_template = RounterTemplate.format(destinations="\n".join(destinations))
# print("路由模板：\n", router_template)
router_prompt = PromptTemplate(
            template=router_template,
            input_variables=["input"],
            output_parser=RouterOutputParser()
            )
router_chain = LLMRouterChain.from_llm(llm, router_prompt, verbose=True)
# print(router_prompt)
default_chain = ConversationChain(llm=llm,
                                  output_key="text",
                                  verbose=True)
chain = MultiPromptChain(
    router_chain=router_chain,
    destination_chains=chain_map,
    default_chain=default_chain,
    verbose=True
)
# print(chain.run("如何为玫瑰浇水？"))
print(chain.run("如何为婚礼场地装饰花朵？"))
print(chain.run("如何考入哈佛大学？"))

