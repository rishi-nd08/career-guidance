"""
Database configuration and models for the Career Guidance Agent
"""

import sqlite3
import asyncio
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import os

# Database configuration
DATABASE_URL = "sqlite:///./data/career_guidance.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class CareerQueryDB(Base):
    """Database model for storing career queries"""
    __tablename__ = "career_queries"
    
    id = Column(Integer, primary_key=True, index=True)
    field = Column(String, nullable=False)
    specialization = Column(String)
    experience_level = Column(String, nullable=False)
    target_companies = Column(Text)  # JSON string
    target_roles = Column(Text)  # JSON string
    skills = Column(Text)  # JSON string
    location_preference = Column(String)
    query_text = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class CompanyDataDB(Base):
    """Database model for storing company data"""
    __tablename__ = "company_data"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)
    hiring_status = Column(String, nullable=False)
    open_positions = Column(Integer, default=0)
    average_salary = Column(Float)
    required_skills = Column(Text)  # JSON string
    company_size = Column(String)
    industry = Column(String)
    last_updated = Column(DateTime, default=datetime.utcnow)

class JobPostingDB(Base):
    """Database model for storing job postings"""
    __tablename__ = "job_postings"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    company = Column(String, nullable=False)
    location = Column(String)
    salary_range = Column(String)
    requirements = Column(Text)  # JSON string
    posted_date = Column(DateTime, default=datetime.utcnow)
    job_type = Column(String)
    experience_level = Column(String)
    skills_required = Column(Text)  # JSON string
    source = Column(String)

class MarketTrendDB(Base):
    """Database model for storing market trends"""
    __tablename__ = "market_trends"
    
    id = Column(Integer, primary_key=True, index=True)
    trend_type = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    impact = Column(String)
    timeframe = Column(String)
    source = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

class LayoffDataDB(Base):
    """Database model for storing layoff data"""
    __tablename__ = "layoff_data"
    
    id = Column(Integer, primary_key=True, index=True)
    company = Column(String, nullable=False)
    layoff_count = Column(Integer, nullable=False)
    percentage = Column(Float)
    date = Column(DateTime, nullable=False)
    reason = Column(Text)
    affected_departments = Column(Text)  # JSON string
    created_at = Column(DateTime, default=datetime.utcnow)

class SkillRequirementDB(Base):
    """Database model for storing skill requirements"""
    __tablename__ = "skill_requirements"
    
    id = Column(Integer, primary_key=True, index=True)
    role = Column(String, nullable=False)
    essential_skills = Column(Text)  # JSON string
    nice_to_have_skills = Column(Text)  # JSON string
    experience_required = Column(String)
    certifications = Column(Text)  # JSON string
    last_updated = Column(DateTime, default=datetime.utcnow)

class RoadmapDB(Base):
    """Database model for storing roadmaps"""
    __tablename__ = "roadmaps"
    
    id = Column(Integer, primary_key=True, index=True)
    field = Column(String, nullable=False)
    specialization = Column(String)
    total_duration = Column(String)
    steps = Column(Text)  # JSON string
    skills_covered = Column(Text)  # JSON string
    created_at = Column(DateTime, default=datetime.utcnow)

async def init_db():
    """Initialize the database and create tables"""
    # Ensure data directory exists
    os.makedirs("data", exist_ok=True)
    
    # Create all tables
    Base.metadata.create_all(bind=engine)
    print("Database initialized successfully!")

def get_db():
    """Get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Sample data insertion functions
async def insert_sample_data():
    """Insert sample data for testing"""
    db = SessionLocal()
    
    try:
        # Sample company data
        sample_companies = [
            CompanyDataDB(
                name="Google",
                hiring_status="Active",
                open_positions=150,
                average_salary=120000.0,
                required_skills='["Python", "Machine Learning", "Cloud Computing"]',
                company_size="Large",
                industry="Technology"
            ),
            CompanyDataDB(
                name="Microsoft",
                hiring_status="Active",
                open_positions=200,
                average_salary=115000.0,
                required_skills='["C#", "Azure", "Software Development"]',
                company_size="Large",
                industry="Technology"
            ),
            CompanyDataDB(
                name="McKinsey & Company",
                hiring_status="Active",
                open_positions=50,
                average_salary=130000.0,
                required_skills='["Strategy", "Analytics", "Business Analysis"]',
                company_size="Large",
                industry="Consulting"
            ),
            CompanyDataDB(
                name="ZS Associates",
                hiring_status="Active",
                open_positions=75,
                average_salary=125000.0,
                required_skills='["Marketing Analytics", "Data Science", "Consulting"]',
                company_size="Large",
                industry="Marketing Consulting"
            ),
            CompanyDataDB(
                name="Nielsen",
                hiring_status="Active",
                open_positions=40,
                average_salary=110000.0,
                required_skills='["Market Research", "Consumer Insights", "Analytics"]',
                company_size="Large",
                industry="Market Research"
            ),
            CompanyDataDB(
                name="Bain & Company",
                hiring_status="Active",
                open_positions=30,
                average_salary=140000.0,
                required_skills='["Strategy", "Marketing", "Case Interview", "Analytics"]',
                company_size="Large",
                industry="Management Consulting"
            ),
            CompanyDataDB(
                name="Boston Consulting Group",
                hiring_status="Active",
                open_positions=25,
                average_salary=135000.0,
                required_skills='["Strategy", "Marketing", "Problem Solving", "Leadership"]',
                company_size="Large",
                industry="Management Consulting"
            ),
            CompanyDataDB(
                name="Prophet",
                hiring_status="Active",
                open_positions=15,
                average_salary=120000.0,
                required_skills='["Brand Strategy", "Marketing", "Creative Thinking", "Client Management"]',
                company_size="Medium",
                industry="Brand Consulting"
            )
        ]
        
        for company in sample_companies:
            existing = db.query(CompanyDataDB).filter(CompanyDataDB.name == company.name).first()
            if not existing:
                db.add(company)
        
        # Sample market trends
        sample_trends = [
            MarketTrendDB(
                trend_type="AI/ML Growth",
                description="Artificial Intelligence and Machine Learning roles are growing at 25% annually",
                impact="High",
                timeframe="2024-2025",
                source="LinkedIn Jobs Report"
            ),
            MarketTrendDB(
                trend_type="Remote Work",
                description="Remote work opportunities have increased by 40% post-pandemic",
                impact="Medium",
                timeframe="2024",
                source="Glassdoor Survey"
            )
        ]
        
        for trend in sample_trends:
            existing = db.query(MarketTrendDB).filter(
                MarketTrendDB.trend_type == trend.trend_type
            ).first()
            if not existing:
                db.add(trend)
        
        db.commit()
        print("Sample data inserted successfully!")
        
    except Exception as e:
        db.rollback()
        print(f"Error inserting sample data: {e}")
    finally:
        db.close()
