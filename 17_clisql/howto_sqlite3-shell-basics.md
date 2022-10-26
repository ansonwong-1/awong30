# how-to :: Sqlite3 Shell Basics
---
## Overview
Sqlite3 is a library that allows users access a database. This how-to will teach the basics of creating and populating tables as well as viewing the information stored.

### Estimated Time Cost: 0.3 hrs

### Prerequisites:

- SQLite3 installed

0. Run `sqlite3 <db name>` in your terminal
1. To create a table, run `CREATE TABLE <table_name>(<field_name0> <optional data type>, <field_name1> ,...);`. You can check if this table exists with `.tables`.
3. To insert values and create a record, run `INSERT INTO <table_name>(<val0>, <val1>""""));`. The order will correspond to the order of the fields when you created the table.
4. To view all records, run `SELECT <field_name> from <table_name>;`. This will return a list of the field values.


### Resources
* [Python Docs](https://docs.python.org/3/library/sqlite3.html)
* [SQLite](https://www.sqlite.org)

---

Accurate as of (last update): 2022-10-24

#### Contributors:  
Nicholas Tarsis pd. 2  
Anson Wong pd. 2  
