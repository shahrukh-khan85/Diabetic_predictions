# import a library
from flask import Flask , render_template, request
import joblib

# instance of an app
app = Flask(__name__)

# loading the model

model = joblib.load("diabetic_79.pkl")

@app.route("/")
def contact():
    return render_template("form.html")


@app.route("/submit", methods=["POST"])
def form_data():
    preg = request.form.get("preg")
    plas = request.form.get("plas")
    pres = request.form.get("pres")
    skin = request.form.get("skin")
    test = request.form.get("test")
    mass = request.form.get("mass")
    pedi = request.form.get("pedi")
    age = request.form.get("age")    

    result = model.predict([[preg, plas, pres, skin, test, mass, pedi, age]])

    if result[0]==0:
        out = "not Diabetic"
    else:
        out = "diabetic"

    return render_template("predict.html", data = f'Person is {out}')

if __name__=="__main__":
    app.run(debug=True)