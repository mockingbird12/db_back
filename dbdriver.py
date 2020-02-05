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
engine = create_engine("postgresql://memo_back:111111@localhost/memo_db")

class Answers(Base):
    __tablename__ = 'answers'
    id = Column(Integer, Sequence('answers_seq'), primary_key=True)
    time = Column(DateTime)
    user_id = Column(Integer)
    module_id = Column(Integer)
    lesson_id = Column(Integer)
    word_id = Column(Integer)
    answer = Column(String)
    author_id = Column(Integer)

    def __init__(self, time, user_id, module_id, lesson_id, word_id, answer, author_id):
        self.time = time
        self.user_id = user_id
        self.module_id = module_id
        self.lesson_id = lesson_id
        self.word_id = word_id
        self.answer = answer
        self.author_id = author_id

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

    def __init__(self, login, password,token,name,status, my_authors, my_students, email):
        self.login = login
        self.password = password
        self.token = token
        self.name = name
        self.status = status
        self.my_authors = my_authors
        self.my_students = my_students
        self.email = email

class Lessons(Base):
    __tablename__ = 'lessons'
    id = Column(Integer, Sequence('lessons_seq'), primary_key=True)
    module_id = Column(Integer)
    name = Column(String)
    comment = Column(String)
    words = Column(String)
    visible = Column(Boolean)

    def __init__(self, module_id, name, comment, words, visible):
        self.module_id = module_id
        self.name = name
        self.comment = comment
        self.words = words
        self.visible = visible

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
    student_ids = None

    def __init__(self, lang_from, lang_to, name, comment, visible, lessons, user_id, students_ids):
        self.lang_from = lang_from
        self.lang_to = lang_to
        self.name = name
        self.comment = comment
        self.visible = visible
        self.lessons = lessons
        self.user_id = user_id
        self.student_ids = students_ids

class Words(Base):
    __tablename__ = 'words'
    id = Column(Integer, Sequence('words_seq'), primary_key=True)
    lesson_id = Column(Integer)
    word = Column(String)
    translate = Column(String)
    comment = Column(String)

    def __init__(self, lesson_id, word, translate, comment):
        self.lesson_id = lesson_id
        self.word = word
        self.translate = translate
        self.comment = comment

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


if __name__ == '__main__':
    word = Words(2, 'hello', 'translate', 'comm1')
    session.add(word)
    session.commit()
