from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.orm import declarative_base
from datetime import datetime

engine = create_engine('sqlite:///users.db', echo=True)

session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()

"""
    class Post:
    id int
    post str
    date_added datetime
"""


# Create the Post in the Database

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer(), primary_key=True)
    post = Column(String(), nullable=False)
    datetime = Column(DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return f"<Post {self.id}>"


Base.metadata.create_all(bind=engine)
