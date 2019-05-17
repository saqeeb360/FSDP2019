# -*- coding: utf-8 -*-
"""
Created on Thu May 16 18:31:28 2019

@author: Windows
"""

import sqlite3
from pandas import DataFrame

conn = sqlite3.connect ( 'db_University')
c = conn.cursor()

c.execute("DROP TABLE students")
c.execute ("""CREATE TABLE students(
          id INTEGER,
          first  TEXT,
          last TEXT,
          year INTEGER
          )""")

c.execute("INSERT INTO students VALUES (01,'Sylvester', 'Fernandes', 1)")
c.execute("INSERT INTO students VALUES (02,'Yogendra', 'Singh', 2)")
c.execute("INSERT INTO students VALUES (03,'Pradeep', 'Natani',3)")
c.execute("INSERT INTO students VALUES (04,'Kunal', 'Vaid', 3)")
c.execute("INSERT INTO students VALUES (05,'Devendra', 'Shekhawat', 4)")

c.execute("SELECT * FROM students")

df = DataFrame(c.fetchall())  
df.columns = ["id","first","last","year"]

