# Django RESTful API with JWT Authentication

This project demonstrates how to set up a **Django REST API** with **JWT (JSON Web Token)** authentication, allowing users to log in and access protected API endpoints. It includes an API for managing books, and the endpoints support CRUD operations (Create, Read, Update, Delete).

## Features

- **Django REST framework** for building APIs.
- **JWT Authentication** for secure user login and access control.
- **Books API** as an example of a protected resource.
- **Register User API** to allow users to sign up.
- **Token-based authentication** using `SimpleJWT`.

## What I Have Done

- **Created a Django project** and an app for managing books with Django REST framework.
- Implemented **JWT authentication** using `djangorestframework-simplejwt` to protect API endpoints.
- Created multiple endpoints to interact with the books resource:
  - **List books** (GET)
  - **Add a new book** (POST)
  - **Update an existing book** (PUT)
  - **Delete a book** (DELETE)
- **User registration** endpoint for creating a new user.
- Used **Postman** to test the API, including obtaining JWT tokens, and performing authenticated CRUD operations (GET, POST, PUT, DELETE) on books.
- **Secured the book data** API with authentication, ensuring that only logged-in users with valid JWT tokens can access and modify the data.

© 2024 Engr. Mohammad Salman. All rights reserved.
