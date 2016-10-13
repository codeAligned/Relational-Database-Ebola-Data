# Import Partner Orgs from ETC.csv

import pymysql
import csv
from db_connect import *

def import_csv():
    insert_prefix = "INSERT INTO Partner_Orgs (partner_org) VALUES ("

    try:
        csvfile = open("../Datasets/ETC.csv", "rb")
        reader = csv.reader(csvfile)

        
        for i, row in enumerate(reader):
            if i==0: continue                           # skip column names row      
            insert_stmt = insert_prefix
            
            for j, val in enumerate(row):
                if val:
                    if j==4:
                        insert_stmt += "'" + val + "'"
                    else:                                   
                        continue

            insert_stmt += ");"

            run_insert(insert_stmt)
                
    except IOError as e:
        print ("IO Error: " + e.strerror)

def main():
    import_csv()
main()
