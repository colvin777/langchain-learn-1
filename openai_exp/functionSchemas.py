schemasWeather = [
  {
    "name": "getCurrentWeather",
    "description": "Get the current weather in a given location",
    "parameters": {
      "type": "object",
      "properties": {
        "location": {
          "type": "string",
          "description": "The city and state, e.g. San Francisco, CA",
        },
        "unit": { "type": "string", "enum": ["celsius", "fahrenheit"] },
      },
      "required": ["location"],
    },
  },
  {
    "name": "getDaysWeatherForecast",
    "description": "Get an N-day weather forecast",
    "parameters": {
      "type": "object",
      "properties": {
        "location": {
          "type": "string",
          "description": "The city and state, e.g. San Francisco, CA",
        },
        "format": {
          "type": "string",
          "enum": ["celsius", "fahrenheit"],
          "description":
            "The temperature unit to use. Infer this from the users location.",
        },
        "numDays": {
          "type": "integer",
          "description": "The number of days to forecast",
        },
      },
      "required": ["location", "format", "numDays"],
    },
  },
]