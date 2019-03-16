from actions.action import Action

'''
Экшены нужны для регистрации каких-либо действий.
Каждый раз, когда вызывается одна из функций в этом файле,
файл ниже присваивает атрибутам объекта, что вызвал функцию, новые значения,
переданные в данную функцию.
'''

def set_guide_filter(guide):
    return Action('SET_GUIDE_FILTER', guide=guide)
