from kivy.uix.modalview import ModalView
from kivy.properties import ObjectProperty, NumericProperty
from contents.list.storelist import store
from contents.list.actions import add_list
from kivy.lang import Builder

Builder.load_file(r'contents/list/containers/elements/addlist.kv')

class AddList(ModalView):

    def clear_text_inp(self):
        self.ids.text_inp.text = ''
        
    def add_list_close_callback(self):
        text_inp = self.ids.text_inp
        store.dispatch(add_list(text_inp.text))
        text_inp.text = ''
        self.dismiss()
