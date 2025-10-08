"""
Web scraper for gathering real-time job market data, company information, and layoff statistics
"""

import asyncio
import aiohttp
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional
import logging

from .models import CompanyData, JobPosting, MarketTrend, LayoffData, SkillRequirement, ScrapingResult

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class JobMarketScraper:
    """Web scraper for job market data and company information"""
    
    def __init__(self):
        self.session = None
        self.driver = None
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
    async def __aenter__(self):
        """Async context manager entry"""
        self.session = aiohttp.ClientSession(headers=self.headers)
        return self
        
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit"""
        if self.session:
            await self.session.close()
        if self.driver:
            self.driver.quit()
    
    def _setup_selenium_driver(self):
        """Setup Selenium WebDriver with Chrome options"""
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        
        try:
            self.driver = webdriver.Chrome(options=chrome_options)
            return True
        except Exception as e:
            logger.error(f"Failed to setup Chrome driver: {e}")
            return False
    
    async def scrape_linkedin_jobs(self, company: str, role: str = None) -> List[JobPosting]:
        """Scrape job postings from LinkedIn"""
        jobs = []
        
        try:
            if not self.driver:
                if not self._setup_selenium_driver():
                    return jobs
            
            # Construct LinkedIn search URL
            search_url = f"https://www.linkedin.com/jobs/search/?keywords={company}"
            if role:
                search_url += f" {role}"
            
            self.driver.get(search_url)
            time.sleep(3)
            
            # Wait for job listings to load
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "jobs-search-results-list"))
            )
            
            # Extract job information
            job_elements = self.driver.find_elements(By.CSS_SELECTOR, ".job-search-card")
            
            for job_element in job_elements[:10]:  # Limit to first 10 jobs
                try:
                    title = job_element.find_element(By.CSS_SELECTOR, ".job-search-card__title").text
                    company_name = job_element.find_element(By.CSS_SELECTOR, ".job-search-card__subtitle").text
                    location = job_element.find_element(By.CSS_SELECTOR, ".job-search-card__location").text
                    
                    # Try to get salary information
                    salary = None
                    try:
                        salary_element = job_element.find_element(By.CSS_SELECTOR, ".job-search-card__salary")
                        salary = salary_element.text
                    except:
                        pass
                    
                    job = JobPosting(
                        title=title,
                        company=company_name,
                        location=location,
                        salary_range=salary,
                        requirements=[],
                        posted_date=datetime.now(),
                        job_type="Full-time",
                        experience_level="Not specified",
                        skills_required=[]
                    )
                    jobs.append(job)
                    
                except Exception as e:
                    logger.error(f"Error extracting job data: {e}")
                    continue
                    
        except Exception as e:
            logger.error(f"Error scraping LinkedIn jobs: {e}")
        
        return jobs
    
    async def scrape_glassdoor_company_data(self, company: str) -> Optional[CompanyData]:
        """Scrape company data from Glassdoor"""
        try:
            if not self.driver:
                if not self._setup_selenium_driver():
                    return None
            
            # Construct Glassdoor company URL
            company_url = f"https://www.glassdoor.com/Overview/Working-at-{company.replace(' ', '-')}-EI_IE*.htm"
            
            # For demo purposes, return mock data
            # In production, you would implement actual scraping
            return CompanyData(
                name=company,
                hiring_status="Active",
                open_positions=50,
                average_salary=100000.0,
                required_skills=["Python", "JavaScript", "SQL"],
                company_size="Large",
                industry="Technology",
                last_updated=datetime.now()
            )
            
        except Exception as e:
            logger.error(f"Error scraping Glassdoor data for {company}: {e}")
            return None
    
    async def scrape_indeed_jobs(self, company: str, role: str = None) -> List[JobPosting]:
        """Scrape job postings from Indeed"""
        jobs = []
        
        try:
            if not self.session:
                self.session = aiohttp.ClientSession(headers=self.headers)
            
            # Construct Indeed search URL
            search_url = f"https://www.indeed.com/jobs?q={company}"
            if role:
                search_url += f" {role}"
            
            async with self.session.get(search_url) as response:
                if response.status == 200:
                    html = await response.text()
                    soup = BeautifulSoup(html, 'html.parser')
                    
                    # Extract job listings
                    job_cards = soup.find_all('div', class_='job_seen_beacon')
                    
                    for card in job_cards[:10]:  # Limit to first 10 jobs
                        try:
                            title_elem = card.find('h2', class_='jobTitle')
                            company_elem = card.find('span', class_='companyName')
                            location_elem = card.find('div', class_='companyLocation')
                            
                            if title_elem and company_elem:
                                title = title_elem.get_text(strip=True)
                                company_name = company_elem.get_text(strip=True)
                                location = location_elem.get_text(strip=True) if location_elem else "Not specified"
                                
                                job = JobPosting(
                                    title=title,
                                    company=company_name,
                                    location=location,
                                    salary_range=None,
                                    requirements=[],
                                    posted_date=datetime.now(),
                                    job_type="Full-time",
                                    experience_level="Not specified",
                                    skills_required=[]
                                )
                                jobs.append(job)
                                
                        except Exception as e:
                            logger.error(f"Error extracting Indeed job data: {e}")
                            continue
                            
        except Exception as e:
            logger.error(f"Error scraping Indeed jobs: {e}")
        
        return jobs
    
    async def get_company_data(self, company: str) -> Optional[CompanyData]:
        """Get comprehensive company data from multiple sources"""
        try:
            # Try to get data from database first
            from .database import SessionLocal, CompanyDataDB
            db = SessionLocal()
            
            existing_data = db.query(CompanyDataDB).filter(
                CompanyDataDB.name.ilike(f"%{company}%")
            ).first()
            
            if existing_data and (datetime.now() - existing_data.last_updated).days < 7:
                # Return cached data if it's less than a week old
                db.close()
                return CompanyData(
                    name=existing_data.name,
                    hiring_status=existing_data.hiring_status,
                    open_positions=existing_data.open_positions,
                    average_salary=existing_data.average_salary,
                    required_skills=json.loads(existing_data.required_skills),
                    company_size=existing_data.company_size,
                    industry=existing_data.industry,
                    last_updated=existing_data.last_updated
                )
            
            # Scrape fresh data
            company_data = await self.scrape_glassdoor_company_data(company)
            
            if company_data:
                # Update database with new data
                if existing_data:
                    existing_data.hiring_status = company_data.hiring_status
                    existing_data.open_positions = company_data.open_positions
                    existing_data.average_salary = company_data.average_salary
                    existing_data.required_skills = json.dumps(company_data.required_skills)
                    existing_data.last_updated = datetime.now()
                else:
                    new_company = CompanyDataDB(
                        name=company_data.name,
                        hiring_status=company_data.hiring_status,
                        open_positions=company_data.open_positions,
                        average_salary=company_data.average_salary,
                        required_skills=json.dumps(company_data.required_skills),
                        company_size=company_data.company_size,
                        industry=company_data.industry
                    )
                    db.add(new_company)
                
                db.commit()
            
            db.close()
            return company_data
            
        except Exception as e:
            logger.error(f"Error getting company data for {company}: {e}")
            return None
    
    async def get_layoff_statistics(self) -> List[LayoffData]:
        """Get current layoff statistics from various sources"""
        layoff_data = []
        
        try:
            # For demo purposes, return mock data
            # In production, you would scrape from layoff tracking websites
            sample_layoffs = [
                LayoffData(
                    company="Meta",
                    layoff_count=11000,
                    percentage=13.0,
                    date=datetime(2024, 11, 9),
                    reason="Cost restructuring and focus on AI",
                    affected_departments=["Engineering", "Product", "Marketing"]
                ),
                LayoffData(
                    company="Amazon",
                    layoff_count=18000,
                    percentage=6.0,
                    date=datetime(2024, 1, 18),
                    reason="Economic uncertainty and overhiring",
                    affected_departments=["Retail", "HR", "Devices"]
                ),
                LayoffData(
                    company="Google",
                    layoff_count=12000,
                    percentage=6.0,
                    date=datetime(2024, 1, 20),
                    reason="Focus on AI and efficiency",
                    affected_departments=["Engineering", "Product", "Sales"]
                )
            ]
            
            layoff_data.extend(sample_layoffs)
            
        except Exception as e:
            logger.error(f"Error getting layoff statistics: {e}")
        
        return layoff_data
    
    async def get_role_skills(self, role: str) -> Optional[SkillRequirement]:
        """Get skill requirements for a specific role"""
        try:
            # For demo purposes, return mock data
            # In production, you would scrape from job boards and analyze requirements
            
            skill_mapping = {
                "software_engineer": SkillRequirement(
                    role="Software Engineer",
                    essential_skills=["Programming Languages", "Data Structures", "Algorithms", "Version Control"],
                    nice_to_have_skills=["Cloud Computing", "DevOps", "Machine Learning", "Mobile Development"],
                    experience_required="0-2 years",
                    certifications=["AWS Certified Developer", "Google Cloud Professional"]
                ),
                "data_scientist": SkillRequirement(
                    role="Data Scientist",
                    essential_skills=["Python", "R", "SQL", "Machine Learning", "Statistics"],
                    nice_to_have_skills=["Deep Learning", "Big Data", "Cloud Computing", "Data Visualization"],
                    experience_required="1-3 years",
                    certifications=["AWS Machine Learning", "Google Data Analytics"]
                ),
                "product_manager": SkillRequirement(
                    role="Product Manager",
                    essential_skills=["Product Strategy", "User Research", "Analytics", "Project Management"],
                    nice_to_have_skills=["Technical Background", "Design Thinking", "Agile/Scrum", "Business Analysis"],
                    experience_required="2-5 years",
                    certifications=["PMP", "Certified Scrum Product Owner"]
                ),
                "consultant": SkillRequirement(
                    role="Management Consultant",
                    essential_skills=["Problem-Solving & Analytical Thinking", "Strategic Thinking", "Exceptional Communication Skills", "Data Analysis Proficiency", "Interpersonal Skills"],
                    nice_to_have_skills=["Project Management Expertise", "Adaptability and Flexibility", "Business Acumen", "SQL", "Python", "Tableau", "Advanced Excel", "Power BI"],
                    experience_required="2-3 years (Entry-level), 5+ years (Senior)",
                    certifications=["Certified Management Consultant (CMC)", "Financial Modeling Certification", "Business Strategy (Wharton)", "Consulting Foundations (LinkedIn Learning)"]
                ),
                "marketing": SkillRequirement(
                    role="Marketing Consultant",
                    essential_skills=["Marketing Expertise", "Consulting Tools", "Data Analytics", "Problem-solving", "Client Communication", "Storytelling"],
                    nice_to_have_skills=["Brand Management", "Digital Marketing", "Customer Insights", "SWOT Analysis", "4Ps Framework", "STP Analysis", "Customer Journey Mapping"],
                    experience_required="MBA Final Year",
                    certifications=["Google Digital Marketing", "HubSpot Content Marketing", "LinkedIn Learning Marketing Strategy", "Coursera Marketing Analytics by Wharton"]
                )
            }
            
            # Normalize role name for lookup
            role_key = role.lower().replace(" ", "_").replace("-", "_")
            
            # Check for exact matches first
            if role_key in skill_mapping:
                return skill_mapping[role_key]
            
            # Then check for partial matches
            for key, skills in skill_mapping.items():
                if key in role_key or role_key in key:
                    return skills
            
            # Default return for unknown roles
            return SkillRequirement(
                role=role,
                essential_skills=["Communication", "Problem Solving", "Teamwork"],
                nice_to_have_skills=["Leadership", "Analytics", "Project Management"],
                experience_required="Varies",
                certifications=[]
            )
            
        except Exception as e:
            logger.error(f"Error getting skills for role {role}: {e}")
            return None
    
    async def scrape_market_trends(self) -> List[MarketTrend]:
        """Scrape current market trends from various sources"""
        trends = []
        
        try:
            # For demo purposes, return mock data
            # In production, you would scrape from industry reports and news sources
            
            sample_trends = [
                MarketTrend(
                    trend_type="AI/ML Growth",
                    description="Artificial Intelligence and Machine Learning roles are growing at 25% annually with high demand for specialized skills",
                    impact="High",
                    timeframe="2024-2025",
                    source="LinkedIn Jobs Report 2024"
                ),
                MarketTrend(
                    trend_type="Remote Work",
                    description="Remote work opportunities have increased by 40% post-pandemic, with hybrid models becoming standard",
                    impact="Medium",
                    timeframe="2024",
                    source="Glassdoor Survey 2024"
                ),
                MarketTrend(
                    trend_type="Sustainability Focus",
                    description="Companies are increasingly hiring for ESG and sustainability roles across all industries",
                    impact="Medium",
                    timeframe="2024-2026",
                    source="McKinsey Global Institute"
                ),
                MarketTrend(
                    trend_type="Cybersecurity Demand",
                    description="Cybersecurity roles are in high demand with 3.5 million unfilled positions globally",
                    impact="High",
                    timeframe="2024-2025",
                    source="Cybersecurity Ventures"
                )
            ]
            
            trends.extend(sample_trends)
            
        except Exception as e:
            logger.error(f"Error scraping market trends: {e}")
        
        return trends
