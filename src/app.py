from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load your model
model = joblib.load("models/random_forest_model.joblib")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(force=True)
    # Expecting data as a list of features, e.g. {"features": [val1, val2, ..., valN]}
    features = data.get("features")

    if features is None:
        return jsonify({"error": "No features provided"}), 400
    
    # Convert to numpy array and reshape for a single sample
    features = np.array(features).reshape(1, -1)
    
    # Predict
    prediction = model.predict(features)
    prediction_proba = model.predict_proba(features).tolist()

    return jsonify({
        "prediction": prediction[0],
        "probabilities": prediction_proba[0]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
