import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

df=pd.read_csv(r'C:\DataScience-GenerativeAI-AgenticAI\Practical\DS-GenAi-AgenticAI-Bootcamp\6-month-AI-Roadmap_2025\6. Shared\Ice_cream selling data.csv')
df.head()
df.shape

#Check Null vlaues
print("No's of null value in dataset",df.isnull().sum())

#Graphical representation
sns.scatterplot(data=df,x='temp',y='icecream')
plt.show()

#Apply linear regression on above dataset
x=df[['temp']]
y=df['icecream']

##Train and split data with linear regression
X_train,X_test,Y_train,Y_test=train_test_split(x,y,test_size=0.2,random_state=0)

##Train model with linear regresssion
LR=LinearRegression()
LR.fit(X_train,Y_train)

##Let's draw line
sns.scatterplot(data=df,x='temp',y='icecream')
sns.lineplot(data=df,x='temp',y=LR.predict(x))
plt.show()

# As we get incorrect line
#Let's apply Polynominal regression

PN=PolynomialFeatures() #default degree=2
x=PN.fit_transform(x)

X_train,X_test,Y_train,Y_test=train_test_split(x,y,test_size=0.2,random_state=0)

LR_Poly=LinearRegression()
LR_Poly.fit(X_train,Y_train)

LR_Poly.score(X_train,Y_train)

plt.scatter(df['temp'],df['icecream'])
plt.plot(df['temp'],LR_Poly.predict(x),color='red')
plt.show()

















 



