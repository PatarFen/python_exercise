import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn=None

    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)

    except Error as e:
        print(e)

    return conn
    """
    finally:
        if conn:
            conn.close()
    """

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    db = r"pythonsqlite.db"

    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS promote_codes (
                                        id integer PRIMARY KEY,
                                        code text NOT NULL
                                    ); """
    conn = create_connection(db)

    if conn is not None:
        create_table(conn, sql_create_projects_table)
    else:
        print("Error! Cannot create the databse connection")

if __name__ == '__main__':
    main()