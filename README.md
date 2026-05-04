# Production-Ready E-commerce Backend

Scalable backend system for an e-commerce platform built using FastAPI.

## Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy
- Redis
- JWT Authentication
- Alembic
- Docker

## Features

- Secure authentication using JWT
- Role-based access control
- Product catalog and inventory
- Shopping cart system
- Order processing
- Redis caching for optimized product queries
- Background order processing

## Run Project

Install dependencies

pip install -r requirements.txt

Run server

uvicorn app.main:app --reload

## API Documentation

Swagger UI

http://localhost:8000/docs

## Database Migration

alembic revision --autogenerate -m "init"

alembic upgrade head
