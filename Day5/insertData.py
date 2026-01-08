import sqlite3

con=sqlite3.connect("mydb.db")

#create cursor object

cursor=con.cursor()
 
cursor.execute('''
        INSERT INTO USER(NAME ,PHONE, EMAIL) VALUES ('JOHN','12173134561','john@gmail.com')

''')

con.commit()
print("data inserted")