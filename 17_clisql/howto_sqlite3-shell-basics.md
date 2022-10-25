# how-to :: Sqlite3 Shell Basics
---
## Overview
Sqlite3 is a library that allows users access a database. This how-to will teach the basics of creating and populating tables as well as viewing the information stored.

### Estimated Time Cost: 0.3 hrs

### Prerequisites:

- Python installed
- Basic Python Knowledge

0. In a python file of your choice, `import sqlite3`.
1. Connect to a database and create a cursor for it with `<connection_name> = sqlite3.connect("<database name>")` and `<cursor_name> = <connection_name>.cursor()`. The database named will be created if it does not already exist. An example of this is:
  ```
  db = sqlite3.connect("foo")
  c = db.cursor()
  ```
2. To create a table, run `<cursor_name>.execute("CREATE TABLE <table_name>(<col_name0> <optional data type>, <col_name1> ,...)")`. An example of this is:
```
c.execute("CREATE TABLE roster(name TEXT, userid INTEGER)")
```
You can check if the table exists by doing `<var> = <cursor_name>.execute("SELECT name from sqlite_master")` and `print(<var>.fetchone())`, which will fetch the first table name or `print(<var>.fetchall())` which will fetch all the table names. Keep in mind that the order matters and if you execute a different statement before printing, it will return what you executed most recently as execute only executes a single statement at a time.
3. To insert values, run `<cursor_name>.execute("""INSERT INTO <table_name>(<val0>, <val1>""""));`. The triple quotes make it so you can have single quotes, which you need if you've specified a column data type as TEXT. The order will correspond to the order of the columns.
4. To view these records, run `<var>= <cursor_name>.execute("SELECT <col_name> from <table_name>")` and `print(<var>.fetchall())`. THis will return a list of the column values.


### Resources
* [Python Docs](https://docs.python.org/3/library/sqlite3.html)
* [SQLite](https://www.sqlite.org)

---

Accurate as of (last update): 2022-10-24

#### Contributors:  
Nicholas Tarsis pd. 2  
Anson Wong pd. 2  
