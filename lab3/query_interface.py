# CLI query interface for Ebola database in Python
import pymysql
from db_connect import *
from query_functions import *

def print_menu():
    print ('\nQuery options:')
    print ('1:  List ETCs in a country having a minimum number of open beds.')
    print ('2:  List average age & education of respondents in a country, by gender.')
    print ('3:  Count number of respondents with a minimum education level, by gender.')
    print ('4:  List partner orgs with longitude/latitude coordinates.')
    print ('5:  List ETC codes affiliated with an organization.')
    print ('6:  List all distinct organization types.')
    print ('7:  List respondent\'s info & country of origin, by gender.')
    print ('8:  List open ETCs and partner orgs.')
    print ('9:  List countries in ascending order by GDP.')
    print ('10: Count respondents who think their community was well organized, by gender, education level, and country.')
    print ('11: List survey respondents with non-identifying info, ordered by age.')
    print ('12: List ETC names with Partner Orgs, ordered by ETC names.')
    print ('13: List ETC name and Country GDP of an organization, ordered by Country.')
    print ('14: List average age of survey respondents, by gender.')
    print ('15: List average education level of survey respondents, by gender.\n')

def run_another():
    opt = raw_input('Run another query? (y/n): ')
    if (opt == 'y' or opt == 'Y'):
        print_menu()
        run_query_case()
    else:
        print("Goodbye. Don't forget to wash your hands!")

def run_query_case():
    case = raw_input('Enter query option number: ')
    try:
        case = int (case)
    except ValueError:
        print('This is not a valid option.')
        run_another()
        return 

    if (case == 1):
        etc_open_beds()
        run_another()
    elif (case == 2):
        age_edu_sex_country()
        run_another()
    elif (case == 3):
        count_sex_educ()
        run_another()
    elif (case == 4):
        partner_lat_long()
        run_another()
    elif (case == 5):
        org_ETC_codes()
        run_another()
    elif (case == 6):
        distinct_org_types()
        run_another()
    elif (case == 7):
        respondent_country_info()
        run_another()
    elif (case == 8):
        non_closed_ETC_partner()
        run_another()
    elif (case == 9):
        country_gdp()
        run_another()
    elif (case == 10):
        count_organized()
        run_another()
    elif (case == 11):
        surveyresp_country_byAge()
        run_another()
    elif (case == 12):
        etc_limited_byName()
        run_another()
    elif (case == 13):
        partner_org_limited_byCountry()
        run_another()
    elif (case == 14):
        avg_age_resp()
        run_another()
    elif (case == 15):
        avg_edu_resp()
        run_another()
    else:
        print('This is not a valid option.')
        run_another()


def main():
    print ('========= QUERY INTERFACE FOR EBOLA DATABSE =========\n')

    # create views
    print ('...Creating views')
    create_view_SurveyResp_Country()
    create_view_etc_limited()
    
    # print query options menu
    print_menu()
    
    # prompt user for query option
    run_query_case()

    print('\n============== END PROGRAM ==============')
main()
