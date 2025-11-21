from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import joblib
import pandas as pd
import numpy as np
import os
import json

CSV_PATH = "data/Salary_Data_Procesada_Numerica.csv"
REG_MODEL_PATH = "regresion_model.pkl"
REG_SCALER_PATH = "scaler_regresion.pkl"
KNN_MODEL_PATH = "knn_model.pkl"
KNN_SCALER_PATH = "scaler_knn.pkl"
MLP_MODEL_PATH = "mlp_model.pkl"
MLP_SCALER_PATH = "scaler_mlp.pkl"
JOB_TITLES_JSON_PATH = "data/job_titles.json"

app = Flask(__name__, static_folder="frontend")
CORS(app)

df = pd.read_csv(CSV_PATH, sep=";").dropna()

salary_labels = ["Muy bajo","Bajo","Medio","Alto","Muy alto"]
bins = df["Salary"].quantile([0.0,0.2,0.4,0.6,0.8,1.0]).tolist()

X_full = df.drop(columns=["Salary"])
X_full_ohe = pd.get_dummies(X_full, columns=["Job Title"], drop_first=True)
ohe_columns = X_full_ohe.columns.tolist()

try:
    with open(JOB_TITLES_JSON_PATH, "r", encoding="utf-8") as f:
        job_title_dict = json.load(f)
        job_titles_json = sorted(job_title_dict.keys())
except:
    job_title_dict = {}
    job_titles_json = sorted(df["Job Title"].unique().tolist())

job_title_reverse = {v: k for k, v in job_title_dict.items()}

job_titles_reg = []
for num in sorted(df["Job Title"].unique()):
    if num in job_title_reverse:
        job_titles_reg.append(job_title_reverse[num])
if not job_titles_reg:
    job_titles_reg = job_titles_json

def safe_load(path):
    if os.path.exists(path):
        return joblib.load(path)
    return None

reg_model = safe_load(REG_MODEL_PATH)
reg_scaler = safe_load(REG_SCALER_PATH)
knn_model = safe_load(KNN_MODEL_PATH)
knn_scaler = safe_load(KNN_SCALER_PATH)
mlp_model = safe_load(MLP_MODEL_PATH)
mlp_scaler = safe_load(MLP_SCALER_PATH)

def build_feature_row(payload):
    row = {
        "Age": [payload.get("Age")],
        "Gender": [payload.get("Gender")],
        "Education Level": [payload.get("Education Level")],
        "Job Title": [payload.get("Job Title")],
        "Years of Experience": [payload.get("Years of Experience")]
    }
    df_row = pd.DataFrame(row)
    df_ohe = pd.get_dummies(df_row, columns=["Job Title"], drop_first=True)
    df_ohe = df_ohe.reindex(columns=ohe_columns, fill_value=0)
    return df_ohe

def reg_pred_to_category(value):
    return str(pd.cut([value], bins=bins, labels=salary_labels, include_lowest=True)[0])

@app.route("/metadata", methods=["GET"])
def metadata():
    return jsonify({
        "job_titles_json": job_titles_json,
        "job_titles_reg": job_titles_reg
    })

@app.route("/predict", methods=["POST"])
def predict():
    content = request.get_json()
    model_name = content.get("model")
    features = content.get("features")

    if model_name == "knn":
        X_row = build_feature_row(features)
        X_scaled = knn_scaler.transform(X_row)
        pred = knn_model.predict(X_scaled)
        return jsonify({"model":"knn", "label": str(pred[0])})

    if model_name == "mlp":
        X_row = build_feature_row(features)
        X_scaled = mlp_scaler.transform(X_row)
        pred = mlp_model.predict(X_scaled)
        return jsonify({"model":"mlp", "label": str(pred[0])})

    if model_name == "regression":
        X_row = build_feature_row(features)
        X_row = X_row[ohe_columns]
        X_scaled = reg_scaler.transform(X_row.to_numpy())
        pred_salary = reg_model.predict(X_scaled)[0]
        pred_cat = reg_pred_to_category(pred_salary)
        return jsonify({
            "model":"regression",
            "predicted_salary": float(pred_salary),
            "predicted_category": pred_cat
        })

@app.route("/", methods=["GET"])
def serve_frontend():
    return send_from_directory("frontend", "index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
