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

def add_prod(database = 'general.db', table, prod): #prod = [p_id, name, units(, global_rating)]
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

def del_record(database = 'general.db', table, id_column, record_id):
    con = sqlite3.connect(database)
    cur = con.cursor()
    cur.execute('DELETE FROM {} WHERE {} = "{}"'.format(table, id_column, record_id))
    con.commit()
    cur.close()
    con.close()

def update_record(database = 'general.db', table, param_column, param_val, id_column, record_id):
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
                                                           'qty FLOAT,
                                                           'units STRING,'
                                                           'local_rating FLOAT,'
                                                           'global_rating FLOAT)')
    
    cur.execute('CREATE TABLE IF NOT EXISTS my_products(p_id STRING,'#В формате m1, m2..
                                                       'name TEXT,'
                                                       'strikethrough INTEGER,'
                                                       'price FLOAT,'
                                                       'qty FLOAT,
                                                       'units STRING,'
                                                       'local_rating FLOAT)')

    cur.close()
    con.close()

def add_prod_in_local_db(database = 'local.db', p_id, name, strikethrough = 0, price = 0,
                         qty = 0, units = 'шт', local_rating = -1, global_rating = -1):
    con = sqlite.connect()
    cur = con.cursor()
    
    if p_id.split('')[0] == 'p':
        prod_values = list(cur.execute('SELECT * FROM products WHERE p_id = "{}"'.format(p_id)))
        prod = [prod_values[:6], -1, -1]

    cur.execute('INSERT INTO {} VALUES(?,?,?,?,?,?,?,?)'.format(l_id), prod)
    
def make_list(database = 'local.db', l_id):
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

def del_list(database, l_id):
    con = sqlite3.connect(database)
    cur = con.cursor()
    cur.execute('DROP TABLE IF EXIST {}'.format(l_id))
    cur.close()
    con.close()
    
    
def add_prod_in_list(l_id, p_id):
    con = sqlite.connect()
    cur = con.cursor()
    if p_id.split('')[0] == 'p':
        prod_values = list(cur.execute('SELECT * FROM products WHERE p_id = "{}"'.format(p_id)))
        prod = [prod_values[:6], -1, -1]
    if p_id.split('')[0] == 'e':
        prod_values = list(cur.execute('SELECT * FROM exists_products WHERE p_id = "{}"'.format(p_id)))
        prod = prod_values
    if p_id.split('')[0] == 'm':
        prod_values = list(cur.execute('SELECT * FROM my_products WHERE p_id = "{}"'.format(p_id)))
        prod = [prod_values[:7], -1]
    cur.execute('INSERT INTO {} VALUES(?,?,?,?,?,?,?,?)'.format(l_id), prod)
    con.commit()
    cur.close()
    con.close()

if __name__ == '__main__':
    l_id = str(0)
    make_local_database()
    make_list(l_id)
    add_prod_in_list(l_id, 'p0')
    add_prod_in_list(l_id, 'e0')
    add_prod_in_list(l_id, 'm0')
