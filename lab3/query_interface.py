# CLI query interface for Ebola database in Python
import pymysql
from db_connect import *

def print_menu():
    print ('Query options:')
    print ('1: List ETCs in Guinea having greater than 50 open beds.')
    print ('2: List average age and education level of males in Liberia.')
    print ('3: Count number of female survey respondents that have at least '
            'an education level of 6.')
    print ('4: ')
    print ('5: ')
    print ('6: ')
    print ('7: ')
    print ('8: ')
    print ('9: ')
    print ('10: ')
    print ''

def create_view_SurveyResp_Country():
    stmt = 'CREATE VIEW SurveyResp_Country (gender, age, education, country_name) AS SELECT gender, age, education, country_name FROM Survey_Respondent;'
    run_insert(stmt)

def create_view_etc_limited():
    stmt = 'CREATE VIEW ETC_limited (etc_name, country_name, partner_org) AS SELECT etc_name, country_name, partner_orgFROM ETC, Partner_Orgs;'
    run_insert(stmt)

def etc_open_beds():
    stmt = "SELECT * FROM ETC WHERE country_name = 'Guinea' HAVING beds_open > 50 ORDER BY beds_open;"
    run_insert(stmt)

def age_edu_male_liberia():
    stmt = "SELECT AVG(age) as avg_age, AVG(education) as avg_education FROM survey_respondent WHERE gender = 'M' AND country_name = 'liberia' AND (education != 88 OR education != NULL);"
    run_insert(stmt)


def main():

    print ('========= QUERY INTERFACE FOR EBOLA DATABSE =========\n')

    # create views
    print ('...Creating views')
    create_view_SurveyResp_Country()
    create_view_etc_limited()
    
    # print query options menu
    print_menu()
    
    # prompt user for query option
    case = int(input('Enter query option number: '))
    if (case == 1):
        etc_open_beds()
    elif (case == 2):
        age_edu_male_liberia()





    print('\n============== END PROGRAM ==============')

main()
