"""
    Data Preprocessing

"""
#import library as alias
import pandas as pd #importing library
dataset=pd.read_csv(r"C:\Users\swati\Desktop\100 days of ml code\Data.csv") #importing dataset
print(dataset)
m=dataset.iloc[1:3,2:4].values #Here, first input x:y is for rows and second input a:b is for columns where y and b are exclusive.
print(m)

