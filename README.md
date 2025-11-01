# Aisha Backend

A FastAPI-based backend service for managing waiting lists and integrating with Google Gemini AI and WhatsApp Business API.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Environment Setup](#environment-setup)
- [Project Structure](#project-structure)
- [Database Configuration](#database-configuration)
- [API Endpoints](#api-endpoints)
- [WhatsApp Integration](#whatsapp-integration)
- [Error Handling](#error-handling)
- [Best Practices](#best-practices)
- [Development](#development)
- [Deployment](#deployment)

## Features

✅ **Waiting List Management** - Add and manage users in a waiting list  
✅ **Gemini AI Integration** - Generate intelligent responses using Google Gemini API  
✅ **WhatsApp Webhook** - Receive and respond to WhatsApp messages  
✅ **Phone Number Validation** - Support for Kenyan phone number formats  
✅ **CORS Enabled** - Cross-origin resource sharing configured  
✅ **Async/Await Support** - Full async operations for better performance  
✅ **Database Connection Pooling** - Optimized database connections  
✅ **Error Handling** - Comprehensive try-catch exception handling  

## Prerequisites

- Python 3.9+
- PostgreSQL 12+
- pip (Python package manager)
- Virtual environment (recommended)

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Aisha_backend
```

### 2. Create Virtual Environment

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Environment Setup

### Create .env File

Create a `.env` file in the project root directory with the following variables:

```
# Database Configuration
DATABASE_URL=postgresql://username:password@localhost:5432/aisha_db

# Google Gemini API
GEMINI_API_KEY=your_gemini_api_key_here

# WhatsApp Business API
WHATSAPP_TOKEN=your_whatsapp_business_token
WHATSAPP_APP_SECRET=your_whatsapp_app_secret
WEBHOOK_VERIFY_TOKEN=your_secure_random_token

# Server Configuration
HOST=0.0.0.0
PORT=8000
```

### Environment Variables Template

Create `.env.example` for other developers:

```
DATABASE_URL=postgresql://user:password@localhost:5432/aisha_db
GEMINI_API_KEY=your_api_key_here
WHATSAPP_TOKEN=your_token_here
WHATSAPP_APP_SECRET=your_secret_here
WEBHOOK_VERIFY_TOKEN=your_verify_token_here
HOST=0.0.0.0
PORT=8000
```

⚠️ **Never commit the `.env` file to version control!**

## Project Structure

```
Aisha_backend/
├── main.py                 # FastAPI application entry point
├── database.py             # Database configuration and session management
├── models.py               # SQLAlchemy models
├── requirements.txt        # Project dependencies
├── .env.example            # Environment variables template
├── .gitignore              # Git ignore file
├── README.md               # This file
├── service/
│   └── api_service.py      # External API calls (Gemini, WhatsApp)
└── migrations/             # Alembic database migrations (optional)
```

## Database Configuration

### Features

- **Connection Pooling** - Improves performance with connection reuse
- **Automatic Reconnection** - Handles connection failures gracefully
- **PostgreSQL Driver** - Uses psycopg2 for PostgreSQL connections
- **Security** - Credentials stored in environment variables

### Setup PostgreSQL

```bash
# Create database
createdb aisha_db

# Update DATABASE_URL in .env with your credentials
```

### Run Migrations

```bash
# Create tables
python -c "from database import Base, engine; Base.metadata.create_all(bind=engine)"
```

## API Endpoints

### 1. Health Check

```http
GET /
```

**Response:**
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
  "username": "John Doe",
  "phone_number": "0712345678"
}
```

**Response:**
```json
{
  "message": "Added to waiting list",
  "id": 1
}
```

**Phone Number Formats:**
- `0712345678` (local format)
- `+254712345678` (international format)
- `254712345678` (country code format)

### 3. Gemini AI Response

```http
POST /gemini
Content-Type: application/json

{
  "prompt": "What is machine learning?"
}
```

**Response:**
```json
{
  "response": "Machine learning is a subset of artificial intelligence..."
}
```

### 4. WhatsApp Webhook (Verification)

```http
GET /webhook/whatsapp?hub.mode=subscribe&hub.challenge=CHALLENGE&hub.verify_token=TOKEN
```

### 5. WhatsApp Webhook (Receive Messages)

```http
POST /webhook/whatsapp
```

## WhatsApp Integration

### Setup Steps

1. **Create Meta Developer Account**
   - Visit: https://developers.facebook.com/
   - Create a WhatsApp Business App

2. **Configure Webhook**
   - Set Webhook URL: `https://your-domain/webhook/whatsapp`
   - Set Verify Token: Use value from `.env` file
   - Subscribe to: `messages`, `message_status`

3. **Obtain Credentials**
   - Phone Number ID
   - Business Account ID
   - Access Token (WhatsApp Token)
   - App Secret

4. **Test with ngrok (Development)**

```bash
# Install ngrok
# Run your FastAPI app
uvicorn main:app --reload

# In another terminal
ngrok http 8000
```

Use the ngrok URL for your webhook configuration.

## Error Handling

### Exception Types Handled

| Exception | Status Code | Response |
|-----------|------------|----------|
| `ValidationError` | 422 | Validation error details |
| `HTTPStatusError` | 500 | HTTP error from external API |
| `HTTPException` | 400/500 | Generic HTTP exceptions |
| `General Exception` | 500 | Unexpected server error |

### Try-Except Best Practices

✅ **Catch Specific Exceptions First**
```python
try:
    # code
except ValueError as e:
    # Handle specific error
except Exception as e:
    # Handle general error
```

✅ **Use Finally for Cleanup**
```python
try:
    # code
finally:
    # Cleanup resources
    db.close()
```

✅ **Log Errors**
```python
import logging
logging.error(f"Error occurred: {str(e)}")
```

## Best Practices

### Security

- ✅ Use environment variables for sensitive data
- ✅ Validate all user inputs
- ✅ Implement webhook signature verification
- ✅ Use HTTPS in production
- ✅ Never log sensitive information

### Performance

- ✅ Use connection pooling
- ✅ Implement caching where appropriate
- ✅ Use async/await for I/O operations
- ✅ Add request timeouts

### Code Quality

- ✅ Follow PEP 8 style guide
- ✅ Use type hints
- ✅ Write docstrings for functions
- ✅ Handle errors gracefully
- ✅ Keep functions focused and small

## Development

### Running Locally

```bash
# Activate virtual environment
source venv/bin/activate

# Run with hot reload
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Application will be available at http://localhost:8000
```

### Interactive API Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Installing Dependencies

```bash
# Add a new package
pip install package_name

# Update requirements.txt
pip freeze > requirements.txt
```

## Deployment

### Production Checklist

- [ ] Set `DEBUG=False`
- [ ] Use strong secret keys
- [ ] Configure HTTPS/SSL
- [ ] Set up proper logging
- [ ] Use a production WSGI server (Gunicorn, Uvicorn)
- [ ] Enable CORS for specific domains only
- [ ] Set up database backups
- [ ] Monitor application performance
- [ ] Implement rate limiting
- [ ] Set up error tracking (Sentry, etc.)

### Deploy with Gunicorn

```bash
pip install gunicorn
gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
```

### Environment Variables in Production

Store sensitive data using:
- AWS Secrets Manager
- Azure Key Vault
- HashiCorp Vault
- Environment variable services

## Troubleshooting

### Database Connection Issues

```bash
# Test PostgreSQL connection
psql -h localhost -U username -d aisha_db
```

### WhatsApp Webhook Not Receiving Messages

- Verify webhook URL is publicly accessible
- Check verify token matches configuration
- Ensure webhook is subscribed to `messages` field
- Check application logs for errors

### Gemini API Errors

- Verify API key is valid
- Check API quota limits
- Ensure correct model name and endpoint

## Support

For issues or questions:
1. Check the troubleshooting section
2. Review error logs
3. Open an issue on GitHub

## License

[Add your license here]

## Contributors

[Add contributor information]

from typing import Generic, Literal, TypeVar, Any
from pydantic import BaseModel
from abc import ABC, abstractmethod

# Define a generic type variable
T = TypeVar("T")

# The Resource protocol defines the required structure.
# We use an abstract class to ensure subclasses implement the 'status' and 'data' properties.
# Literal is used for type-checking to enforce specific string values for the status.
class ResourceProtocol(ABC, Generic[T]):
    @property
    @abstractmethod
    def status(self) -> Literal["success", "failure", "loading"]:
        ...

    @property
    @abstractmethod
    def data(self) -> T | None:
        ...

class Loading(BaseModel, ResourceProtocol[Any]):
    status: Literal["loading"] = "loading"
    data: None = None

class Success(BaseModel, ResourceProtocol[T]):
    status: Literal["success"] = "success"
    data: T

class Failure(BaseModel, ResourceProtocol[Any]):
    status: Literal["failure"] = "failure"
    data: None = None
    error: str
