"""Application settings module."""

import os

# Mandatory env variable, must be predefined in `.env` file.
SECRET_KEY = os.environ['SECRET_KEY']

# SQLAlchemy Database URI
SQLALCHEMY_DATABASE_URI = 'sqlite:////app/sqlite.db'

# FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant
# overhead and will be disabled by default in the future.
SQLALCHEMY_TRACK_MODIFICATIONS = False
