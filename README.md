# Aisha - AI-Powered Client Management Platform

**Aisha** is an intelligent WhatsApp-based customer engagement platform designed for African businesses. It combines AI-powered conversations, automated waiting list management, and real-time customer communication to help businesses scale their customer support without proportional cost increases.

> **Tagline:** Your AI-powered customer communication superpower for African businesses.

## 📋 Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Key Features](#key-features)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Environment Setup](#environment-setup)
- [Running the Application](#running-the-application)
- [API Documentation](#api-documentation)
- [WhatsApp Integration](#whatsapp-integration)
- [Database Configuration](#database-configuration)
- [API Endpoints](#api-endpoints)
- [Error Handling](#error-handling)
- [Best Practices](#best-practices)
- [Contributing](#contributing)
- [Development](#development)
- [Deployment](#deployment)
- [Troubleshooting](#troubleshooting)
- [Support](#support)

---

## 🎯 Overview

Aisha is a backend service that empowers businesses to:

- 📱 **Engage customers directly on WhatsApp** - The most popular messaging platform in Africa
- 🤖 **Automate responses with AI** - Using Google Gemini for intelligent, context-aware conversations
- ⏳ **Manage customer queues** - Track waiting lists and send automated notifications
- 📊 **Track customer interactions** - Analytics and insights on customer engagement
- 💰 **Reduce support costs** - Scale customer support from $2,000-5,000/month to just $50-500/month

### Problem Solved

Traditional customer support channels are:
- ❌ **Expensive** - Require dedicated support teams
- ❌ **Limited hours** - Not available 24/7
- ❌ **Inefficient** - Manual queue management and follow-ups
- ❌ **Poor experience** - Customers wait in queues without updates

**Aisha solves this** by automating customer communication through WhatsApp with AI-powered responses.

---

## 🏗️ Architecture

### System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                       Client Applications                        │
│              (Web, Mobile, Third-party Services)                 │
└────────────────────────┬────────────────────────────────────────┘
                         │
                    HTTP/REST
                         │
┌────────────────────────▼────────────────────────────────────────┐
│                     FastAPI Backend                              │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  - Request handling & routing                            │   │
│  │  - Business logic & validation                           │   │
│  │  - WebSocket connections for real-time updates          │   │
│  └──────────────────────────────────────────────────────────┘   │
└─────┬────────────────┬────────────────┬───────────────────────────┘
      │                │                │
      ▼                ▼                ▼
  ┌─────────┐   ┌──────────────┐  ┌──────────────┐
  │PostgreSQL│   │Google Gemini │  │ Twilio API   │
  │ Database │   │     AI       │  │(WhatsApp)    │
  └─────────┘   └──────────────┘  └──────────────┘
```

### Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Framework** | FastAPI | High-performance async web framework |
| **Language** | Python 3.9+ | Backend logic and API development |
| **Database** | PostgreSQL 12+ | Scalable, secure data storage |
| **AI** | Google Gemini API | Natural language processing & intelligent responses |
| **Messaging** | Twilio WhatsApp Business API | WhatsApp message delivery |
| **ORM** | SQLAlchemy | Database abstraction layer |
| **Validation** | Pydantic | Request/response validation |
| **Async** | AsyncIO | Non-blocking I/O operations |
| **Server** | Uvicorn/Gunicorn | ASGI server for production |

---

## ✨ Key Features

✅ **Waiting List Management**
- Add/remove users from waiting lists
- Track position and status
- Send automated position updates

✅ **AI-Powered Conversations**
- Google Gemini AI for intelligent responses
- Context-aware customer interactions
- Natural language understanding

✅ **WhatsApp Integration**
- Send/receive messages via Twilio
- Message templates for compliance
- Rich media support (images, documents, videos)
- Webhook for real-time message handling

✅ **Phone Number Management**
- Support for multiple Kenyan phone formats
- International number support
- Automatic format normalization

✅ **Scalable Architecture**
- Connection pooling for database efficiency
- Async/await for high concurrency
- Horizontal scaling ready

✅ **Comprehensive Error Handling**
- Detailed error responses
- Graceful failure recovery
- Structured logging

✅ **Security**
- Environment-based configuration
- Input validation on all endpoints
- Webhook signature verification
- CORS configuration

---

## 📁 Project Structure

```
Aisha_backend/
│
├── main.py                          # FastAPI application entry point
│   ├── Endpoints: waiting-list, gemini, whatsapp
│   └── CORS, middleware, error handlers
│
├── database.py                      # Database configuration
│   ├── Connection pooling setup
│   ├── Session management
│   └── SQLAlchemy engine creation
│
├── models.py                        # SQLAlchemy ORM models
│   ├── WaitingListUser
│   ├── WhatsAppMessage
│   ├── CustomerInteraction
│   └── MessageTemplate
│
├── schemas.py                       # Pydantic validation schemas
│   ├── Request models
│   ├── Response models
│   └── Generic Resource protocol
│
├── service/
│   ├── api_service.py              # External API calls
│   │   ├── Gemini AI calls
│   │   ├── Twilio WhatsApp API
│   │   └── HTTP client management
│   │
│   ├── whatsapp_service.py         # WhatsApp business logic
│   │   ├── send_message()
│   │   ├── send_template_message()
│   │   ├── send_media_message()
│   │   └── Phone number normalization
│   │
│   ├── gemini_service.py           # Google Gemini AI integration
│   │   ├── Generate responses
│   │   ├── Process conversations
│   │   └── Context management
│   │
│   └── waiting_list_service.py     # Waiting list business logic
│       ├── Add to list
│       ├── Get position
│       ├── Send notifications
│       └── Manage queue
│
├── requirements.txt                 # Python dependencies
├── .env.example                    # Environment variables template
├── .gitignore                      # Git ignore rules
├── README.md                       # This file
│
└── migrations/                     # Alembic database migrations (optional)
    ├── versions/
    └── env.py
```

### File Responsibilities

| File | Responsibility |
|------|-----------------|
| **main.py** | FastAPI app setup, route definitions, error handlers |
| **database.py** | PostgreSQL connection, session factory, pooling config |
| **models.py** | Database schema definitions (tables, relationships) |
| **schemas.py** | Request/response validation and serialization |
| **api_service.py** | External API integrations (Gemini, Twilio) |
| **whatsapp_service.py** | WhatsApp message handling logic |
| **gemini_service.py** | AI response generation |

---

## 📚 Documentation

### System Requirements & Product Specification

📖 **[Aisha PRD (Product Requirements Document)](https://www.notion.so/Aisha-Client-Management-Superpower-Product-Requirement-Document-PRD-25a14f56cedb804bb0ced6dfb6ff591d)**

This document contains:
- Complete feature specifications
- User stories and use cases
- System architecture details
- API requirements
- Success metrics

### API Documentation

🔗 **Interactive API Docs:**
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

These auto-generated docs include:
- All available endpoints
- Request/response schemas
- Try-it-out functionality
- Authentication details

---

## 🚀 Prerequisites

- **Python** 3.9 or higher
- **PostgreSQL** 12 or higher
- **pip** (Python package manager)
- **Virtual environment** (recommended: venv or conda)
- **Git** for version control

### External Services Required

- **Google Cloud Project** with Gemini API enabled
- **Twilio Account** with WhatsApp Business API access
- **WhatsApp Business Account** (approved by Meta)

---

## 📥 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Aisha_backend.git
cd Aisha_backend
```

### 2. Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Verify Installation

```bash
# Check Python version
python --version

# Check installed packages
pip list
```

---

## ⚙️ Environment Setup

### 1. Create .env File

Create a `.env` file in the project root:

```bash
cp .env.example .env
```

### 2. Configure Environment Variables

Edit `.env` with your actual credentials:

```env
# ===== Database Configuration =====
DATABASE_URL=postgresql://api_user:Excalibar598@localhost:5433/waiting_list_db

# ===== Google Gemini API =====
GEMINI_API_KEY=AIzaSyA11NyaEUfh0642RYVPgVF4Qw6SRbzqqaA

# ===== Twilio WhatsApp Configuration =====
TWILIO_ACCOUNT_SID=your_account_sid_here
TWILIO_AUTH_TOKEN=your_auth_token_here
TWILIO_WHATSAPP_NUMBER=+1234567890

# ===== Server Configuration =====
HOST=0.0.0.0
PORT=8000
DEBUG=False

# ===== Environment =====
ENVIRONMENT=development
```

### 3. Environment Variables Reference

| Variable | Description | Example |
|----------|-------------|---------|
| `DATABASE_URL` | PostgreSQL connection string | `postgresql://user:pass@host/db` |
| `GEMINI_API_KEY` | Google Gemini API key | `AIzaSyA1...` |
| `TWILIO_ACCOUNT_SID` | Twilio account identifier | `AC1234567890...` |
| `TWILIO_AUTH_TOKEN` | Twilio authentication token | `1234567890abcdef...` |
| `TWILIO_WHATSAPP_NUMBER` | Twilio WhatsApp sandbox number | `+1234567890` |

### ⚠️ Security Warning

**Never commit `.env` to version control!** It's already in `.gitignore`.

---

## 🏃 Running the Application

### Development Mode

```bash
# Start with hot reload
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Application runs at http://localhost:8000
```

### Production Mode

```bash
# Using Gunicorn (production-ready)
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app

# Using Uvicorn (basic production)
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

### Verify Server is Running

```bash
curl http://localhost:8000/
# Response: {"message": "Waiting List API is running"}
```

---

## 📖 API Documentation

### Interactive Documentation

Once the server is running, access:

- **Swagger UI**: http://localhost:8000/docs
  - Full API explorer
  - Try-it-out functionality
  - Request/response schemas

- **ReDoc**: http://localhost:8000/redoc
  - Beautiful API documentation
  - Alternative view of endpoints

### API Endpoints Overview

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Health check |
| `POST` | `/waiting-list/` | Add user to waiting list |
| `GET` | `/waiting-list/{id}` | Get waiting list user by ID |
| `POST` | `/gemini` | Get AI response from Gemini |
| `POST` | `/whatsapp/send-text` | Send WhatsApp text message |
| `POST` | `/whatsapp/send-media` | Send WhatsApp media message |
| `POST` | `/webhook/whatsapp` | Receive WhatsApp messages |

### Example Requests

**Add to Waiting List:**
```bash
curl -X POST http://localhost:8000/waiting-list/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "John Doe",
    "phone_number": "0712345678"
  }'
```

**Send WhatsApp Message:**
```bash
curl -X POST http://localhost:8000/whatsapp/send-text \
  -H "Content-Type: application/json" \
  -d '{
    "phone_number": "+254712345678",
    "message": "Hello from Aisha!"
  }'
```

**Get AI Response:**
```bash
curl -X POST http://localhost:8000/gemini \
  -H "Content-Type: application/json" \
  -d '{"prompt": "What is machine learning?"}'
```

---

## 📱 WhatsApp Integration

### Setup Instructions

#### 1. Create Twilio Account

- Visit: https://www.twilio.com/try-twilio
- Sign up and verify email/phone
- Get your Account SID and Auth Token

#### 2. Enable WhatsApp Sandbox

- Go to Twilio Console → Messaging → Try it out
- Request WhatsApp Sandbox access
- Follow approval process

#### 3. Configure Credentials

Update `.env` with your Twilio credentials:

```env
TWILIO_ACCOUNT_SID=your_sid
TWILIO_AUTH_TOKEN=your_token
TWILIO_WHATSAPP_NUMBER=+1234567890
```

#### 4. Test Webhook (Development)

Use ngrok for local webhook testing:

```bash
# Install ngrok
# Run FastAPI
uvicorn main:app --reload

# In another terminal
ngrok http 8000
# Use the ngrok URL for webhook configuration
```

#### 5. Configure Webhook

In your application/platform:
- Webhook URL: `https://yourdomain.com/webhook/whatsapp`
- Subscribe to: `messages`, `message_status`

---

## 🗄️ Database Configuration

### PostgreSQL Setup

```bash
# Create database
createdb aisha_db

# Connect to database
psql -U postgres -d aisha_db
```

### Initialize Database

```bash
# From Python shell
python
>>> from database import Base, engine
>>> Base.metadata.create_all(bind=engine)
>>> exit()
```

### Connection Pooling

Connection pooling is configured in `database.py`:

```python
engine = create_engine(
    DATABASE_URL,
    poolclass=QueuePool,
    pool_size=20,
    max_overflow=40,
    pool_pre_ping=True,
)
```

This ensures:
- ✅ Efficient database connections
- ✅ Automatic reconnection on failure
- ✅ Prevents connection leaks

---

## 🔌 API Endpoints

### 1. Health Check

```http
GET /
```

**Response (200):**
```json
{
  "message": "Waiting List API is running"
}
```

### 2. Add to Waiting List

```http
POST /waiting-list/
Content-Type: application/json

{
  "username": "Jane Smith",
  "phone_number": "0712345678"
}
```

**Response (201):**
```json
{
  "id": 1,
  "username": "Jane Smith",
  "phone_number": "+254712345678",
  "position": 1,
  "created_at": "2024-11-04T10:30:00",
  "status": "active"
}
```

**Phone Number Formats Accepted:**
- Local: `0712345678`
- International: `+254712345678`
- Country code: `254712345678`

### 3. Get Waiting List User

```http
GET /waiting-list/{id}
```

**Response (200):**
```json
{
  "id": 1,
  "username": "Jane Smith",
  "position": 5,
  "status": "active"
}
```

### 4. Send WhatsApp Message

```http
POST /whatsapp/send-text
Content-Type: application/json

{
  "phone_number": "+254712345678",
  "message": "Hello! Your order is ready for pickup."
}
```

**Response (200):**
```json
{
  "success": true,
  "data": {
    "message_id": "SM1234567890abcdef",
    "status": "sent",
    "to": "+254712345678"
  }
}
```

### 5. Send WhatsApp Media

```http
POST /whatsapp/send-media
Content-Type: application/json

{
  "phone_number": "+254712345678",
  "media_url": "https://example.com/invoice.pdf",
  "media_type": "document",
  "caption": "Your Invoice"
}
```

### 6. Get AI Response

```http
POST /gemini
Content-Type: application/json

{
  "prompt": "What products do you recommend for beginners?"
}
```

**Response (200):**
```json
{
  "response": "For beginners, I recommend...",
  "tokens_used": 150
}
```

### 7. WhatsApp Webhook

```http
POST /webhook/whatsapp
```

**Webhook Payload:**
```json
{
  "from": "+254712345678",
  "body": "When will my order arrive?",
  "message_id": "wamid.123456"
}
```

---

## ⚠️ Error Handling

### Error Response Format

All errors follow this structure:

```json
{
  "success": false,
  "error": "Error message",
  "details": "Additional context"
}
```

### HTTP Status Codes

| Status | Meaning | Example |
|--------|---------|---------|
| `200` | Success | Message sent successfully |
| `201` | Created | User added to waiting list |
| `400` | Bad Request | Invalid phone number format |
| `422` | Validation Error | Missing required field |
| `500` | Server Error | Database connection failed |
| `503` | Service Unavailable | External API unreachable |

### Common Error Scenarios

**Invalid Phone Number:**
```json
{
  "success": false,
  "error": "Invalid phone number format"
}
```

**Missing API Key:**
```json
{
  "success": false,
  "error": "GEMINI_API_KEY not configured"
}
```

**WhatsApp API Error:**
```json
{
  "success": false,
  "error": "HTTP Status 401",
  "details": "Twilio authentication failed"
}
```

---

## 🎯 Best Practices

### Security

✅ **Never commit `.env` file**
```bash
# Verify in .gitignore
echo ".env" >> .gitignore
```

✅ **Use environment variables** for all sensitive data
```python
api_key = os.getenv("GEMINI_API_KEY")
```

✅ **Validate all inputs**
```python
@app.post("/endpoint")
async def endpoint(data: YourSchema):
    # Pydantic validates automatically
    pass
```

✅ **Verify webhook signatures** (when implementing)
```python
def verify_signature(body, signature, token):
    # Implement verification
    pass
```

### Performance

✅ **Use async/await** for I/O operations
```python
async def fetch_data():
    # Non-blocking I/O
    pass
```

✅ **Enable connection pooling** (already configured)

✅ **Implement caching** for frequently accessed data
```python
from functools import lru_cache

@lru_cache(maxsize=128)
def get_user(user_id: int):
    pass
```

✅ **Add timeouts** to external API calls
```python
timeout = Timeout(10.0)  # 10 second timeout
```

### Code Quality

✅ **Follow PEP 8** style guide
```python
# Good
def send_message(phone_number: str, message: str) -> dict:
    """Send WhatsApp message."""
    pass
```

✅ **Use type hints** for all functions
```python
def process(data: str) -> dict[str, Any]:
    pass
```

✅ **Write docstrings** for modules and functions
```python
"""Module for WhatsApp integration."""

def send_message(phone: str) -> None:
    """Send a WhatsApp message to the specified phone number."""
    pass
```

✅ **Handle exceptions gracefully**
```python
try:
    result = await call_api()
except httpx.TimeoutException:
    logger.error("API timeout")
except Exception as e:
    logger.error(f"Unexpected error: {str(e)}")
```

---

## 🤝 Contributing

We welcome contributions! Whether it's bug fixes, features, or documentation improvements, your help is appreciated.

### Contribution Guidelines

#### 1. Fork the Repository

```bash
# Click "Fork" on GitHub
# Clone your fork
git clone https://github.com/yourusername/Aisha_backend.git
cd Aisha_backend
```

#### 2. Create a Feature Branch

```bash
# Always create a new branch for your work
git checkout -b feature/your-feature-name

# Branch naming conventions:
# - feature/description       (for new features)
# - fix/description           (for bug fixes)
# - docs/description          (for documentation)
# - refactor/description      (for code refactoring)
```

#### 3. Make Your Changes

```bash
# Ensure your code follows PEP 8
pip install black flake8
black .
flake8 .

# Add tests for new functionality
# Update README if needed
```

#### 4. Commit Your Changes

```bash
# Use clear, descriptive commit messages
git add .
git commit -m "feat: add new WhatsApp template feature"

# Commit message format:
# feat:     A new feature
# fix:      A bug fix
# docs:     Documentation changes
# refactor: Code refactoring
# test:     Adding tests
# chore:    Build, dependencies, etc.
```

#### 5. Push to Your Fork

```bash
git push origin feature/your-feature-name
```

#### 6. Open a Pull Request

- Go to GitHub
- Click "Compare & pull request"
- Fill in the PR template
- Describe changes clearly
- Link any related issues

### Pull Request Checklist

- [ ] Code follows PEP 8 style guide
- [ ] All tests pass locally
- [ ] New tests added for new functionality
- [ ] README updated if needed
- [ ] No sensitive data in commits
- [ ] Commit messages are clear and descriptive
- [ ] No merge conflicts

### Code Review Process

1. **Automated Checks**
   - Tests must pass
   - Code style validation
   - Security scanning

2. **Manual Review**
   - At least 1 approval required
   - Maintainers review for quality
   - Discussion and feedback

3. **Merge**
   - Approved and all checks pass
   - Merge to main branch

### Testing

```bash
# Run tests
pytest

# With coverage
pytest --cov=. --cov-report=html

# Run specific test
pytest tests/test_whatsapp_service.py
```

### Setting Up Development Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies including dev tools
pip install -r requirements-dev.txt

# Pre-commit hooks
pre-commit install

# Now all commits will run checks automatically
```

### Getting Help

- 📧 Email: team@aisha.dev
- 💬 Discussions: GitHub Discussions
- 🐛 Issues: GitHub Issues
- 📚 Docs: https://docs.aisha.dev

---

## 💻 Development

### Local Development Setup

```bash
# 1. Activate virtual environment
source venv/bin/activate

# 2. Install development dependencies
pip install -r requirements-dev.txt

# 3. Create .env file
cp .env.example .env

# 4. Update .env with your credentials
nano .env

# 5. Start development server
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Project Layout for New Features

When adding new features:

```
feature_name/
├── models.py        # Database models
├── schemas.py       # Pydantic schemas
├── service.py       # Business logic
├── routes.py        # API endpoints
└── tests/
    └── test_feature.py
```

### Useful Commands

```bash
# Format code
black .

# Lint code
flake8 .
pylint .

# Run type checker
mypy .

# Run tests
pytest

# Generate coverage report
pytest --cov=.

# Install pre-commit hooks
pre-commit install

# Run pre-commit manually
pre-commit run --all-files
```

---

## 🚀 Deployment

### Production Checklist

Before deploying to production:

- [ ] All tests pass
- [ ] No hardcoded secrets
- [ ] Database backups configured
- [ ] Error logging setup
- [ ] Rate limiting enabled
- [ ] HTTPS/SSL configured
- [ ] CORS properly configured
- [ ] Database migrations run
- [ ] Environment variables set
- [ ] Load testing completed

### Deployment Options

#### Docker Deployment

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "main:app"]
```

```bash
# Build image
docker build -t aisha-backend .

# Run container
docker run -p 8000:8000 --env-file .env aisha-backend
```

#### Cloud Deployment (AWS/GCP/Azure)

1. **AWS Elastic Beanstalk**
   ```bash
   eb create aisha-backend
   eb deploy
   ```

2. **Google Cloud Run**
   ```bash
   gcloud run deploy aisha-backend --source .
   ```

3. **Azure App Service**
   ```bash
   az webapp up --name aisha-backend
   ```

### Production Server Setup

```bash
# Using Gunicorn
pip install gunicorn

# Run with 4 workers
gunicorn -w 4 \
  -k uvicorn.workers.UvicornWorker \
  --bind 0.0.0.0:8000 \
  --timeout 120 \
  --access-logfile - \
  main:app
```

### Environment Variables in Production

Use managed secrets services:

- **AWS**: Secrets Manager / Parameter Store
- **GCP**: Secret Manager
- **Azure**: Key Vault
- **Generic**: HashiCorp Vault

```python
# Example: Load from AWS Secrets Manager
import boto3

client = boto3.client('secretsmanager')
secret = client.get_secret_value(SecretId='aisha-backend')
```

---

## 🔧 Troubleshooting

### Common Issues & Solutions

#### Database Connection Failed

```
Error: could not connect to server: Connection refused
```

**Solution:**
```bash
# 1. Check PostgreSQL is running
sudo systemctl status postgresql

# 2. Verify DATABASE_URL in .env
echo $DATABASE_URL

# 3. Test connection
psql -d $DATABASE_URL
```

#### Gemini API Key Invalid

```
Error: Invalid API key
```

**Solution:**
```bash
# 1. Verify API key in .env
echo $GEMINI_API_KEY

# 2. Check API key is enabled
# - Go to Google Cloud Console
# - Enable Gemini API

# 3. Regenerate if needed
```

#### WhatsApp Messages Not Sending

```
Error: Twilio authentication failed (401)
```

**Solution:**
```bash
# 1. Check Twilio credentials
echo $TWILIO_ACCOUNT_SID
echo $TWILIO_AUTH_TOKEN

# 2. Verify WhatsApp is enabled in Twilio
# - Go to Twilio Console
# - Check Messaging → WhatsApp

# 3. Test with simple script
python test_twilio.py
```

#### Port Already in Use

```
Error: Address already in use
```

**Solution:**
```bash
# Find process using port 8000
lsof -i :8000

# Kill the process
kill -9 <PID>

# Or use different port
uvicorn main:app --port 8001
```

### Debug Mode

Enable detailed logging:

```python
# In main.py
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
```

Then run:
```bash
uvicorn main:app --reload --log-level debug
```

---

## 📞 Support

### Getting Help

1. **Check Documentation**
   - [Aisha PRD](https://www.notion.so/Aisha-Client-Management-Superpower-Product-Requirement-Document-PRD-25a14f56cedb804bb0ced6dfb6ff591d)
   - [API Docs](http://localhost:8000/docs)
   - This README

2. **Search Existing Issues**
   - GitHub Issues
   - GitHub Discussions

3. **Create an Issue**
   - Use issue templates
   - Provide minimal reproducible example
   - Include error logs

4. **Contact Team**
   - 📧 Email: support@aisha.dev
   - 💬 Slack: #aisha-support

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👥 Contributors

- **Lead Developer**: [Your Name]
- **Contributors**: [List contributors here]

### Acknowledgments

- FastAPI for the amazing framework
- Google for Gemini API
- Twilio for WhatsApp integration
- PostgreSQL for reliable data storage

---

## 🎯 Roadmap

### Q4 2024
- [ ] Complete Twilio integration
- [ ] Deploy beta version
- [ ] Gather user feedback

### Q1 2025
- [ ] Advanced analytics dashboard
- [ ] Custom AI model training
- [ ] Multi-language support

### Q2 2025
- [ ] Mobile app release
- [ ] Enterprise features
- [ ] East Africa expansion

---

**Last Updated**: November 4, 2024  
**Status**: Active Development 🚀

For the latest updates, star ⭐ this repository!


## Railway
