from groq import Groq

from backend.app.core.config import settings

from backend.app.ai.providers.base import BaseLLMProvider


class GroqProvider(BaseLLMProvider):

    def __init__(self):

        self.client = Groq(
            api_key=settings.GROQ_API_KEY
        )

    def generate(self, prompt: str) -> str:

        completion = self.client.chat.completions.create(

            model="llama-3.3-70b-versatile",

            temperature=0,

            response_format={
                "type": "json_object"
            },

            messages=[
                {
                    "role": "system",
                    "content": "You are HireSense AI."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return completion.choices[0].message.content