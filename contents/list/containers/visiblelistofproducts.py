from contents.list.components.listofproducts import ListOfProducts
from contents.list.storelist import store
from kivy.factory import Factory
from contents.list.actions import del_listfilter, strikethrough_text
import numpy as np


def get_list_of_products(products, vis_filter):
   prods = filter(lambda x: vis_filter in x['listfilter'].keys(), products)
   try:
      new_prods = sorted(list(prods), key=lambda x: (x['strikethrough'], x['text']))
   except:
      new_prods = list(prods)
   new_prods.append('im so stupid')
   return new_prods

def map_state_to_props(state, widget):
   return {'products': get_list_of_products(state['products'],
                                            state['visibility_filter'])}
   
def map_dispatch_to_props(dispatch, widget):
   return {'assign': {
      'item_callback_del': lambda p_id: dispatch(del_listfilter(p_id)),
      'item_callback_strikethrough': lambda p_id: dispatch(strikethrough_text(p_id))
      }
           }
VisibleListOfProducts = store.connect(map_state_to_props,
                            map_dispatch_to_props,
                            ListOfProducts)

Factory.register('VisibleListOfProducts', VisibleListOfProducts)
