# Functions for use with query_interface.py
import pymysql
from db_connect import *

# Query functions on base tables
def etc_open_beds(): # user input on country, beds_open
    country = raw_input('Enter Country: ')
    beds_open = raw_input('Enter minimum number of open beds: ')
    stmt = "SELECT * FROM ETC WHERE country_name = '" + country + "' HAVING beds_open > " + beds_open + " ORDER BY beds_open;"
    run_insert(stmt)

def age_edu_sex_country(): # user input on gender, country
    gender = raw_input('Enter gender (M/F): ')
    country = raw_input('Enter country: ')
    stmt = "SELECT AVG(age) as avg_age, AVG(education) as avg_education FROM survey_respondent WHERE gender = '" + gender + "' AND country_name = '" + country + "' AND (education != 88 OR education != NULL);"
    run_insert(stmt)

def count_sex_educ(): # user input on education, gender
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


# Query functions on views
def surveyresp_country_byAge():
    stmt = 'SELECT * FROM surveyresp_country ORDER BY age;'
    run_insert(stmt)

def etc_limited_byName():
    stmt = 'SELECT etc_name, partner_org FROM etc_limited ORDER BY etc_name;'
    run_insert(stmt)

def partner_org_limited_byCountry(): # needs user input for partner_org
    stmt = 'SELECT etc_name, partner_org, country.country_name, gdp_cap FROM etc_limited INNER JOIN country WHERE partner_org = \'World Health Organization\' ORDER BY country.country_name;'
    run_insert(stmt)

def avg_age_resp(): # needs user input for gender
    stmt = 'SELECT gender, AVG(age) AS average_age FROM surveyresp_country GROUP BY gender HAVING gender = \'F\';'
    run_insert(stmt)

def avg_edu_resp(): # needs user input for gender
    stmt = 'SELECT gender, AVG(education) AS average_education FROM surveyresp_country GROUP BY gender HAVING gender = \'M\';'
    run_insert(stmt)



# Functions to create views
def create_view_SurveyResp_Country():
    stmt = 'CREATE VIEW SurveyResp_Country (gender, age, education, country_name) AS SELECT gender, age, education, country_name FROM Survey_Respondent;'
    run_insert(stmt)

def create_view_etc_limited():
    stmt = 'CREATE VIEW ETC_limited (etc_name, country_name, partner_org) AS SELECT etc_name, country_name, partner_org FROM ETC, Partner_Orgs;'
    run_insert(stmt)
