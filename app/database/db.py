# create_part

from datetime import datetime
import time
import sqlite3
from os.path import exists as path_exists

sqlite = 'app/database/db.sqlite3'
# sqlite = 'db.sqlite3'
while not path_exists(sqlite):
    print(datetime.now(), "=> SQLite file is not found")
    time.sleep(1)

connection = sqlite3.connect(sqlite)
cursor = connection.cursor()

create_table_orders = """
   create table if not exists orders(
   
        id integer primary key autoincrement,
        created_at text default current_timestamp,
        phone_number varchar(25),
        addres varchar(50),
        product_title varchar(25),
        product_kilo varchar(25),
        product_count varchar(25),
        telegram_id integer(15),
        username varchar(25)
   
   ) 
"""


def commit(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        connection.commit()
        return result

    return wrapper


@commit
def create_table():
    cursor.execute(create_table_orders)


@commit
def new_order(phone_number, addres, product_title, product_kilo, product_count, telegram_id, username):
    inser_into_order = """
        insert into orders (phone_number,addres,product_title,product_kilo,product_count,telegram_id,username) values (?,?,?,?,?,?,?)
    """

    params = (phone_number, addres, product_title, product_kilo, product_count, telegram_id, username)
    cursor.execute(inser_into_order, params)


def init():
    create_table()

# init()
