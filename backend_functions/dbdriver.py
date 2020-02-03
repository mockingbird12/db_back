from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import Sequence


Base = declarative_base()
engine = create_engine("postgres://postgres:passwd@localhost/db_test")

class Answers(Base):
    __tablename__ = 'answers'
    time = Column(DateTime)
    user_id = Column(Integer)
    module_id = Column(Integer)
    lesson_id = Column(Integer)
    word_id = Column(Integer)
    answer = Column(String)
    author_id = Column(Integer)

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('users_seq'), primary_key=True)
    login = Column(String)
    password = Column(String)
    token = Column(String)
    name = Column(String)
    status = Column(String)
    my_authors = Column(String)
    my_students = Column(String)
    email = Column(String)

class Lessons(Base):
    __tablename__ = 'lessons'
    id = Column(Integer, Sequence('lessons_seq'), primary_key=True)
    module_id = Column(Integer)
    name = Column(String)
    comment = Column(String)
    words = Column(String)
    visible = Column(Boolean)

class Modules(Base):
    __tablename__ = 'modules'
    id = Column(Integer, Sequence('modules_seq'), primary_key=True)
    lang_from = Column(String)
    lang_to = Column(String)
    name = Column(String)
    comment = Column(String)
    visible = Column(Boolean)
    lessons = None
    user_id = Column(Integer)

class Words(Base):
    _tablename__ = 'words'
    id = Column(Integer, Sequence('words_seq'), primary_key=True)
    lesson_id = Column(Integer)
    word = Column(String)
    translate = Column(String)
    comment = Column(String)

Session = sessionmaker(bind=engine)
session = Session()
