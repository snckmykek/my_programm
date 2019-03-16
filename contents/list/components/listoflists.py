from kivy.properties import ListProperty, ObjectProperty, NumericProperty
from kivy.uix.scrollview import ScrollView
from contents.list.components.list import List
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
import numpy as np

class ListOfLists(ScrollView):
    lists = ListProperty([])
    item_callback = ObjectProperty(None)
    
    def on_lists(self, instanсe, value):
        container = self.ids.lists
        container.clear_widgets()
        last_list_id = 0
        for lst in value:
            last_list_id = lst['l_id']
            l = List(l_id = lst['l_id'], height = 50, size_hint_y = None)
            l.ids.list_button.text = lst['text']
            l.ids.remove_button.release_callback = self.item_callback
            container.add_widget(l)
        if last_list_id > int(np.load('last_list_id.npy')): #Счетчик для пасхалки 
            np.save('last_list_id.npy', last_list_id)       #в миллион списков:)
