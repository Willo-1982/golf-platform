# /fastapi-backend/models.py
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Text, Table
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

# Many-to-many table for group memberships
group_members = Table(
    "group_members", Base.metadata,
    Column("group_id", Integer, ForeignKey("groups.id")),
    Column("user_id", Integer, ForeignKey("users.id"))
)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    name = Column(String)

    rounds = relationship("Round", back_populates="owner")
    groups = relationship("Group", secondary=group_members, back_populates="members")
    friends = relationship("Friend", back_populates="owner")

class Friend(Base):
    __tablename__ = "friends"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    friend_email = Column(String)

    owner = relationship("User", back_populates="friends")

class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    owner_user_id = Column(Integer, ForeignKey("users.id"))
    members = relationship("User", secondary=group_members, back_populates="groups")

class Round(Base):
    __tablename__ = "rounds"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    date = Column(DateTime(timezone=True), server_default=func.now())
    course_name = Column(String)
    score = Column(Integer)
    differential = Column(Float)
    sg_tee = Column(Float, default=0)
    sg_approach = Column(Float, default=0)
    sg_putting = Column(Float, default=0)
    video_url = Column(Text, nullable=True)

    owner = relationship("User", back_populates="rounds")
