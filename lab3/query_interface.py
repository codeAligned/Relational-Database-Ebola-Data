# CLI query interface for Ebola database in Python
import pymysql
from db_connect import *

def create_view_SurveyResp_Country():
    file = open('queries.sql', 'r')
    stmt = ''
    for i, line in enumerate (file):
        if (i > 5 and i < 9 ):
            stmt += "".join(line.strip() + ' ') 
        else:
            continue
    print (stmt)
    run_insert(stmt)
    file.close()

def create_view_etc_limited():
    file = open('queries.sql', 'r')
    stmt = ''
    for i, line in enumerate (file):
        if (i > 11 and i < 14 ):
            stmt += "".join(line.strip() + ' ') 
        else:
            continue
    print (stmt)
    run_insert(stmt)
    file.close()


def main():

    print ('========= QUERY INTERFACE FOR EBOLA DATABSE =========')

    print ('...Creating views')
    create_view_SurveyResp_Country()
    create_view_etc_limited()

    print ('Query options:')
    print ('1: show ETCs in selected country having greater than selected number
    of open_beds')
    print ('2: ')
    print ('3: ')
    print ('4: ')
    print ('5: ')
    print ('6: ')
    print ('7: ')
    print ('8: ')
    print ('9: ')
    print ('10: ')

    case = int(input('Enter query option number: '))
    if (case == 1):
        create_view_SurveyResp_Country()




    print('============== END PROGRAM ==============')

main()
