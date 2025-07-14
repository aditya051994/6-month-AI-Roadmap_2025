import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv(r'C:\DataScience-GenerativeAI-AgenticAI\Practical\DS-GenAi-AgenticAI-Bootcamp\6-month-AI-Roadmap_2025\6. Shared\House_data.csv')
df.columns
df_updated=df.drop(['id', 'date', 'bathrooms', 'floors', 'waterfront', 'view', 'condition','grade','sqft_basement', 'yr_built', 'yr_renovated', 'zipcode',
       'lat', 'long', 'sqft_living15', 'sqft_lot15'],axis=1)


print('Number of null values',df_updated.isna().sum())

### Identify X and Y value

X=df_updated.iloc[:,1:]
Y=df_updated.iloc[:,0]

#Split mode in train and split
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.20,random_state=0)


#Choose simple linear regression model

from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(X_train,Y_train)

Y_Predict=model.predict(X_test)

#Create dataframe to compare test and prediction values
df_Compare=pd.DataFrame(
    {'Actual': Y_test,
     'Predicted':Y_Predict     
     })

bias=model.score(X_train,Y_train)
print(bias)
variance=model.score(X_test,Y_test)
print(variance)

from sklearn.metrics import r2_score,mean_squared_error
r_sq=r2_score(Y_test,Y_Predict)
print(r_sq)
MSE=mean_squared_error(Y_test, Y_Predict)
print(MSE)




