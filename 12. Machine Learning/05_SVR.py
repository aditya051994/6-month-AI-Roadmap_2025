import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures,StandardScaler


df=pd.read_csv(r'C:\DataScience-GenerativeAI-AgenticAI\Practical\DS-GenAi-AgenticAI-Bootcamp\6-month-AI-Roadmap_2025\6. Shared\bangalore house price prediction OHE-data.csv')
df.head()
df.isnull().sum()

#Banglore House Price Predection
X=df.drop(columns=['price'],axis=1)
Y=df['price']

## train test split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=0)

## Make Normalization 
standard_Scalar=StandardScaler()
standard_Scalar.fit(X_train)
standard_Scalar.transform(X_train)
standard_Scalar.transform(X_test)

## Support Vector Regression
from sklearn.svm import SVR
svr_rbf=SVR( kernel="rbf")
svr_rbf.fit(X_train,Y_train)
svr_rbf.score(X_test, Y_test)
##40%
from sklearn.svm import SVR
svr_poly=SVR( kernel="poly")
svr_poly.fit(X_train,Y_train)
svr_poly.score(X_test, Y_test) # with degreee 2 =75%

svr_poly=SVR( kernel="linear")
svr_poly.fit(X_train,Y_train)
svr_poly.score(X_test, Y_test) 


predicted_df=pd.DataFrame({
    'Actual':X_test,
    'Predcited':svr_poly.predict(X_test)   
    })










