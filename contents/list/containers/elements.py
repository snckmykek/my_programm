from contents.list.actions import add_list
from contents.list.storelist import store
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivy.clock import Clock
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.modalview import ModalView
from kivy.uix.textinput import TextInput
import time

from kivy.lang import Builder
Builder.load_file(r'contents/list/containers/elements.kv')

'''
Мелкие элементы, типо кнопок и текстинпутов
'''

class AddList(ModalView): #Окно добавления Списка в список Списков:)

    def clear_text_inp(self):
        self.ids.text_inp.text = ''
        
    def add_list_close_callback(self):
        text_inp = self.ids.text_inp
        store.dispatch(add_list(text_inp.text))
        text_inp.text = ''
        self.dismiss()

class AllProductButton(Button): #Кнопка-элемент(часть) виджета ОллПродукта
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

class AllProductSettingTextInput(TextInput): #ну короче понятно для чего

    name_text_inp = StringProperty('')
    names = {'price': 'Цена', 'qty': 'Количество', 'units': 'Единицы'}
    
    def on_focus(self, instance, value):
        if value:
            if (self.text == self.names[self.name_text_inp]) or (self.text == '0'):
                self.text = ''
                self.foreground_color = (0,0,0,1)
        else:
            if (self.text == '') or (self.text == '0'):
                self.text = self.names[self.name_text_inp]
                self.foreground_color = (0,0,0,.35)

class FlatButton(ButtonBehavior, Label): #Просто кнопка, юзается где угодно
    pass

class ListButton(ButtonBehavior, Label): #Кнопка, часть Списка в списке Списков
    pass
