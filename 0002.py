import db
import sqlite3
import string
import random
from sqlite3 import Error

def insert_promote_code(c, code):
    t = (code,)
    c.execute('INSERT INTO promote_codes VALUES (?)',t)

def code_generator(c, code_len, num_of_code):
    all_chars = string.ascii_letters + string.digits
    result = " "
    code_list = []
    for _ in range(num_of_code):
        result = " "
        for _ in range(code_len):
            result = result + (random.choice(all_chars))
        while (result in code_list):
            for _ in range(code_len):
                result = result + (random.choice(all_chars))
        code_list.append(result)
        insert_promote_code(c,result)
        
    #return code_list
    print("codes generation is done~")

def create_table(conn):
    try:
        conn.execute(""" CREATE TABLE IF NOT EXISTS promote_codes (
                                        code text PRIMARY KEY
                                    ); """)
    except Error as e:
        print(e)

if __name__ == "__main__":
    database = r"pythonsqlite.db"
    conn = db.create_connection(database)
    c = conn.cursor()
    create_table(c)
    code_generator(c, 8, 200)
    conn.commit()
    conn.close()