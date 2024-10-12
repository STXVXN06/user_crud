"""
This module defines the User class that represents an user with its ID, name, email, 
password, account_type, role.
"""

from pydantic import BaseModel


class User(BaseModel):
    """
    Represents an event with ID, name, email, password, account_type, role.

    Attributes:
        id (int): Unique identifier for the user.
        name (str): Name of the user.
        email (str): email of the user.
        password (str): password of the user.
        account_type (str): account type of the user (individual/family)
        role (str): role of the user (admin/member)
    """

    id: int
    name: str
    email: str
    password: str
    account_type: str
    role: str
