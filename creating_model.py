from sklearn.linear_model import LinearRegression
import pandas as pd
import joblib
dataset=pd.read_csv('SalaryData.csv')
y=dataset['Salary']
x=dataset['YearsExperience']
x=x.values
x=x.reshape(-1,1)
y=y.values
y=y.reshape(-1,1)
model=LinearRegression()
model.fit(x,y)
model.predict([[10.8]])
joblib.dump(model,'salary.pk1')
