# Create connection to database

import pymysql

def create_connection():
    try:
        connection = pymysql.connect(host   = "localhost",
                                     user   = "root",
                                     passwd = "",
                                     db     = "ebola")
    
    except pymysql.Error as error:
        print ("connection error: ", error)
   
    return connection


def destroy_connection(conn):
    conn.close()


def run_insert(insert_stmt):
    try:
        conn = create_connection()
        cur = conn.cursor()
        cur.execute(insert_stmt)
        conn.commit()
        destroy_connection(conn)

    except pymysql.Error as error:
        print ("insert error: ", error)

def run_prep_stmt (stmt, param):
    try:
        conn = create_connection()
        cur = conn.cursor()
        cur.execute(stmt, param)
        conn.commit()
        destroy_connection(conn)

    except pymysql.Error as error:
        print "db_error: ", error
