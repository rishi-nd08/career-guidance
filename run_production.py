#!/usr/bin/env python3
"""
Career Guidance Agent - Production Runner
Production-ready script without reload mode
"""

import asyncio
import sys
from pathlib import Path

# Add the project root to Python path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

from src.database import init_db, insert_sample_data
from app import app
import uvicorn

async def setup_application():
    """Initialize the application with database and sample data"""
    print("🚀 Starting Career Guidance Agent...")
    
    # Initialize database
    print("📊 Initializing database...")
    await init_db()
    
    # Insert sample data
    print("📝 Inserting sample data...")
    await insert_sample_data()
    
    print("✅ Application setup complete!")
    print("🌐 Starting server at http://localhost:8000")
    print("📚 API documentation available at http://localhost:8000/docs")

def main():
    """Main function to run the application"""
    try:
        # Run the setup
        asyncio.run(setup_application())
        
        # Start the server (production mode without reload)
        uvicorn.run(
            app,  # Direct app object for production
            host="0.0.0.0",
            port=8000,
            reload=False,  # Disable reload for production
            log_level="info"
        )
    except KeyboardInterrupt:
        print("\n👋 Shutting down Career Guidance Agent...")
    except Exception as e:
        print(f"❌ Error starting application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
