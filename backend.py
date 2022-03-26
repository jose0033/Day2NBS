import joblib

app = Flask(_name_)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return(render_template("index.html", result1="1", result2="1", result3="1"))

    else:
        return(render_template("index.html", result1="2", result2="2", result3='2'))


if _name_ == "_main_":
    app.run()