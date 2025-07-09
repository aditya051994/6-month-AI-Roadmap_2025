import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Step 1: Import Employee salary and experience data using pandas
employee_DS = pd.read_csv(r'C:\Users\a864911\Downloads\Salary_Data.csv')

# Step 2: Identify independent and dependent variables from dataset
# INDEPENDENT VARIABLE
X = employee_DS.iloc[:, :-1]
# DEPENDENT VARIABLE
Y = employee_DS.iloc[:, -1]

# Step 3: Check missing values in dataset
print("Missing value in Employee dataset: ", employee_DS.isnull().sum())
# No missing value

# Step 4: Split dataset into X_train, X_test, Y_train, Y_test
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, train_size=0.80, random_state=0)
# Train data is 80% of actual data; remaining 20% for test

# Step 5: Apply simple linear regression model
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, Y_train)

# Predict salaries for test data
Y_Predict = regressor.predict(X_test)

# Create dataframe for comparison
df = pd.DataFrame({'Actual': Y_test, 'Predict': Y_Predict})
print(df)

# Make plotting
plt.scatter(X_test, Y_test, color='red')
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.title('Simple Linear Regression: Salary vs Experience')
plt.show()

# Predict salary for candidate with 12 years of experience
m_slope = regressor.coef_
c_intercept = regressor.intercept_
# y = mx + c
y_12 = (m_slope * 12) + c_intercept
print("Predicted salary for 12 years of experience:", y_12[0])
#o/p 138531.00


##Calculate Stats
#Mean
print("Mean")
print(employee_DS.mean())
print(employee_DS['Salary'].mean())
print(employee_DS['YearsExperience'].mean())

print("#####Median######")
print(employee_DS.median())

print("###Mode###")
print(employee_DS['Salary'].mode())

print(employee_DS.var())

print("Variance ",employee_DS['Salary'].var())
print("Mean ",employee_DS['Salary'].mean())

print("Variance ",employee_DS['YearsExperience'].var())
print("Mean ",employee_DS['YearsExperience'].mean())

#############Standard Deviatation
print("Standard Deviatation",employee_DS['Salary'].std())
print("Mean Deviatation",employee_DS['Salary'].mean())

### Coefficiant of Variatation

from scipy.stats import variation
print(variation(employee_DS.values))

### co-relatation
employee_DS.corr()

##Skewness
employee_DS.skew()

##Standard Error
employee_DS.sem()


### Z-Score
import scipy.stats as stats
employee_DS.apply(stats.zscore)


###  Degree of Freedom
a=employee_DS.shape[0]
b=employee_DS.shape[1]
print(a," And ",b)
print(a-b)

#SSR
SSR=np.sum((Y_Predict-np.mean(Y))**2)
print("SSR=",SSR)

y=Y[0:6] #Prediction values for test we are using 6 points
SSE=np.sum((y-Y_Predict)**2)
print(SSE)

##SST
SST=SSR+SSE
print(SST)

## R-Square
r_Square=1-(SSR/SST)
print(r_Square)



###
import pickle
#Save train model to desk
fileName='linear_regression_model.pkl'

#Open file with write-binary and dump model
with open(fileName,'wb') as file:
    pickle.dump(regressor,file) 

print("Model has been pickled and saved")

import os
print(os.getcwd())

##bias
bias=regressor.score(X_train, Y_train)
print(bias)

variance=regressor.score(X_test,Y_test)
print(variance)


























































