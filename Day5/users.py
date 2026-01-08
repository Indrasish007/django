import sqlite3

class Users:
    def __init__(self,name,email,city):
        self.__name=name
        self.__email=email
        self.__city=city

    def create_table(self):
        con=sqlite3.connect("mydb2.db")
        cursor=con.cursor()
        SQL='''
            create table if not exists
            users(
            user_id integer primary key autoincrement,
            name text not null,
            email text not null unique,
            city text default 'Kolkata'
            )
        '''
        cursor.execute(SQL)
        con.commit()
        con.close()
        #print("Table created successfully")

    def addUsers(self):
        con=sqlite3.connect("mydb2.db")
        insertCursor=con.cursor()
        SQL='''
            insert into users(name,email)values(?,?)
        '''
        insertCursor.execute(SQL,(self.__name,self.__email))
        con.commit()
        con.close()
        print("User Added Successfully")
    def addUsersWithCity(self):
        con=sqlite3.connect("mydb2.db")
        insertCursor=con.cursor()
        SQL='''
            insert into users(name,email,city)values(?,?,?)
        '''
        insertCursor.execute(SQL,(self.__name,self.__email,self.__city))
        con.commit()
        con.close()
        print("User Added Successfully")
    def getUserById(self,uid):
        con=sqlite3.connect("mydb2.db")
        readCursor=con.cursor()
        readCursor.execute('''
            select * from users where user_id=?
        ''',(uid,))
        user=readCursor.fetchone()
        if user:
            print(f"Name: {user[1]} Email: {user[2]}")
        else:
            print("No user Founded")
    def getAllUsers(self):
        con=sqlite3.connect("mydb2.db")
        readCursor=con.cursor()
        readCursor.execute('''
            select * from users
        ''')
        users=readCursor.fetchall()
        for user in users:
            print(user[1],user[2],user[3])
        con.close()
    def updateUsers(self,user_id):
        con=sqlite3.connect("mydb2.db")
        updateCursor=con.cursor()
        SQL='''
            update users set
                    name=?,
                    email=?,
                    city=?
                    where user_id=?
        '''
        updateCursor.execute(SQL,(self.__name,self.__email,self.__city,user_id))
        con.commit()
        con.close()
        print("User Updated Successfully")
    def deleteUser(self,user_id):
        con=sqlite3.connect("mydb2.db")
        delCursor=con.cursor()
        SQL='''
            delete from users where user_id=?
        '''
        delCursor.execute(SQL,(user_id,))
        con.commit()
        con.close()
        print("User Deleted Successfully")
#Mainscripts
choice=int(input('''
                1.Create new user.
                2.Read User By UserID.
                3.Read All Users.
                4.Update an User.
                5.Delete an User.
'''))
myUser=Users("","","")
myUser.create_table()

if choice==1:
    name=str(input("Enter name: "))
    email=str(input("Enter email: "))
    #at run time left blank
    city=str(input("Enter city: "))
    myUser=Users(name,email,city)
    if city=="" or city==None:
        myUser.addUsers()
    else:
        myUser.addUsersWithCity()
elif choice==2:
    user_id=int(input("Enter To View Details: "))
    myUser.getUserById(user_id)
elif choice==3:
    myUser.getAllUsers()
elif choice==4:
    name=input("Enter Name: ")
    email=input("Enter Email:")
    city=input("Enter City: ")
    myUser=Users(name,email,city)
    user_id=int(input("Enter User ID  : "))
    myUser.updateUsers(user_id)
elif choice==5:
    user_id=int(input("Enter User ID: "))
    myUser.deleteUser(user_id)