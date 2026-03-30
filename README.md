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

```markdown
## API Endpoints

- `/accounts/register/` (POST) – Register a new user
- `/accounts/login/` (POST) – Obtain auth token
- `/accounts/logout/` (POST) – Logout user and delete token
- `/watch/list/` (GET) – List all watchlist items
- `/watch/list/` (POST) – Add a new watchlist item (Admins only)
- `/watch/<id>/` (GET) – Retrieve a specific movie/show
- `/watch/<id>/reviews/` (GET) – List reviews for a movie
- `/watch/<id>/reviews/` (POST) – Add a review for a movie (one per user)
- `/reviews/<id>/` (PUT/PATCH/DELETE) – Update or delete a review (author-only)
- `/reviews/<user_id>/` – List of all reviews done by a user
- `/watch/stream/` – List all streaming services
- `/watch/stream/<id>/` – Detail of a streaming service
