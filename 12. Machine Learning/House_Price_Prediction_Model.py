import pandas as pd
import seaborn as sns
import matplot.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score

df=pd.read_csv(r'C:\Users\a864911\OneDrive - ATOS\Desktop\GenAi+AgenticAI\Mechine Learning\HOUSING REGRESSOR\USA_Housing.csv')
df.isnull().sum()

X=df.drop(columns=['Address','Price'])
y=df.iloc[:,-2]

#Check how data 
sns.pairplot(data=df)
plt.show()
#Train model 
X_train,X_test,Y_train,Y_test=train_test_split(X,y,test_size=0.2,random_state=0)

##Lineaer Regression
linear_regression=LinearRegression()
linear_regression.fit(X_train,Y_train)
##Score 
linear_regression.score(X_test,Y_test)
##Error checking
MAE=mean_absolute_error(Y_test, linear_regression.predict(X_test))
MAE
MSE=mean_squared_error(Y_test, linear_regression.predict(X_test))
MSE







