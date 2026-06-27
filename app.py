from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Load model and preprocessor
model = joblib.load("model/LightGBM_model.pkl")
prep = joblib.load("model/preprocessor.pkl")


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


# ---------------- PREDICTION API ----------------
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = pd.DataFrame([request.json])

        data_encoded = prep.transform(data)

        prediction = model.predict(data_encoded)

        return jsonify({
            "predicted_salary": round(float(prediction[0]), 2)
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 400


if __name__ == "__main__":
    app.run(debug=True)