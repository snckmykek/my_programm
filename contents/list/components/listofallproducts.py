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
        ''' Сюда приходит такой список: [{'p_id': 99, 'text': 'Баклажан',
        'listfilter': {86: {'price': None, 'qty': 1}}, 'strikethrough': False,
        'selected': True}, ... ] (Ну и добавленный в список "im so stupid" :) )
        в listfilter находятся ключи-фильтры(номер списка, к которому
        относятся данные) и данные к ним. То есть 86 - это номер списка, что
        вызвал данное окно, и через который вызовутся все последующие окна.
        '''
    
        vis_filter = np.load('data.npy').item()['visibility_filter']
        try:
            value.remove('im so stupid') #Я даун не могу придумать как еще затриггерить он_продукст
        except:
            pass
        container = self.ids.all_products
        container.clear_widgets()
        last_prod_id = 0
        for prod in value:
            last_prod_id = prod['p_id']
            p = AllProduct(p_id=prod['p_id'], name_of_prod=prod['text'])
            try:
                p.price=prod['info'][vis_filter]['price']
                p.qty=prod['info'][vis_filter]['qty']
                p.units=prod['info'][vis_filter]['units']
            except:
                p.price=0
                p.qty=0
                p.units='шт'
            p.ids.prod_button.text = prod['text']
            if prod['selected'] == True:
                p.ids.prod_button.background_normal = 'images/ProductSelectedBackground.png'
                p.ids.prod_button.background_down = 'images/ProductSelectedBackground.png'
            else:
                p.ids.prod_button.background_normal = ''
                p.ids.prod_button.background_down = ''
            p.ids.qty_button.text = str(p.qty*100) + ' г'
            p.ids.price_button.text = str(p.price*10.2) + ' р'
            p.ids.prod_button.release_callback2 = self.item_callback_change
            p.ids.remove_button.release_callback = self.item_callback_remove
            container.add_widget(p)
        if last_prod_id > int(np.load('last_prod_id.npy')): #Счетчик для пасхалки 
            np.save('last_prod_id.npy', last_prod_id)       #в миллиард продуктов:)
