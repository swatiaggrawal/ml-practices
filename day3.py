import numpy as np
from sklearn.impute import SimpleImputer #Configure Scikit Pre-processor Library and import its Imputer function
#handling missing data
imp=SimpleImputer(missing_values=np.nan,strategy="mean")
"""
Create an object imputer of Imputer Class and pass three parameters to parameterized constructor.
    1.missing_values = 'NaN' -> Tells to work upon Null values
    2.strategy -> Tells what to replace the null values with. It can be mean, median, etc.
    3.axis -> Tells to work on rows (1) or columns (0)
"""
imp.fit([[1,2],[np.nan,3],[7,6]]) #Fit the imputer object on the matrix it has to work upon. 
#This matrix must contain only those rows or columns that contain NaN keyword. Remember: b and y are exclusive
X=[[np.nan,3],[6,np.nan],[7,6]] #Transform the Data matrix and store it in the data matrix.
print(X)
print(imp.transform(X))



