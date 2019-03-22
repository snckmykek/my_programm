import numpy as np
from copy import deepcopy

def products(action, state=[]):
    if action.action_type == 'ADD_PRODUCT':
        return state + [{'p_id': action.p_id, 'text': action.text,
                         'info': action.info, 'listfilter': action.listfilter,
                         'strikethrough':action.strikethrough}]

    elif action.action_type == 'SETTING_PRODUCT':
        new_state = []
        vis_fil = np.load('data.npy').item()['visibility_filter']
        for prod in state:
            if prod['p_id'] == action.p_id:
                prod['info'][vis_fil] = {'price': action.price,
                                                  'qty': action.qty}
            new_state += [{'p_id': prod['p_id'], 'text': prod['text'],
                           'info': prod['info'], 'listfilter': prod['listfilter'],
                           'strikethrough': prod['strikethrough']
                           }]
        return new_state
    
    elif action.action_type == 'REMOVE_PRODUCT':
        new_state = []
        for prod in state:
            if prod['p_id'] != action.p_id:           
                new_state += [{'p_id': prod['p_id'], 'text': prod['text'],
                               'info': prod['info'],
                               'listfilter': prod['listfilter'],
                               'strikethrough': prod['strikethrough']
                               }]
        return new_state

    elif action.action_type == 'CHANGE_LISTFILTER':
        new_state = []
        vis_fil = np.load('data.npy').item()['visibility_filter']
        for prod in state:
            if prod['p_id'] == action.p_id:
                try:
                    prod['listfilter'].remove(vis_fil)
                except:
                    prod['listfilter'].append(vis_fil)
                prod['strikethrough'] = False
            new_state += [{'p_id': prod['p_id'], 'text': prod['text'],
                           'info': prod['info'],'listfilter': prod['listfilter'],
                           'strikethrough': prod['strikethrough']}]
        return new_state

    elif action.action_type == 'REMOVE_LIST':
        new_state = []
        for prod in state:
            if action.l_id in prod['info'].keys():
                prod['info'].pop(action.l_id)
                if action.l_id in prod['listfilter']:
                    prod['listfilter'].remove(action.i_id)
            new_state += [{'p_id': prod['p_id'], 'text': prod['text'],
                           'info': prod['info'], 'listfilter': prod['listfilter'],
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
