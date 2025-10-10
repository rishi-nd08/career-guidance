"""
Pydantic models for the Career Guidance Agent
"""

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime
from enum import Enum

class FieldType(str, Enum):
    TECH = "tech"
    MBA = "mba"

class ExperienceLevel(str, Enum):
    FRESH_GRADUATE = "fresh_graduate"
    ENTRY_LEVEL = "entry_level"
    MID_LEVEL = "mid_level"
    SENIOR_LEVEL = "senior_level"

class CareerQuery(BaseModel):
    """Input model for career guidance queries"""
    field: FieldType = Field(..., description="Field of study (tech or mba)")
    specialization: Optional[str] = Field(None, description="Specific specialization within the field")
    experience_level: ExperienceLevel = Field(..., description="Current experience level")
    target_companies: Optional[List[str]] = Field(None, description="Companies of interest")
    target_roles: Optional[List[str]] = Field(None, description="Target job roles")
    skills: Optional[List[str]] = Field(None, description="Current skills")
    location_preference: Optional[str] = Field(None, description="Preferred work location")
    query_text: str = Field(..., description="Specific question or guidance needed")

class RoadmapStep(BaseModel):
    """Individual step in a career roadmap"""
    title: str
    description: str
    duration: str
    resources: List[str]
    prerequisites: List[str]
    difficulty: str

class Roadmap(BaseModel):
    """Complete career roadmap"""
    field: str
    specialization: str
    total_duration: str
    steps: List[RoadmapStep]
    skills_covered: List[str]

class CompanyData(BaseModel):
    """Company-specific market data"""
    name: str
    hiring_status: str
    open_positions: int
    average_salary: Optional[float]
    required_skills: List[str]
    company_size: str
    industry: str
    last_updated: datetime

class MarketTrend(BaseModel):
    """Market trend data"""
    trend_type: str
    description: str
    impact: str
    timeframe: str
    source: str

class LayoffData(BaseModel):
    """Layoff statistics and data"""
    company: str
    layoff_count: int
    percentage: float
    date: datetime
    reason: str
    affected_departments: List[str]

class SkillRequirement(BaseModel):
    """Skill requirements for specific roles"""
    role: str
    essential_skills: List[str]
    nice_to_have_skills: List[str]
    experience_required: str
    certifications: List[str]

class CareerResponse(BaseModel):
    """Complete career guidance response"""
    query: CareerQuery
    roadmap: Optional[Roadmap]
    market_data: List[CompanyData]
    market_trends: List[MarketTrend]
    layoff_statistics: List[LayoffData]
    skill_requirements: List[SkillRequirement]
    recommendations: List[str]
    generated_at: datetime = Field(default_factory=datetime.now)

class JobPosting(BaseModel):
    """Job posting data"""
    title: str
    company: str
    location: str
    salary_range: Optional[str]
    requirements: List[str]
    posted_date: datetime
    job_type: str
    experience_level: str
    skills_required: List[str]

class ScrapingResult(BaseModel):
    """Result from web scraping operations"""
    source: str
    data: List[Dict[str, Any]]
    scraped_at: datetime = Field(default_factory=datetime.now)
    success: bool
    error_message: Optional[str] = None

