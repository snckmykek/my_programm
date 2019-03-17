from kivy.uix.textinput import TextInput

from kivy.lang import Builder
Builder.load_file(r'contents/list/containers/elements/allproductsettingtextinputqty.kv')

class AllProductSettingTextInputQty(TextInput):

    def click_text_inp(self):
        self.parent.clear_text_inp(self)
