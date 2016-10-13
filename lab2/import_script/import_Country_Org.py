# Import Country_Org junction table

import pymysql
import csv
from db_connect import *

db = pymysql.connect (host   ="localhost", # your host, for this lab, you don't need to change
                      user   = "root",     # your username
                      passwd = "",         # your password
                      db     = "ebola")    # name of the database

def import_csv():

    insert_stmt = "INSERT INTO Country_Org (country_name, org_name) VALUES ("
    
    try:

        csvfile = open("../Datasets/orgs_involved.csv", "rb")
        reader = csv.reader(csvfile)
        
        for i, row in enumerate(reader):
            if i==0: continue                           # skip column names row

            for j, val in enumerate(row):
                if j==0:
                    insert_stmt += "'" + val + "', "
                elif j==2:
                    insert_stmt += "'" + val + "'"
            insert_stmt += ");"

            if i==1:
                print(insert_stmt)
            run_insert(insert_stmt)
                
    except IOError as e:
        print ("IO Error: " + e.strerror)

if __name__ == '__main__':
    import_csv()
