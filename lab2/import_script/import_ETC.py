# Import ETC from ETC.csv

import pymysql
import csv
from db_connect import *

def import_csv():
    insert_prefix = "INSERT INTO ETC (etc_code,	etc_name, status, beds_open, partner_org, latitude, longitude, lab_present, country_name) VALUES ("

    try:
        csvfile = open("../Datasets/ETC.csv", "rb")
        reader = csv.reader(csvfile)

        for i, row in enumerate(reader):
            if i==0: continue                           # skip column names row      
            insert_stmt = insert_prefix
            
            for j, val in enumerate(row):
                if val:
                    if j==0 or j==1 or j==2 or j==4 or j==7:
                        insert_stmt += "'" + val + "', "
                    elif j==3 or j==5 or j==6:              # handles numeric types
                        insert_stmt += val + ", "
                    else:                                   # handles last value
                        insert_stmt += "'" + val + "'"
                else:
                    if j == 8:
                        insert_stmt += "NULL"
                    else:
                        insert_stmt += "Null" + ", "
            insert_stmt += ");"

            # print(insert_stmt)
            run_insert(insert_stmt)
                
    except IOError as e:
        print ("IO Error: " + e.strerror)

def main():
    import_csv()
main()
