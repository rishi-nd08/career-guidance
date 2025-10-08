"""
Comprehensive Management Consulting Resources and Skills Guide
Based on the detailed requirements provided by the user
"""

from typing import Dict, List, Any

class ManagementConsultingResources:
    """Comprehensive resources and skills for management consulting"""
    
    @staticmethod
    def get_skills_breakdown() -> Dict[str, Any]:
        """Get detailed breakdown of required skills for management consulting"""
        
        return {
            "problem_solving": {
                "title": "🧠 Problem Solving & Structured Thinking",
                "description": "Ability to break down complex problems using frameworks (MECE, issue trees)",
                "key_skills": [
                    "Hypothesis-driven thinking",
                    "Prioritization of issues",
                    "MECE (Mutually Exclusive, Collectively Exhaustive) structuring",
                    "Root cause analysis"
                ],
                "tools_concepts": [
                    "Market entry frameworks",
                    "Profitability frameworks", 
                    "Pricing frameworks",
                    "M&A frameworks",
                    "80/20 rule",
                    "Issue trees"
                ]
            },
            "analytical": {
                "title": "📊 Analytical & Quantitative Skills",
                "description": "Quick mental math, data analysis and interpretation, logical reasoning",
                "key_skills": [
                    "Quick mental math",
                    "Data analysis and interpretation",
                    "Logical reasoning",
                    "Basic business math"
                ],
                "tools_to_learn": [
                    "Microsoft Excel (VLOOKUP, PivotTables, quick models)",
                    "Charts & Graphs interpretation",
                    "Basic modeling (revenue, cost, break-even, etc.)"
                ]
            },
            "communication": {
                "title": "🗣️ Communication & Storytelling",
                "description": "Clear and concise verbal communication, executive-style writing and slide-making",
                "key_skills": [
                    "Clear and concise verbal communication",
                    "Executive-style writing and slide-making",
                    "Storytelling with data",
                    "Handling stress and pressure in interviews"
                ],
                "skills_to_build": [
                    "Structuring your answers (PREP/STAR method)",
                    "Client-friendly email and PowerPoint skills",
                    "Data visualization and presentation"
                ]
            },
            "teamwork": {
                "title": "👥 Teamwork & Leadership",
                "description": "Ability to work in diverse teams, project management skills",
                "key_skills": [
                    "Ability to work in diverse teams",
                    "Project management skills",
                    "Handling feedback and client dynamics",
                    "Leadership in team settings"
                ]
            },
            "business_knowledge": {
                "title": "🎯 Business & Industry Knowledge",
                "description": "Understanding of common industries and awareness of current events",
                "key_skills": [
                    "Understanding of common industries: healthcare, retail, tech, finance",
                    "Awareness of current events, market trends, and case studies",
                    "Industry-specific knowledge and insights"
                ]
            }
        }
    
    @staticmethod
    def get_learning_resources() -> Dict[str, List[Dict[str, str]]]:
        """Get comprehensive learning resources for management consulting"""
        
        return {
            "case_interview_prep": [
                {
                    "resource": "Case in Point by Marc Cosentino",
                    "description": "Classic book with beginner-friendly frameworks",
                    "type": "Book"
                },
                {
                    "resource": "Case Interview Secrets by Victor Cheng",
                    "description": "Focuses on mindset, structure, and strategy",
                    "type": "Book"
                },
                {
                    "resource": "PrepLounge",
                    "description": "Practice platform with peers and experts (has paid/free cases)",
                    "type": "Platform"
                },
                {
                    "resource": "CaseCoach",
                    "description": "Premium course used by many MBA students (school discounts may apply)",
                    "type": "Course"
                },
                {
                    "resource": "RocketBlocks",
                    "description": "Interactive drills on math, frameworks, and fit",
                    "type": "Platform"
                },
                {
                    "resource": "Crafting Cases (YouTube)",
                    "description": "Free, well-explained case walkthroughs and frameworks",
                    "type": "Video"
                },
                {
                    "resource": "Victor Cheng's LOMS (Look Over My Shoulder)",
                    "description": "Real recordings of case interviews (audio)",
                    "type": "Audio"
                }
            ],
            "behavioral_interview_prep": [
                {
                    "resource": "Consulting Interview Bible (by Management Consulted)",
                    "description": "Real examples of 'fit' questions and how to answer them",
                    "type": "Book"
                },
                {
                    "resource": "Big Interview (Behavioral Section)",
                    "description": "STAR method prep for stories",
                    "type": "Platform"
                },
                {
                    "resource": "Tell Me About a Time… by Rob Yeung",
                    "description": "Book for behavioral interview storytelling",
                    "type": "Book"
                },
                {
                    "resource": "HBR's Guide to Persuasive Presentations",
                    "description": "Build communication and storytelling skills",
                    "type": "Book"
                }
            ],
            "business_industry_awareness": [
                {
                    "resource": "McKinsey Insights",
                    "description": "Latest research, trends, and industry briefs",
                    "type": "Website"
                },
                {
                    "resource": "Bain Insights / BCG Perspectives",
                    "description": "Real consulting cases and trends",
                    "type": "Website"
                },
                {
                    "resource": "Harvard Business Review",
                    "description": "Articles on strategy, management, and innovation",
                    "type": "Publication"
                },
                {
                    "resource": "The Economist / Financial Times",
                    "description": "Stay updated on global business context",
                    "type": "Publication"
                },
                {
                    "resource": "Morning Brew (Newsletter)",
                    "description": "Daily summary of business news (free & fast)",
                    "type": "Newsletter"
                }
            ],
            "tools": [
                {
                    "resource": "Excel",
                    "description": "Basic modeling, analysis, client deliverables",
                    "type": "Software"
                },
                {
                    "resource": "PowerPoint",
                    "description": "Slide creation, structured communication",
                    "type": "Software"
                },
                {
                    "resource": "Notion / Miro / Whimsical",
                    "description": "Brainstorming frameworks, mapping ideas",
                    "type": "Software"
                },
                {
                    "resource": "Grammarly",
                    "description": "Writing clarity for documents and communication",
                    "type": "Software"
                }
            ],
            "free_courses": [
                {
                    "resource": "Business Strategy (Wharton)",
                    "description": "Coursera course on business strategy",
                    "platform": "Coursera"
                },
                {
                    "resource": "Foundations of Business Strategy",
                    "description": "Coursera course on business strategy foundations",
                    "platform": "Coursera"
                },
                {
                    "resource": "Strategy and the Sustainable Enterprise",
                    "description": "U. of Virginia course on strategy",
                    "platform": "edX"
                },
                {
                    "resource": "Consulting Foundations",
                    "description": "LinkedIn Learning course on consulting",
                    "platform": "LinkedIn Learning"
                },
                {
                    "resource": "Business Analysis for Consultants",
                    "description": "LinkedIn Learning course on business analysis",
                    "platform": "LinkedIn Learning"
                },
                {
                    "resource": "Making Sense of Strategy",
                    "description": "Free course on strategy",
                    "platform": "OpenLearn"
                }
            ]
        }
    
    @staticmethod
    def get_comprehensive_guide() -> Dict[str, Any]:
        """Get the complete management consulting guide"""
        
        return {
            "title": "Management Consulting Skills & Resources Guide",
            "skills_breakdown": ManagementConsultingResources.get_skills_breakdown(),
            "learning_resources": ManagementConsultingResources.get_learning_resources(),
            "timeline": {
                "months_1_2": "Focus on Problem Solving & Structured Thinking",
                "months_3_4": "Develop Analytical & Quantitative Skills", 
                "months_5_6": "Build Communication & Storytelling Skills",
                "months_7_10": "Master Case Interview Preparation",
                "months_11_12": "Develop Business & Industry Knowledge",
                "ongoing": "Networking & Applications"
            },
            "success_tips": [
                "Start case interview prep early - don't wait until the last minute",
                "Practice mental math daily - it's crucial for case interviews",
                "Read business news daily to stay current on industry trends",
                "Join consulting clubs and practice with peers",
                "Build a strong network of alumni in consulting",
                "Prepare 10+ STAR stories for behavioral interviews",
                "Master Excel shortcuts and PowerPoint design",
                "Practice explaining complex concepts simply"
            ],
            "indian_employer_requirements": {
                "title": "🔧 Top Skills Sought by Indian Employers in Management Consultants",
                "skills": [
                    {
                        "skill": "Problem-Solving & Analytical Thinking",
                        "importance": "Consultants are expected to dissect complex business challenges and devise actionable solutions",
                        "practice": "Employers look for candidates who can analyze data, identify root causes, and apply frameworks to address issues effectively",
                        "source": "Indeed"
                    },
                    {
                        "skill": "Strategic Thinking",
                        "importance": "The ability to anticipate market trends and align strategies with business goals is crucial",
                        "practice": "Consultants should demonstrate foresight in designing impactful strategies that consider risks and opportunities",
                        "source": "TimesPro"
                    },
                    {
                        "skill": "Exceptional Communication Skills",
                        "importance": "Clear articulation of findings and recommendations is essential for client engagement",
                        "practice": "Proficiency in preparing detailed reports, delivering presentations, and maintaining transparent communication with clients is highly valued",
                        "source": "TimesPro"
                    },
                    {
                        "skill": "Data Analysis Proficiency",
                        "importance": "In the digital age, data-driven decisions are paramount",
                        "practice": "Consultants should be adept in tools like SQL, Python, Tableau, and advanced Excel to process complex datasets and derive meaningful insights",
                        "source": "TimesPro"
                    },
                    {
                        "skill": "Interpersonal Skills",
                        "importance": "Building trust and understanding client needs are fundamental to successful consulting",
                        "practice": "Consultants must foster professional relationships, listen actively, and collaborate effectively with diverse stakeholders",
                        "source": "Indeed"
                    },
                    {
                        "skill": "Project Management Expertise",
                        "importance": "Managing consulting projects requires effective coordination and resource allocation",
                        "practice": "Employers seek candidates with experience in overseeing project timelines, managing teams, and ensuring successful project outcomes",
                        "source": "thecareerhub.brainwonders.in"
                    },
                    {
                        "skill": "Adaptability and Flexibility",
                        "importance": "The consulting landscape is dynamic, requiring professionals to adjust to varying client needs and industries",
                        "practice": "Consultants should demonstrate openness to new challenges and the ability to pivot strategies as necessary",
                        "source": "thecareerhub.brainwonders.in"
                    },
                    {
                        "skill": "Business Acumen",
                        "importance": "Understanding business operations and market dynamics is critical for providing strategic advice",
                        "practice": "Consultants should possess a deep understanding of business operations, market dynamics, and financial principles to offer relevant recommendations",
                        "source": "thecareerhub.brainwonders.in"
                    }
                ],
                "additional_insights": {
                    "educational_background": "A bachelor's degree in economics, finance, marketing, or related fields is typically required. An MBA from a reputed institution is often preferred",
                    "certifications": "While not mandatory, certifications such as Certified Management Consultant (CMC) or in financial modeling can enhance credibility and demonstrate expertise",
                    "experience": "Entry-level positions may require 2–3 years of relevant experience, while senior roles demand proven expertise in consulting or a specialized field"
                },
                "indian_specific_tools": [
                    "SQL for data analysis",
                    "Python for advanced analytics",
                    "Tableau for data visualization",
                    "Advanced Excel for financial modeling",
                    "Power BI for business intelligence",
                    "R for statistical analysis"
                ],
                "indian_consulting_firms": [
                    "McKinsey India",
                    "Bain India",
                    "BCG India",
                    "Deloitte Consulting India",
                    "PwC India",
                    "EY India",
                    "KPMG India",
                    "Accenture India",
                    "IBM Consulting India",
                    "Capgemini India"
                ]
            }
        }
