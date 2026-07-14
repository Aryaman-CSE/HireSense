from backend.app.ai.intelligence_service import IntelligenceService

service = IntelligenceService()

sample_resume = """
John Doe

Senior Python Developer

Email: john@example.com

Phone: +91 9876543210

Skills:

Python
FastAPI
Docker
Redis
PostgreSQL

Education:

B.Tech Computer Science

Projects:

HireSense

Built an AI Resume Intelligence Platform
"""

result = service.analyze_resume(
    sample_resume
)

print(result.model_dump_json(indent=4))