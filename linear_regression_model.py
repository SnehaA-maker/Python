import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

dataSet=pd.read_csv("car.csv")
print(dataSet)

x=dataSet[['engine_size']].values
y=dataSet[['price']].values

X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
model=LinearRegression()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
print(y_pred)
