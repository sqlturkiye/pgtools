# PostgreSQL Connection Check
db_name= input("Veritabanı Adını Giriniz : ")
user_name = input("Kullanıcı Adını Giriniz : ")
passwd = input("Şifrenizi Giriniz : ")
host_ = input("Host Bilginizi Giriniz : ")
prt = input("Port : ")
export_query = input("Export edilecek query ya da tabloyu giriniz : ")
path_ = input("Path bilgisini giriniz : ")
delimiter_ = input("Delimiter : ")
#export_type = input("CSV ? JSON ?")
import psycopg2
con = psycopg2.connect(database=db_name, user=user_name, password=passwd, host=host_, port=prt)
print("Connecting to Database")
con.autocommit = True
cursor = con.cursor()
#    database="demo", user='sqltr_usr', password='Abc12345', host='', port='5432'

s1 = "COPY "
s2 = " TO "
s3 = " DELIMITER "
s4 = " CSV HEADER ;"
query = s1+export_query+s2+"'"+path_+"'"+s3+"'"+delimiter_+"'"+s4
print(query)
cursor.execute(query)
con.commit()

# Bu programın amacı , İstediğiniz herhangi bir postgreSQL server 'ında istenilen veritabanında sorgu ve tabloyu istediğiniz path altında export unu csv olarak çıkarmak.
# Programda Örnek giriş bilgileri aşağıdadır.
# Veritabanı Adını Giriniz : demo
# Kullanıcı Adını Giriniz : sqltr_usr
# Şifrenizi Giriniz : Abc12345
# Host Bilginizi Giriniz : IP /hostname
# Port : 5432
# Export edilecek query ya da tabloyu giriniz : test
# Path bilgisini giriniz : /tmp/demo99.csv
# Delimiter : ,
