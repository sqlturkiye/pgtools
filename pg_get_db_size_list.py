# Bu programın amacı ,
# İstediğiniz herhangi bir postgreSQL server 'ında bulunan db lerin size bilgilerine erişmenizi sağlamaktır.
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

q1 = "SELECT datname,pg_size_pretty(pg_database_size(datname))as size_pretty,pg_database_size(datname) as size,(SELECT pg_size_pretty (SUM( pg_database_size(datname))::bigint) FROM pg_database)  AS total,((pg_database_size(datname) / (SELECT SUM( pg_database_size(datname)) FROM pg_database) ) * 100)::numeric(6,3) AS pct FROM pg_database ORDER BY datname;"
query = q1
df = psql.read_sql(query, con)
print(df)

con.commit()
con.close()
