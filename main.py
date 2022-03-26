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
