#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
data=pd.read_csv(r"C:\Users\ashis\Downloads\salary_data.csv")
print(data)
X=data[["YearsExperience"]]
y=data["Salary"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model=LinearRegression()
model.fit(X_train,y_train)
predictions=model.predict(X_test)
print("Actual:", list(y_test))
print("Predicted:", predictions)
score = r2_score(y_test, predictions)
print("R2 score:", score)
print("Salary for 12 years:", model.predict([[12]]))
plt.scatter(X, y, color="blue")
plt.plot(X, model.predict(X), color="red")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.title("Salary Prediction Model")
plt.show()


# In[ ]:




