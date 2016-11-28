#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 13:01:32 2016

@author: juliannecrea
"""
use ebola;

drop table if exists Major;
create table Major (
  code int auto_increment primary key,
  name varchar(32) not null,
  college varchar(32) not null
);

insert into Major (name, college) values('Finance', 'Business');
insert into Major (name, college) values('Information Systems', 'Business');
insert into Major (name, college) values('Journalism', 'Communications');
insert into Major (name, college) values('Film', 'Communications');
insert into Major (name, college) values('Biology', 'Natural Sciences');
insert into Major (name, college) values('Chemisty', 'Natural Sciences');
insert into Major (name, college) values('Physics', 'Natural Sciences');
insert into Major (name, college) values('Math', 'Natural Sciences');
insert into Major (name, college) values('Computer Science', 'Natural Sciences');
insert into Major (name, college) values('Mechanical Engineering', 'Engineering');
insert into Major (name, college) values('Electrical Engineering', 'Engineering');
insert into Major (name, college) values('Biomedical Engineering', 'Engineering');
insert into Major (name, college) values('Economics', 'Liberal Arts');
insert into Major (name, college) values('Plan II', 'Liberal Arts');
insert into Major (name, college) values('Philosophy', 'Liberal Arts');
insert into Major (name, college) values('Psychology', 'Liberal Arts');

alter table Student add column major_code int;
alter table Student add constraint fk_major_code 
  foreign key (major_code) references Major(code);

-- assign a major to the existing student records
update Student set major_code = 1 where lower(eid) like 'a%' or lower(eid) like 'b%' or lower(eid) like 'c%';
update Student set major_code = 2 where lower(eid) like 'd%' or lower(eid) like 'e%' or lower(eid) like 'f%';
update Student set major_code = 3 where lower(eid) like 'g%' or lower(eid) like 'h%' or lower(eid) like 'i%';
update Student set major_code = 4 where lower(eid) like 'j%' or lower(eid) like 'k%' or lower(eid) like 'l%';
update Student set major_code = 5 where lower(eid) like 'm%' or lower(eid) like 'n%' or lower(eid) like 'o%';
update Student set major_code = 6 where lower(eid) like 'p%' or lower(eid) like 'q%' or lower(eid) like 'r%';
update Student set major_code = 7 where lower(eid) like 's%' or lower(eid) like 't%' or lower(eid) like 'u%';
update Student set major_code = 8 where lower(eid) like 'v%' or lower(eid) like 'w%' or lower(eid) like 'x%';
update Student set major_code = 9 where lower(eid) like 'y%' or lower(eid) like 'z%';

drop table if exists Tweet;
create table Tweet (
  tweet_id varchar(32) generated always 
     as (json_unquote(json_extract(tweet_doc, '$.id_str'))) stored primary key,
  screen_name varchar(32) generated always 
     as (json_unquote(json_extract(tweet_doc, '$.user.screen_name'))) stored,
  created_at datetime generated always 
     as (str_to_date(json_unquote(json_extract(tweet_doc, '$.created_at')), 
     '%a %b %d %H:%i:%s +0000 %Y')) stored,
  tweet_doc json,
  major_code int,
  foreign key (major_code) references Major(code)
);