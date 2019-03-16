from kivy.uix.modalview import ModalView
from kivy.properties import ObjectProperty, NumericProperty
from contents.list.storelist import store
from contents.list.containers.allproducts import AllProducts
from contents.list.storelist import store
from contents.list.actions import change_vis_filter
from contents.list.containers.visiblelistofproducts import VisibleListOfProducts
from kivy.lang import Builder

Builder.load_file(r'contents/list/containers/productslist.kv')

class ProductsList(ModalView):
     parent_id = NumericProperty(None)
     all_product_list_popup = AllProducts()
     
     def open_AllProducts(self):
          store.dispatch(change_vis_filter(self.parent_id))
          self.all_product_list_popup.parent_id = self.parent_id
          self.all_product_list_popup.open()
