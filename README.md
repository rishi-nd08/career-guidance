# Career Guidance Agent for PG Students

A comprehensive career guidance platform designed specifically for postgraduate students in Technology and MBA fields. This agent provides personalized career roadmaps, real-time job market insights, and expert guidance to help students make informed career decisions.

## 🚀 Features

### Core Functionality
- **Personalized Career Roadmaps**: Generate structured learning paths based on roadmap.sh and tailored to your specific field and goals
- **Real-time Market Data**: Access current hiring trends, salary information, and company insights from major job boards
- **Layoff Statistics**: Stay informed about market trends and layoff statistics to make better career decisions
- **Skill Requirements**: Discover essential skills needed for specific companies and roles in your field
- **Expert Recommendations**: Receive personalized advice and recommendations based on current market conditions
- **Comprehensive Database**: Access a vast database of career information updated with real-time market data

### Supported Fields
- **Technology**: Frontend, Backend, Data Science, DevOps, Mobile Development, Cybersecurity, AI/ML
- **MBA/Business**: Consulting, Finance, Marketing, Operations, Strategy, Entrepreneurship, HR

## 🛠️ Technology Stack

- **Backend**: FastAPI (Python)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Database**: SQLite with SQLAlchemy ORM
- **Web Scraping**: BeautifulSoup, Selenium, aiohttp
- **UI Framework**: Bootstrap 5
- **Styling**: Custom CSS with modern design principles

## 📋 Prerequisites

- Python 3.8 or higher
- Chrome browser (for Selenium web scraping)
- ChromeDriver (automatically managed by Selenium)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd career-guidance-agent
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Create a .env file in the root directory
   touch .env
   
   # Add any required environment variables
   # (Currently no external API keys required)
   ```

5. **Initialize the database**
   ```bash
   python -c "from src.database import init_db; import asyncio; asyncio.run(init_db())"
   ```

## 🏃‍♂️ Running the Application

1. **Start the FastAPI server**
   ```bash
   python app.py
   ```

2. **Access the application**
   - Open your browser and navigate to `http://localhost:8000`
   - The application will be available with a beautiful, responsive interface

3. **API Documentation**
   - FastAPI automatically generates interactive API docs at `http://localhost:8000/docs`
   - Alternative docs at `http://localhost:8000/redoc`

## 📖 Usage

### Web Interface
1. Navigate to the homepage
2. Fill out the career guidance form with your details:
   - Select your field (Tech or MBA)
   - Choose your specialization
   - Specify your experience level
   - Add target companies and roles
   - List your current skills
   - Ask your specific career question
3. Click "Generate Career Roadmap"
4. View your personalized career guidance report

### API Endpoints

#### Get Career Guidance
```http
POST /api/career-guidance
Content-Type: application/json

{
  "field": "tech",
  "specialization": "frontend",
  "experience_level": "fresh_graduate",
  "target_companies": ["Google", "Microsoft"],
  "target_roles": ["Software Engineer"],
  "skills": ["JavaScript", "React"],
  "query_text": "How can I become a frontend developer?"
}
```

#### Get Roadmap
```http
GET /api/roadmap/frontend
```

#### Get Market Data
```http
GET /api/market-data/Google
```

#### Get Layoff Statistics
```http
GET /api/layoff-stats
```

#### Get Skill Requirements
```http
GET /api/skills/software_engineer
```

## 🏗️ Project Structure

```
career-guidance-agent/
├── app.py                 # FastAPI application entry point
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── .env                  # Environment variables
├── src/                  # Source code directory
│   ├── __init__.py
│   ├── models.py         # Pydantic models
│   ├── database.py       # Database configuration and models
│   ├── web_scraper.py    # Web scraping functionality
│   ├── roadmap_generator.py # Roadmap generation logic
│   └── career_agent.py   # Main career guidance agent
├── templates/            # HTML templates
│   └── index.html        # Main application interface
├── static/               # Static assets
│   ├── css/
│   │   └── style.css     # Custom styles
│   └── js/
│       └── app.js        # Frontend JavaScript
└── data/                 # Database and data files
    └── career_guidance.db # SQLite database
```

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the root directory with the following variables:

```env
# Database
DATABASE_URL=sqlite:///./data/career_guidance.db

# Web Scraping
USER_AGENT=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36

# Optional: External API keys for enhanced functionality
# OPENAI_API_KEY=your_openai_api_key
# LINKEDIN_API_KEY=your_linkedin_api_key
```

### Customization
- **Roadmaps**: Modify `src/roadmap_generator.py` to add new specializations or update existing roadmaps
- **Scraping Sources**: Update `src/web_scraper.py` to add new job boards or data sources
- **UI**: Customize the interface by modifying files in `templates/` and `static/`

## 🧪 Testing

Run the application and test the following scenarios:

1. **Basic Career Query**
   - Submit a form with tech field and frontend specialization
   - Verify roadmap generation and market data retrieval

2. **MBA Career Query**
   - Submit a form with MBA field and consulting specialization
   - Check for appropriate business-focused recommendations

3. **API Testing**
   - Use the interactive API docs at `/docs` to test endpoints
   - Verify data formats and error handling

## 🚀 Deployment

### Local Development
The application runs on `http://localhost:8000` by default.

### Production Deployment
For production deployment, consider:

1. **Environment Setup**
   ```bash
   # Install production dependencies
   pip install gunicorn
   
   # Set production environment variables
   export ENVIRONMENT=production
   ```

2. **Run with Gunicorn**
   ```bash
   gunicorn app:app -w 4 -k uvicorn.workers.UvicornWorker
   ```

3. **Docker Deployment** (Optional)
   ```dockerfile
   FROM python:3.9-slim
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   COPY . .
   CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
   ```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 for Python code
- Add type hints for all functions
- Include docstrings for classes and methods
- Write tests for new functionality
- Update documentation for new features

## 📊 Data Sources

The application gathers data from various sources:

- **Job Boards**: LinkedIn, Indeed, Glassdoor
- **Company Data**: Official company websites and career pages
- **Market Trends**: Industry reports and news sources
- **Roadmap References**: roadmap.sh and similar educational platforms

## 🔒 Privacy and Ethics

- All user queries are stored locally in the SQLite database
- No personal information is shared with external services
- Web scraping follows robots.txt and rate limiting guidelines
- Data is used solely for providing career guidance

## 🐛 Troubleshooting

### Common Issues

1. **ChromeDriver Issues**
   ```bash
   # Update ChromeDriver
   pip install --upgrade selenium
   ```

2. **Database Connection Issues**
   ```bash
   # Ensure data directory exists
   mkdir -p data
   ```

3. **Port Already in Use**
   ```bash
   # Change port in app.py
   uvicorn.run(app, host="0.0.0.0", port=8001)
   ```

### Debug Mode
Enable debug mode by setting:
```python
# In app.py
uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
```

## 📈 Future Enhancements

- [ ] Integration with LinkedIn API for enhanced job data
- [ ] Resume scanning and analysis capabilities
- [ ] Machine learning for personalized recommendations
- [ ] Integration with learning platforms (Coursera, Udemy)
- [ ] Real-time notifications for job opportunities
- [ ] Advanced analytics and career progression tracking
- [ ] Multi-language support
- [ ] Mobile application

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [roadmap.sh](https://roadmap.sh) for providing excellent learning roadmaps
- FastAPI community for the excellent framework
- Bootstrap team for the responsive UI components
- All the open-source libraries that made this project possible

## 📞 Support

For support, email your-email@example.com or create an issue in the repository.

---

**Built with ❤️ for PG students seeking career guidance**
