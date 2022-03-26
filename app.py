from flask import Flask, request, render_template
import joblib

app = Flask(_name_)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        purchases = request.form.get("purchases")
        suppcard = request.form.get("suppcard")
        print(purchases, suppcard)
        model1 = joblib.load("CART")
        purchases = float(purchases)
        suppcard = float(suppcard)
        pred1 = model1.predict([[purchases, suppcard]])

        model2 = joblib.load("RF")
        purchases = float(purchases)
        suppcard = float(suppcard)
        pred2 = model1.predict([[purchases, suppcard]])

        model3 = joblib.load("GB")
        purchases = float(purchases)
        suppcard = float(suppcard)
        pred3 = model1.predict([[purchases, suppcard]])

        return (render_template("index.html", result1="1", result2="1", result3="1"))

    else:
        return (render_template("index.html", result1="2", result2="2", result3='2'))


if _name_ == "_main_":
    app.run()
