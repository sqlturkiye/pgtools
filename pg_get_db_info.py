# Bu programın amacı ,
# İstediğiniz herhangi bir postgreSQL server 'ında bulunan db leri hakkında genel bilgileri çekmenizi sağlamaktadır.
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

q1 = "SELECT db.datname,au.rolname as datdba,pg_encoding_to_char(db.encoding) as encoding,db.datallowconn,db.datconnlimit,db.datfrozenxid,tb.spcname as tblspc,db.datacl FROM pg_database db JOIN pg_authid au ON au.oid = db.datdba JOIN pg_tablespace tb ON tb.oid = db.dattablespace ORDER BY 1;"
query = q1
df = psql.read_sql(query, con)
print(df)

con.commit()
con.close()

