from kivy.uix.modalview import ModalView
from kivy.properties import StringProperty, NumericProperty
from contents.list.storelist import store
from contents.list.actions import setting_product

from kivy.lang import Builder
Builder.load_file(r'contents/list/containers/allproductsetting.kv')

class AllProductSetting(ModalView):
    p_id = NumericProperty(0)
    price = NumericProperty(0)
    qty = NumericProperty(0)
    units = StringProperty('шт')
    name_of_prod = StringProperty('')
        
    def add_product_setting_close_callback(self):
        i = 0
        txt_price = self.ids.price_text_inp.text
        if (txt_price == 'Цена') or (txt_price == ''):
            txt_price = 0
        try:
            self.price = txt_price
            i += 1
        except:
            print('По-твоему, цена товара может быть {}? Можно оставить поле пустым или со значением "Цена"'.format(txt_price))

        txt_qty = self.ids.qty_text_inp.text
        if (txt_qty == 'Количество') or (txt_qty == ''):
            txt_qty = 0
        try:
            self.qty = txt_qty
            i += 1
        except:
            print('По-твоему, количество товара может быть {}? Можно оставить поле пустым или со значением "Количество"'.format(txt_qty))

        if i == 2:
            store.dispatch(setting_product(self.p_id, self.price, self.qty))
            self.dismiss()

    def change_unit(self, but):
        if but.text == 'шт':
            but.text = 'кг/л'
        elif but.text == 'кг/л':
            but.text = 'г/мл'
        elif but.text == 'г/мл':
            but.text = 'шт'
        
