import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report
iris = load_iris()
df=pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target']=iris.target
print(df.head())

x=df.drop('target', axis=1)
y=df['target']
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)
model=GaussianNB()
model.fit(X_train, y_train)

y_pred=model.predict(X_test)
accuracy=accuracy_score(y_test, y_pred)
print('accuracy:', accuracy)
print('Classification Report:\n', classification_report(y_test, y_pred))