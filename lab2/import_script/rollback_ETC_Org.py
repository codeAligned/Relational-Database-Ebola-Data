# Import Country Table

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


def run_insert(insert_stmt):
    try:
        conn = create_connection()
        cur = conn.cursor()
        cur.execute(insert_stmt)
        conn.commit()
        destroy_connection(conn)

    except pymysql.Error as error:
        print ("insert error: ", error)


def rollback():
    insert_stmt = "DELETE FROM ETC_Org;"
    try:
            print(insert_stmt)
            run_insert(insert_stmt)
                
    except IOError as e:
        print ("IO Error: " + e.strerror)


def destroy_connection(conn):
    conn.close()


def main():
    rollback()
main()
