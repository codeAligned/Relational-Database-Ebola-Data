# Import Partner_Org_ETC from ETC.csv

import pymysql
import csv
from db_connect import *

def import_csv():
    insert_prefix = "INSERT INTO Partner_Org_ETC (etc_code, partner_org) VALUES ("

    try:
        csvfile = open("../Datasets/ETC.csv", "rb")
        reader = csv.reader(csvfile)

        for i, row in enumerate(reader):
            if i==0: continue                           # skip column names row      
            insert_stmt = insert_prefix
            
            for j, val in enumerate(row):
                if val:
                    if j==0:
                        insert_stmt += "'" + val + "', "
                    elif j==4:                          # handles numeric types
                        insert_stmt += "'" + val + "'"
                    else:                                   # handles last value
                        continue
 #               else:
#                    if j == 4:
#                        insert_stmt += "NULL"
#                    else:
#                        insert_stmt += "Null" + ", "
            insert_stmt += ");"
            if i==4:
                print(insert_stmt)
            run_insert(insert_stmt)
                
    except IOError as e:
        print ("IO Error: " + e.strerror)

def main():
    import_csv()
main()
