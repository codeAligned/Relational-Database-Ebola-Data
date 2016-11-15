# CLI query interface for Ebola database in Python
import pymysql
from db_connect import *

def print_menu():
    print ('Query options:')
    print ('1:  List ETCs in the country __ having more than __ open beds.')
    print ('2:  List average age & education of respondents whose sex=__ and live in __.')
    print ('3:  Count the respondents whose sex=__ and who have at least an education of __.')
    print ('4:  Display partner organizations with their longitude/latitude coordinates.')
    print ('5:  Display a chosen organization __ & codes of the ETCs it is working with.')
    print ('6:  Display all distinct organization types.')
    print ('7:  Display every respondent\'s (whose sex=__) info & their country\'s info.')
    print ('8:  Display every ETC that isn\'t closed & its info/partner organization.')
    print ('9:  List countries in ascending order by GDP.')
    print ('10: Count the respondents (with sex=__, education>=__, and country=__) who think their community was well organized.')
    print ''

def run_query_case():
    case = int(input('Enter query option number: '))
    if (case == 1):
        etc_open_beds()
    elif (case == 2):
        age_edu_sex_country()
    elif (case == 3):
        count_sex_educ()
    elif (case == 4):
        partner_lat_long()
    elif (case == 5):
        org_ETC_codes()
    elif (case == 6):
        distinct_org_types()
    elif (case == 7):
        respondent_country_info()
    elif (case == 8):
        non_closed_ETC_partner()
    elif (case == 9):
        country_gdp()
    elif (case == 10):
        count_organized()
    else:
        print("Sorry, that is not an option.")

# Ten queries functions
def etc_open_beds(): # needs user input on country, beds_open number
    stmt = 'SELECT * FROM ETC WHERE country_name = \'Guinea\' HAVING beds_open > 50 ORDER BY beds_open;'
    run_insert(stmt)
def age_edu_sex_country(): # needs user input on gender, country
    stmt = 'SELECT AVG(age) as avg_age, AVG(education) as avg_education FROM survey_respondent WHERE gender = \'M\' AND country_name = \'liberia\' AND (education != 88 OR education != NULL);'
    run_insert(stmt)
def count_sex_educ(): # needs user input on education, gender
    stmt = 'SELECT COUNT(education) as selected_educ_or_higher FROM survey_respondent WHERE education >= 6 AND GENDER = \'F\';'
    run_insert(stmt)
def partner_lat_long():
    stmt = 'SELECT partner_org, latitude, longitude FROM Partner_orgs INNER JOIN ETC WHERE (latitude != 0 OR longitude != 0);'
    run_insert(stmt)
def org_ETC_codes(): # needs user input on org_name
    stmt = 'SELECT org_name, etc_code FROM Country_Org INNER JOIN ETC WHERE org_name = \'UNMEER\' ORDER BY etc_code;'
    run_insert(stmt)
def distinct_org_types():
    stmt = 'SELECT DISTINCT org_type FROM Organization;'
    run_insert(stmt)
def respondent_country_info(): # needs user input on gender
    stmt = 'SELECT * FROM Country LEFT OUTER JOIN Survey_Respondent on Country.country_name = Survey_Respondent.country_name WHERE gender = \'M\';'
    run_insert(stmt)
def non_closed_ETC_partner():
    stmt = 'SELECT * FROM ETC LEFT OUTER JOIN Partner_org_ETC on ETC.etc_code=Partner_org_ETC.etc_code WHERE status=\'Open\' or status=\'Under Construction\';'
    run_insert(stmt)
def country_gdp():
    stmt = 'SELECT * FROM Country ORDER BY gdp_cap;'
    run_insert(stmt)
def count_organized(): # needs used input for gender, educ, countryName
    stmt = 'SELECT COUNT(corganizedae) as count_organized FROM Survey_Respondent WHERE gender = \'M\' AND corganizedae = 1 AND education >= 3 AND country_name = \'Liberia\';'
    run_insert(stmt)

# Functions to create views
def create_view_SurveyResp_Country():
    stmt = 'CREATE VIEW SurveyResp_Country (gender, age, education, country_name) AS SELECT gender, age, education, country_name FROM Survey_Respondent;'
    run_insert(stmt)

def create_view_etc_limited():
    stmt = 'CREATE VIEW ETC_limited (etc_name, country_name, partner_org) AS SELECT etc_name, country_name, partner_orgFROM ETC, Partner_Orgs;'
    run_insert(stmt)

# Functions to run queries
def etc_open_beds():
    stmt = "SELECT * FROM ETC WHERE country_name = 'Guinea' HAVING beds_open > 50 ORDER BY beds_open;"
    run_insert(stmt)

def age_edu_male_liberia():
    stmt = "SELECT AVG(age) as avg_age, AVG(education) as avg_education FROM survey_respondent WHERE gender = 'M' AND country_name = 'liberia' AND (education != 88 OR education != NULL);"
    run_insert(stmt)

def count_female_edu6():
    stmt = "SELECT COUNT(education) AS number_females FROM survey_respondent WHERE education >= 6 AND GENDER = 'F';"
    run_insert(stmt)


# run_insert error checking
# ...


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
