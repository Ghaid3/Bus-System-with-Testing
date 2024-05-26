
"""
Created on Fri Mar  3 22:22:53 2023

@author: ruaa
"""

DATA_BASE_NAME = "students.db"

import sqlite3

conn = sqlite3.connect(DATA_BASE_NAME)

# conn.execute('''CREATE TABLE MANEGER
#           (ID            INT     PRIMARY KEY     NOT NULL,
#           NAME           TEXT    NOT NULL,
#           PASSWORD       TEXT    NOT NULL,
#           PHONE_NUMBER   INT );
#           ''')
          
# conn.execute('''CREATE TABLE STUDENT
#                     (ID            INT     PRIMARY KEY     NOT NULL,
#                     NAME           TEXT    NOT NULL,
#                     PHONE_NUMBER   INT,
#                       in_bus       INT);
#                     ''')

# conn.close()

def createManeger(userId, name , password , phone):
    conn = sqlite3.connect(DATA_BASE_NAME)
    cursor = conn.execute("""INSERT INTO MANEGER VALUES (%d,'%s','%s',%d);
                          """%(userId,name,password,phone))
    for row in cursor:
        print(    row)                      
    conn.commit()
    conn.close()

def login(username, password):
    conn = sqlite3.connect(DATA_BASE_NAME)
    result = conn.execute("""SELECT id 
                          from MANEGER where name='%s' 
                          and password='%s'"""%(username,password))
    data = result.fetchall()
    print(data)
    if(len(data)!=1):
        print("not found")
        conn.close()
        return False
    else :
        print(data[0])
        conn.close()
        return True
    

    
def createStudent(userId, name , phone , in_bus):
    conn = sqlite3.connect(DATA_BASE_NAME)
    cursor = conn.execute("""INSERT INTO STUDENT VALUES (%d,'%s',%d ,%d);
                          """%(userId,name,phone,in_bus))
                      
    conn.commit()
    conn.close()

    
def getAllStudents():
    conn = sqlite3.connect(DATA_BASE_NAME)
    cursor = conn.execute("""SELECT * FROM STUDENT ;""")
    studens = cursor.fetchall()
    conn.close()
    return studens

def countStudentsInBus():
    conn = sqlite3.connect(DATA_BASE_NAME)
    cursor = conn.execute("""SELECT ID FROM STUDENT where in_bus = 1;""")
    studensID = cursor.fetchall()
    conn.close()
    return studensID

for student in getAllStudents():
    print (student[0])

def updateStudent(userId,in_bus):
    conn = sqlite3.connect(DATA_BASE_NAME)
    cursor = conn.execute("""update  STUDENT set in_bus=%d where id=%d ;
                          """%(in_bus,userId))
                      
    conn.commit()
    conn.close()

'''New'''
    
    

#createStudent(11,"khalid",99884811,1)
#createStudent(12,"saleh",99889811,1)
# createStudent(3,"mazin",99866811,1)


#createStudent(333,"ahmed",93293815,1)

