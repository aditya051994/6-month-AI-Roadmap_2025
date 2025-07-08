import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


dataset=pd.read_csv(r'C:\Users\a864911\OneDrive - ATOS\Desktop\DataSet\Salary_Data.csv')

pd.isnull(dataset).sum()

# INDEPENDENT VARIABLE
X = dataset.iloc[:, :-1]
# DEPENDENT VARIABLE
Y = dataset.iloc[:,-1]  


from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.20,random_state=0)

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X_train,Y_train)

Y_pred=regressor.predict(X_test)


#Compareion Table
comparison=pd.DataFrame({'Actual':Y_test,'Predected':Y_pred})
print(comparison)

#Visualization
plt.scatter(X_test, Y_test, color='red')
plt.xlabel('Year of Exp')
plt.ylabel('Salary')

plt.show()
plt.plot(X_train,regressor.predict(X_train),color='blue')
plt.show()







