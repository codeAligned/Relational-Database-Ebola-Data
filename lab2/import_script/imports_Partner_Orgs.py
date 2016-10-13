# Import Partner Orgs from ETC.csv

import pymysql
import csv
from db_connect import *

def import_csv():
    insert_prefix = "INSERT INTO Partner_Orgs (partner_org) VALUES ("

    try:
        partners_used = list()
        rows = list(csv.reader(open('../Datasets/ETC.csv', 'rb'), delimiter=","))
        rows.remove(rows[0])
        unique_rows = list()
        for row in rows:
            partner = row[4]
            if len(partner) == 0:
                partners_used.append(partner)
            if partner not in partners_used:
                partners_used.append(row[4])
                unique_rows.append(row)

        for i, row in enumerate(unique_rows):
            insert_stmt = insert_prefix
            
            for j, val in enumerate(row):
                if val:
                    if j==4:
                        insert_stmt += "'" + val + "'"
                    else:
                        continue


            insert_stmt += ");"
            print(insert_stmt)
                    

            run_insert(insert_stmt)
                
    except IOError as e:
        print ("IO Error: " + e.strerror)

def main():
    import_csv()
main()
