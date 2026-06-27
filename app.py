from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load model and preprocessor
model = joblib.load("model/LightGBM_model.pkl")
prep = joblib.load("model/preprocessor.pkl")

# GET endpoint
@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Salary Prediction API Running",
        "status": "success"
    })

# POST endpoint
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = pd.DataFrame([request.json])

        data_encoded = prep.transform(data)

        print("Encoded shape:", data_encoded.shape)

        prediction = model.predict(data_encoded)

        return jsonify({
            "predicted_salary": round(float(prediction[0]), 2)
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)