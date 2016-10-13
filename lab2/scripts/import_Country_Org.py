# Populate Country_Org junction table from orgs_involved.csv
import pymysql
import csv
from db_connect import *

def import_Country_Org():
    is_success = True
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
            insert_status = run_insert(insert_stmt)
            if insert_status is False:
                is_success = False
                return is_success
                
    except IOError as e:
        is_success = False
        print ("import_Country_Org Error: " + e.strerror)
    
    return is_success
