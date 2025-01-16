import os
from groq import Groq

client = Groq(
    api_key=os.environ.get("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"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
            {"role": "user", "content": "what is coding"}

        }

    ],

    model="llama-3.3-70b-versatile",

)


print(chat_completion.choices[0].message.content)