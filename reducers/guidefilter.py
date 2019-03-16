def guide_filter(action, state='GO_PROGRESS'):
    if action.action_type == 'SET_GUIDE_FILTER':
        return action.guide
    else:
        return state
