from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label

from kivy.lang import Builder
Builder.load_file(r'contents/list/containers/elements/listbutton.kv')

class ListButton(ButtonBehavior, Label):
    pass
