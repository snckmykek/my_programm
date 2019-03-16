from kivy.properties import StringProperty
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class HeaderLabel(BoxLayout):
    header_text = StringProperty(None)
    
    def on_header_text(self, instance, value):
        header = self.ids.header
        header.text = value
