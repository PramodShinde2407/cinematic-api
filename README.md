# Cinematic API - Movie Review & Rating Platform

A modern, feature-rich REST API built with FastAPI for discovering movies, reading reviews, and managing user ratings. Cinematic API provides seamless integration with movie databases and user authentication, enabling developers to build interactive movie discovery applications.

## 🎬 Key Features

### **Movie Discovery**
- 🔍 Search movies by name with real-time results
- 📊 Retrieve detailed movie information (release date, genres, budget, revenue, ratings)
- 💾 Access comprehensive movie metadata stored in PostgreSQL
- 📈 Movie information caching for optimal performance

### **Review Management**
- ⭐ Post and retrieve user reviews with ratings
- 👥 Support for both user-generated and external reviews
- 🕐 Track review timestamps and sources
- 📝 Full review history and analytics

### **User Authentication**
- 🔐 Secure user registration and authentication
- 🔑 JWT-based token authentication
- 🛡️ Role-based access control
- 🔒 Password security with hashing and verification

### **RESTful API**
- ✅ Well-documented endpoints with Swagger UI
- 📋 Request/Response validation with Pydantic
- ⚡ Async/await for high performance
- 🔄 CORS support for cross-origin requests

## 🛠 Tech Stack

| Component | Technology |
|-----------|-----------|
| **Framework** | FastAPI 0.95+ |
| **Database** | PostgreSQL |
| **ORM** | SQLAlchemy |
| **Authentication** | JWT (python-jose) |
| **Password Hashing** | Passlib |
| **Environment Config** | python-dotenv |
| **Language** | Python 3.8+ |

## 📁 Project Structure

```
cinematic-api/
├── core/
│   └── security.py              # JWT token generation and validation
├── crud/                         # CRUD operations (if needed)
├── database/
│   ├── __init__.py
│   ├── base.py                  # SQLAlchemy Base model
│   ├── connection.py            # Database engine configuration
│   └── session.py               # Session management
├── middleware/                  # Custom middleware
├── models/
│   ├── __init__.py
│   ├── movie.py                 # Movie database model
│   ├── reviews.py               # Reviews database model
│   └── user.py                  # User database model
├── routes/
│   ├── __init__.py
│   ├── auth_routes.py           # Authentication endpoints
│   ├── movies_routes.py         # Movie endpoints
│   ├── registration_route.py    # User registration endpoints
│   └── reviews_routes.py        # Review endpoints
├── schema/
│   ├── __init__.py
│   ├── movie.py                 # Movie request/response schemas
│   ├── reviews.py               # Reviews request/response schemas
│   ├── userIn.py                # User input schema
│   └── userOut.py               # User output schema
├── services/
│   ├── auth_service.py          # Authentication business logic
│   ├── movie_details.py         # Movie details service
│   ├── movie_list.py            # Movie listing service
│   └── reviews.py               # Review service logic
├── utils/
│   └── security.py              # Password hashing utilities
├── config/                      # Configuration files
├── main.py                      # Application entry point
├── test.py                      # Test suite
├── requirements.txt             # Project dependencies
├── .env.example                 # Environment variables template
└── README.md                    # This file
```

## 🚀 Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:
- **Python** 3.8 or higher
- **PostgreSQL** 12 or higher
- **pip** (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/cinematic-api.git
   cd cinematic-api
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and configure:
   ```
   DATABASE_URL=postgresql://username:password@localhost:5432/cinematic_db
   SECRET_KEY=your-secret-key-here
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_TIME=30
   ```

5. **Create the database**
   ```bash
   # Using PostgreSQL CLI
   createdb cinematic_db
   ```

6. **Run the application**
   ```bash
   python main.py
   ```
   
   The API will be available at `http://localhost:8000`

### API Documentation

Once the server is running, access the interactive API documentation:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 📚 API Endpoints

### Authentication
- `POST /auth/login` - User login with credentials
- `POST /register` - Register new user account

### Movies
- `GET /movies/search?movie_name=<name>` - Search movies by name
- `GET /movies/details?movie_id=<id>` - Get detailed movie information

### Reviews
- `GET /reviews?movie_id=<id>` - Get all reviews for a movie
- `POST /reviews` - Post a new review
- `GET /reviews/<review_id>` - Get specific review details

## 🔐 Environment Variables

Create a `.env` file in the root directory with the following variables:

```env
# Database Configuration
DATABASE_URL=postgresql://user:password@localhost:5432/cinematic_db

# JWT Configuration
SECRET_KEY=your-super-secret-key-change-in-production
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_TIME=30

# Server Configuration
DEBUG=True
```

**Security Note**: Never commit `.env` file to version control. Use `.env.example` as a template.

## 🧪 Testing

Run the test suite:
```bash
python -m pytest test.py -v
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please ensure:
- Code follows PEP 8 style guidelines
- Tests are included for new features
- Documentation is updated accordinglya

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📧 Contact & Support

- **Author**: Pramod Shinde
- **Email**: pramodshinde2005@gmail.com
- **GitHub**: [@PramodShinde2407](https://github.com/PramodShinde2407)

For issues and feature requests, please open an issue on GitHub.

## 🚦 Roadmap

- [ ] Add movie recommendations based on ratings
- [ ] Implement pagination for large datasets
- [ ] Add movie poster and image support
- [ ] User profile functionality
- [ ] Advanced search filters
- [ ] Rate limiting and caching strategies
- [ ] Docker containerization
- [ ] CI/CD pipeline setup

## 📊 Status

- ✅ Core API functionality
- ✅ Authentication system
- ✅ Database integration
- 🚧 Testing coverage
- 🚧 Performance optimization

---

**Happy Coding! 🎬⭐**
