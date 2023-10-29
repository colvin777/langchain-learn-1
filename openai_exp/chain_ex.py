from typing import Optional
from langchain.pydantic_v1 import BaseModel, Field
from langchain.chains.openai_functions import (
    create_openai_fn_chain,
    create_structured_output_chain,
)
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a world class algorithm for recording entities."),
        ("human", "Make calls to the relevant function to record the entities in the following input: {input}"),
        ("human", "Tip: Make sure to answer in the correct format"),
    ]
)

llm = ChatOpenAI(model="gpt-4", temperature=0)

class OptionalFavFood(BaseModel):
    """Either a food or null."""

    food: Optional[str] = Field(
        None,
        description="Either the name of a food or null. Should be null if the food isn't known.",
    )


def record_person(name: str, age: int, fav_food: OptionalFavFood) -> str:
    """Record some basic identifying information about a person.

    Args:
        name: The person's name.
        age: The person's age in years.
        fav_food: An OptionalFavFood object that either contains the person's favorite food or a null value. Food should be null if it's not known.
    """
    return f"Recording person {name} of age {age} with favorite food {fav_food.food}!"


chain = create_openai_fn_chain([record_person], llm, prompt, verbose=True)
res = chain.run(
    "The most important thing to remember about Tommy, my 12 year old, is that he'll do anything for apple pie."
)

print(res)