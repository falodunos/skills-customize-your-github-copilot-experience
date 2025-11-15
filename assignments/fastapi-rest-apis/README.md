# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build modern, production-ready REST APIs using the FastAPI framework. You'll create a web service with multiple endpoints, request validation, and proper HTTP status codes while practicing backend development fundamentals.

## 📝 Tasks

### 🛠️ Create a Task Management API

#### Description
Build a REST API for managing tasks using FastAPI. Implement endpoints for creating, reading, updating, and deleting tasks. Use Pydantic models for request validation and store tasks in memory (or optionally in a database).

#### Requirements
Completed program should:

- Create a FastAPI application with proper routing and endpoint structure
- Implement GET endpoint to retrieve all tasks or a specific task by ID
- Implement POST endpoint to create new tasks with validation
- Implement PUT endpoint to update existing tasks
- Implement DELETE endpoint to remove tasks
- Use appropriate HTTP status codes (200, 201, 404, etc.)
- Return JSON responses with proper data formatting


### 🛠️ Add Advanced Features

#### Description
Enhance your Task Management API with filtering, pagination, and error handling. Implement query parameters for filtering and sorting tasks, add comprehensive error messages, and document your API.

#### Requirements
Completed program should:

- Support query parameters for filtering tasks (by status, priority, etc.)
- Include pagination for retrieving tasks (limit and offset parameters)
- Handle and return meaningful error messages for invalid requests
- Include API documentation (use FastAPI's automatic Swagger UI)
- Validate input data using Pydantic models with type hints
- Use proper request/response models for type safety
