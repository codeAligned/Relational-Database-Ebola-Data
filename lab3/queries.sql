-- SQL Queries

-- VIEWS
create view SurveyResp_Country (gender, age, education, country_name) as select gender, age, education, country_name from Survey_Respondent;


--------------------------------------------------------------

-- show ETCs in a selected country that have greater than a selected number of open beds
SELECT * FROM ETC 
WHERE country_name = ['Guinea'] 
HAVING beds_open > [50];

-- show average age and average education level of a selected gender population
-- in a selected country
SELECT AVG(age) as avg_age, AVG(education) as avg_education 
FROM survey_respondent 
WHERE gender = ['M'] 
AND country_name = ['liberia'] 
AND (education != 88 OR education != NULL);

-- count number of gender selected, survey respondents that have 
-- a selected educuation level or higher 
SELECT COUNT(education) as selected_educ_or_higher
FROM survey_respondent
WHERE education >= [6]
AND GENDER = ['F'];


-- show Partner Orgs with their longitude/latitude coordinates
SELECT partner_org, latitude, longitude  
FROM Partner_orgs INNER JOIN ETC 
WHERE (latitude != 0 OR longitude != 0);

-- show ETCs by etc_code that selected Organization is working with
SELECT org_name,  etc_code  
FROM Country_Org INNER JOIN ETC 
WHERE org_name = ['UNMEER'];




