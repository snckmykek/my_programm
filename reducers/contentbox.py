from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from contents.list.list import List

def content_box(action, cont_box = None):
    if action.action_type == 'SET_GUIDE_FILTER':
        if action.guide == 'GO_BUDGET':
            return Label()
        elif action.guide == 'GO_RECIPES':
            return Label()
        elif action.guide == 'GO_PROGRESS':
            return Label()
        elif action.guide == 'GO_LIST':
            return List
        elif action.guide == 'GO_GLIDER':
            return Label()
    else:
        return cont_box
