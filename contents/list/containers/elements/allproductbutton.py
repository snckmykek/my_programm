from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.properties import NumericProperty
from kivy.uix.popup import Popup
from contents.list.actions import add_listfilter, del_listfilter
from contents.list.containers.elements.allproductsettingtextinputprice import AllProductSettingTextInputPrice
from contents.list.containers.elements.allproductsettingtextinputqty import AllProductSettingTextInputQty

import time

from kivy.lang import Builder
Builder.load_file(r'contents/list/containers/elements/allproductbutton.kv')

class AllProductButton(Button):
    __events__ = ('on_long_press','on_short_press' , )

    long_press_time = NumericProperty(.4)
    easter_egg_time = NumericProperty(5)
    func_time = 0
    func_time2 = 0
    
    
    def on_state(self, instance, value):
        lpt = self.long_press_time
        if value == 'down':
            self.func_time = time.time()
            self._clockev = Clock.schedule_once(self._do_long_press, lpt)
        else:
            self._clockev.cancel()
            self.func_time2 = time.time() - self.func_time
            if self.func_time2 < lpt:
                self._do_short_press()
            elif self.func_time2 > self.easter_egg_time:
                print('Пасхалка')

    def _do_long_press(self, dt):
        self.dispatch('on_long_press')
        
    def on_long_press(self, *largs):
        self.parent.open_AllProductSetting()

    def _do_short_press(self):
        self.dispatch('on_short_press')
        
    def on_short_press(self, *largs):
        pass

