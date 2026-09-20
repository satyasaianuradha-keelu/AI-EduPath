import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

from api.routes import profile, skills, roadmap, practice, assessment, adaptive, chat, dashboard

app = FastAPI(
    title="EduPath - Personalized Learning & Skill Gap Agent API",
    description="Agentic AI Backend for EduPath Hackathon Application",
    version="1.0.0"
)

# CORS configuration for local React Vite frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API Routers
app.include_router(profile.router)
app.include_router(skills.router)
app.include_router(roadmap.router)
app.include_router(practice.router)
app.include_router(assessment.router)
app.include_router(adaptive.router)
app.include_router(chat.router)
app.include_router(dashboard.router)

@app.get("/api/health")
def health_check():
    return {
        "status": "online",
        "service": "EduPath Agentic AI Backend",
        "ai_service_configured": bool(os.getenv("LLM_API_KEY"))
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
