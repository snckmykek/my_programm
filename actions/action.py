class Action(object):

    def __init__(self, action_type, **kwargs):
        self.action_type = action_type
        for key in kwargs: 
            setattr(self, key, kwargs[key])
