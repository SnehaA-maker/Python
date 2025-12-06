d={"name":"sneha","branch":"ece","clg":"reva"}
print(type(d))
print(d)
d["name"]="ram"
d["city"]="bangalore"
d.pop("city")
print(d)

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

dataSet=pd.read_csv("sneha2.csv")
print(dataSet)

x=dataSet[["ram","display","color"]]
y=dataSet[["price"]]
X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.1,random_state=42)
model=LinearRegression()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
print(X_test)
print(y_pred)