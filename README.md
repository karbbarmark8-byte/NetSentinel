# 🛡️ NetSentinel AI
### AI-Powered Network Intrusion Detection System

NetSentinel AI is a machine learning-based Network Intrusion Detection System (NIDS) developed as a university cybersecurity project. It uses a Random Forest classification model to analyse network traffic records and identify normal activity and potentially malicious network behaviour.

The application provides an interactive dashboard built with Streamlit, allowing users to upload network traffic CSV files, analyse predictions, evaluate model performance and download detection reports.

---

## 🎯 Project Objectives

- Detect potentially malicious network traffic.
- Identify different categories of cyberattacks.
- Classify normal and suspicious network activity.
- Apply machine learning to network intrusion detection.
- Present detection results through an interactive dashboard.
- Generate downloadable traffic analysis reports.

---

## 🚀 Key Features

- CSV-based network traffic analysis.
- 15-class network traffic classification.
- Random Forest machine learning algorithm.
- Interactive cybersecurity dashboard.
- Dark-themed user interface.
- Normal traffic and potential attack filtering.
- Traffic distribution visualisation.
- Prediction confidence scores.
- Model performance evaluation.
- Classification report and confusion matrix.
- Downloadable CSV prediction reports.

---

## 🧠 Machine Learning Model

The project uses a supervised machine learning algorithm called Random Forest Classifier.

The model analyses 78 network traffic features and predicts one of 15 traffic categories.

### Model Configuration

| Parameter | Value |
|---|---|
| Algorithm | Random Forest |
| Number of estimators | 200 |
| Input features | 78 |
| Classification classes | 15 |
| Training records | 71,255 |
| Testing records | 17,814 |

### Supported Traffic Categories

1. BENIGN
2. Bot
3. DDoS
4. DoS GoldenEye
5. DoS Hulk
6. DoS Slowhttptest
7. DoS slowloris
8. FTP-Patator
9. Heartbleed
10. Infiltration
11. PortScan
12. SSH-Patator
13. Web Attack - Brute Force
14. Web Attack - Sql Injection
15. Web Attack - XSS

---

## 📊 Model Performance

The model achieved the following results on its internal stratified test dataset:

| Evaluation Metric | Result |
|---|---:|
| Accuracy | 98.25% |
| Precision | 98.39% |
| Recall | 98.25% |
| F1-Score | 98.30% |
| Correct Predictions | 17,502 |
| Incorrect Predictions | 312 |

**Note:** These results represent performance on the project's test split. They do not guarantee equivalent performance on unseen real-world network traffic.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Dataset processing |
| NumPy | Numerical operations |
| Scikit-learn | Machine learning |
| Random Forest | Traffic classification |
| Joblib | Model loading and storage |
| Streamlit | Interactive web application |
| Plotly | Data visualisation |
| Matplotlib | Evaluation visualisation |

---

## 📁 Project Structure

```text
NetSentinel_AI/
│
├── app.py
├── requirements.txt
├── README.md
│
├── models/
│   └── multiclass_random_forest_v3.pkl
│
├── data/
│   ├── raw/
│   └── processed/
│       └── multiclass_training_v3_train.csv
│
├── reports/
│
├── src/
│
└── .streamlit/
    └── config.toml
```

---

## ⚙️ Installation and Setup

### 1. Install Python

Install Python 3.13 or a compatible version.

### 2. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 3. Open the project directory

```bash
cd NetSentinel_AI
```

### 4. Create a virtual environment

```bash
python -m venv .venv
```

### 5. Activate the virtual environment

Windows:

```bash
.venv\Scripts\activate
```

### 6. Install dependencies

```bash
pip install -r requirements.txt
```

### 7. Run the application

```bash
streamlit run app.py
```

The application will open in your web browser.

---

## 📖 How to Use NetSentinel AI

1. Launch the application.
2. Open the Detection Results page.
3. Upload a compatible network traffic CSV file.
4. The system checks the required input features.
5. The Random Forest model analyses the uploaded records.
6. Review normal traffic and potential attack statistics.
7. Explore the predicted traffic categories.
8. Filter normal traffic or potential attacks.
9. Review model evaluation metrics when actual labels are available.
10. Download the prediction report as a CSV file.

---

## 📚 Dataset

This project uses the CICIDS2017 network intrusion detection dataset.

The dataset contains benign network traffic and multiple categories of malicious activities.

The dataset was processed and prepared for multiclass machine learning classification.

---

## ⚠️ Project Limitations

- The application analyses uploaded CSV network-flow records.
- It does not perform live network packet capture or real-time monitoring.
- Prediction performance depends on the quality and characteristics of the input data.
- Some attack categories have limited training examples.
- High internal test accuracy does not guarantee real-world detection accuracy.
- Model confidence scores are not calibrated probabilities of correctness.

---

## 🎓 Project Information

**Project Name:** NetSentinel AI  
**Project Type:** University Cybersecurity Project  
**Domain:** Cybersecurity and Machine Learning  
**Application:** AI-Powered Network Intrusion Detection System  
**Classification Algorithm:** Random Forest  

---

## 🔮 Future Enhancements

- Real-time network traffic monitoring.
- Integration with packet capture tools.
- Advanced intrusion detection techniques.
- Improved detection of rare attack categories.
- Alert and detection history management.
- Database integration for persistent analysis records.

---

### 🛡️ NetSentinel AI
**Intelligent Network Traffic Analysis Through Machine Learning.**