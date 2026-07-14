from backend.app.ai.job_intelligence_service import JobIntelligenceService

service = JobIntelligenceService()

sample_job = """
Software Engineer

Google

Minimum Qualifications

Bachelor's degree in Computer Science.

2+ years of experience in Python.

Experience with FastAPI.

Experience with Docker.

Preferred Qualifications

Redis

Kubernetes

AWS

Responsibilities

Develop backend APIs.

Build scalable systems.

Collaborate with cross-functional teams.
"""

result = service.analyze_job(
    sample_job
)

print(
    result.model_dump_json(
        indent=4
    )
)