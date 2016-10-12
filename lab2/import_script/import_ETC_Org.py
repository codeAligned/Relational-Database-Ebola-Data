# Import ETC_Org junction table

import pymysql

db = pymysql.connect (host   ="localhost", # your host, for this lab, you don't need to change
                      user   = "root",     # your username
                      passwd = "",         # your password
                      db     = "ebola")    # name of the database

cur_etc = db.cursor()
cur_org = db.cursor()
cur_jnc = db.cursor()


for row in cur_jnc.fetchall():
    for row in cur_etc.fetchall():
        cur_etc.execute("SELECT etc_code INTO @ecode FROM ETC")
    for row in cur_org.fetchall():
        cur_org.execute("SELECT org_name INTO @oname FROM Organization")
    cur_jnc.execute("INSERT INTO ETC_Org (etc_code, org_name) VALUES (@ecode, @oname)")


db.close()
