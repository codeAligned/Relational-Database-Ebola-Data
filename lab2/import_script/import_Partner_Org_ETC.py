# Import Partner_Org_ETC from ETC.csv

import pymysql
import csv
from db_connect import *

def import_csv():
    insert_prefix = "INSERT INTO Partner_Org_ETC (etc_code, partner_org) VALUES ("

    try:
        rows = list(csv.reader(open('../Datasets/ETC.csv', 'rb'), delimiter=","))
        rows.remove(rows[0])
        code_partner_combos = []
        for row in rows:
            code = row[0]
            partner = row[4]
            code_partner = [code, partner]
            if len(code_partner[1]) != 0:
                code_partner_combos.append(code_partner)

        for i,row in enumerate(code_partner_combos):
            insert_stmt = insert_prefix
            
            for j,val in enumerate(row):
                if val:
                    if j==0:
                        insert_stmt += "'" + val + "', "
                    elif j==1:
                        insert_stmt += "'" + val + "'"

            insert_stmt += ");"
            run_insert(insert_stmt)
                

    except IOError as e:
        print ("IO Error: " + e.strerror)

def main():
    import_csv()
main()
