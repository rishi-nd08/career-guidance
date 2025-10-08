"""
Roadmap generator that creates personalized career roadmaps based on roadmap.sh
"""

import requests
import json
from typing import List, Dict, Any, Optional
from datetime import datetime, timedelta
import logging

from .models import Roadmap, RoadmapStep, FieldType
from .marketing_consultant_roadmap import MarketingConsultantRoadmap

logger = logging.getLogger(__name__)

class RoadmapGenerator:
    """Generates personalized career roadmaps using roadmap.sh as reference"""
    
    def __init__(self):
        self.roadmap_base_url = "https://roadmap.sh"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    async def generate_roadmap(self, field: str, specialization: str = None) -> Roadmap:
        """Generate a personalized roadmap for the given field"""
        try:
            if field.lower() == "tech":
                return await self._generate_tech_roadmap(specialization)
            elif field.lower() == "mba":
                return await self._generate_mba_roadmap(specialization)
            else:
                raise ValueError(f"Unsupported field: {field}")
                
        except Exception as e:
            logger.error(f"Error generating roadmap for {field}: {e}")
            return self._get_default_roadmap(field)
    
    async def _generate_tech_roadmap(self, specialization: str = None) -> Roadmap:
        """Generate tech roadmap based on roadmap.sh structure"""
        
        # Define tech specializations and their roadmaps
        tech_roadmaps = {
            "frontend": {
                "total_duration": "6-12 months",
                "steps": [
                    RoadmapStep(
                        title="HTML & CSS Fundamentals",
                        description="Learn the basics of web structure and styling",
                        duration="2-3 weeks",
                        resources=["MDN Web Docs", "freeCodeCamp", "CSS-Tricks"],
                        prerequisites=[],
                        difficulty="Beginner"
                    ),
                    RoadmapStep(
                        title="JavaScript Basics",
                        description="Master JavaScript fundamentals and ES6+ features",
                        duration="4-6 weeks",
                        resources=["JavaScript.info", "Eloquent JavaScript", "MDN JavaScript Guide"],
                        prerequisites=["HTML & CSS"],
                        difficulty="Beginner"
                    ),
                    RoadmapStep(
                        title="React/Vue/Angular",
                        description="Choose and master a modern frontend framework",
                        duration="6-8 weeks",
                        resources=["React Official Docs", "Vue.js Guide", "Angular Tutorial"],
                        prerequisites=["JavaScript"],
                        difficulty="Intermediate"
                    ),
                    RoadmapStep(
                        title="State Management",
                        description="Learn Redux, Vuex, or NgRx for complex applications",
                        duration="3-4 weeks",
                        resources=["Redux Toolkit", "Vuex Guide", "NgRx Documentation"],
                        prerequisites=["React/Vue/Angular"],
                        difficulty="Intermediate"
                    ),
                    RoadmapStep(
                        title="Testing & Deployment",
                        description="Learn testing frameworks and deployment strategies",
                        duration="3-4 weeks",
                        resources=["Jest", "Cypress", "Vercel", "Netlify"],
                        prerequisites=["Frontend Framework"],
                        difficulty="Intermediate"
                    )
                ],
                "skills_covered": ["HTML", "CSS", "JavaScript", "React", "Testing", "Git", "Responsive Design"]
            },
            "backend": {
                "total_duration": "8-12 months",
                "steps": [
                    RoadmapStep(
                        title="Programming Language",
                        description="Master Python, Java, or Node.js for backend development",
                        duration="6-8 weeks",
                        resources=["Python.org", "Oracle Java Docs", "Node.js Guide"],
                        prerequisites=[],
                        difficulty="Beginner"
                    ),
                    RoadmapStep(
                        title="Database Management",
                        description="Learn SQL and NoSQL databases",
                        duration="4-6 weeks",
                        resources=["PostgreSQL Docs", "MongoDB University", "SQLBolt"],
                        prerequisites=["Programming Language"],
                        difficulty="Beginner"
                    ),
                    RoadmapStep(
                        title="API Development",
                        description="Build RESTful APIs and GraphQL endpoints",
                        duration="4-6 weeks",
                        resources=["FastAPI", "Spring Boot", "Express.js"],
                        prerequisites=["Programming Language", "Database"],
                        difficulty="Intermediate"
                    ),
                    RoadmapStep(
                        title="Authentication & Security",
                        description="Implement secure authentication and authorization",
                        duration="3-4 weeks",
                        resources=["JWT.io", "OAuth 2.0", "OWASP Security"],
                        prerequisites=["API Development"],
                        difficulty="Intermediate"
                    ),
                    RoadmapStep(
                        title="Cloud & DevOps",
                        description="Deploy applications using cloud platforms",
                        duration="4-6 weeks",
                        resources=["AWS", "Docker", "Kubernetes", "CI/CD"],
                        prerequisites=["API Development"],
                        difficulty="Advanced"
                    )
                ],
                "skills_covered": ["Python/Java/Node.js", "SQL", "REST APIs", "Authentication", "Cloud Computing", "Docker"]
            },
            "data_science": {
                "total_duration": "10-14 months",
                "steps": [
                    RoadmapStep(
                        title="Python & Statistics",
                        description="Learn Python programming and statistical concepts",
                        duration="6-8 weeks",
                        resources=["Python.org", "Statistics.com", "Khan Academy"],
                        prerequisites=[],
                        difficulty="Beginner"
                    ),
                    RoadmapStep(
                        title="Data Manipulation",
                        description="Master pandas, NumPy, and data cleaning techniques",
                        duration="4-6 weeks",
                        resources=["Pandas Docs", "NumPy Guide", "DataCamp"],
                        prerequisites=["Python"],
                        difficulty="Beginner"
                    ),
                    RoadmapStep(
                        title="Machine Learning",
                        description="Learn ML algorithms and scikit-learn",
                        duration="6-8 weeks",
                        resources=["Scikit-learn", "Coursera ML Course", "Kaggle Learn"],
                        prerequisites=["Data Manipulation"],
                        difficulty="Intermediate"
                    ),
                    RoadmapStep(
                        title="Deep Learning",
                        description="Explore neural networks and TensorFlow/PyTorch",
                        duration="6-8 weeks",
                        resources=["TensorFlow", "PyTorch", "Deep Learning Specialization"],
                        prerequisites=["Machine Learning"],
                        difficulty="Advanced"
                    ),
                    RoadmapStep(
                        title="Data Visualization",
                        description="Create compelling visualizations and dashboards",
                        duration="3-4 weeks",
                        resources=["Matplotlib", "Seaborn", "Plotly", "Tableau"],
                        prerequisites=["Data Manipulation"],
                        difficulty="Intermediate"
                    )
                ],
                "skills_covered": ["Python", "Statistics", "Machine Learning", "Deep Learning", "Data Visualization", "SQL"]
            },
            "devops": {
                "total_duration": "8-12 months",
                "steps": [
                    RoadmapStep(
                        title="Linux & Command Line",
                        description="Master Linux administration and shell scripting",
                        duration="4-6 weeks",
                        resources=["Linux Academy", "Bash Guide", "Linux Documentation"],
                        prerequisites=[],
                        difficulty="Beginner"
                    ),
                    RoadmapStep(
                        title="Version Control",
                        description="Learn Git and GitHub/GitLab workflows",
                        duration="2-3 weeks",
                        resources=["Git Documentation", "GitHub Learning Lab", "Atlassian Git Tutorials"],
                        prerequisites=[],
                        difficulty="Beginner"
                    ),
                    RoadmapStep(
                        title="Containerization",
                        description="Master Docker and container orchestration",
                        duration="4-6 weeks",
                        resources=["Docker Docs", "Kubernetes.io", "Docker Compose"],
                        prerequisites=["Linux"],
                        difficulty="Intermediate"
                    ),
                    RoadmapStep(
                        title="Cloud Platforms",
                        description="Learn AWS, Azure, or GCP services",
                        duration="6-8 weeks",
                        resources=["AWS Training", "Azure Learn", "Google Cloud Training"],
                        prerequisites=["Containerization"],
                        difficulty="Intermediate"
                    ),
                    RoadmapStep(
                        title="CI/CD & Monitoring",
                        description="Implement continuous integration and monitoring",
                        duration="4-6 weeks",
                        resources=["Jenkins", "GitLab CI", "Prometheus", "Grafana"],
                        prerequisites=["Cloud Platforms"],
                        difficulty="Advanced"
                    )
                ],
                "skills_covered": ["Linux", "Docker", "Kubernetes", "AWS/Azure/GCP", "CI/CD", "Monitoring"]
            }
        }
        
        # Get roadmap based on specialization
        if specialization and specialization.lower() in tech_roadmaps:
            roadmap_data = tech_roadmaps[specialization.lower()]
        else:
            # Default to frontend if no specialization specified
            roadmap_data = tech_roadmaps["frontend"]
        
        return Roadmap(
            field="tech",
            specialization=specialization or "frontend",
            total_duration=roadmap_data["total_duration"],
            steps=roadmap_data["steps"],
            skills_covered=roadmap_data["skills_covered"]
        )
    
    async def _generate_mba_roadmap(self, specialization: str = None) -> Roadmap:
        """Generate MBA roadmap for business careers"""
        
        mba_roadmaps = {
            "consulting": {
                "total_duration": "12-18 months",
                "steps": [
                    RoadmapStep(
                        title="Problem Solving & Structured Thinking",
                        description="Master MECE frameworks, hypothesis-driven thinking, and issue prioritization",
                        duration="6-8 weeks",
                        resources=["Case in Point", "Victor Cheng", "MECE Frameworks", "80/20 Rule"],
                        prerequisites=[],
                        difficulty="Beginner"
                    ),
                    RoadmapStep(
                        title="Analytical & Quantitative Skills",
                        description="Develop mental math, data analysis, and business modeling capabilities",
                        duration="6-8 weeks",
                        resources=["Excel Mastery", "Quick Mental Math", "Business Math", "Chart Interpretation"],
                        prerequisites=["Problem Solving"],
                        difficulty="Intermediate"
                    ),
                    RoadmapStep(
                        title="Communication & Storytelling",
                        description="Build executive communication, presentation, and storytelling skills",
                        duration="4-6 weeks",
                        resources=["PREP/STAR Method", "PowerPoint Skills", "Executive Writing", "Data Storytelling"],
                        prerequisites=["Analytical Skills"],
                        difficulty="Intermediate"
                    ),
                    RoadmapStep(
                        title="Case Interview Mastery",
                        description="Practice case interviews with frameworks and real scenarios",
                        duration="8-10 weeks",
                        resources=["Case in Point", "PrepLounge", "CaseCoach", "RocketBlocks", "Crafting Cases"],
                        prerequisites=["Communication Skills"],
                        difficulty="Advanced"
                    ),
                    RoadmapStep(
                        title="Business & Industry Knowledge",
                        description="Develop deep understanding of key industries and market trends",
                        duration="4-6 weeks",
                        resources=["McKinsey Insights", "Bain Insights", "BCG Perspectives", "HBR", "The Economist"],
                        prerequisites=["Case Interview Prep"],
                        difficulty="Intermediate"
                    ),
                    RoadmapStep(
                        title="Networking & Applications",
                        description="Build professional network and apply to consulting firms",
                        duration="Ongoing",
                        resources=["LinkedIn", "Alumni Networks", "Company Events", "Behavioral Interview Prep"],
                        prerequisites=["Industry Knowledge"],
                        difficulty="Advanced"
                    )
                ],
                "skills_covered": ["Problem Solving", "Analytical Skills", "Communication", "Case Interview", "Business Knowledge", "Leadership"]
            },
            "finance": {
                "total_duration": "10-14 months",
                "steps": [
                    RoadmapStep(
                        title="Financial Fundamentals",
                        description="Learn accounting, finance, and valuation principles",
                        duration="8-10 weeks",
                        resources=["CFA Institute", "Investopedia", "Financial Modeling Prep"],
                        prerequisites=[],
                        difficulty="Beginner"
                    ),
                    RoadmapStep(
                        title="Financial Modeling",
                        description="Master Excel and build financial models",
                        duration="6-8 weeks",
                        resources=["Wall Street Prep", "Corporate Finance Institute", "Excel Skills"],
                        prerequisites=["Financial Fundamentals"],
                        difficulty="Intermediate"
                    ),
                    RoadmapStep(
                        title="Investment Banking Prep",
                        description="Prepare for investment banking interviews and technical questions",
                        duration="6-8 weeks",
                        resources=["Breaking Into Wall Street", "Vault Guides", "Technical Interview Prep"],
                        prerequisites=["Financial Modeling"],
                        difficulty="Advanced"
                    ),
                    RoadmapStep(
                        title="Networking & Applications",
                        description="Connect with finance professionals and apply to roles",
                        duration="Ongoing",
                        resources=["LinkedIn", "Finance Clubs", "Industry Events"],
                        prerequisites=["Investment Banking Prep"],
                        difficulty="Advanced"
                    )
                ],
                "skills_covered": ["Financial Modeling", "Valuation", "Excel", "PowerPoint", "Industry Analysis"]
            },
            "marketing_consultant": {
                "total_duration": "Final MBA Year (8 months)",
                "steps": [
                    RoadmapStep(
                        title="Refine Focus + Skills (Oct-Nov)",
                        description="Identify marketing consulting niche and build foundational skills",
                        duration="2 months",
                        resources=["Strategic Marketing Electives", "Brand Management Courses", "CV & LinkedIn Updates"],
                        prerequisites=[],
                        difficulty="Beginner"
                    ),
                    RoadmapStep(
                        title="Build Consulting Skills (Nov-Dec)",
                        description="Master case interviews and consulting frameworks",
                        duration="2 months",
                        resources=["Case in Point", "Crack the Marketing Case", "Consulting Clubs", "Mock Interviews"],
                        prerequisites=["Marketing Fundamentals"],
                        difficulty="Intermediate"
                    ),
                    RoadmapStep(
                        title="Portfolio Building (Dec-Jan)",
                        description="Create marketing consulting portfolio and case studies",
                        duration="2 months",
                        resources=["Personal Blog", "LinkedIn Posts", "Live Projects", "Freelance Consulting"],
                        prerequisites=["Consulting Skills"],
                        difficulty="Intermediate"
                    ),
                    RoadmapStep(
                        title="Apply for Roles (Jan-Feb)",
                        description="Target consulting firms and marketing strategy roles",
                        duration="2 months",
                        resources=["Bain", "McKinsey", "ZS", "Nielsen", "Boutique Firms", "STAR Stories"],
                        prerequisites=["Portfolio"],
                        difficulty="Advanced"
                    ),
                    RoadmapStep(
                        title="Networking + Mentorship (Feb-Apr)",
                        description="Build professional network and seek mentorship",
                        duration="2 months",
                        resources=["LinkedIn Alumni", "Informational Interviews", "Referrals", "Project Shadowing"],
                        prerequisites=["Applications"],
                        difficulty="Advanced"
                    ),
                    RoadmapStep(
                        title="Final Push (Apr-Jun)",
                        description="Final interview preparation and job offer finalization",
                        duration="2 months",
                        resources=["Interview Prep", "Flexible Role Options", "Offer Negotiation"],
                        prerequisites=["Networking"],
                        difficulty="Advanced"
                    )
                ],
                "skills_covered": ["Marketing Expertise", "Consulting Tools", "Data Analytics", "Problem-solving", "Client Communication", "Storytelling"]
            },
            "operations": {
                "total_duration": "10-14 months",
                "steps": [
                    RoadmapStep(
                        title="Operations Fundamentals",
                        description="Learn supply chain, operations management, and process optimization",
                        duration="8-10 weeks",
                        resources=["APICS", "MIT Operations Course", "Lean Six Sigma"],
                        prerequisites=[],
                        difficulty="Beginner"
                    ),
                    RoadmapStep(
                        title="Data Analysis & Tools",
                        description="Master Excel, SQL, and operations analytics",
                        duration="6-8 weeks",
                        resources=["Excel Advanced", "SQL for Operations", "Tableau"],
                        prerequisites=["Operations Fundamentals"],
                        difficulty="Intermediate"
                    ),
                    RoadmapStep(
                        title="Project Management",
                        description="Learn project management methodologies and tools",
                        duration="4-6 weeks",
                        resources=["PMI", "Agile/Scrum", "Microsoft Project"],
                        prerequisites=["Data Analysis"],
                        difficulty="Intermediate"
                    ),
                    RoadmapStep(
                        title="Industry Applications",
                        description="Apply operations knowledge to specific industries",
                        duration="4-6 weeks",
                        resources=["Industry Case Studies", "Company Research", "Professional Networks"],
                        prerequisites=["Project Management"],
                        difficulty="Advanced"
                    )
                ],
                "skills_covered": ["Supply Chain", "Process Optimization", "Project Management", "Data Analysis", "Lean Six Sigma"]
            }
        }
        
        # Get roadmap based on specialization
        if specialization and specialization.lower() == "marketing":
            # Use the detailed marketing consultant roadmap for marketing specialization
            return MarketingConsultantRoadmap.get_roadmap_as_model()
        elif specialization and specialization.lower() in mba_roadmaps:
            roadmap_data = mba_roadmaps[specialization.lower()]
        else:
            # Default to consulting if no specialization specified
            roadmap_data = mba_roadmaps["consulting"]
        
        return Roadmap(
            field="mba",
            specialization=specialization or "consulting",
            total_duration=roadmap_data["total_duration"],
            steps=roadmap_data["steps"],
            skills_covered=roadmap_data["skills_covered"]
        )
    
    def _get_default_roadmap(self, field: str) -> Roadmap:
        """Get a default roadmap when generation fails"""
        return Roadmap(
            field=field,
            specialization="general",
            total_duration="6-12 months",
            steps=[
                RoadmapStep(
                    title="Foundation Learning",
                    description="Build fundamental knowledge in your chosen field",
                    duration="2-3 months",
                    resources=["Online Courses", "Books", "Tutorials"],
                    prerequisites=[],
                    difficulty="Beginner"
                ),
                RoadmapStep(
                    title="Skill Development",
                    description="Develop specific skills relevant to your career goals",
                    duration="2-3 months",
                    resources=["Practice Projects", "Certifications", "Mentorship"],
                    prerequisites=["Foundation Learning"],
                    difficulty="Intermediate"
                ),
                RoadmapStep(
                    title="Portfolio Building",
                    description="Create a portfolio showcasing your skills and projects",
                    duration="1-2 months",
                    resources=["Personal Projects", "Case Studies", "GitHub"],
                    prerequisites=["Skill Development"],
                    difficulty="Intermediate"
                ),
                RoadmapStep(
                    title="Job Search & Networking",
                    description="Apply to positions and build professional network",
                    duration="Ongoing",
                    resources=["LinkedIn", "Job Boards", "Professional Events"],
                    prerequisites=["Portfolio Building"],
                    difficulty="Advanced"
                )
            ],
            skills_covered=["Communication", "Problem Solving", "Technical Skills", "Industry Knowledge"]
        )
    
    async def get_roadmap_by_url(self, roadmap_url: str) -> Optional[Dict[str, Any]]:
        """Fetch roadmap data from roadmap.sh URL"""
        try:
            response = self.session.get(roadmap_url)
            if response.status_code == 200:
                # Parse the roadmap data from the webpage
                # This would need to be implemented based on roadmap.sh's structure
                return {"status": "success", "data": "Roadmap data fetched"}
            else:
                return None
        except Exception as e:
            logger.error(f"Error fetching roadmap from URL {roadmap_url}: {e}")
            return None
