import numpy as np
from copy import deepcopy

def products(action, state=[]):
    if action.action_type == 'ADD_PRODUCT':
        return state + [{'p_id': action.p_id, 'text': action.text,
                         'listfilter': action.listfilter,
                         'strikethrough':action.strikethrough}]
    
    if action.action_type == 'ADD_LISTFILTER':
        action.vis_fil = np.load('data.npy').item()['visibility_filter']
        new_state = []
        for prod in state:
            if prod['p_id'] == action.p_id:
                new_listfilter = {action.vis_fil: action.new_listfilter_value}
                prod['listfilter'].update(new_listfilter)
            new_state += [{'p_id': prod['p_id'], 'text': prod['text'],
                           'listfilter': prod['listfilter'],
                           'strikethrough': prod['strikethrough']
                           }]
        return new_state
    
    elif action.action_type == 'REMOVE_PRODUCT':
        new_state = []
        for prod in state:
            if prod['p_id'] != action.p_id:           
                new_state += [{'p_id': prod['p_id'], 'text': prod['text'],
                               'listfilter': prod['listfilter'],
                               'strikethrough': prod['strikethrough']
                               }]
        return new_state

    elif action.action_type == 'DEL_LISTFILTER':
        new_state = []
        for prod in state:
            if prod['p_id'] == action.p_id:
                prod['listfilter'].pop(np.load('data.npy').item()['visibility_filter'])
                prod['strikethrough'] = False
            new_state += [{'p_id': prod['p_id'], 'text': prod['text'],
                           'listfilter': prod['listfilter'],
                           'strikethrough': prod['strikethrough']}]
        return new_state
        
    elif action.action_type == 'LOAD':
        state = []
        try:
            for d in np.load('data.npy').item()['products']:
                state += [d]
        except:
            print('data.npy нет, загрузить не могу')
        return state

    if action.action_type == 'STRIKETHOUGH_TEXT':
        for prod in state:
            if prod['p_id'] == action.p_id:
                deepcopy_prod = deepcopy(prod)
                prod['strikethrough'] = not deepcopy_prod['strikethrough']
        return state
        
    else:
        return state
