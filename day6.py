"""
Simple Linear Regression
"""
#libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#reading dataset
dt=pd.read_csv(r"C:\Users\swati\Desktop\100 days of ml code\Salary_Data.csv")
X=dt.iloc[:,:-1].values
y=dt.iloc[:,1].values

#train test split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=0)
"""
#Feature Scaling
sc_X=StandardScaler()
X_train=sc_X.fit_transform(X_train)
X_test=sc_X.transform(X_test)
sc_y=StandardScaler()
y_train=sc_y.fit_transform(y_train)
"""
#fitting Simple linear Regression to the training set
regressor=LinearRegression()
regressor.fit(X_train,y_train)

#prediction
y_pred=regressor.predict(X_test)

#visualization of training results
plt.scatter(X_train,y_train,color='blue')
plt.plot(X_train,regressor.predict(X_train),color="yellow")
plt.title('Salary VS experience (training data)')
plt.xlabel('years of experience')
plt.ylabel('Salary')
plt.show()

#visualization of test results
plt.scatter(X_test,y_test,color="purple")
plt.plot(X_train,regressor.predict(X_train),color="yellow")
plt.title('Salary VS experience (test data)')
plt.xlabel('years of experience')
plt.ylabel('Salary')
plt.show()
