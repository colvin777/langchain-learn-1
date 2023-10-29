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
# Step 1: send the conversation and available functions to GPT
messages = [{
    "role": "user",
    "content":
      "What's the weather like in Boston, and what's the weather in Huston?",
  }]

functions = [schemasWeather[0]]
response = chat(messages,{
    "functions": functions,
    "function_call": "auto" #auto is default, but we'll be explicit
})
# print(response);
# print(type(response.arguments))

# if response != object:
# Step 3: Call the function
# Note: The JSON response may not always be valid; be sure to handle errors
function_call_name = response["name"]
if function_call_name == 'getCurrentWeather':
    args = json.loads(response.arguments)
    funcResponse = getCurrentWeather(args)
# print(funcResponse)


#Step 4: Send the info on the function call and function response to GPT
# Extend conversation with assistant's reply
messages.append({"role": "assistant",
                 "function_call": response,
                 "content": ''
                 })
#Extend conversation with function response
messages.append({
    "role": "function",
    "name": function_call_name,
    "content": json.dumps(funcResponse)
})

res = chat(messages)
print(res)