# Bu programın amacı ,
# İstediğiniz herhangi bir postgreSQL server 'ında db ve kullanıcı bazlı connection sayılarını vermektedir.
# Programda Örnek giriş bilgileri aşağıdadır.
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

q1 = "SELECT usename, count(*) FROM pg_stat_activity GROUP BY 1 ORDER BY 1;"
query = q1
df = psql.read_sql(query, con)
print(df)

con.commit()
con.close()


