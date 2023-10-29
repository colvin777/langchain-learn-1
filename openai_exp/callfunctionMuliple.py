from chat import chat
from functionSchemas import schemasWeather
import json
def getCurrentWeather(location, unit = "fahrenheit"):
    return {
    "unit":unit,
    "location":location,
    "temperature": "72",
    "forecast": ["sunny", "windy"],
  }
#Helper function to call and print assistant response
def callAssistant(messages):
    response = chat(messages, {
        "functions": schemasWeather
    })
    # if response == object:
    #     return response
    return response


# Prompt the model about the current weather, it will respond with some clarifying questions

messages = [
    {
      "role": "system",
      "content":
        "Don't make assumptions about what values to plug into functions. Ask for clarification if a user request is ambiguous.",
    },
    { "role": "user", "content": "What's the weather like today" },
  ]
response = callAssistant(messages)
print(response)
# Once we provide the missing info, it will generate the appropriate function arguments
messages.append({
    "role": "assistant", "content": response
})
messages.append({
    "role": "user", "content": "I'm in Glasgow, Scotland."
})
response = callAssistant(messages)
print(response)
#  By prompting it differently, we can get it to target the other function we've told
# messages=messages[-1:]

messages.append({
    "role": "user",
    "content":
        "what is the weather going to be like in Glasgow, Scotland over the next x days",
})
response = callAssistant(messages);
print(response)
print('------------------------------------------------------------')
# Let's provide the num of days, and model will generate the call to the other function
messages.append({
    "role": "assistant", "content": json.dumps(response)
})
messages.append({
    "role": "user", "content": "5 days"
})
response = callAssistant(messages);
print(response)
