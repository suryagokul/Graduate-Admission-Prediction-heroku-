import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import sklearn
import pickle
import flask

print(sklearn.__version__)

print(pd.__version__)

print(flask.__version__)

df = pd.read_csv("Admission_Predict_Ver1.1.csv")

df.drop('Serial No.', axis=1, inplace=True)

df.columns = ['GRE_Score', 'TOEFL_Score', 'University_Rating', 'SOP', 'LOR', 'CGPA', 'Research', 'Chance of Admit']

X = df.drop(labels='Chance of Admit', axis=1)

y = df['Chance of Admit']

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=10, test_size=0.3)

LR = LinearRegression()

LR.fit(X_train, y_train)

# Saving model to disk
pickle.dump(LR, open('model.pkl', 'wb'))

