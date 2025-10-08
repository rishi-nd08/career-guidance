"""
Career Guidance Agent for PG Students
A comprehensive tool for personalized career roadmaps and job market insights
"""

import os
import asyncio
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import uvicorn
from dotenv import load_dotenv

from src.database import init_db
from src.models import CareerQuery, CareerResponse
from src.career_agent import CareerGuidanceAgent
from src.web_scraper import JobMarketScraper
from src.roadmap_generator import RoadmapGenerator

# Load environment variables
load_dotenv()

app = FastAPI(
    title="Career Guidance Agent",
    description="Comprehensive career guidance for PG students with personalized roadmaps and market insights",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize components
career_agent = CareerGuidanceAgent()
job_scraper = JobMarketScraper()
roadmap_generator = RoadmapGenerator()

@app.on_event("startup")
async def startup_event():
    """Initialize database and components on startup"""
    await init_db()
    print("Career Guidance Agent started successfully!")

@app.get("/", response_class=HTMLResponse)
async def root():
    """Serve the main application interface"""
    try:
        with open("templates/index.html", "r", encoding="utf-8") as f:
            return HTMLResponse(
                content=f.read(),
                headers={
                    "Cache-Control": "no-cache, no-store, must-revalidate",
                    "Pragma": "no-cache",
                    "Expires": "0"
                }
            )
    except FileNotFoundError:
        # Fallback HTML if template file is not found
        fallback_html = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Career Guidance Agent</title>
            <style>
                body { font-family: Arial, sans-serif; margin: 40px; }
                .container { max-width: 800px; margin: 0 auto; }
                .header { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                         color: white; padding: 20px; border-radius: 10px; text-align: center; }
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">
                    <h1>🎓 Career Guidance Agent</h1>
                    <p>Your Personal Career Guidance Platform for PG Students</p>
                </div>
                <h2>✅ Server is Running Successfully!</h2>
                <p>The Career Guidance Agent is now live and ready to help you with your career planning.</p>
                <p><a href="/docs">View API Documentation</a></p>
            </div>
        </body>
        </html>
        """
        return HTMLResponse(content=fallback_html)

@app.post("/api/career-guidance", response_model=CareerResponse)
async def get_career_guidance(query: CareerQuery):
    """
    Main endpoint for career guidance queries
    """
    try:
        # Process the career guidance query
        response = await career_agent.process_query(query)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/roadmap/{field}")
async def get_roadmap(field: str, specialization: str = None):
    """
    Get personalized roadmap for a specific field
    """
    try:
        roadmap = await roadmap_generator.generate_roadmap(field, specialization)
        return roadmap
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/market-data/{company}")
async def get_market_data(company: str):
    """
    Get current market data for a specific company
    """
    try:
        market_data = await job_scraper.get_company_data(company)
        return market_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/layoff-stats")
async def get_layoff_statistics():
    """
    Get current layoff statistics and market trends
    """
    try:
        layoff_data = await job_scraper.get_layoff_statistics()
        return layoff_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/skills/{role}")
async def get_required_skills(role: str):
    """
    Get essential skills for a specific role
    """
    try:
        skills = await job_scraper.get_role_skills(role)
        return skills
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/marketing-consultant-roadmap")
async def get_marketing_consultant_roadmap():
    """
    Get the detailed marketing consultant roadmap for final year MBA students
    """
    try:
        from src.marketing_consultant_roadmap import MarketingConsultantRoadmap
        detailed_roadmap = MarketingConsultantRoadmap.get_detailed_roadmap()
        return detailed_roadmap
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/management-consulting-guide")
async def get_management_consulting_guide():
    """
    Get the comprehensive management consulting skills and resources guide
    """
    try:
        from src.management_consulting_resources import ManagementConsultingResources
        guide = ManagementConsultingResources.get_comprehensive_guide()
        return guide
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
