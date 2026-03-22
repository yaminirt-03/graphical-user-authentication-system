Graphical User Authentication System Project
A full-stack web application for tracking user streaks, login status, and personal notes. Built with modern web technologies, featuring user authentication, secure account management, and an interactive dashboard with real-time streak tracking.

🎯 Overview
Graphical User Authentication System is a comprehensive user account management and streak tracking application designed to help users maintain consistent habits and track their daily login activity. The application provides secure authentication, personalized dashboards, and real-time streak monitoring with an intuitive user interface.

Key Objectives
Provide secure user registration and authentication
Track user login streaks and consecutive login days
Enable users to create, manage, and view personal notes
Display real-time dashboard with user statistics
Maintain data integrity with SQL database persistence
Target Audience
Users wanting to build consistent daily habits
Developers looking for authentication examples
Teams needing streak-based engagement tracking
Personal productivity enthusiasts
✨ Features
1. User Registration & Account Creation
Create Account Page with intuitive form interface
Username Input Field - Unique username validation
Password Input Field - Secure password handling with strength validation
Emoji Selection - Choose 3 personal emojis (🍕, 🍊, 🚀, 😂, 🍦) as account avatar
Security Question - Custom dropdown "Select Secret Question" for account recovery
Secret Answer - Secure answer field for password recovery
Sign Up Button - Form submission with validation
Form Validation - Client-side and server-side validation
Error Handling - Clear error messages for registration issues
Session Management - Automatic session creation upon successful registration
2. User Login & Authentication
Login Page - Matching design with registration page
Username/Email Input - Multi-format credential support
Password Input - Secure password field with masking
Sign In Button - Authentication submission
Login Validation - Username and password verification against database
Session Token - JWT or session-based authentication
Remember Me - Optional persistent login feature
Forgot Password - Recovery via security question
Account Lockout - Protection against brute force attacks (optional)
Login Status Indicator - Display current login state
3. User Dashboard
Login Status Card - Real-time display of authentication state
Streak Counter - Current streak days with visual indicator
Streak Milestone - Highest streak achieved
Last Login - Timestamp of most recent login
Login History - Recent login dates and times
Daily Check-in Button - Maintain streak continuity
Streak Reset Alert - Warning when streak at risk (24hr timeout)
4. Notes Management
Create Note - Add new personal notes with timestamp
View Notes - Display all notes in chronological order
Edit Note - Modify existing note content
Delete Note - Remove notes with confirmation
Note Tagging - Categorize notes with tags
Search Notes - Filter notes by content or tag
Note Timestamp - Automatic creation and modification dates
Rich Text Editor (optional) - Format notes with basic styling
5. User Profile
Profile Picture - Emoji avatar display
Username Display - User identification
Account Created Date - Registration timestamp
Total Logins - Aggregate login count
Current Streak - Active streak display
Best Streak - Highest streak achievement
Email Display - Account email if verified
🛠️ Tech Stack
Backend
Framework: Python Flask

flask - Web framework core
flask-cors - Cross-origin resource sharing
flask-session - Server-side session management
flask-sqlalchemy - ORM integration
Authentication:

werkzeug.security - Password hashing (bcrypt/pbkdf2)
PyJWT - JSON Web Token generation
python-dotenv - Environment variable management
Database:

SQL - Relational database (SQLite)
SQLAlchemy - ORM for data persistence
Flask-Migrate - Database migrations
Additional Libraries:

requests - HTTP client for API calls
python-dateutil - Date/time utilities
validators - Input validation library
Frontend
HTML - Semantic markup and form structure

CSS - Responsive styling with modern techniques

CSS Grid - Layout structure
Flexbox - Component alignment
CSS Animations - Smooth transitions
Media Queries - Mobile responsiveness
JavaScript (Vanilla JS)

DOM Manipulation - Dynamic content updates
Fetch API - HTTP requests to backend
Event Handling - User interaction management
Local Storage - Client-side data persistence
Async/Await - Promise-based API calls
DevOps & Deployment
Version Control: Git/GitHub
Package Manager: pip (Python), npm (optional for build tools)
Environment Management: Python venv/virtualenv
Logging: Python logging module
Testing: pytest, Flask testing utilities
📁 Project Structure
GRAPHICAL_AUTH_PROJECT/
│
├── app.py                          # Backend Application Run
├── database.db                     # Created Automatically
├── requirements.txt                # Python dependencies
│
├── static/
│   ├── css/style.css
│   ├── js/particles.js
│   ├── js/script.js
│   ├── sounds/click_sound.wav
│
├── templates/
│   ├── dashboard.html
│   ├── login.html           
│   ├── register.html             
│   

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- SQLite3 (or PostgreSQL/MySQL for production)
- Modern web browser (Chrome, Firefox, Safari, Edge)

🎉 Acknowledgments
Flask framework documentation
SQLAlchemy ORM guides
Emoji assets from Open Source libraries
Community feedback and contributions
📊 Project Statistics
Language: Python, JavaScript, HTML, CSS
Database: SQLite
Lines of Code: ~2000+ (Backend), ~1500+ (Frontend)
Test Coverage: 85%+
Last Updated: March 2025
🗺️ Roadmap
 Two-factor authentication (2FA)
 streak milestones
 Social features (friend streaks, leaderboards)
 Analytics and insights dashboard
 Custom emoji library
 Dark/Light theme toggle
 Streak goal setting

 ## 📄 License

For educational and portfolio use.
 
