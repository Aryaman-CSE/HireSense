from backend.app.ai.intelligence_service import IntelligenceService
from backend.app.ai.job_intelligence_service import JobIntelligenceService
from backend.app.matching.semantic_match import SemanticMatchEngine

resume_service = IntelligenceService()
job_service = JobIntelligenceService()

resume = resume_service.analyze_resume(
"""
John Doe

Python
FastAPI
Docker
Redis

Projects:
Built scalable APIs.

Experience:
2 years Python Developer.
"""
)

job = job_service.analyze_job(
"""
Software Engineer

Required:
Python
FastAPI
Docker

Preferred:
Redis
AWS
Kubernetes
"""
)

engine = SemanticMatchEngine()

result = engine.match(
    resume.resume,
    job,
)

print(result)