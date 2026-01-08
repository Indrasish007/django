import sqlite3

con=sqlite3.connect("mydb.db")

#create cursor object

cursor=con.cursor()

cursor.execute('''
               create table if not exists
                user(
                    user_id integer primary  key autoincrement,
                    name text not null,
                    phone text not null unique,
                    email text not null unique
                    
                )                
            
''')

con.commit()
#close the database connection
con.close()

print("Users table successfully created ")