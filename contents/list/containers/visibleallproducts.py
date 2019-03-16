from contents.list.components.listofallproducts import ListOfAllProducts
from contents.list.storelist import store
from kivy.factory import Factory
from contents.list.actions import remove_product, add_listfilter, del_listfilter
import numpy as np

def get_list_of_products(products, resort, vis_fil):
   state = []
   for i in range(len(products)):
      if resort.lower() in products[i]['text'].lower():
         state.append(products[i])
   new_products = sorted(state, key=lambda x: x['text'])[:10]
   for prod in new_products:
      if vis_fil in prod['listfilter'].keys():
         prod['selected'] = True
      else:
         prod['selected'] = False
   new_products.append('im so stupid')
   return new_products

def map_state_to_props(state, widget):
   return {'products': get_list_of_products(state['products'], state['resort'],
                                            state['visibility_filter'])}
   

def map_dispatch_to_props(dispatch, widget):
   return {'assign': {
                'item_callback_remove': lambda p_id: dispatch(remove_product(p_id)),
                'item_callback_add': lambda p_id: dispatch(add_listfilter(p_id)),
                'item_callback_del': lambda p_id: dispatch(del_listfilter(p_id))
                }
        }
VisibleAllProducts = store.connect(map_state_to_props,
                            map_dispatch_to_props,
                            ListOfAllProducts)
Factory.register('VisibleAllProducts', VisibleAllProducts)
