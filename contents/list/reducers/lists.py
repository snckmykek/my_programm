import numpy as np

def lists(action, state=[]):
    if action.action_type == 'ADD_LIST':
        return state + [{'l_id': action.l_id, 'text': action.text}]
    
    elif action.action_type == 'REMOVE_LIST':
        new_state = []
        for lst in state:
            if lst['l_id'] != action.l_id:
                new_state += [{'l_id': lst['l_id'], 'text': lst['text']}]
        return new_state
    
    elif action.action_type == 'LOAD':
        state = []
        try:
            for d in np.load('data.npy').item()['lists']:
                state += [d]
        except:
            print('data.npy нет, загрузить не могу')
        return state

    else:
        return state
