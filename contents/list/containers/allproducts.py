from kivy.uix.modalview import ModalView
from kivy.properties import ObjectProperty, NumericProperty
from contents.list.storelist import store
from contents.list.actions import add_product
from contents.list.actions import resort_products
from contents.list.containers.visibleallproducts import VisibleAllProducts
from kivy.uix.textinput import TextInput

from kivy.lang import Builder
Builder.load_file(r'contents/list/containers/allproducts.kv')

class AllProducts(ModalView):
    parent_id = NumericProperty(None)
    
    def add_product_in_list_callback(self):
        store.dispatch(add_product(self.ids.text_inp_new_prod.text,
                                   self.parent_id))
        self.ids.text_inp_new_prod.text = ''

    def resort_prods(self):
        text_inp = self.ids.text_inp_new_prod
        store.dispatch(resort_products(text_inp.text))

class AllProductsTextInput(TextInput):

    def on_focus(self, instance, value):
        if value:
            self.text = ''
