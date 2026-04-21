from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base


class Actor(Base):
    __tablename__ = "actors"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    nationality = Column(String)
    bio = Column(String)


class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)

    actor_id = Column(Integer, ForeignKey("actors.id"))