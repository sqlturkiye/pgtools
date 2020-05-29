# Bu programın amacı ,
# İstediğiniz herhangi bir postgreSQL server 'ında istenilen veritabanında istediğiniz veya oluşturduğunuz tabloya CSV dosyanız içerisinde ki verileri Import etmenizi sağlayacak.
# Programda Örnek giriş bilgileri aşağıdadır.
# Veritabanı Adını Giriniz : db_name
# Kullanıcı Adını Giriniz : user
# Şifrenizi Giriniz : Pass
# Host Bilginizi Giriniz : IP /hostname
# Port : 5432
# Import edilecek tabloyu giriniz : test
# Path bilgisini giriniz : /tmp/demo99.csv
# Delimiter : ,

db_name = input("Veritabanı Adını Giriniz : ")
user_name = input("Kullanıcı Adını Giriniz : ")
passwd = input("Şifrenizi Giriniz : ")
host_ = input("Host Bilginizi Giriniz : ")
prt = input("Port : ")
export_query = input("Import edilecek tabloyu giriniz : ")
path_ = input("Path bilgisini giriniz : ")
delimiter_ = input("Delimiter : ")
# export_type = input("CSV ? JSON ?")
import psycopg2

con = psycopg2.connect(database=db_name, user=user_name, password=passwd, host=host_, port=prt)
print("Connecting to Database")
con.autocommit = True
cursor = con.cursor()

s1 = "COPY "
s2 = " FROM "
s3 = " DELIMITER "
s4 = " CSV HEADER ;"
query = s1 + export_query + s2 + "'" + path_ + "'" + s3 + "'" + delimiter_ + "'" + s4
print(query)
cursor.execute(query)
con.commit()
