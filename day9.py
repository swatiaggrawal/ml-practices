import pandas as pd
#open file using pandas
df1=pd.read_csv(r"C:\Users\swati\Desktop\100 days of ml code\datasets\aug_train.csv")
print(df1)

#opening files with url
import requests
from io import StringIO

url = "https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0"}
req=requests.get(url,headers=headers)
data=StringIO(req.text)

df2=pd.read_csv(data)
print(df2)

#sep parameter
df3=pd.read_csv(r"C:\Users\swati\Desktop\100 days of ml code\datasets\movie_titles_metadata.tsv",sep='\t',names=['sno','name','relese_year','rating','votes','genres'])
print(df3)

#index_col
df4=pd.read_csv(r"C:\Users\swati\Desktop\100 days of ml code\datasets\aug_train.csv",index_col='enrollee_id')
print(df4)

#header parameter
df5=pd.read_csv(r"C:\Users\swati\Desktop\100 days of ml code\datasets\test.csv",header=1)
print(df5)

#use_cols
df6=pd.read_csv(r"C:\Users\swati\Desktop\100 days of ml code\datasets\aug_train.csv",usecols=['enrollee_id','gender'])
print(df6)

#squeeze
df7=pd.read_csv(r"C:\Users\swati\Desktop\100 days of ml code\datasets\aug_train.csv",usecols=['gender'],squeeze=True)
print(df7)

#skiprows
df8=pd.read_csv(r"C:\Users\swati\Desktop\100 days of ml code\datasets\aug_train.csv",skiprows=[0,1,2])
print(df8)

#nrows
df9=pd.read_csv(r"C:\Users\swati\Desktop\100 days of ml code\datasets\aug_train.csv",nrows=10)
print(df9)

#encoding parameter
df10=pd.read_csv(r"C:\Users\swati\Desktop\100 days of ml code\datasets\zomato.csv",encoding='latin-1')
print(df10)


"""
skip bad lines
df11=pd.read_csv("aug_train.csv",error_bad_lines=False)
print(df11)
"""

#dtypes
df12=pd.read_csv(r"C:\Users\swati\Desktop\100 days of ml code\datasets\aug_train.csv",dtype={'target':int})
print(df12.info())

#handlingdates

df13=pd.read_csv(r"C:\Users\swati\Desktop\100 days of ml code\datasets\IPL Matches 2008-2020.csv",parse_dates=['date'])
print(df13.info())

#convertors
def rename(name):
    if(name=="Royal Challengers Bangalore"):
        return "RCB"
    else:
        return name 

df14=pd.read_csv(r"C:\Users\swati\Desktop\100 days of ml code\datasets\IPL Matches 2008-2020.csv",converters={'team1':rename},usecols=['team1'])
print(df14)

#na_values
df15=pd.read_csv(r"C:\Users\swati\Desktop\100 days of ml code\datasets\aug_train.csv",na_values=['Male'])
print(df15)

#loading huge data into chunks
df16=pd.read_csv(r"C:\Users\swati\Desktop\100 days of ml code\datasets\aug_train.csv",chunksize=10000)

for chunks in df16:
    print(chunks.shape)