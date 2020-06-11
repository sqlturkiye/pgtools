# Bu programın amacı ,
# İstediğiniz herhangi bir postgreSQL server 'ında  db lerin Cache Hit Ratio değerlerini elde ederek tuning süreçlerinizi yönetebilmenizi sağlayacak.
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

q1 = "SELECT pg_stat_database.datname, pg_stat_database.blks_read, pg_stat_database.blks_hit, round((pg_stat_database.blks_hit::double precision / (pg_stat_database.blks_read + pg_stat_database.blks_hit +1)::double precision * 100::double precision)::numeric, 2) AS cachehitratio FROM pg_stat_database WHERE pg_stat_database.datname !~ " +  "'^(template(0|1)|postgres)$'" + "::text ORDER BY round((pg_stat_database.blks_hit::double precision / (pg_stat_database.blks_read + pg_stat_database.blks_hit + 1)::double precision * 100::double precision)::numeric, 2) DESC;"
query = q1
df = psql.read_sql(query, con)
print(df)

con.commit()
con.close()

