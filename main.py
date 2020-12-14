from flask import Flask, render_template, request, jsonify, abort
import joblib
# import xgboost
from flask_bootstrap import Bootstrap
import gspread
import oauth2client
from oauth2client.service_account import ServiceAccountCredentials

# Setup Google API
credential = ServiceAccountCredentials.from_json_keyfile_name("credentials.json",
                                                              ["https://spreadsheets.google.com/feeds",                                                               "https://www.googleapis.com/auth/spreadsheets",                                                        "https://www.googleapis.com/auth/drive.file",                                                        "https://www.googleapis.com/auth/drive"])
client = gspread.authorize(credential)

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
    # Insert new data to dataset
    gsheet = client.open("Heart Failure Prediction New Data (Basic)").sheet1
    str_list = list(filter(None, gsheet.col_values(1)))
    new_row = len(str_list)+1

    age = int(request.form['age'])
    sex = 1 if request.form['sex']=='L' else 0
    anaemia = 1 if request.form['anaemia']=='Y' else 0
    diabetes = 1 if request.form['diabetes']=='Y' else 0
    high_blood_pressure = 1 if request.form['high_blood_pressure']=='Y' else 0
    smoking = 1 if request.form['smoking']=='Y' else 0

    row = [age, anaemia, diabetes, high_blood_pressure, sex, smoking]
    gsheet.insert_row(row, new_row)

    # Predict data
    # basic_model = joblib.load('./model/Heart Failure Prediction (Basic).joblib') 


    # predict_df = pd.DataFrame([[age, anaemia, diabetes, high_blood_pressure, sex, smoking]],
                              # columns=['age', 'anaemia', 'diabetes', 'high_blood_pressure', 'sex', 'smoking'])

    # pred = basic_model.predict(predict_df)[0]

    pred = 1
    if pred==1: return render_template("basic_result.html", title='Result (Basic)', pred_result=True)
    else: return render_template("basic_result.html", title='Result (Basic)', pred_result=False)


@app.route("/advanced")
def advanced():
    return render_template("advanced.html", title='Advanced')

@app.route('/predict_advanced', methods=['POST'])
def predict_advanced():
    # Insert new data to dataset
    gsheet = client.open("Heart Failure Prediction New Data (Advanced)").sheet1
    str_list = list(filter(None, gsheet.col_values(1)))
    new_row = len(str_list)+1

    age = int(request.form['age'])
    ejection_fraction = float(request.form['ejection_fraction'])
    serum_creatinine = float(request.form['serum_creatinine'])
    serum_sodium = float(request.form['serum_sodium'])

    row = [age, ejection_fraction, serum_creatinine, serum_sodium]
    gsheet.insert_row(row, new_row)

    # Predict data
    # advanced_model = joblib.load('./model/Heart Failure Prediction (Advanced).joblib') 

    # predict_df = pd.DataFrame([[age, ejection_fraction, serum_creatinine, serum_sodium]],
                              # columns=[['age', 'ejection_fraction', 'serum_creatinine', 'serum_sodium']])

    # pred = advanced_model.predict(predict_df)[0]
    pred = 1
    if pred==1: return render_template("advanced_result.html", title='Result (Advanced)', pred_result=True)
    else: return render_template("advanced_result.html", title='Result (Advanced)', pred_result=False)

if __name__ == "__main__":
    app.run(debug=True)
