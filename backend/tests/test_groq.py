from backend.app.ai.providers.groq_provider import GroqProvider


provider = GroqProvider()

response = provider.generate("""

Return ONLY JSON

{
    "status":"working"
}

""")

print(response)