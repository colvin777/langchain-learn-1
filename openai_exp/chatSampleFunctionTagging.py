from chat import chat
import json
input ="Estoy increiblemente contento de haberte conocido! Creo que seremos muy buenos amigos!"
prompt = """ Extract the desired information from the following passage.

    Passage:
    ${input}
    """
functions = [
    {
      "name": "information_extraction",
      "description": "Extracts the relevant information from the passage.",
      "parameters": {
        "type": "object",
        "properties": {
          "sentiment": { "type": "string" },
          "tone": { "type": "string" },
          "language": { "type": "string" },
        },
        "required": ["tone", "language"],
      },
    },
  ]

response =chat(prompt, { "functions": functions });

print(json.loads(response.arguments))