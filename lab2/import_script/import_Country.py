# Import Country Table

import pymysql
import csv
from db_connect import *


def import_csv():
    insert_prefix = "INSERT INTO Country (country_name, urban_pop, health_exp, gdp_cap) VALUES ("

    try:
        csvfile = open('../Datasets/CIA_World_Factbook.csv', "rb")
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
            # print(insert_stmt)
            run_insert(insert_stmt)
                
    except IOError as e:
        print ("IO Error: " + e.strerror)

def main():
    import_csv()
main()
