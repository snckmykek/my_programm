# -*- coding: utf-8 -*-
import sqlite3

'''
Операции на стороне СЕРВЕРА
На сервере надодятся 2 базы:
1) Список продуктов (Молоко, хлеб);
2) Список реальных продуктов с их полным названием (+ нужна возможность оправления
запроса на добавление нового товара клиентом)
Есть функции для добавления/редактирования/(и на всякий случай)удаления продуктов
в обоих списках.
API?
'''

def make_general_database(database = 'general.db'): #Создание (если нет) 2 баз
    con = sqlite3.connect(database)
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS products(p_id STRING,'
                                                    'name TEXT,'
                                                    'units STRING)')
    cur.execute('CREATE TABLE IF NOT EXISTS exists_products(p_id STRING,'
                                                           'name TEXT,'
                                                           'units STRING,'
                                                           'global_rating FLOAT)')

    cur.close()
    con.close()

def add_prod(table, prod, database = 'general.db'): #prod = [p_id, name, units(, global_rating)]
    con = sqlite3.connect(database)
    cur = con.cursor()
    if table == 'products':
        if prod[1] in cur.execute('SELECT name FROM {}'.format(table)):
            print('Продукт {} уже есть в списке'.format(prod[1]))
        elif prod[0] in cur.execute('SELECT p_id FROM {}'.format(table)):
            print('Айди {} уже есть в списке'.format(prod[0]))
        else:
            cur.execute('INSERT INTO {} VALUES(?,?,?)'.format(table), prod)
    elif table == 'exists_products':
        if prod[1] in cur.execute('SELECT name FROM {}'.format(table)):
            print('Продукт {} уже есть в списке'.format(prod[1]))
        elif prod[0] in cur.execute('SELECT p_id FROM {}'.format(table)):
            print('Айди {} уже есть в списке'.format(prod[0]))
        else:
            cur.execute('INSERT INTO {} VALUES(?,?,?,?)'.format(table), prod)
    con.commit()
    cur.close()
    con.close()

def del_record(table, id_column, record_id, database = 'general.db'):
    con = sqlite3.connect(database)
    cur = con.cursor()
    cur.execute('DELETE FROM {} WHERE {} = "{}"'.format(table, id_column, record_id))
    con.commit()
    cur.close()
    con.close()

def update_record(table, param_column, param_val, id_column, record_id, database = 'general.db'):
    # param_column, param_val - имя колонки и новое значение для нее
    # d_column, record_id - имя колонки и значение, при котором выполнится замена
    con = sqlite3.connect(database)
    cur = con.cursor()
    cur.execute('UPDATE {} SET {} = "{}" WHERE {} = "{}"'.format(table, param_column,
                                                             param_val, id_column, record_id))
    con.commit()
    cur.close()
    con.close()   

'''
Операции на стороне КЛИЕНТА
У клиента находится 3 базы: первые 2 продублированыс сервера, последняя локальная, состоит из продуктов, созданных клиентом.
С сервером контактируют только 1, 2 базы, а так же запросы на добавления продуктов в общие базы.
'''

def make_local_database(database = 'local.db'): #Создание (если нет) 3 баз
    con = sqlite3.connect(database)
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS products(p_id STRING,' #В формате p1, p2..
                                                    'name TEXT,'
                                                    'strikethrough INTEGER,'
                                                    'price FLOAT,'
                                                    'qty FLOAT,'
                                                    'units STRING)')
    
    cur.execute('CREATE TABLE IF NOT EXISTS exists_products(p_id STRING,'#В формате e1, e2..
                                                           'name TEXT,'
                                                           'strikethrough INTEGER,'
                                                           'price FLOAT,'
                                                           'qty FLOAT,'
                                                           'units STRING,'
                                                           'local_rating FLOAT,'
                                                           'global_rating FLOAT)')
    
    cur.execute('CREATE TABLE IF NOT EXISTS my_products(p_id STRING,'#В формате m1, m2..
                                                       'name TEXT,'
                                                       'strikethrough INTEGER,'
                                                       'price FLOAT,'
                                                       'qty FLOAT,'
                                                       'units STRING,'
                                                       'local_rating FLOAT)')

    cur.close()
    con.close()

def add_prod_in_local_db(table, name, database = 'local.db', strikethrough = 0, price = 0,
                         qty = 0, units = 'шт', local_rating = -1, global_rating = -1):
    # table - куда его добавлять ('products', 'exists_products', 'my_products')
    
    con = sqlite3.connect(database)
    cur = con.cursor()

    prefixes = {'products': 'p', 'exists_products': 'e', 'my_products': 'm'}
    try:
        next_p_id = prefixes[table] + str(max([int(p_id[0][1:]) for p_id in cur.execute('SELECT p_id FROM {}'.format(table))]) + 1)
    except:
        next_p_id = prefixes[table] + str(0)

    values_for_tables = {'products': '?,?,?,?,?,?', 'exists_products': '?,?,?,?,?,?,?,?', 'my_products': '?,?,?,?,?,?,?'} 
    new_prod = [next_p_id, name, strikethrough, price, qty, units]
    cur.execute('INSERT INTO {} VALUES({})'.format(table, values_for_tables[tables]), new_prod)
        
    con.commit()
    cur.close()
    con.close()
    
def make_list(l_id, database = 'local.db'):
    con = sqlite3.connect(database)
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS {}(p_id INTEGER,'
                                              'name TEXT,'
                                              'strikethrough INTEGER,'
                                              'price FLOAT,'
                                              'qty FLOAT,'
                                              'units STRING,'
                                              'local_rating FLOAT,'
                                              'global_rating FLOAT)'.format(l_id))
    cur.close()
    con.close()

def del_list(l_id, database = 'local.db'):
    con = sqlite3.connect(database)
    cur = con.cursor()
    cur.execute('DROP TABLE IF EXISTS {}'.format(l_id))
    cur.close()
    con.close()
    
    
def add_prod_in_list(l_id, p_id, database = 'local.db'):
    con = sqlite3.connect(database)
    cur = con.cursor()
    if p_id[0] == 'p':
        prod_values = list(tuple(cur.execute('SELECT * FROM products WHERE p_id = "{}"'.format(p_id)))[0])
        prod = prod_values + [-1, -1]
    elif p_id[0] == 'e':
        prod_values = list(tuple(cur.execute('SELECT * FROM exists_products WHERE p_id = "{}"'.format(p_id)))[0])
        prod = prod_values
    elif p_id[0] == 'm':
        prod_values = list(tuple(cur.execute('SELECT * FROM my_products WHERE p_id = "{}"'.format(p_id)))[0])
        prod = prod_values + [-1]
    else:
        print('Ошибка в айди {}'.format(p_id[0]))
    cur.execute('INSERT INTO {} VALUES(?,?,?,?,?,?,?,?)'.format(l_id), prod)
    con.commit()
    cur.close()
    con.close()

if __name__ == '__main__':
    l_id = 'l_0'
    make_local_database()
    add_prod_in_local_db('products', 'Ананас')
    add_prod_in_local_db('products', 'Абрикос')
    add_prod_in_local_db('products', 'Софья', price = 149000000)
    add_prod_in_local_db('exists_products', 'Молоко Простоквашино 2.5%', local_rating = 1, global_rating = 1)
    add_prod_in_local_db('exists_products', 'Молоко Простоквашино 3.2%', local_rating = 2)
    add_prod_in_local_db('exists_products', 'Масло сливочное Крестьянское 72,5%', local_rating = 5)
    add_prod_in_local_db('my_products', 'Сырок вкусный понравился за 50р', local_rating = 3)
    make_list(l_id)
    add_prod_in_list(l_id, 'p0')
    add_prod_in_list(l_id, 'e0')
    add_prod_in_list(l_id, 'm0')
    del_list(l_id)
