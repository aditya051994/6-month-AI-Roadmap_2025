import numpy as np
import pandas as pd

df=pd.read_csv(r'C:\Users\a864911\OneDrive - ATOS\Desktop\GenAi+AgenticAI\ML\10th- mlr\10th- mlr\MLR\Investment.csv')

X=df.iloc[:,0:4]
y=df.iloc[:,-1]

X=pd.get_dummies(X,dtype=int)


from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,y,test_size=0.2,random_state=0)

from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X_train,Y_train)

Y_Predict=regressor.predict(X_test)

df_Compare=pd.DataFrame({
    'Actual Value':Y_test,
    'Predicted':Y_Predict
    })

bias=regressor.score(X_train,Y_train)
print(bias)
variance=regressor.score(X_test,Y_test)
print(variance)

#6 values as we use formula y=mx+c so for 6 test set it generate 6 numbers
slop=regressor.coef_
slop

intercept=regressor.intercept_
intercept

#y=b0+b1x1+b2x3...... (Multple linear regression)
#Appending 1 as constant

#X=np.append(np.ones((50,1)).astype(int),axis=1,values=X)    
X=np.append(np.ones((50,1)),axis=1,values=X)  

#We have to find where should i invest so that get profit

import statsmodels.api as sm
X_opt=X[:,[0,1,2,3,4,5]]
regressor_OLS=sm.OLS(endog=y,exog=X_opt).fit()
regressor_OLS.summary() 


import statsmodels.api as sm
X_opt=X[:,[0,1,2,3,5]]
regressor_OLS=sm.OLS(endog=y,exog=X_opt).fit()
regressor_OLS.summary()  

import statsmodels.api as sm
X_opt=X[:,[0,1,2,3]]
regressor_OLS=sm.OLS(endog=y,exog=X_opt).fit()
regressor_OLS.summary()  

#P value are greater than 0.05 so we are removinf
import statsmodels.api as sm
X_opt=X[:,[0,1,2]]
regressor_OLS=sm.OLS(endog=y,exog=X_opt).fit()
regressor_OLS.summary()  

import statsmodels.api as sm
X_opt=X[:,[0,1]]
regressor_OLS=sm.OLS(endog=y,exog=X_opt).fit()
regressor_OLS.summary()  

#Digital Marketing can invest money













































