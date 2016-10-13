# Import Organization from orgs_involved.csv

import pymysql
import csv
from db_connect import *

def import_csv():

    insert_prefix = "INSERT INTO Organization (country_name, org_acronym, org_name, org_type) VALUES ("

    try:
        orgs_used = list()
        three_countries = list()
        rows = list(csv.reader(open('../Datasets/orgs_involved.csv', 'rb'), delimiter=','))
        rows.remove(rows[0])
        for i in rows:
            if i[0] in ("Guinea", "Liberia", "Sierra Leone"):
                three_countries.append(i)
        
        unique_rows = list() 
        for row in three_countries:
            org_name = row[2]  
            if org_name not in orgs_used:
                orgs_used.append(row[2])
                unique_rows.append(row)

        for i, row in enumerate(unique_rows):
            insert_stmt = insert_prefix

            for j, val in enumerate(row):
                if val:
                    if j!=3:
                        insert_stmt += "'" + val + "', "
                    else:
                        insert_stmt += "'" + val + "'"
                else:
                    if j==3:
                        insert_stmt += "NULL"
                    else:
                        insert_stmt += "NULL" + ", "

            insert_stmt += ");"
            run_insert(insert_stmt)
                    
                



                


    except IOError as e:
        print ('IO Error: ' + e.strerror)

if __name__ == '__main__':
    import_csv()
