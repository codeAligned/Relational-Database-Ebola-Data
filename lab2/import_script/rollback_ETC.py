# Rollback ETC Table

import pymysql

def create_connection():
    try:
        connection = pymysql.connect(host="127.0.0.1",
                                     user="root",
                                     passwd="",
                                     db="Ebola")
        return connection
    
    except pymysql.Error as error:
        print ("connection error: ", error)


def run_insert(rollback_stmt):
    try:
        conn = create_connection()
        cur = conn.cursor()
        cur.execute(rollback_stmt)
        conn.commit()
        destroy_connection(conn)

    except pymysql.Error as error:
        print ("insert error: ", error)


def rollback():
    rollback_stmt = "DELETE FROM ETC;"
    try:
            print(rollback_stmt)
            run_insert(rollback_stmt)
                
    except IOError as e:
        print ("IO Error: " + e.strerror)


def destroy_connection(conn):
    conn.close()


def main():
    rollback()
main()
