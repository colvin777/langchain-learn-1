import json

from chat import chat
input ="""input =
    `Alex is 5 feet tall. Claudia is 4 feet taller Alex and jumps higher than him. Claudia is a brunette and Alex is blonde.
Alex's dog Frosty is a labrador and likes to play hide and seek.`;"""
prompt ='Extract and save the relevant entities mentioned in the following passage together with their properties.\
    Passage:\
    ${input}'
functions = [
    {
      "name": "information_extraction",
      "description": "Extracts the relevant information from the passage.",
      "parameters": {
        "type": "object",
        "properties": {
          "info": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "person-name": { "type": "string" },
                "person-age": { "type": "number" },
                "person-hair-color": { "type": "string" },
                "dog-name": { "type": "string" },
                "dog-breed": { "type": "string" },
              },
              "required": [],
            },
          },
        },
        "required": ["info"],
      },
    },
  ]
response =chat(prompt, { "functions": functions });

print(json.loads(response.arguments))