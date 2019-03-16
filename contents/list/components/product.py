from kivy.uix.label import Label
from kivy.properties import ObjectProperty, NumericProperty
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

from kivy.lang import Builder
Builder.load_file(r'contents/list/components/product.kv')

class Product(BoxLayout):
    release_callback = ObjectProperty(None)
    release_callback2 = ObjectProperty(None)
    p_id = NumericProperty(None)

