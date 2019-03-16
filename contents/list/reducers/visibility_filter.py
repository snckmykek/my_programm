import numpy as np

def visibility_filter(action, state=[]):
    if action.action_type == 'CHANGE_VIS_FILTER':
        return action.l_id
    else:
        try:
            return np.load('data.npy').item()['visibility_filter']
        except:
            return None
