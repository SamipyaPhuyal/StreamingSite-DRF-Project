# Streaming Site API

A RESTful API built with Django REST Framework (DRF) for a streaming platform that allows users to view, review, and manage movies and TV shows. Demonstrates authentication, authorization, pagination, filtering, throttling, and token-based API access.

## Features
- User registration, login, and logout
- Token-based authentication using DRF Authtoken
- CRUD operations for Watchlist items (movies/shows)
- CRUD operations for Reviews (one review per user per movie)
- Average rating calculation for movies
- Pagination for large datasets
- Filtering by author username and review status (`active`)
- Request throttling for review creation
- Browsable API interface for easy testing

## Tech Stack
- **Backend:** Django, Django REST Framework
- **Authentication:** DRF Token Authentication
- **Database:** SQLite (default), compatible with PostgreSQL/MySQL
- **Filters & Pagination:** DjangoFilterBackend, PageNumberPagination
- **Testing & API Exploration:** Postman / DRF Browsable API / Swagger

## Setup Instructions
```bash
--git clone <repository-url>
--cd StreamingSite-DRF-Project
--python -m venv venv
--venv\Scripts\activate  # Windows
--pip install -r requirements.txt
--python manage.py migrate
--python manage.py createsuperuser  # Optional
--python manage.py runserver
