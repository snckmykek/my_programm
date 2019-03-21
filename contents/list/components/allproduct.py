from kivy.uix.label import Label
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from contents.list.containers.allproductsetting import AllProductSetting

from kivy.lang import Builder
Builder.load_file(r'contents/list/components/allproduct.kv')

class AllProduct(BoxLayout):
    release_callback = ObjectProperty(None)
    release_callback2 = ObjectProperty(None)
    p_id = NumericProperty(None)
    price = NumericProperty(0)
    qty = NumericProperty(0)
    name_of_prod = StringProperty('')

    all_product_setting_popup = AllProductSetting()

    def open_AllProductSetting(self):
        self.all_product_setting_popup.p_id = self.p_id
        self.all_product_setting_popup.price = self.price
        self.all_product_setting_popup.qty = self.qty
        self.all_product_setting_popup.name_of_prod = self.name_of_prod
        self.all_product_setting_popup.open()
