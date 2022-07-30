"""
Working with json (javascript object notation)
"""
import pandas as pd
df=pd.read_json(r"C:\Users\swati\Desktop\100 days of ml code\datasets\train.json")
print(df)

df2=pd.read_json("https://api.exchangerate-api.com/v4/latest/INR")
print(df2)

"""
Working with SQL(structured query language)
"""

import mysql.connector
con=mysql.connector.connect(host='localhost',user='user',password="",database='world')

pd.read_sql_query("SELECT * FROM city",con)