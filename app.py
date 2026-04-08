from flask import Flask, request, jsonify, render_template
import pickle
from features import extract_features

app = Flask(__name__)

# Load model
model = pickle.load(open("model/model.pkl", "rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    url = data['url']
    
    features, reasons = extract_features(url)
    prediction = model.predict([features])[0]

    if len(reasons) >= 2:
        result = "Phishing"
    else:
        result = "Safe"
    
    return jsonify({
        "result": result,
        "reasons": reasons
    })

if __name__ == "__main__":
    app.run(debug=True)