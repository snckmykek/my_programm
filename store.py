from actions.action import Action
from reducers import todo_reducers

class Store(object):

    def __init__(self, reducers):
        self.reducers = reducers
        self.state_map_callbacks = {}
        self.data_store = self.init_store()

    def init_store(self):
        reducers = self.reducers
        action = Action(None)
        new_state = {}
        for key in reducers:
            new_state[key] = reducers[key](action)
        return new_state

    def update_store(self, action):
        reducers = self.reducers
        data_store = self.data_store
        new_state = {}
        for key in reducers:
            new_state[key] = reducers[key](action, data_store[key])
        return new_state

    def map_state(self):
        state_map_callbacks = self.state_map_callbacks
        for widget in state_map_callbacks:
            new_data = state_map_callbacks[widget](self.data_store, widget)
            for key in new_data:
                setattr(widget, key, new_data[key])

    def _connect(self, map_state, map_dispatch, widget):
        self.state_map_callbacks[widget] = map_state
        init_data = map_state(self.data_store, widget)
        dispatches = map_dispatch(self.dispatch, widget)
        events = dispatches.get('bind', {})
        assigns = dispatches.get('assign', {})
        for key in assigns:
            setattr(widget, key, assigns[key])
        widget.bind(**events)
        return widget

    def connect(self, map_state, map_dispatch, widget_type):
        return lambda *args, **kwargs: self._connect(map_state,
                                                     map_dispatch,
                                                     widget_type(*args,
                                                                 **kwargs)
                                                    )

    def dispatch(self, action):
        self.data_store = self.update_store(action)
        self.map_state()


store = Store(todo_reducers)
