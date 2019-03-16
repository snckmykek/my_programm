from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.lang import Builder
from contents.list import containers
from contents.list.storelist import store
from contents.list.actions.action import Action

Builder.load_file(r'contents/list/list.kv')

class ListContent(BoxLayout):
   pass

List = ListContent()
store.dispatch(Action('LOAD')) # Повторно загружает всё, что в редукторах 'LOAD' из файла data.npy, 
                               # иначе не обновляется виджет со списками ???
                               # Мб второй раз грузить продукты больно жирно?
