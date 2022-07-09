import pandas as pd
from sklearn.model_selection import train_test_split #Library: sklearn.cross_validation Class: train_test_split
from sklearn.preprocessing import StandardScaler
dt=pd.read_csv(r"C:\Users\swati\Desktop\100 days of ml code\Data.csv")
X=dt.iloc[:,1:-1].values
Y=dt.iloc[:,3].values
#train test split
#Create 4 variables -> 2 for test and 2 for train for both dependent and independent variables
#Argument of train_test_split ->
#All the arrays -> variables matrix
#test_size (between 0 and 1 exclusive denoting percent of dataset to be assigned)
#random_state -> to remove randomness and get same split always
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=0)
print(X_train)
print(X_test)
print(Y_train)
print(Y_test)

#feature scaling
sc=StandardScaler()
X_train=sc.fit_transform(X_train)  # Assign X_train by fitting and transforming scaled object
X_test=sc.transform(X_test)  # No need to fit because test data already takes fitted train data 

print(X_train)
print(X_test)