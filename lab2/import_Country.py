# Import Country Table

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
    insert_prefix = "insert into Country (country_name, urban_pop, health_exp, gdp_cap) values ("
    try:
        csvfile = open("CIA_World_Factbook.csv", "rb")
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if i==0: continue                           # skip column names row      
            insert_stmt = insert_prefix
            
            for j, val in enumerate(row):
                if j==0:
                    insert_stmt += "'" + val + "', "
                elif j==1 or j==2:                      # handles numeric types
                    insert_stmt += val + ", "
                else:                                   # handles last/numeric value
                    insert_stmt += val 
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




        
    
