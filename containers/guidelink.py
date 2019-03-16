from components import Link
from actions import set_guide_filter
from store import store
from kivy.factory import Factory

def map_state_to_props(state, widget):
    if widget.guide == state['guide_filter']:
        return {'state': 'down'}
    else:
        return {'state': 'normal'}

def map_dispatch_to_props(dispatch, widget):
    return {'bind': {
                'on_release': lambda i: dispatch(
                                        set_guide_filter(widget.guide)),
                }
            }


GuideLink = store.connect(map_state_to_props, map_dispatch_to_props, Link)
Factory.register('GuideLink', GuideLink)
