"""
Database module
"""
from peewee import *
from config.settings import DATABASE

print(DATABASE)

database = MySQLDatabase(
    DATABASE["name"],
    user=DATABASE["user"],
    passwd=DATABASE["password"],
    host=DATABASE["host"],
    port=DATABASE["port"],
)


class UserModel(Model):
    """
    Class representing the user model.

    Attributes:
        id (int): Unique identifier for the user.
        name (str): Name of the user.
        email (str): email of the user.
        password (str): password of the user.
        account_type (str): account type of the user (individual/family)
        role (str): role of the user (admin/member)
    """
    id = AutoField(primary_key=True)
    username = CharField(max_length=50)
    email = CharField(max_length=100)
    password = CharField(max_length=100)
    account_type = CharField(max_length=50)
    role = CharField(max_length=50)

    class Meta: # pylint: disable=too-few-public-methods
        """
        Configuration for the UserModel class.

        Attributes:
            database: Database used.
            table_name: Name of the table in the database.
        """

        database = database
        table_name = "users"
