# Bu programın amacı ,
# İstediğiniz herhangi bir postgreSQL server 'ında istenilen veritabanında sorgunuzun çalıştırılmasını sağlamak. Ve çıktıyı görmek.
# Programda Örnek giriş bilgileri aşağıdadır.
# Veritabanı Adını Giriniz : db_name
# Kullanıcı Adını Giriniz : user
# Şifrenizi Giriniz : Pass
# Host Bilginizi Giriniz : IP /hostname
# Port : 5432
# quer : Bu bölüme görmek istediğiniz datanın query sinizi yazınız.
db_name = input("Veritabanı Adını Giriniz : ")
user_name = input("Kullanıcı Adını Giriniz : ")
passwd = input("Şifrenizi Giriniz : ")
host_ = input("Host Bilginizi Giriniz : ")
prt = input("Port : ")
query = input("Query yazınız : ")
import psycopg2

con = psycopg2.connect(database=db_name, user=user_name, password=passwd, host=host_, port=prt)
import pandas as psql

print("Connecting to Database - Source")

df = psql.read_sql(query, con)

print(df)
