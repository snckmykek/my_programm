from kivy.uix.modalview import ModalView
from kivy.properties import StringProperty, NumericProperty
from contents.list.storelist import store
from contents.list.actions import setting_product

from kivy.lang import Builder
Builder.load_file(r'contents/list/containers/allproductsetting.kv')

class AllProductSetting(ModalView):
    p_id = NumericProperty(None)
    price = NumericProperty(None)
    qty = NumericProperty(None)
    name_of_prod = StringProperty('')

    def clear_text_inp(self, ti):
        ti.text = ''
        ti.color = (0,0,0,1)
        
    def add_product_setting_close_callback(self):
        self.price = self.ids.price_text_inp.text
        self.qty = self.ids.qty_text_inp.text
        store.dispatch(setting_product(self.p_id, self.price, self.qty))
        self.dismiss()
