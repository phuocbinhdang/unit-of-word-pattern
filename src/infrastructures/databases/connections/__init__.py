from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from infrastructures.configurations.database import DatabaseConfiguration


Session = scoped_session(
    sessionmaker(create_engine(DatabaseConfiguration.DATABASE_URL_WRITE))
)
