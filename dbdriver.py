from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Boolean
from sqlalchemy import Text
from sqlalchemy import Sequence


user = 'new_memo'
passwd = '111111'
host = 'localhost'
dbname = 'new_memo'
Base = declarative_base()
engine = create_engine("postgresql://{0}:{1}@{2}/{3}".format(user,passwd,host, dbname))

class Answers(Base):
    __tablename__ = 'answers'
    id = Column(Integer, Sequence('answers_seq'), primary_key=True)
    time = Column(Text)
    user_id = Column(Integer)
    module_id = Column(Integer)
    lesson_id = Column(Integer)
    word_id = Column(Integer)
    answer = Column(Text)
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
    login = Column(Text, unique=True)
    password = Column(Text)
    token = Column(Text, unique=True)
    name = Column(Text)
    status = Column(Text)
    my_authors = Column(Text)
    my_students = Column(Text)
    email = Column(Text)

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
    name = Column(Text)
    comment = Column(Text)
    words = Column(Text)
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
    lang_from = Column(Text)
    lang_to = Column(Text)
    name = Column(Text)
    comment = Column(Text)
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
    word = Column(Text)
    translate = Column(Text)
    comment = Column(Text)

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
