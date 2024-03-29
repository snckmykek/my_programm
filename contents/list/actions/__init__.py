from contents.list.actions.action import Action
import numpy as np

try:
    next_list_id = int(np.load('last_list_id.npy'))
    next_list_id += 1
except:    
    next_list_id = 0

try:
    next_prod_id = int(np.load('last_prod_id.npy'))
    next_prod_id += 1
except:    
    next_prod_id = 0

def add_list(text):
    global next_list_id
    action = Action('ADD_LIST', l_id = next_list_id, text = text)
    next_list_id += 1
    return action
    
def remove_list(l_id):
    return Action('REMOVE_LIST', l_id = l_id)

def add_product(text, parent_id, price = 0, qty = 1, strikethrough = False):
    global next_prod_id
    info = {parent_id: {'price': price, 'qty': qty}}
    listfilter = [parent_id]
    action = Action('ADD_PRODUCT', p_id = next_prod_id, text = text,
                    listfilter = listfilter, info = info,
                    strikethrough = strikethrough)
    next_prod_id += 1
    return action
    
def remove_product(p_id):
    return Action('REMOVE_PRODUCT', p_id = p_id)

def change_vis_filter(l_id):
    return Action('CHANGE_VIS_FILTER', l_id = l_id)

def change_listfilter(p_id):
    return Action('CHANGE_LISTFILTER', p_id = p_id)

def resort_products(text_for_sort):
    return Action('RESORT_PRODUCTS', text_for_sort = text_for_sort)

def strikethrough_text(p_id):
    return Action('STRIKETHOUGH_TEXT', p_id = p_id)

def setting_product(p_id, price, qty): 
    return Action('SETTING_PRODUCT', p_id = p_id, price = price, qty = qty)
