from contents.list.reducers.lists import lists
from contents.list.reducers.products import products
from contents.list.reducers.visibility_filter import visibility_filter
from contents.list.reducers.resort import resort

list_reducers = {'lists': lists,
                 'products': products,
                 'visibility_filter': visibility_filter,
                 'resort': resort
                 }
