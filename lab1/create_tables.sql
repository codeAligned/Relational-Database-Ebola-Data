-- Ebola database
-- SQL script

DROP DATABASE IF EXISTS Ebola;
CREATE DATABASE IF NOT EXISTS Ebola;
USE Ebola;

SELECT 'CREATING DATABASE STRUCTURE' as 'INFO';


DROP TABLE IF EXISTS    Country,
                        ETC,
                        Survey_Respondent,
                        Organization,
                        ETC_Org;

set default_storage_engine = InnoDB;

select CONCAT('storage engine: ', @@default_storage_engine) as INFO;

CREATE TABLE Country (
    country_name    VARCHAR(20)     NOT NULL,
    health_exp      INTEGER         NOT NULL,
    gdp_cap         INTEGER         NOT NULL,
    urban_pop       INTEGER         NOT NULL,
    PRIMARY KEY (country_name)
);

CREATE TABLE ETC (
    etc_code        CHAR(8)         NOT NULL,
    country_name    VARCHAR(20)     NOT NULL,
    partner_org     VARCHAR(20),
    etc_name        VARCHAR(20)     NOT NULL,
    latitude        double          NOT NULL,
    longitude       double          NOT NULL,
    lab_present     CHAR(1)         NOT NULL,
    status          VARCHAR(20)     NOT NULL,
    beds_open       INTEGER         NOT NULL,
    PRIMARY KEY (etc_code),
    FOREIGN KEY (country_name)  REFERENCES Country (country_name)    ON DELETE CASCADE
);

CREATE TABLE Survey_Respondent (
    respid          INTEGER         NOT NULL,
    country_name    VARCHAR(20)     NOT NULL,
    gender          CHAR(1)         NOT NULL,
    age             INTEGER         NOT NULL,
    education       INTEGER         NOT NULL,
    corganizedae    INTEGER         NOT NULL,
    PRIMARY KEY (respid),
    FOREIGN KEY (country_name)  REFERENCES Country (country_name)    ON DELETE CASCADE
);

CREATE TABLE Organization (
    acronym         VARCHAR(20)     NOT NULL,
    country_name    VARCHAR(20)     NOT NULL,
    etc_code        CHAR(8)         NOT NULL,
    org_name        VARCHAR(50)     NOT NULL,
    org_type        VARCHAR(20)     NOT NULL,
    PRIMARY KEY (acronym),
    FOREIGN KEY (country_name)  REFERENCES Country (country_name)    ON DELETE CASCADE
);

CREATE TABLE ETC_Org (
    etc_code        CHAR(8)         NOT NULL,
    acronym         VARCHAR(20)     NOT NULL,
    CONSTRAINT PK_ETC_Org PRIMARY KEY
    (
        etc_code,
        acronym
    ),
    FOREIGN KEY (etc_code) REFERENCES ETC (etc_code),
    FOREIGN KEY (acronym) REFERENCES Organization (acronym)
);
