from sqlalchemy import Table, Column, Integer, String, ForeignKey
from web.database import Base
from web.database import init_db
from web.database import db_session


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(100),nullable=False)
    age = Column(Integer)
    height = Column(Integer)
    weight = Column(Integer)

    def __init__(self, name=None, age=None, height=None, weight=None):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def __repr__(self):
        return f'<User {self.name!r}>'



