# Bu programın amacı ,
# İstediğiniz herhangi bir postgreSQL server 'ında istediğiniz db de ki tabloların listesini çekmeye yarar.
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

q1 = "SELECT table_schema as schema,  table_name as table FROM information_schema.tables WHERE table_type = " + "'BASE TABLE'" + " AND table_schema NOT IN (" + "'pg_catalog', 'information_schema'" + ") ORDER BY 1, 2;"
query = q1
df = psql.read_sql(query, con)
print(df)

con.commit()
con.close()