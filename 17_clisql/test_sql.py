# Flying Turtles | Nicholas Tarsis, Anson Wong
# SoftDev
# K17 -- Starting sqlite3 Shell Basics
# 2022-10-25
#time spent: 0.5

import sqlite3 #enable SQLite operations

#open db if exists, otherwise create
db = sqlite3.connect("foo") #connection to database foo

#needed to execute statements & fetch results from queries
c = db.cursor() #facilitate db ops

#adds a table to database by executing "CREATE TABLE <name> (<col name> <data type>)" "
c.execute("CREATE TABLE roster(name TEXT, userid INTEGER)")
c.fetchone()
c.execute("INSERT INTO roster VALUES("frist", 19) ")

db.commit() #save changes
db.close()
