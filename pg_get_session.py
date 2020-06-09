# Bu programın amacı ,
# İstediğiniz herhangi bir postgreSQL server 'ında aktif çalışan query leri görmek ve çıktıya ulaşmak.
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

q1 = "SELECT age(clock_timestamp(), query_start) as age, pid, query, usename, wait_event_type, wait_event, datname, client_hostname, client_addr, application_name, state, count(*) over () FROM pg_stat_activity WHERE 1 = 1 AND pid <> pg_backend_pid() AND state <>"
q2 = " 'idle' "
q3 = " order by age desc;"
query = q1 + q2 + q3
df = psql.read_sql(query, con)
print(df)

con.commit()
con.close()