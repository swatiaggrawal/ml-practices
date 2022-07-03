"""
    Data Preprocessing

"""
#import library as alias
import pandas as pd #importing library
from sklearn.impute import SimpleImputer #Configure Scikit Pre-processor Library and import its Imputer function
dataset=pd.read_csv(r"C:\Users\swati\Desktop\100 days of ml code\Data.csv") #importing dataset
print(dataset)
m=dataset.iloc[1:3,2:4].values #Here, first input x:y is for rows and second input a:b is for columns where y and b are exclusive.
print(m)
#handling missing data
imputer=SimpleImputer(missing_values='NaN',strategy='mean')
""" Create an object imputer of Imputer Class and pass three parameters to parameterized constructor.
    1.missing_values = 'NaN' -> Tells to work upon Null values
    2.strategy -> Tells what to replace the null values with. It can be mean, median, etc.
    3.axis -> Tells to work on rows (1) or columns (0)
"""
dataset = dataset.reset_index()
X=dataset.iloc[:,:-1].values
y = dataset.iloc[:, 3].values
imputer=imputer.fit(X[:,1:3]) #Fit the imputer object on the matrix it has to work upon. 
#This matrix must contain only those rows or columns that contain NaN keyword. Remember: b and y are exclusive
X[:,1:3]=imputer.transform(X[:,1:3])#Transform the Data matrix and store it in the data matrix.
print(X)
