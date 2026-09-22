# KZ E-Sports Platform API 🎮

A RESTful API service built with FastAPI for managing a registry and statistics of esports athletes in Kazakhstan. This project serves as a backend platform to track gamers, their main disciplines, and performance metrics.

*Currently in active development (MVP stage: 50-70% complete).*

!! Please pay attention. This project has some issues(bugs) !!

## 🚀 Tech Stack

**Backend:**
*   **Framework:** Python 3, FastAPI, Uvicorn
*   **ORM / Database:** SQLAlchemy, PostgreSQL (via `asyncpg`), Supabase
*   **Caching & Performance:** Redis
*   **Authentication:** JWT (via `authx`)
*   **Validation:** Pydantic

**Infrastructure & DevOps:**
*   Docker & Docker Compose
*   Kubernetes (K8s manifests for pods, services, and deployments)

**Frontend:**
*   React / TypeScript (Vite) - *Minimal integration for MVP*

## 🏗️ Architecture & Project Structure

The project follows a modular monolithic architecture, easily adaptable for microservices:

```text
├── app/
│   ├── api/          # API routers and endpoints (e.g., gamers.py)
│   ├── core/         # Core configurations, Redis setup, Security
│   ├── db/           # Database sessions and engine initialization
│   ├── models/       # SQLAlchemy database models
│   ├── schemas/      # Pydantic models for data validation
│   └── services/     # Business logic and caching services
├── frontend/         # Minimal Vite-based frontend
├── kuber/            # Kubernetes deployment manifests
├── Dockerfile
├── docker-compose.yaml
└── requirements.txt
```

## 🔌 Core API Endpoints

### Gamers Management
*   `POST /gamers/setup` - Initialize database tables.
*   `POST /gamers/` - Register a new esports athlete. Automatically invalidates the Redis cache.
*   `GET /gamers/` - Fetch the list of gamers (Optimized with Redis caching).

### Authentication
*   `POST /gamers/login` - Authenticate user and issue JWT token via HTTP-only cookies.
*   `GET /gamers/protected` - Example endpoint requiring JWT authorization.

## 🛠️ Local Development Setup

**1. Clone the repository and set up environment variables:**
Create a `.env` file in the root directory based on your PostgreSQL and Redis configurations.

**2. Run with Docker Compose (Recommended):**
```bash
docker-compose up -d --build
```

**3. Run manually:**
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## ☸️ Kubernetes Deployment

The project includes K8s manifests in the `/kuber` directory for scalable deployment:
*   `myapp-backend-pod.yaml` & `myapp-backend-service.yaml`
*   `myapp-redis-deploy.yaml`
*   `myapp-frontend-deploy.yaml` (here's not all the Deployment and Service manifests) 
