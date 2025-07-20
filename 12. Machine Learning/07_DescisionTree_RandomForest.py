import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


dataset=pd.read_csv(r'C:\DataScience-GenerativeAI-AgenticAI\Practical\DS-GenAi-AgenticAI-Bootcamp\6-month-AI-Roadmap_2025\6. Shared\emp_sal.csv')

X = dataset.iloc[:, 1:2].values
y = dataset['Salary']


from sklearn.tree import DecisionTreeRegressor
dt_reg=DecisionTreeRegressor()
dt_reg.fit(X, y)

dt_pred=dt_reg.predict([[6]])
print(dt_pred)

## Random forest
from sklearn.ensemble import RandomForestRegressor
rf_reg=RandomForestRegressor() ##random_state=0 to stop getting multiple output
rf_reg.fit(X, y)

rf_pred=rf_reg.predict([[6]])
print(rf_pred)

##FeatureScaling
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,y,test_size=0.2,random_state=0)


from sklearn.preprocessing import StandardScaler
standard_scaler=StandardScaler()
X_train_SS=standard_scaler.fit_transform(X_train)

##Min/Max Scaling
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,y,test_size=0.2,random_state=0)


from sklearn.preprocessing import minmax_scale
minmax=StandardScaler()
X_train_MM=minmax.fit_transform(X_train)

















    



