Streaming Site API:
A RESTful API built with Django REST Framework (DRF) for a streaming platform that allows users to view, review, and manage movies and TV shows.
This project demonstrates authentication, authorization, pagination, filtering, throttling, and token-based API access.

Features
[User registration, login, and logout]
Token-based authentication using DRF Authtoken
CRUD operations for Watchlist items (movies/shows)
CRUD operations for Reviews with one review per user per movie
Average rating calculation for movies
Pagination for large datasets
Filtering by author username and review status (active)
Request throttling for review creation
Browsable API interface for easy testing
Tech Stack
Backend: Django, Django REST Framework
Authentication: DRF Token Authentication
Database: SQLite (default), compatible with PostgreSQL/MySQL
Filters & Pagination: DjangoFilterBackend, PageNumberPagination
Testing & API Exploration: Postman / DRF Browsable API /Swagger

API EndPoints:
/admin/ For admin Panel
/accounts/register/	POST	Register a new user
/accounts/login/	POST	Obtain auth token
/accounts/logout/	POST	Logout user and delete token
/watch/list/	GET	List all watchlist items
/watch/list/	POST	Only Admins can add a new watchitem to the site
/watch/<id>/	GET	Retrieve a specific movie/show
/watch/<id>/reviews/	GET	List reviews for a movie
/watch/<id>/reviews/	POST	Add a review for a movie(only one review per user)
/reviews/<id>/	PUT/PATCH/DELETE	Update or delete a review (author-only)
/reviews/<username>/ List of all reviews done by a user
/watch/stream/	List of all available Streaming Services
/watch/stream/1 	Detail of Streaming Service

Setup Instructions:

Clone the repository:
git clone <repository-url>
cd StreamingSite-DRF-Project

Create a virtual environment:
python -m venv venv
venv\Scripts\activate      # Windows

Install dependencies:
pip install -r requirements.txt

Apply migrations:
python manage.py migrate

Create a superuser (optional):
python manage.py createsuperuser
Run the server
python manage.py runserver
