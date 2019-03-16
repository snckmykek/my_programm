from kivy.uix.togglebutton import ToggleButton
from kivy.properties import ObjectProperty, StringProperty

class Link(ToggleButton): #
    guide = StringProperty(None)

    def on_guide(self, instance, value):
        options = {'GO_BUDGET': '1', 'GO_RECIPES': '2',
                   'GO_PROGRESS': '3', 'GO_LIST': '4', 'GO_GLIDER': '5', }
        background_normals = {'GO_BUDGET': '',
                              'GO_RECIPES': '',
                              'GO_PROGRESS': '',
                              'GO_LIST': '',
                              'GO_GLIDER': ''
                              }
        background_downs = {'GO_BUDGET': 'images\GuideButtonBackgroundDown.png',
                              'GO_RECIPES': 'images\GuideButtonBackgroundDown.png',
                              'GO_PROGRESS': 'images\GuideButtonBackgroundDown.png',
                              'GO_LIST': 'images\GuideButtonBackgroundDown.png',
                              'GO_GLIDER': 'images\GuideButtonBackgroundDown.png'
                            }
        self.text = options[value]
        self.background_normal = background_normals[value]
        self.background_down = background_downs[value]

    def on_touch_down(self, touch):
        if self.state == 'down':
            return False
        else:
            super(Link, self).on_touch_down(touch)
