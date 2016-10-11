# Import ETC Table

import pymysql
import csv

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


def import_csv():
    insert_prefix = "insert into ETC (etc_code,	etc_name, status, beds_open, partner_org, latitude, longitude, lab_present, country_name) values ("
    try:
        csvfile = open("ETC.csv", "rb")
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if i==0: continue                           # skip column names row      
            insert_stmt = insert_prefix
            
            for j, val in enumerate(row):
                if j==0 or j==1 or j==2 or j==4 or j==7:
                    insert_stmt += "'" + val + "', "
                elif j==3 or j==5 or j==6:              # handles numeric types
                    insert_stmt += val + ", "
                else:                                   # handles last value
                    insert_stmt += "'" + val + "'"
            insert_stmt += ");"
            print(insert_stmt)
            run_insert(insert_stmt)
                
    except IOError as e:
        print ("IO Error: " + e.strerror)


def destroy_connection(conn):
    conn.close()


def main():
    import_csv()
main()




        
    
