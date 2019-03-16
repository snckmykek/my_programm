import numpy as np

def resort(action, state=''):
    if action.action_type == 'RESORT_PRODUCTS':
        return action.text_for_sort
    else:
        return state
