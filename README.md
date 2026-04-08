# 🔐 Phishing Detection System

A Machine Learning-based web application that detects whether a given URL is **phishing or safe**.
The system analyzes URL patterns and provides **explainable results** to help users understand potential risks.

---

## 🚀 Features

* 🔍 URL-based phishing detection
* 🧠 Machine Learning model (Random Forest)
* 📊 Feature extraction from URLs
* 💡 Explainable results (why a URL is phishing)
* 🌐 Simple and interactive web interface (Flask)
* 🎨 Clean UI with real-time prediction

---

## 🛠️ Tech Stack

* **Backend:** Python, Flask
* **Machine Learning:** Scikit-learn
* **Frontend:** HTML, CSS, JavaScript
* **Libraries:** Pandas, NumPy, Pickle

---

## 📂 Project Structure

```
phishing-detector/
│
├── app.py                # Flask backend
├── train.py              # Model training script
├── features.py           # Feature extraction logic
├── model/
│   └── model.pkl         # Trained ML model
├── templates/
│   └── index.html        # Frontend UI
├── .gitignore
└── README.md
```

---

## ⚙️ How It Works

1. User enters a URL
2. System extracts features:

   * URL length
   * HTTPS presence
   * Number of dots
   * Suspicious keywords
   * Special characters
3. Machine Learning model predicts:

   * **Safe** or **Phishing**
4. System also provides **reasons** for the prediction

---

## ▶️ How to Run Locally

### 1. Clone the repository

```
git clone https://github.com/YOUR_USERNAME/phishing-detection-system.git
cd phishing-detection-system
```

### 2. Create virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```
pip install pandas numpy scikit-learn flask
```

### 4. Train the model

```
python3 train.py
```

### 5. Run the app

```
python3 app.py
```

### 6. Open in browser

```
http://127.0.0.1:5000
```

---

## 🧪 Example

| URL                        | Result   |
| -------------------------- | -------- |
| https://google.com         | Safe     |
| http://fake-login-bank.com | Phishing |

---

## 📈 Future Improvements

* Use real-world phishing datasets
* Improve model accuracy
* Add Chrome Extension
* Deploy application online
* Integrate real-time threat intelligence

---

## 🎯 Use Case

This project can be used for:

* Cybersecurity awareness
* Educational purposes
* URL safety analysis
* Research demonstrations

---

## 👨‍💻 Author

**Sahil Nabi**
GitHub: https://github.com/sahilnabi279

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!
