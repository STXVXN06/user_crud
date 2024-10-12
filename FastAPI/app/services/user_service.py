"""
Service layer for User operations.

This module contains the business logic for managing users.
It interacts with the UserModel from the database and uses
the User Pydantic model for data validation.
"""

from typing import Optional
from datetime import datetime
from peewee import DoesNotExist
from config.database import UserModel
from models.user import User


class UserService:
    """Service layer for User operations."""

    @staticmethod
    def create_user(name: str = None, email: str = None, password: str = None,
                    account_type: str = None, role: str = None) -> User:
        """
        Create a new user.

        Args:    
            name (str): Name of the user.
            email (str): email of the user.
            password (str): password of the user.
            account_type (str): account type of the user (individual/family)
            role (str): role of the user (admin/member)

        Returns:
            User: The created user instance as a Pydantic model.
        """
        user_instance = UserModel.create(
            name=name, email=email, password=password, account_type=account_type, role=role
        )
        return User(
            id=user_instance.id,
            usarname=user_instance.username,
            email=user_instance.email,
            password=user_instance.password,
            account_type=user_instance.account_type,
            role=user_instance.role
        )

    @staticmethod
    def get_user_by_id(user_id: int) -> Optional[User]:
        """
        Retrieve an user by ID.

        Args:
            user_id (int): The ID of the user to retrieve.

        Returns:
            Optional[user]: The user instance as a Pydantic model if found, else None.
        """
        try:
            user_instance = UserModel.get_by_id(user_id)
            return User(
                id=user_instance.id,
                name=user_instance.name,
                email=user_instance.email,
                password=user_instance.password,
                account_type=user_instance.account_type,
                role=user_instance.role
            )
        except DoesNotExist:
            return None

    @staticmethod
    def update_user(
        user_id: int,
        name: Optional[str] = None,
        email: Optional[datetime] = None,
        password: Optional[str] = None,
        account_type: Optional[str] = None,
        role: Optional[str] = None,
    ) -> Optional[User]:
        """
        Update an existing user by ID.

        Args:
            user_id (int): The ID of the user to update.
            name (Optional[str]): The new name of the user.
            email (Optional[datetime]): The new email of the user.
            password (Optional[str]): The new password of the user.
            account_type (Optional[str]): The new account type of the user.
            role (Optional[str]): The new role of the user.

        Returns:
            Optional[User]: The updated user instance as a Pydantic model if successful,
            else None.
        """
        try:
            user_instance = UserModel.get_by_id(user_id)
            if name:
                user_instance.name = name
            if email:
                user_instance.email = email
            if password:
                user_instance.password = password
            if account_type:
                user_instance.account_type = account_type
            if role:
                user_instance.role = role
            user_instance.save()  # Save changes to the database

            return User(
                id=user_instance.id,
                name=user_instance.name,
                email=user_instance.email,
                password=user_instance.password,
                account_type=user_instance.account_type,
                role=user_instance.role
            )
        except DoesNotExist:
            return None

    @staticmethod
    def delete_user(user_id: int) -> bool:
        """
        Delete an user by ID.

        Args:
            user_id (int): The ID of the user to delete.

        Returns:
            bool: True if the user was deleted, else False.
        """
        try:
            user_instance = UserModel.get_by_id(user_id)
            user_instance.delete_instance()
            return True
        except DoesNotExist:
            return False
