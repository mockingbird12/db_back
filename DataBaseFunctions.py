from dbdriver import session
from dbdriver import Users
from dbdriver import Modules
from dbdriver import Lessons
from dbdriver import Words
from dbdriver import Answers


def AddUser(login,password,name,status):
    token = None
    my_authors = None
    my_students = None
    email = None
    user = Users(login, password, token , name, status, my_authors, my_students, email)
    session.add(user)
    session.commit()


def GetAllUsers():
    return session.query(Users).all()


def GetUserInfoBy(id):
    user = session.query(Users).filter(Users.id == id).one()
    return user


def GetUserNameBy(user_id):
    user = session.query(Users).filter(Users.id == user_id).one()
    return user.name


def GetAuthorModulesByLang(lang_from, lang_to, user_id):
    res = session.query(Modules).filter(Modules.lang_from == lang_from).filter(Modules.lang_to == lang_to).filter(Modules.user_id == user_id)
    return res.id


def AddModule(lang_from, lang_to, name, comment, visible, lessons, user_id, students_ids):
    module = Modules(lang_from, lang_to, name, comment, visible, lessons, user_id, students_ids)
    session.add(module)
    session.commit()


def DeleteModule(module_id, user_id):
    # Зачем нам здесь user_id???
    module = session.query(Modules).filter(Modules.id == module_id).filter(Users.id == user_id).one()
    session.delete(module)
    session.commit()


def ChangeModuleName(module_id, new_name):
    modulle = session.query(Modules).filter(Modules.id == module_id).one()
    modulle.name = new_name
    session.add(modulle)
    session.commit()


def AddModuleForStudents(lang_from, lang_to, name, comment, visible, lessons, user_id, students_ids):
    # это я не понимаю зачем и как
    module = Modules(lang_from, lang_to, name, comment, visible, lessons, user_id, students_ids)
    pass

def UpdateModuleComment(module_id,comment):
    module = session.query(Modules).filter(Modules.id == module_id).one()
    module.comment = comment
    session.add(module)
    session.commit()


def GetModuleLessons(module_id):
    lessons = session.query(Modules).filter(Modules.id == module_id).all()
    res = []
    for lesson in lessons:
        res.append(lesson.id)
    return res


def AddLesson(module_id, name, comment,  visible):
    lesson = Lessons(module_id, name, comment, visible)
    session.add(lesson)
    session.commit()


def DeleteLesson(lesson_id):
    lesson = session.query(Lessons).filter(Lessons.id == lesson_id)
    session.delete(lesson)
    session.commit()


def ChangeLessonName(lesson_id,new_name):
    lesson = session.query(Lessons).filter(Lessons.id == lesson_id)
    lesson.name = new_name
    session.add(lesson)
    session.commit()

def UpdateLessonComment(lesson_id,comment):
    # Мне кажется лучше не плодить функции с одинаковым функционалом а объединить их под одной функцией
    lesson = session.query(Lessons).filter(Lessons.id == lesson_id)
    lesson.comment = comment
    session.add(lesson)
    session.commit()


def GetLessonWords(lesson_id):
    words = session.query(Words).filter(Words.lesson_id == lesson_id).all()
    res = []
    for word in words:
        res.append(word.word)
    return res


def AddWord(lesson_id, word, translate, comment):
    word = Words(lesson_id, word, translate, comment)
    session.add(word)
    session.commit()


def DeleteWord(word_id):
    word = session.query(Words).filter(Words.id == word_id).one()
    session.delete(word)
    session.commit()


def ChangeWord(word_id,word,translate):
    word_instance = session.query(Words).filter(Words.id == word_id).one()
    word_instance.word = word
    word_instance.translate = translate
    session.add(word_instance)
    session.commit()

def UpdateWordComment(word_id,comment):
    word_instance = session.query(Words).filter(Words.id == word_id).one()
    word_instance.comment = comment
    session.add(word_instance)
    session.commit()


def AddNewAnswer(answer_time, user_id, module_id, lesson_id, word_id, answer,author_id):
    answer_inst = Answers(answer_time, user_id, module_id, lesson_id, word_id, answer,author_id)
    id = answer_inst.id
    session.add(answer_inst)
    session.commit()
    return id


def GetAllUserAnswers(user_id):
    answers = session.query(Answers).filter(Answers.user_id == user_id).all()
    res = []
    for ans in answers:
        res.append(ans.answer)
    return res


def GetLessonAnswers(user_id,lesson_id):
    answers = session.query(Answers).filter(Answers.user_id == user_id).filter(Answers.lesson_id == lesson_id).all()
    res = []
    for ans in answers:
        res.append(ans.answer)
    return res

def GetAllSearchAuthors():
    author_inst = session.query(Users).filter(Users.status == 'author').all()
    return author_inst

if __name__ == '__main__':
    print('Run db functions')
    print('AddUser:')
    AddUser('login1', 'passwd1', 'user1', 'status1')
    # print('GetAllUsers')
    # print(GetAllUsers())
    # print('Get user by id')
    # print(GetUserInfoBy(1))
    # print('GetUserNameBy')
    # print(GetUserNameBy(1))
    # print('GetAuthorModulesByLang')
    # print(GetAuthorModulesByLang())
    # print('AddModule')
    # AddModule('eng','france','module1','comment',True,1)
    # print('AddModuleForStudents')
    AddModuleForStudents('eng','france','module1','comment',True,1, 2, 1)
    # print('DeleteModule')
    # DeleteModule(2, 1)
    # print('ChangeModuleName')
    # ChangeModuleName(3, 'new_name_1')
    # print('UpdateModuleComment')
    # UpdateModuleComment(3, 'new_comment')
    # print('GetModuleLessons')
    # print(GetModuleLessons(3))
    # print('AddLesson')
    # AddLesson(3, 'lesson3', 'comment3', True)
    # print('DeleteLesson')
    # DeleteLesson(4)
    # print('ChangeLessonName')
    # ChangeLessonName(4, 'new_name_4')
    # print('UpdateLessonComment')
    # UpdateLessonComment(4, 'new_comment')
    # print('GetLessonWords')
    # print(GetLessonWords(4))
    # print('AddWord')
    # AddWord(4, 'new_word_jdi', 'perevod', 'comment')
    # print('DeleteWord')
    # DeleteWord(2)
    # print('ChangeWord')
    # ChangeWord(2, 'change_word', 'change_perevod')
    # print('UpdateWordComment')
    # UpdateWordComment(2, 'new_comment')
    # print('AddNewAnswer')
    # print(AddNewAnswer('Sep 2', 1, 2, 2, 2, 'ans1', 2))
    # print('GetAllUserAnswers')
    # print(GetAllUserAnswers(3))
    # print('GetLessonAnswers')
    # print(GetLessonAnswers(3, 2))
    # print('GetAllSearchAuthors')
    # print(GetAllSearchAuthors())


