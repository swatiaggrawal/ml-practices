"""
    Data Preprocessing
"""
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder,OneHotEncoder

dt=pd.read_csv(r"C:\Users\swati\Desktop\100 days of ml code\Data.csv")
X=dt.iloc[:,:-1].values
y=dt.iloc[:,0].values
print(dt)
#handle missing data
imputer=SimpleImputer(missing_values=np.nan,strategy='mean')
imputer=imputer.fit(X[:,1:3])
X[:,1:3]=imputer.transform(X[:,1:3])
print(X);
print(y)

#Encoding categorical data
#encoding the independent variable
# Encode 1 variable at a time
# Encoding independent variable -> Encode then convert to Dummy variable
labelEncoder_X=LabelEncoder()
X[:,0]=labelEncoder_X.fit_transform(X[:,0])  # All rows and column number 0
Onehotencoder=OneHotEncoder()
X=Onehotencoder.fit_transform(X).toarray()
#encoding dependent variable
# Encode dependent variable -> only encode
labelencoder_y=LabelEncoder()
y=labelencoder_y.fit_transform(y)
print(X[:,:])
print(y)
