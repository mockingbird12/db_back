from dbdriver import session
from dbdriver import Users
from dbdriver import Modules
from dbdriver import Lessons
from dbdriver import Words
from dbdriver import Answers


def AddUser(login, password,token,name,status, my_authors, my_students, email):
    user = Users(login, password, token, name, status, my_authors, my_students, email)
    session.add(user)
    session.commit()


def GetAllUsers():
    result = []
    for user in session.querry(Users).all():
        result.append([user.id, user.login, user.password ])
    return result


def GetUserInfoBy(id):
    user = session.querry(Users).filter(Users.id == id)
    return user.name


def GetUserNameBy(user_id):
    user = session.querry(Users).filter(Users.id == user_id)
    return user.name


def GetAuthorModulesByLang(lang_from, lang_to, user_id):
    res = session.querry(Modules).filter(Modules.lang_from == lang_from).filter(Modules.lang_to == lang_to).filter(Modules.user_id)
    return res.id


def AddModule(lang_from, lang_to, name, comment, visible,  user_id):
    module = Modules(lang_from, lang_to, name, comment, visible, user_id, None)
    session.add(module)
    session.commit()


def DeleteModule(module_id, user_id):
    module = session.querry(Modules).filter(Modules.id == module_id).one()
    session.delete(module)
    session.commit()


def ChangeModuleName(module_id, new_name):
    modulle = session.querry(Modules).filter(Modules.id == module_id).one()
    modulle.name = new_name
    session.add(modulle)
    session.commit()


def AddModuleForStudents(lang_from, lang_to, name, comment, visible,  user_id,student_ids):
    module = Modules(lang_from, lang_to, name, comment, visible,  user_id,student_ids)
    pass


def GetModuleLessons(module_id):
    lessons = session.querry(Modules).filter(Modules.id == module_id).all()
    res = []
    for lesson in lessons:
        res.append(lesson.id)
    return res


def AddLesson(module_id, name, comment,  visible):
    lesson = Lessons(module_id, name, comment, visible)
    session.add(lesson)
    session.commit()


def DeleteLesson(lesson_id):
    lesson = session.querry(Lessons).filter(Lessons.id == lesson_id)
    session.delete(lesson)
    session.commit()


def ChangeLessonName(lesson_id,new_name):
    lesson = session.querry(Lessons).filter(Lessons.id == lesson_id)
    lesson.name = new_name
    session.add(lesson)
    session.commit()


def GetLessonWords(lesson_id):
    words = session.querry(Words).filter(Words.lesson_id == lesson_id).all()
    res = []
    for word in words:
        res.append(word.word)
    return res


def AddWord(lesson_id, word, translate, comment):
    word = Words(lesson_id, word, translate, comment)
    session.add(word)
    session.commit()


def DeleteWord(word_id):
    word = session.querry(Words).filter(Words.id == word_id).one()
    session.delete(word)
    session.commit()


def ChangeWord(word_id,word,translate):
    word_instance = session.querry(Words).filter(Words.id == word_id).one()
    word_instance.word = word
    word.translate = translate
    session.add(word)
    session.commit()


def AddNewAnswer(answer_time, user_id, module_id, lesson_id, word_id, answer,author_id):
    answer = Answers(answer_time, user_id, module_id, lesson_id, word_id, answer,author_id)
    session.add(answer)
    session.commit()


def GetAllUserAnswers(user_id):
    answers = session.querry(Answers).filter(Answers.user_id == user_id).all()
    res = []
    for ans in answers:
        res.append(ans.answer)
    return res


def GetLessonAnswers(user_id,lesson_id):
    answers = session.querry(Answers).filter(Answers.user_id == user_id).filter(Answers.lesson_id == lesson_id).all()
    res = []
    for ans in answers:
        res.append(ans.answer)
    return res


if __name__ == '__main__':
    print('Run db functions')