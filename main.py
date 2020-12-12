from flask import Flask, render_template, request
import joblib
# import xgboost
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/basic")
def basic():
    return render_template("basic.html", title='Basic')

@app.route('/predict_basic', methods=['POST'])
def predict_basic():
    basic_model = joblib.load('./model/Heart Failure Prediction (Basic).joblib') 

    age = int(request.form['age'])
    sex = 1 if request.form['sex']=='L' else 0
    anaemia = 1 if request.form['anaemia']=='Y' else 0
    diabetes = 1 if request.form['diabetes']=='Y' else 0
    high_blood_pressure = 1 if request.form['high_blood_pressure']=='Y' else 0
    smoking = 1 if request.form['smoking']=='Y' else 0

    predict_df = pd.DataFrame([[age, anaemia, diabetes, high_blood_pressure, sex, smoking]],
                              columns=['age', 'anaemia', 'diabetes', 'high_blood_pressure', 'sex', 'smoking'])

    pred = basic_model.predict(predict_df)[0]

    # pred = 1
    if pred==1: return render_template("basic_result.html", title='Result (Basic)', pred_result=True)
    else: return render_template("basic_result.html", title='Result (Basic)', pred_result=False)


@app.route("/advanced")
def advanced():
    return render_template("advanced.html", title='Advanced')

@app.route('/predict_advanced', methods=['POST'])
def predict_advanced():
    advanced_model = joblib.load('./model/Heart Failure Prediction (Advanced).joblib') 

    age = int(request.form['age'])
    ejection_fraction = float(request.form['ejection_fraction'])
    serum_creatinine = float(request.form['serum_creatinine'])
    serum_sodium = float(request.form['serum_sodium'])

    predict_df = pd.DataFrame([[age, ejection_fraction, serum_creatinine, serum_sodium]],
                              columns=[['age', 'ejection_fraction', 'serum_creatinine', 'serum_sodium']])

    pred = advanced_model.predict(predict_df)[0]

    if pred==1: return render_template("advanced_result.html", title='Result (Advanced)', pred_result=True)
    else: return render_template("advanced_result.html", title='Result (Advanced)', pred_result=False)

if __name__ == "__main__":
    app.run(debug=True)
