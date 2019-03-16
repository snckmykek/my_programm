from contents.list.components import ListOfLists
from contents.list.storelist import store
from kivy.factory import Factory
from contents.list.actions import remove_list
import numpy as np

def get_list_of_lists(lists, vis_filter):
   return lists

def map_state_to_props(state, widget):
   return {'lists': get_list_of_lists(state['lists'],
                                         state['visibility_filter']
                                         )
           }
   

def map_dispatch_to_props(dispatch, widget):
    return {'assign': {
                'item_callback': lambda l_id: dispatch(remove_list(l_id))
                }
        }
VisibleListOfLists = store.connect(map_state_to_props,
                            map_dispatch_to_props,
                            ListOfLists)

Factory.register('VisibleListOfLists', VisibleListOfLists)
