from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.lang import Builder

class ProgressContent(BoxLayout):
   orientation = 'vertical'

Mem = ProgressContent()

def check(Progress = Mem):
   Progress.add_widget(Label(text='11111', color=(0,0,0,1), size_hint = (1, None),
                         height = 40))
   Progress.add_widget(Label(text='2222', color=(0,0,0,1), size_hint = (1, None),
                         height = 40))
   Progress.add_widget(Label(text='33333', color=(0,0,0,1), size_hint = (1, None),
                         height = 40))
   Progress.add_widget(Label(text='444444', color=(0,0,0,1), size_hint = (1, None),
                         height = 40))
   Progress.add_widget(Label(text='hhhhhhhh', color=(0,0,0,1), size_hint = (1, None),
                         height = 40))
   Progress.add_widget(Label(text='ffffffff', color=(0,0,0,1), size_hint = (1, None),
                         height = 40))
   Progress.add_widget(Label(text='77777777f11', color=(0,0,0,1), size_hint = (1, None),
                         height = 40))
   Progress.bind(minimum_height=Progress.setter('height'))
   return Progress

Progress = check()
