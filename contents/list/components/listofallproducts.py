from kivy.properties import ListProperty, ObjectProperty, NumericProperty
from kivy.uix.scrollview import ScrollView
from contents.list.components.allproduct import AllProduct
import numpy as np
from kivy.uix.label import Label

class ListOfAllProducts(ScrollView):
    products = ListProperty([])
    item_callback = ObjectProperty(None)
    item_callback2 = ObjectProperty(None)
    
    def on_products(self, instanсe, value):
        try:
            value.remove('im so stupid') #Я даун не могу придумать как еще затриггерить он_продукст
        except:
            pass
        container = self.ids.all_products
        container.clear_widgets()
        last_prod_id = 0
        for prod in value:
            last_prod_id = prod['p_id']
            p = AllProduct(p_id = prod['p_id'], height = 50, size_hint_y = None)
            p.ids.prod_button.text = prod['text']
            if prod['selected'] == True:
                p.ids.prod_button.state = 'down'
                p.ids.prod_button.release_callback2 = self.item_callback_del
            else:
                p.ids.prod_button.release_callback2 = self.item_callback_add
            p.ids.remove_button.release_callback = self.item_callback_remove
            container.add_widget(p)
        if last_prod_id > int(np.load('last_prod_id.npy')): #Счетчик для пасхалки 
            np.save('last_prod_id.npy', last_prod_id)       #в миллиард продуктов:)
