import sqlite3
from sqlite3 import Error
import pandas as pd
import os

cwd = os.getcwd()
database = cwd + '\data\database.db'

def connect():
    conn = None
    try:
        conn = sqlite3.connect(database)
        return conn
    except Error as e:
        print(e)
    return self.conn

def add_userdata_outside(price, url, email):
        conn = connect()
        data_tuple = (price, url, email)
        try:
            c = conn.cursor()
            c.execute("INSERT INTO userdata VALUES(?,?,?);", data_tuple)
            conn.commit()
        except Error as e:
            print(e)

def select_distinct_data():
    conn = connect()
    c = conn.cursor()
    c.execute('SELECT DISTINCT * FROM userdata') 
    return c

class databaseCreation:
    def __init__(self):
        print('cwd = ', cwd)
        # create a database connection
        self.conn = connect()
        self.main()

    def create_table(self, create_table_sql):
        """ create a table from the create_table_sql statement
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        try:
            c = self.conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)

    def add_userdata(self, price, url, email):
        print('adding data!')
        data_tuple = (price, url, email)
        try:
            print('try')
            c = self.conn.cursor()
            c.execute("INSERT INTO userdata VALUES(?,?,?);", data_tuple)
            self.conn.commit()
        except Error as e:
            print(e)

    def main(self):
        sql_create_userdata_table = """ CREATE TABLE IF NOT EXISTS userdata (
                                            price integer,
                                            url varchar(250),
                                            email varchar(250) 
                                        ); """

        # create tables
        if self.conn is not None:
            print('making tables!')
            # create userdata table
            self.create_table(sql_create_userdata_table)
        else:
            print("Error! cannot create the database connection.")

if __name__ == "__main__":
    databaseCreation()