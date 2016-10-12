# Import Organization from orgs_involved.csv

import pymysql
import csv
from db_connect import *

def import_csv():

    insert_stmt = "insert into Organization (country_name, org_acronym, org_name, org_type) values (%s, %s, %s, %s)"

    try:
        csvfile = open('../datasets/orgs_involved.csv', 'rb')
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if i:
                for j, val in enumerate(row):
                    if j == 0:
                        country_name = val
                    elif j == 1:
                        org_acronym = val
                    elif j == 2:
                        org_name = val
                    elif j == 3:
                        org_type = val
                run_prep_stmt (insert_stmt, (country_name, org_acronym,
                    org_name, org_type))

    except IOError as e:
        print ('IO Error: ' + e.strerror)

if __name__ == '__main__':
    import_csv()
