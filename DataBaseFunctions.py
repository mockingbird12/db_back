from dbdriver import session
from dbdriver import Users
from dbdriver import Modules


def GetAllUsers():
    result = []
    for user in session.querry(Users).all():
        result.append([user.id, user.login, user.password ])
    return result

def GetUserInfoBy(id=id):
    user = session.querry(Users).filter(Users.id == id)
    return user.name

def GetUserNameBy(user_id):
    user = session.querry(Users).filter(Users.id == user_id)
    return user.name

def GetAuthorModulesByLang(lang_from, lang_to, user_id):
    res = session.querry(Modules).filter(Modules.lang_from == lang_from).filter(Modules.lang_to == lang_to).filter(Modules.user_id)
    return res.id

def AddModule(lang_from, lang_to, name, comment, visible,  user_id):
    module = Modules(lang_from, lang_to, name, comment, visible, user_id)
    session.add(module)
    session.commit()

def AddModuleForStudents(lang_from, lang_to, name, comment, visible,  user_id,student_ids):



