from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label

class ContentBox(BoxLayout):
    content_box = ObjectProperty(None)
    
    def on_content_box(self, instance, value):
        content_window = self.ids.cont_box
        content_window.clear_widgets()
        value.height = content_window.height
        content_window.add_widget(value)
