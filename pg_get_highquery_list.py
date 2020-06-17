# Bu programın amacı ,
# En yavaş 20 sorguyu görüntülememizi sağlar.
# Veritabanı Adını Giriniz : db_name
# Kullanıcı Adını Giriniz : user
# Şifrenizi Giriniz : Pass
# Host Bilginizi Giriniz : IP /hostname
# Port : 5432

db_name = input("Veritabanı Adını Giriniz : ")
user_name = input("Kullanıcı Adını Giriniz : ")
passwd = input("Şifrenizi Giriniz : ")
host_ = input("Host Bilginizi Giriniz : ")
prt = input("Port : ")
import psycopg2

con = psycopg2.connect(database=db_name, user=user_name, password=passwd, host=host_, port=prt)
import pandas as psql

print("Connecting to Database")

con.autocommit = True
cursor = con.cursor()

q1 = "SELECT rolname, calls, total_time, mean_time, max_time, stddev_time, rows, regexp_replace(query," + " '[ \t\n]+', ' ', 'g'" + ") AS query_text FROM pg_stat_statements JOIN pg_roles r ON r.oid = userid WHERE calls > 100 AND rolname NOT LIKE " + "'%backup'" + " ORDER BY mean_time DESC LIMIT 20;"
query = q1
df = psql.read_sql(query, con)
print(df)

con.commit()
con.close()

