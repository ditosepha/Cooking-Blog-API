# Cooking Blog API

Welcome to the Cooking Blog API repository! This project serves as a RESTful API for a local Cooking Blog, 
allowing users to discover, share, and rate dishes. The API provides endpoints for user registration, 
managing dishes, chef profiles, ingredients, and ratings.

## Features

- **Authentication**: Token-based authentication system for user registration and login.
- **Meal Management**: CRUD operations for adding, searching, updating, and deleting dishes.
- **Chef Profiles**: Users can create chef profiles with culinary backgrounds and specialties.
- **Ingredients**: Ability to manage ingredients for each dish.
- **Ratings**: Users can rate dishes on a 5-point scale.
- **Filtering**: The API supports filtering dishes based on parameters such as name.
- **Permissions**: Custom permission classes ensure that users can only perform certain actions based on their roles. For example, chefs can only edit their own dishes, and authenticated users can rate dishes but not modify them.

- ## Usage

Once the server is running, you can access the API endpoints using tools like cURL or Postman. Here are some example endpoints:

- **Register a new user**: `POST /api/users/`
- **Log in to get an authentication token**: `POST /api/token-auth/`
- **Create a new dish**: `POST /api/dishes/`
- **Retrieve a list of dishes**: `GET /api/dishes/`

## Permissions

The Culinary Guide API implements custom permission classes to enforce access control. Here are some key permissions:

- **IsChefOrReadOnly**: Only chefs can create, update, or delete dishes. Other users have read-only access.
- **IsAuthenticatedOrReadOnly**: Authenticated users can perform read operations, but only chefs can modify data.
