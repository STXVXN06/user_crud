"""
Module that defines the routes for managing users.

This module uses FastAPI to define the routes that allow
creating, reading, updating, and deleting users through a REST API.

Available routes:

- POST /users/: Creates a new user.
- GET /users/{user_id}: Retrieves user information by ID.
- PUT /users/{user_id}: Updates user information.
- DELETE /users/{user_id}: Deletes an user.

Each route uses the UserService to interact with the
business logic related to users.
"""

from services.user_service import UserService
from models.user import User
from fastapi import APIRouter, HTTPException


user_router = APIRouter()


@user_router.post("/users/", response_model=User)
def create_user(name: str, email: str, password: str, account_type: str, role: str) -> User:
    """
    Create a new user.

    Args:
        name (str): Name of the user.
        email (str): email of the user.
        password (str): password of the user.
        account_type (str): account type of the user (individual/family)
        role (str): role of the user (admin/member)

    Returns:
        User: The created user.
    """
    user = UserService.create_user(name, email, password, account_type, role)
    return user


@user_router.get("/users/{user_id}", response_model=User)
def get_user(user_id: int) -> User:
    """
    Retrieve user information by ID.

    Args:
        user_id (int): The ID of the user to retrieve.

    Returns:
        User: The user with the specified ID.

    Raises:
        HTTPException: If the user is not found.
    """
    user = UserService.get_user_by_id(user_id)
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")


@user_router.put("/users/{user_id}", response_model=User)
def update_user(
    user_id: int, name: str = None, email: str = None, password: str = None, account_type: str = None, role: str = None
) -> User:
    """
    Update user information.

    Args:
        user_id (int): Unique identifier for the user.
        name (str): Name of the user.
        email (str): email of the user.
        password (str): password of the user.
        account_type (str): account type of the user (individual/family)
        role (str): role of the user (admin/member)

    Returns:
        User: The updated user.

    Raises:
        HTTPException: If the user is not found.
    """
    user = UserService.update_user(user_id, name, email, password, account_type, role)
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")


@user_router.delete("/users/{user_id}")
def delete_user(user_id: int) -> dict:
    """
    Delete an user by ID.

    Args:
        user_id (int): The ID of the user to delete.

    Returns:
        dict: A confirmation message if the user was deleted.

    Raises:
        HTTPException: If the user is not found.
    """
    if UserService.delete_user(user_id):
        return {"message": "User deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")
