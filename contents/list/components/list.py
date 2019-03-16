from kivy.uix.label import Label
from kivy.properties import ObjectProperty, NumericProperty
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

from contents.list.containers.productslist import ProductsList
from contents.list.storelist import store
from contents.list.actions import change_vis_filter

from kivy.lang import Builder
Builder.load_file(r'contents/list/components/list.kv')


class List(BoxLayout):
    release_callback = ObjectProperty(None)
    l_id = NumericProperty(None)
    product_list_popup = ProductsList()
    def open_ProductsList(self):
        store.dispatch(change_vis_filter(self.l_id))
        self.product_list_popup.parent_id = self.l_id
        self.product_list_popup.open()
