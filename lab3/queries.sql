-- SQL Queries

SELECT * FROM ETC WHERE country_name = ['Guinea'] HAVING beds_open > [50];


SELECT AVG(age) as avg_age, AVG(education) as avg_education 
FROM survey_respondent 
WHERE gender = ['M'] 
AND country_name = ['liberia'] 
AND (education != 88 OR education != NULL);

SELECT COUNT(education) as selected_educ_or_higher
FROM survey_respondent
WHERE education >= [6]
AND GENDER = ['F'];