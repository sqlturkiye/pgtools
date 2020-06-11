# Bu programın amacı ,
# Tüm tablolar için Constraint bilgilerini listeler.
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

q1 = "SELECT rel.relname, con.conname, con.contype, con.consrc FROM pg_class rel JOIN pg_constraint con ON (con.conrelid = rel.oid)  ORDER by relname, contype, conname;"
query = q1
df = psql.read_sql(query, con)
print(df)

con.commit()
con.close()

