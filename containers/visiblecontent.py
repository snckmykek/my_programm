from components import ContentBox
from store import store
from kivy.factory import Factory
from actions import set_guide_filter
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

def map_state_to_props(state, widget):
    return {'content_box': state['content_box']}

def map_dispatch_to_props(dispatch, widget):
    return {'assign': {}}

VisibleContent = store.connect(map_state_to_props, map_dispatch_to_props,
                                ContentBox)
Factory.register('VisibleContent', VisibleContent)
