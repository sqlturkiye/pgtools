# Bu programın amacı ,
# Tüm tablolar için Index bilgilerini listeler.
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

q1 = "SELECT cc.relname as table, ci.relname as index FROM pg_index i JOIN pg_class cc ON (cc.oid = i.indrelid) JOIN pg_class ci ON (ci.oid = i.indexrelid) WHERE ci.relname = " + "'idx_normal_distro_name'" + " ORDER BY 1;"
query = q1
df = psql.read_sql(query, con)
print(df)

con.commit()
con.close()

