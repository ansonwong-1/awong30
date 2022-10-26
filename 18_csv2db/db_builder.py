#Flying Turtles | Nicholas Tarsis, Anson Wong
#SoftDev
#K18 -- (Python + SQLite)3
#2022-10-25
#time spent: 0.5 hours

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================
db.execute("DROP TABLE if exists students")
db.execute("DROP TABLE if exists courses")

c.execute("CREATE TABLE students(name TEXT, age INTEGER, _id INTEGER)")
c.execute("CREATE TABLE courses(name TEXT, age INTEGER, _id INTEGER)")


# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >


with open("students.csv") as students:
    students = csv.DictReader(students)
    for i in students:
        name = i["name"]
        age = int(i["age"])
        _id = int(i["id"])
        #c.execute("""INSERT INTO student VALUES({name},"age","_id")""")#Use triple quotes to allow for "" with the TEXT value
        c.execute("INSERT INTO students VALUES(?, ?, ?)",(name,age,_id))#Use triple quotes to allow for "" with the TEXT value
    names = c.execute("SELECT * from students")
    print(names.fetchall())
    #print(name,age,_id)

print("\n\n\n\n\n\n\n\n\n")
with open("courses.csv") as courses:
    courses = csv.DictReader(courses)
    for i in courses:
        code = i["code"]
        mark = i["mark"]
        _id = i["id"]
        c.execute("INSERT INTO courses VALUES(?, ?, ?)",(code,mark,_id))#Use triple quotes to allow for "" with the TEXT value
    codes = c.execute("SELECT * from courses")
    print(codes.fetchall())
        #print(code,mark,_id)

command = ""          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database
