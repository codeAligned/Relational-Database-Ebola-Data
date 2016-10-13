# import Survey_Respondent from data_survey.csv

import pymysql
import csv
from db_connect import *

def import_csv():
    insert_prefix = "INSERT INTO Survey_Respondent (country_name, respid, gender, age, education, corganizedae) VALUES ("

    try:
        csvfile = open('../Datasets/data_survey.csv', 'rb')
        reader = csv.reader(csvfile)

        for i, row in enumerate(reader):
            if i==0: continue                           # skip column names row      
            insert_stmt = insert_prefix
            
            for j, val in enumerate(row):
                
                if not val:
                    insert_stmt += "'" + "NULL" + "', "

                if j==0 or j==2:
                    insert_stmt += "'" + val + "', "
                elif j==1 or j==3 or j==4:              # handles numeric types
                    insert_stmt += val + ", "
                else:                                   # handles last/numeric value
                    insert_stmt += val 

                # print (j, val)
                

            insert_stmt += ");"
            # print(insert_stmt)

            run_insert(insert_stmt)
                
    except IOError as e:
        print ("IO Error: " + e.strerror)

if __name__ == '__main__':
    import_csv()
