"""
Task Management API with FastAPI

This is a starter template for building a REST API using FastAPI.
Follow the requirements in README.md to complete the assignment.
"""

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="Task Management API")

# TODO: Define a Pydantic model for Task with fields like id, title, description, status, priority


# TODO: Create a list to store tasks in memory
# tasks = []


# TODO: Implement GET endpoint to retrieve all tasks
# GET /tasks


# TODO: Implement GET endpoint to retrieve a specific task by ID
# GET /tasks/{task_id}


# TODO: Implement POST endpoint to create a new task
# POST /tasks


# TODO: Implement PUT endpoint to update a task
# PUT /tasks/{task_id}


# TODO: Implement DELETE endpoint to delete a task
# DELETE /tasks/{task_id}


# Optional: Add query parameters for filtering and pagination
# - Support filtering by status, priority, etc.
# - Add limit and offset for pagination


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
