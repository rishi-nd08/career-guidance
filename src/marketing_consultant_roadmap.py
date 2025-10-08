"""
Detailed Marketing Consultant Roadmap for Final Year MBA Students
Based on the comprehensive roadmap provided by the user
"""

from .models import Roadmap, RoadmapStep
from typing import Dict, Any

class MarketingConsultantRoadmap:
    """Detailed roadmap generator for Marketing Consultant career path"""
    
    @staticmethod
    def get_detailed_roadmap() -> Dict[str, Any]:
        """Get the comprehensive marketing consultant roadmap"""
        
        roadmap_data = {
            "goal": "Secure a role in marketing consulting (or a related role with consulting elements) by the end of your MBA program",
            "timeline": "Final MBA Year (Month-by-Month Breakdown)",
            "total_duration": "8 months (Oct-Jun)",
            "target_audience": "Final Year MBA Students",
            "success_metrics": [
                "Land interviews at 3+ consulting firms",
                "Complete 2+ live consulting projects",
                "Build network of 50+ marketing professionals",
                "Secure job offer by graduation"
            ],
            "steps": [
                {
                    "timeframe": "Oct–Nov (Now)",
                    "focus_area": "🔍 Refine Focus + Skills",
                    "actions": [
                        "Identify niche: brand, digital, analytics, strategy, etc.",
                        "Take advanced electives (e.g. Strategic Marketing, Brand Management)",
                        "Update CV & LinkedIn with marketing projects"
                    ],
                    "duration": "2 months",
                    "difficulty": "Beginner"
                },
                {
                    "timeframe": "Nov–Dec",
                    "focus_area": "🧠 Build Consulting Skills",
                    "actions": [
                        "Practice case interviews (marketing-specific cases)",
                        "Use books like Case in Point, Crack the Marketing Case",
                        "Join consulting clubs/mock interviews"
                    ],
                    "duration": "2 months",
                    "difficulty": "Intermediate"
                },
                {
                    "timeframe": "Dec–Jan",
                    "focus_area": "🛠️ Portfolio Building",
                    "actions": [
                        "Start a personal blog/LinkedIn posts on marketing trends",
                        "Do a live project/freelance consulting for a startup/NGO",
                        "Create a 1-page case study of your work"
                    ],
                    "duration": "2 months",
                    "difficulty": "Intermediate"
                },
                {
                    "timeframe": "Jan–Feb",
                    "focus_area": "💼 Apply for Roles",
                    "actions": [
                        "Target consulting firms with marketing verticals (e.g., Bain, McKinsey, ZS, Nielsen, boutique firms)",
                        "Also apply to marketing strategy roles at MNCs/startups",
                        "Prepare STAR stories for behavioral interviews"
                    ],
                    "duration": "2 months",
                    "difficulty": "Advanced"
                },
                {
                    "timeframe": "Feb–Apr",
                    "focus_area": "💬 Networking + Mentorship",
                    "actions": [
                        "Reach out to alumni in marketing/consulting on LinkedIn",
                        "Set up informational interviews",
                        "Ask for referrals or project shadowing"
                    ],
                    "duration": "2 months",
                    "difficulty": "Advanced"
                },
                {
                    "timeframe": "Apr–Jun",
                    "focus_area": "🚀 Final Push",
                    "actions": [
                        "Interview preparation continues",
                        "Stay flexible (entry roles: analyst, associate, brand strategist)",
                        "Finalize job/internship offers"
                    ],
                    "duration": "2 months",
                    "difficulty": "Advanced"
                }
            ],
            "key_skills": {
                "marketing_expertise": ["Branding", "Digital", "Customer Insights"],
                "consulting_tools": ["SWOT", "4Ps", "STP", "Customer Journey Mapping"],
                "data_savvy": ["Google Analytics", "Excel", "Tableau", "PowerPoint"],
                "soft_skills": ["Problem-solving", "Client communication", "Storytelling"]
            },
            "certifications": [
                "Google Digital Marketing or Analytics Certificate",
                "HubSpot Content Marketing Certification",
                "LinkedIn Learning: Marketing Strategy or Consumer Behavior",
                "Coursera: Marketing Analytics by Wharton"
            ],
            "tools_to_learn": {
                "analytics": ["Google Analytics", "Excel (Pivot, VLOOKUP)", "Power BI/Tableau"],
                "research": ["Statista", "Nielsen", "McKinsey Insights", "Google Trends"],
                "presentation": ["PowerPoint", "Canva", "Figma (for mockups)"],
                "project_management": ["Trello", "Notion", "Asana (for consulting project management)"]
            },
            "side_projects": [
                "Write marketing case studies on real brands (publish on LinkedIn)",
                "Start a personal marketing blog or newsletter",
                "Run a mini social media campaign for a local business",
                "Volunteer for marketing roles in NGOs"
            ],
            "final_deliverables": [
                "Marketing-focused resume + portfolio",
                "1–2 consulting projects (live/freelance/internship)",
                "Strong LinkedIn profile with marketing content or thought leadership",
                "Referrals/networking connections at target firms",
                "Confidence with case and behavioral interviews"
            ],
            "target_companies": {
                "top_tier": ["Bain", "McKinsey", "BCG"],
                "specialized": ["ZS Associates", "Nielsen", "Kantar"],
                "boutique": ["Prophet", "Siegel+Gale", "Landor"],
                "corporate": ["P&G", "Unilever", "Coca-Cola", "Nike"]
            },
            "final_year_specific": {
                "academic_requirements": [
                    "Maintain GPA above 3.5",
                    "Complete Strategic Marketing elective",
                    "Take Brand Management course",
                    "Participate in marketing case competitions",
                    "Complete capstone project in marketing"
                ],
                "networking_strategies": [
                    "Attend all consulting firm presentations on campus",
                    "Join MBA Marketing Club and Consulting Club",
                    "Participate in case interview workshops",
                    "Connect with 2nd year MBA students who got consulting offers",
                    "Attend industry conferences and events"
                ],
                "job_search_tactics": [
                    "Apply to both consulting and corporate strategy roles",
                    "Target firms with marketing verticals",
                    "Prepare 10+ STAR stories for behavioral interviews",
                    "Practice 50+ case interviews",
                    "Create a consulting-style resume"
                ],
                "timeline_milestones": {
                    "October": "Complete skill assessment and gap analysis",
                    "November": "First round of applications submitted",
                    "December": "Complete first live consulting project",
                    "January": "Interview season begins",
                    "February": "Networking and referral requests",
                    "March": "Second round interviews",
                    "April": "Final interviews and offer negotiations",
                    "May": "Accept offer and prepare for role",
                    "June": "Graduation and transition planning"
                }
            },
            "common_pitfalls": [
                "Not starting case interview prep early enough",
                "Focusing only on MBB firms (ignore specialized boutiques)",
                "Not building a strong portfolio of real projects",
                "Neglecting networking and relationship building",
                "Not preparing for behavioral interviews thoroughly"
            ],
            "success_tips": [
                "Start case interview prep in October, not January",
                "Build relationships with 2nd year students who got offers",
                "Do at least one live consulting project before applying",
                "Create a personal brand on LinkedIn with marketing content",
                "Practice both case and behavioral interviews equally"
            ]
        }
        
        return roadmap_data
    
    @staticmethod
    def get_roadmap_as_model() -> Roadmap:
        """Convert the detailed roadmap to a Roadmap model"""
        
        detailed_data = MarketingConsultantRoadmap.get_detailed_roadmap()
        
        steps = []
        for step_data in detailed_data["steps"]:
            step = RoadmapStep(
                title=f"{step_data['timeframe']}: {step_data['focus_area']}",
                description=f"Focus: {step_data['focus_area']}\n\nActions:\n" + "\n".join([f"• {action}" for action in step_data['actions']]),
                duration=step_data['duration'],
                resources=step_data['actions'],
                prerequisites=[],
                difficulty=step_data['difficulty']
            )
            steps.append(step)
        
        # Combine all skills
        all_skills = []
        for skill_category, skills in detailed_data["key_skills"].items():
            all_skills.extend(skills)
        
        return Roadmap(
            field="mba",
            specialization="marketing_consultant",
            total_duration=detailed_data["total_duration"],
            steps=steps,
            skills_covered=all_skills
        )
