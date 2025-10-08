"""
Main Career Guidance Agent that processes queries and provides comprehensive career guidance
"""

import asyncio
import json
from typing import List, Dict, Any, Optional
from datetime import datetime
import logging

from .models import (
    CareerQuery, CareerResponse, Roadmap, CompanyData, 
    MarketTrend, LayoffData, SkillRequirement
)
from .web_scraper import JobMarketScraper
from .roadmap_generator import RoadmapGenerator
from .database import SessionLocal, CareerQueryDB

logger = logging.getLogger(__name__)

class CareerGuidanceAgent:
    """Main career guidance agent that processes queries and provides comprehensive guidance"""
    
    def __init__(self):
        self.web_scraper = JobMarketScraper()
        self.roadmap_generator = RoadmapGenerator()
        
    async def process_query(self, query: CareerQuery) -> CareerResponse:
        """Process a career guidance query and return comprehensive response"""
        try:
            logger.info(f"Processing career query for field: {query.field}")
            
            # Store the query in database
            await self._store_query(query)
            
            # Generate roadmap
            roadmap = await self.roadmap_generator.generate_roadmap(
                query.field.value, 
                query.specialization
            )
            
            # Gather market data
            market_data = await self._gather_market_data(query)
            
            # Get market trends
            market_trends = await self.web_scraper.scrape_market_trends()
            
            # Get layoff statistics
            layoff_stats = await self.web_scraper.get_layoff_statistics()
            
            # Get skill requirements
            skill_requirements = await self._get_skill_requirements(query)
            
            # Generate recommendations
            recommendations = await self._generate_recommendations(query, market_data, market_trends)
            
            return CareerResponse(
                query=query,
                roadmap=roadmap,
                market_data=market_data,
                market_trends=market_trends,
                layoff_statistics=layoff_stats,
                skill_requirements=skill_requirements,
                recommendations=recommendations
            )
            
        except Exception as e:
            logger.error(f"Error processing career query: {e}")
            raise
    
    async def _store_query(self, query: CareerQuery):
        """Store the career query in the database"""
        try:
            db = SessionLocal()
            
            career_query_db = CareerQueryDB(
                field=query.field.value,
                specialization=query.specialization,
                experience_level=query.experience_level.value,
                target_companies=json.dumps(query.target_companies) if query.target_companies else None,
                target_roles=json.dumps(query.target_roles) if query.target_roles else None,
                skills=json.dumps(query.skills) if query.skills else None,
                location_preference=query.location_preference,
                query_text=query.query_text
            )
            
            db.add(career_query_db)
            db.commit()
            db.close()
            
        except Exception as e:
            logger.error(f"Error storing query: {e}")
    
    async def _gather_market_data(self, query: CareerQuery) -> List[CompanyData]:
        """Gather market data for target companies"""
        market_data = []
        
        try:
            # If target companies are specified, get data for each
            if query.target_companies:
                for company in query.target_companies:
                    company_data = await self.web_scraper.get_company_data(company)
                    if company_data:
                        market_data.append(company_data)
            
            # If no target companies specified, get data for popular companies in the field
            else:
                popular_companies = self._get_popular_companies(query.field.value)
                for company in popular_companies[:5]:  # Limit to top 5
                    company_data = await self.web_scraper.get_company_data(company)
                    if company_data:
                        market_data.append(company_data)
                        
        except Exception as e:
            logger.error(f"Error gathering market data: {e}")
        
        return market_data
    
    def _get_popular_companies(self, field: str) -> List[str]:
        """Get list of popular companies for a given field"""
        if field == "tech":
            return [
                "Google", "Microsoft", "Amazon", "Apple", "Meta", 
                "Netflix", "Uber", "Airbnb", "Spotify", "Tesla"
            ]
        elif field == "mba":
            return [
                "McKinsey & Company", "Bain & Company", "Boston Consulting Group",
                "ZS Associates", "Nielsen", "Prophet", "Kantar",
                "Goldman Sachs", "JP Morgan", "Morgan Stanley", "Blackstone",
                "Amazon", "Google", "Microsoft"
            ]
        else:
            return ["Google", "Microsoft", "Amazon"]
    
    async def _get_skill_requirements(self, query: CareerQuery) -> List[SkillRequirement]:
        """Get skill requirements for target roles"""
        skill_requirements = []
        
        try:
            if query.target_roles:
                for role in query.target_roles:
                    skills = await self.web_scraper.get_role_skills(role)
                    if skills:
                        skill_requirements.append(skills)
            else:
                # Get skills for common roles in the field
                common_roles = self._get_common_roles(query.field.value)
                for role in common_roles[:3]:  # Limit to top 3
                    skills = await self.web_scraper.get_role_skills(role)
                    if skills:
                        skill_requirements.append(skills)
                        
        except Exception as e:
            logger.error(f"Error getting skill requirements: {e}")
        
        return skill_requirements
    
    def _get_common_roles(self, field: str) -> List[str]:
        """Get list of common roles for a given field"""
        if field == "tech":
            return [
                "software_engineer", "data_scientist", "product_manager",
                "devops_engineer", "frontend_developer", "backend_developer"
            ]
        elif field == "mba":
            return [
                "consultant", "investment_banker", "product_manager",
                "marketing_manager", "operations_manager", "strategy_analyst"
            ]
        else:
            return ["software_engineer", "consultant"]
    
    async def _generate_recommendations(
        self, 
        query: CareerQuery, 
        market_data: List[CompanyData], 
        market_trends: List[MarketTrend]
    ) -> List[str]:
        """Generate personalized recommendations based on query and market data"""
        recommendations = []
        
        try:
            # Analyze market trends for recommendations
            for trend in market_trends:
                if trend.impact == "High":
                    recommendations.append(
                        f"High Impact Trend: {trend.description}. "
                        f"Consider focusing on skills related to this trend."
                    )
            
            # Analyze company data for recommendations
            if market_data:
                avg_salary = sum(c.average_salary for c in market_data if c.average_salary) / len([c for c in market_data if c.average_salary])
                if avg_salary:
                    recommendations.append(
                        f"Average salary in your target companies: ${avg_salary:,.0f}. "
                        f"Use this as a benchmark for salary negotiations."
                    )
                
                # Check hiring status
                active_companies = [c for c in market_data if c.hiring_status == "Active"]
                if active_companies:
                    recommendations.append(
                        f"{len(active_companies)} out of {len(market_data)} target companies are actively hiring. "
                        f"Focus your applications on these companies first."
                    )
            
            # Field-specific recommendations
            if query.field.value == "tech":
                recommendations.extend([
                    "Build a strong portfolio with real projects on GitHub",
                    "Contribute to open source projects to gain experience",
                    "Consider getting cloud certifications (AWS, Azure, GCP)",
                    "Practice coding problems on platforms like LeetCode and HackerRank"
                ])
            elif query.field.value == "mba":
                if query.specialization and "marketing" in query.specialization.lower():
                    recommendations.extend([
                        "Start case interview preparation immediately - don't wait until January",
                        "Complete at least one live consulting project before applying to firms",
                        "Build relationships with 2nd year MBA students who secured consulting offers",
                        "Create thought leadership content on LinkedIn about marketing trends",
                        "Target both MBB firms and specialized marketing consultancies like ZS Associates",
                        "Practice 50+ case interviews focusing on marketing-specific scenarios",
                        "Prepare 10+ STAR stories for behavioral interviews",
                        "Attend all consulting firm presentations on campus",
                        "Join both Marketing Club and Consulting Club for networking"
                    ])
                elif query.specialization and "consulting" in query.specialization.lower():
                    recommendations.extend([
                        "Master MECE frameworks and structured problem-solving approaches",
                        "Practice case interviews daily using Case in Point and PrepLounge",
                        "Develop quick mental math skills - crucial for case interviews",
                        "Read McKinsey Insights, Bain Insights, and BCG Perspectives daily",
                        "Join consulting clubs and practice with peers regularly",
                        "Build 10+ STAR stories for behavioral interviews",
                        "Master Excel shortcuts and PowerPoint design skills",
                        "Stay current on business news through The Economist and Morning Brew",
                        "Practice explaining complex concepts in simple terms",
                        "Network with alumni in consulting firms for referrals"
                    ])
                else:
                    recommendations.extend([
                        "Build strong analytical and problem-solving skills",
                        "Practice case interviews extensively",
                        "Develop industry-specific knowledge through research",
                        "Build a professional network through LinkedIn and industry events"
                    ])
            
            # Experience level specific recommendations
            if query.experience_level.value == "fresh_graduate":
                recommendations.extend([
                    "Focus on building foundational skills and gaining practical experience",
                    "Consider internships or entry-level positions to build your resume",
                    "Join professional organizations and attend networking events"
                ])
            elif query.experience_level.value == "entry_level":
                recommendations.extend([
                    "Look for opportunities to take on more responsibility",
                    "Seek mentorship from senior professionals",
                    "Consider lateral moves to gain diverse experience"
                ])
            
            # Location-specific recommendations
            if query.location_preference:
                recommendations.append(
                    f"Research the job market in {query.location_preference} and "
                    f"connect with local professionals in your field."
                )
            
        except Exception as e:
            logger.error(f"Error generating recommendations: {e}")
            recommendations.append("Focus on building relevant skills and gaining practical experience.")
        
        return recommendations[:10]  # Limit to top 10 recommendations
    
    async def get_career_insights(self, field: str) -> Dict[str, Any]:
        """Get general career insights for a field"""
        try:
            insights = {
                "field": field,
                "market_trends": await self.web_scraper.scrape_market_trends(),
                "layoff_statistics": await self.web_scraper.get_layoff_statistics(),
                "popular_companies": self._get_popular_companies(field),
                "common_roles": self._get_common_roles(field)
            }
            
            return insights
            
        except Exception as e:
            logger.error(f"Error getting career insights for {field}: {e}")
            return {"field": field, "error": str(e)}
    
    async def analyze_skills_gap(self, current_skills: List[str], target_role: str) -> Dict[str, Any]:
        """Analyze skills gap between current skills and target role requirements"""
        try:
            role_skills = await self.web_scraper.get_role_skills(target_role)
            
            if not role_skills:
                return {"error": "Could not fetch skill requirements for the target role"}
            
            current_skills_lower = [skill.lower() for skill in current_skills]
            essential_skills_lower = [skill.lower() for skill in role_skills.essential_skills]
            nice_to_have_lower = [skill.lower() for skill in role_skills.nice_to_have_skills]
            
            # Find missing essential skills
            missing_essential = [
                skill for skill in role_skills.essential_skills 
                if skill.lower() not in current_skills_lower
            ]
            
            # Find missing nice-to-have skills
            missing_nice_to_have = [
                skill for skill in role_skills.nice_to_have_skills 
                if skill.lower() not in current_skills_lower
            ]
            
            # Find skills you have
            skills_you_have = [
                skill for skill in current_skills 
                if skill.lower() in essential_skills_lower or skill.lower() in nice_to_have_lower
            ]
            
            return {
                "target_role": target_role,
                "skills_you_have": skills_you_have,
                "missing_essential_skills": missing_essential,
                "missing_nice_to_have_skills": missing_nice_to_have,
                "skills_gap_score": len(skills_you_have) / len(role_skills.essential_skills) * 100,
                "recommendations": [
                    f"Focus on learning: {', '.join(missing_essential[:3])}",
                    f"Consider adding: {', '.join(missing_nice_to_have[:3])}",
                    f"Leverage your existing skills: {', '.join(skills_you_have[:3])}"
                ]
            }
            
        except Exception as e:
            logger.error(f"Error analyzing skills gap: {e}")
            return {"error": str(e)}
