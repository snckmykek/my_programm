from kivy.uix.textinput import TextInput

from kivy.lang import Builder
Builder.load_file(r'contents/list/containers/elements/allproductsettingtextinputprice.kv')

class AllProductSettingTextInputPrice(TextInput):

    def click_text_inp(self):
        print('fsdf')
        self.parent.parent.parent.clear_text_inp(self)
