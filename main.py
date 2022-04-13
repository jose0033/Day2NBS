import pandas as pd
from sklearn import tree
from sklearn.metrics import confusion_matrix
import joblib

df = pd.read_csv(r"CreditCardUpgrade.csv")

x = df.loc[:, ["Purchases", "SuppCard"]]

#print(x)

y = df.loc[:, ["Upgraded"]]

#print(y)

model = tree.DecisionTreeClassifier(max_depth=2)

model.fit(x,y)

pred = model.predict(x)

#print(pred)

cm = confusion_matrix(y, pred)

print(cm)

joblib.dump(model, "CART")

#print("Done")

#2nd model-Random Forest

from sklearn.ensemble import RandomForestClassifier

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(x,y, random_state=204)

from sklearn import tree

model = tree.DecisionTreeClassifier(random_state=204)
model.fit(X_train, Y_train)

pred = model.predict(X_train)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_train, pred)
print(cm)

accuracy = (cm[0,0] + cm[1,1]/(sum(sum(cm))))

print(accuracy)

pred = model.predict(X_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test, pred)
print(cm)
accuracy = (cm[0,0] + cm[1,1])/(sum(sum(cm)))
print(accuracy)

model = RandomForestClassifier(ccp_alpha=0.0384)
model.fit(x,y)
pred = model.predict(x)
cm = confusion_matrix(y,pred)
print(cm)
joblib.dump(model, "RF")

#3rd model-GradientBoosting

from sklearn.ensemble import GradientBoostingClassifier
model = GradientBoostingClassifier(min_samples_split=30, random_state=260322)
model.fit(x,y)
pred = model.predict(x)
cm = confusion_matrix(y,pred)
print(cm)
joblib.dump(model,"GB")
