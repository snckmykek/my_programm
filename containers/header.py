from components import HeaderLabel
from store import store
from kivy.factory import Factory

def map_state_to_props(state, widget):
    return {'header_text': state['header_text']}

def map_dispatch_to_props(dispatch, widget):
    return {'assign': {}}


Header = store.connect(map_state_to_props, map_dispatch_to_props, HeaderLabel)
Factory.register('Header', Header)
