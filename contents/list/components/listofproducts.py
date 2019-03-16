from kivy.properties import ListProperty, ObjectProperty, NumericProperty
from kivy.uix.scrollview import ScrollView
from contents.list.components.product import Product

class ListOfProducts(ScrollView):
    products = ListProperty([])
    item_callback = ObjectProperty(None)

    def on_products(self, instanсe, value):
        try:
            value.remove('im so stupid') #Я даун не могу придумать как еще затриггерить он_продукст
        except:
            pass
        container = self.ids.products
        container.clear_widgets()
        for prod in value:
            p = Product(p_id = prod['p_id'], height = 50, size_hint_y = None)
            p.ids.prod_button.strikethrough = prod['strikethrough']
            if prod['strikethrough'] == True:
                p.ids.prod_button.background_color = (.93,.93,.93,1)
                p.ids.remove_button.background_color = (.93,.93,.93,1)
            else:
                p.ids.prod_button.background_color = (1,1,1,1)
                p.ids.remove_button.background_color = (1,1,1,1)
            p.ids.prod_button.release_callback2 = self.item_callback_strikethrough
            p.ids.prod_button.text = prod['text']
            p.ids.remove_button.release_callback = self.item_callback_del
            container.add_widget(p)
