#!/usr/bin/env python
# coding: utf-8

# In[64]:


import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# import joblib - Used to store trained data 
from sklearn import tree 


music_data = pd.read_csv('C:/Users/angwe/OneDrive/Desktop/school/music.csv')
X = music_data.drop(columns = ['genre'])
y = music_data['genre']

# joblib.dump(model, 'music-recommender.joblib')

# X_train, X_test, y_train, y_test = train_test_split (X, y, test_size = 0.2) - Model training 
# model.fit(X_train, y_train)
# predictions = model.predict(X_test)
# score = accuracy_score(y_test, predictions)
# score

model = DecisionTreeClassifier()
model.fit(X, y)
# tree.export_graphviz(model, out_file = 'Music-recommender.dot', feature_names = ['age', 'gender'], class_names = sorted(y.unique()), label = 'all', rounded = True, filled = True) 

predictions = model.predict([[35,1],[22,0]])
predictions


# In[56]:


predictions


# In[ ]:




