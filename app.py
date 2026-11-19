from pathlib import Path

import joblib
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    precision_score,
    recall_score,
    f1_score
)

# -----------------------------
# PROJECT PATHS
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "multiclass_random_forest_v3.pkl"
TRAIN_PATH = (
    BASE_DIR / "data" / "processed" /
    "multiclass_training_v3_train.csv"
)

st.set_page_config(
    page_title="NetSentinel AI",
    page_icon="🛡️",
    layout="wide"
)
# -----------------------------
# CUSTOM CYBERSECURITY DESIGN
# -----------------------------

st.markdown("""
<style>

/* Main background */
.stApp {
    background: linear-gradient(
        135deg,
        #080D19 0%,
        #101B2D 50%,
        #080D19 100%
    );
    color: #E5F3FF;
}

/* Main content spacing */
.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Main headings */
h1, h2, h3 {
    color: #E5F3FF !important;
    font-weight: 700 !important;
}

/* Subheadings */
p, label, .stMarkdown {
    color: #B8C7D9;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #0B1424;
    border-right: 1px solid #1E344D;
}

/* Metric cards */
div[data-testid="stMetric"] {
    background: linear-gradient(
        145deg,
        #14243A,
        #101B2D
    );
    border: 1px solid #25435F;
    padding: 20px;
    border-radius: 14px;
    box-shadow: 0 4px 15px rgba(0, 212, 255, 0.08);
}

/* Metric labels */
div[data-testid="stMetricLabel"] {
    color: #9BB3CC !important;
}

/* Metric values */
div[data-testid="stMetricValue"] {
    color: #00D4FF !important;
    font-weight: 700;
}

/* Buttons */
.stButton > button,
.stDownloadButton > button {
    background: linear-gradient(
        90deg,
        #0077B6,
        #00B4D8
    );
    color: white;
    border: none;
    border-radius: 9px;
    font-weight: 600;
    transition: 0.3s;
}

/* Button hover */
.stButton > button:hover,
.stDownloadButton > button:hover {
    background: #00D4FF;
    color: #07111F;
    border: none;
    box-shadow: 0 0 15px rgba(0, 212, 255, 0.35);
}

/* File uploader */
div[data-testid="stFileUploader"] {
    background: #111F32;
    border: 1px dashed #00A6C8;
    border-radius: 12px;
    padding: 15px;
}

/* Dataframes */
div[data-testid="stDataFrame"] {
    border: 1px solid #25435F;
    border-radius: 10px;
}

/* Select boxes */
div[data-baseweb="select"] > div {
    background-color: #14243A;
    border-color: #25435F;
    border-radius: 8px;
}

/* Information boxes */
div[data-testid="stAlert"] {
    border-radius: 10px;
}

/* Horizontal separators */
hr {
    border-color: #25435F;
}

/* Links */
a {
    color: #00D4FF !important;
}

/* Scrollbar */
::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-track {
    background: #080D19;
}

::-webkit-scrollbar-thumb {
    background: #25435F;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# LOAD MODEL AND TRAINING DATA
# -----------------------------
@st.cache_resource
def load_resources():
    model = joblib.load(MODEL_PATH)
    training_data = pd.read_csv(TRAIN_PATH)

    feature_columns = [
        col for col in training_data.columns
        if col not in ["Label", "Source_File"]
    ]

    medians = (
        training_data[feature_columns]
        .apply(pd.to_numeric, errors="coerce")
        .replace([np.inf, -np.inf], np.nan)
        .median()
        .fillna(0)
    )

    return model, feature_columns, medians
page = st.sidebar.radio(
    "NAVIGATION",
    [
        "🏠 Dashboard",
        "🔍 Detection Results",
        "🧠 Model Information",
        "ℹ️ About Project"
    ]
)
# -----------------------------
# PAGE HEADER
# -----------------------------

if page == "🏠 Dashboard":
    st.title("🛡️ NetSentinel AI")
    st.subheader("AI-Powered Network Intrusion Detection System")

elif page == "🔍 Detection Results":
    st.title("🔍 Detection Results")
    st.subheader("Network Traffic Analysis")

elif page == "🧠 Model Information":
    st.title("🧠 Model Information")
    st.subheader("Random Forest Classification Model")

elif page == "ℹ️ About Project":
    st.title("ℹ️ About NetSentinel AI")
    st.subheader("AI-Powered Network Intrusion Detection System")

# -----------------------------
# CHECK MODEL FILES
# -----------------------------
if not MODEL_PATH.exists():
    st.error(f"Model file not found: {MODEL_PATH}")
    st.stop()

if not TRAIN_PATH.exists():
    st.error(f"Training data not found: {TRAIN_PATH}")
    st.stop()

try:
    model, feature_columns, medians = load_resources()
except Exception as error:
    st.error(f"Could not load the model or training data: {error}")
    st.stop()


# -----------------------------
# PROFESSIONAL SIDEBAR NAVIGATION
# -----------------------------

st.sidebar.markdown(
    """
    <div style="text-align:center; padding:15px 0;">
        <h1 style="color:#38BDF8; font-size:25px;">
            🛡️ NETSENTINEL
        </h1>
        <p style="color:#94A3B8; font-size:11px;">
            AI NETWORK SECURITY
        </p>
    </div>
    """,
    unsafe_allow_html=True
)



st.sidebar.divider()

st.sidebar.markdown("### System Information")
st.sidebar.write("**Model:** Random Forest")
st.sidebar.write("**Classes:** 15")
st.sidebar.write("**Features:** 78")
st.sidebar.write("**Status:** 🟢 Ready")

st.sidebar.divider()

st.sidebar.caption(
    "NetSentinel AI | University Project"
)# -----------------------------
# ABOUT PROJECT PAGE
# -----------------------------

if page == "ℹ️ About Project":

    st.header("ℹ️ About NetSentinel AI")

    st.write("""
    NetSentinel AI is an AI-powered Network Intrusion
    Detection System developed as a university cybersecurity
    project.

    It uses machine learning to analyse recorded network
    traffic and identify potentially malicious activities.
    """)

    st.subheader("Project Objectives")

    st.markdown("""
    - Detect suspicious network traffic.
    - Identify different categories of cyberattacks.
    - Classify normal and malicious network activity.
    - Present detection results through an interactive dashboard.
    - Generate downloadable prediction reports.
    """)

    st.subheader("Technologies Used")

    technologies = {
        "Python": "Core programming language",
        "Pandas": "Dataset processing",
        "NumPy": "Numerical operations",
        "Scikit-learn": "Machine learning",
        "Random Forest": "Traffic classification",
        "Streamlit": "Interactive dashboard",
        "Plotly": "Data visualisation"
    }

    for technology, purpose in technologies.items():
        st.write(f"**{technology}:** {purpose}")

    st.subheader("Dataset")

    st.write("""
    The project uses the CICIDS2017 network traffic dataset,
    containing normal traffic and multiple attack categories.
    """)

    st.info(
        "NetSentinel AI analyses uploaded CSV network-flow "
        "records. It is not a live network monitoring system."
    )

    st.success("About page loaded successfully.")

    st.stop()
# -----------------------------
# MODEL INFORMATION PAGE
# -----------------------------

if page == "🧠 Model Information":

    st.header("🧠 Random Forest Model")

    col1, col2, col3 = st.columns(3)

    col1.metric("Algorithm", "Random Forest")
    col2.metric("Features", "78")
    col3.metric("Classes", "15")

    st.subheader("Model Description")

    st.write("""
    NetSentinel AI uses a supervised machine learning
    algorithm called Random Forest.

    The model analyses network traffic features and
    classifies traffic into 15 categories, including
    normal traffic and different types of cyberattacks.
    """)

    st.subheader("Training Information")

    st.write("Training algorithm: Random Forest Classifier")
    st.write("Number of estimators: 200")
    st.write("Training records: 71,255")
    st.write("Testing records: 17,814")
    st.write("Internal test accuracy: 98.25%")

    st.info(
        "The reported accuracy comes from the project's "
        "stratified test split and does not guarantee "
        "performance on unseen real-world networks."
    )

    st.success("Model information loaded successfully.")
    st.stop()
# -----------------------------
# DASHBOARD OVERVIEW
# -----------------------------
if page == "🏠 Dashboard":

    st.subheader("📊 System Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Model Accuracy", "98.25%")
    col2.metric("Traffic Classes", "15")
    col3.metric("Features", "78")
    col4.metric("Training Records", "71,255")

    st.subheader("🛡️ Detection Capabilities")

    st.write("""
    NetSentinel AI uses a Random Forest machine learning model
    to analyse network traffic and identify potentially malicious
    activities across multiple attack categories.
    """)

    st.info(
        "Upload a network traffic CSV file to begin analysing "
        "normal and potentially malicious traffic."
    )
# -----------------------------
# LIVE TRAFFIC ANALYTICS
# -----------------------------

st.divider()
st.subheader("📡 Latest Traffic Analysis")

if "analysis_summary" in st.session_state:

    summary = st.session_state["analysis_summary"]

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Analysed Records", f"{summary['total']:,}")
    col2.metric("Normal Traffic", f"{summary['normal']:,}")
    col3.metric("Potential Attacks", f"{summary['attacks']:,}")
    col4.metric("Attack Rate", f"{summary['attack_percentage']:.2f}%")

    st.caption(
        f"Latest uploaded file: "
        f"{st.session_state.get('uploaded_filename', 'Unknown')}"
    )

    # Attack distribution chart
    dashboard_results = st.session_state["analysis_results"]

    category_counts = (
        dashboard_results["Predicted_Category"]
        .value_counts()
        .rename_axis("Category")
        .reset_index(name="Records")
    )

    fig = px.pie(
        category_counts,
        names="Category",
        values="Records",
        title="Network Traffic Distribution",
        hole=0.45
    )

    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#E2E8F0")
    )

    st.plotly_chart(fig, use_container_width=True)

else:

    st.info(
        "No traffic analysis available yet. "
        "Visit Detection Results and upload a CSV file "
        "to populate your Dashboard."
    )    
# -----------------------------
# PAGE ACCESS CONTROL
# -----------------------------
if page != "🔍 Detection Results":
    st.stop()
# -----------------------------
# FILE UPLOAD
# -----------------------------
uploaded_file = st.file_uploader(
    "Upload network traffic CSV",
    type=["csv"]
)

if uploaded_file is None:
    st.warning("Upload a CSV file to begin the analysis.")

    st.markdown("### Detection workflow")
    st.write(
        "1. Upload a network traffic CSV file.\n"
        "2. NetSentinel AI checks the required features.\n"
        "3. The Random Forest model predicts traffic categories.\n"
        "4. Review the results and download the predictions."
    )
    st.stop()

# -----------------------------
# READ UPLOADED DATA
# -----------------------------
try:
    data = pd.read_csv(uploaded_file)
    data.columns = data.columns.str.strip()
except Exception as error:
    st.error(f"Could not read the CSV file: {error}")
    st.stop()

if data.empty:
    st.error("The uploaded CSV file contains no records.")
    st.stop()

st.success(f"File uploaded successfully: {len(data):,} records")

# -----------------------------
# PREPARE FEATURES
# -----------------------------
actual_labels = None

if "Label" in data.columns:
    actual_labels = data["Label"].astype(str).str.strip()

missing_features = [
    col for col in feature_columns
    if col not in data.columns
]

if missing_features:
    st.error(
        f"The uploaded file is missing {len(missing_features)} "
        "required model features."
    )
    st.write("Missing feature names:")
    st.code(", ".join(missing_features))
    st.stop()

X = data[feature_columns].copy()

X = X.apply(pd.to_numeric, errors="coerce")
X = X.replace([np.inf, -np.inf], np.nan)
X = X.fillna(medians)

if X.isna().any().any():
    st.error("Some feature values could not be prepared for prediction.")
    st.stop()

# -----------------------------
# MAKE PREDICTIONS
# -----------------------------
with st.spinner("Analysing network traffic..."):
    try:
        predictions = model.predict(X)

        if hasattr(model, "predict_proba"):
            probabilities = model.predict_proba(X)
            confidence = probabilities.max(axis=1) * 100
        else:
            confidence = np.full(len(predictions), np.nan)

    except Exception as error:
        st.error(f"Prediction failed: {error}")
        st.stop()
# Save uploaded file information
st.session_state["uploaded_filename"] = uploaded_file.name        

# -----------------------------
# RESULTS
# -----------------------------
results = data.copy()
results["Predicted_Category"] = predictions
results["Confidence_Percent"] = np.round(confidence, 2)

results["Traffic_Status"] = np.where(
    results["Predicted_Category"] == "BENIGN",
    "Normal",
    "Potential Attack"
)

total_records = len(results)
attack_count = int(
    (results["Predicted_Category"] != "BENIGN").sum()
)
benign_count = total_records - attack_count
attack_percentage = (attack_count / total_records) * 100
# Save analysis results for the Dashboard
st.session_state["analysis_results"] = results.copy()

st.session_state["analysis_summary"] = {
    "total": total_records,
    "normal": benign_count,
    "attacks": attack_count,
    "attack_percentage": attack_percentage
}

st.divider()
st.header("Detection Summary")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Records", f"{total_records:,}")
col2.metric("Normal Traffic", f"{benign_count:,}")
col3.metric("Potential Attacks", f"{attack_count:,}")
col4.metric("Attack Percentage", f"{attack_percentage:.2f}%")

# -----------------------------
# CATEGORY CHART
# -----------------------------
st.subheader("Detected Traffic Categories")

category_counts = (
    results["Predicted_Category"]
    .value_counts()
    .rename_axis("Category")
    .reset_index(name="Records")
)

fig = px.bar(
    category_counts,
    x="Category",
    y="Records",
    color="Category",
    title="Predicted Network Traffic Categories"
)

fig.update_layout(
    template="plotly_dark",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(17,24,39,0.5)",
    font=dict(color="#E2E8F0"),
    xaxis_title="Traffic Category",
    yaxis_title="Number of Records",
    showlegend=False
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# PREDICTION TABLE
# -----------------------------
st.subheader("Prediction Results")

filter_choice = st.selectbox(
    "Filter results",
    ["All Traffic", "Normal Traffic", "Potential Attacks"]
)

if filter_choice == "Normal Traffic":
    displayed_results = results[
        results["Traffic_Status"] == "Normal"
    ]
elif filter_choice == "Potential Attacks":
    displayed_results = results[
        results["Traffic_Status"] == "Potential Attack"
    ]
else:
    displayed_results = results

display_columns = [
    "Predicted_Category",
    "Traffic_Status",
    "Confidence_Percent"
]

if actual_labels is not None:
    results["Actual_Category"] = actual_labels.values
    display_columns.insert(0, "Actual_Category")
    displayed_results = results.loc[displayed_results.index]

st.dataframe(
    displayed_results[display_columns].head(1000),
    use_container_width=True
)

st.caption("The table displays up to the first 1,000 matching records.")

# -----------------------------
# MODEL EVALUATION
# -----------------------------
if actual_labels is not None:

    st.divider()
    st.header("Model Performance Evaluation")

    # Identify labels recognised by the model
    comparable = results[
        results["Actual_Category"].isin(model.classes_)
    ]

    unknown_count = len(results) - len(comparable)

    if len(comparable) > 0:

        y_true = comparable["Actual_Category"]
        y_pred = comparable["Predicted_Category"]

        # Calculate evaluation metrics
        accuracy = accuracy_score(y_true, y_pred) * 100

        precision = precision_score(
            y_true,
            y_pred,
            average="weighted",
            zero_division=0
        ) * 100

        recall = recall_score(
            y_true,
            y_pred,
            average="weighted",
            zero_division=0
        ) * 100

        f1 = f1_score(
            y_true,
            y_pred,
            average="weighted",
            zero_division=0
        ) * 100

        correct = int((y_true == y_pred).sum())
        incorrect = len(comparable) - correct

        # Evaluation summary
        st.subheader("Overall Performance")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Accuracy", f"{accuracy:.2f}%")
        col2.metric("Precision", f"{precision:.2f}%")
        col3.metric("Recall", f"{recall:.2f}%")
        col4.metric("F1-Score", f"{f1:.2f}%")

        st.subheader("Prediction Quality")

        col1, col2, col3 = st.columns(3)

        col1.metric("Evaluated Records", f"{len(comparable):,}")
        col2.metric("Correct Predictions", f"{correct:,}")
        col3.metric("Incorrect Predictions", f"{incorrect:,}")

        if unknown_count > 0:
            st.warning(
                f"{unknown_count:,} records were excluded because "
                "their actual labels were not recognised by the model."
            )

        # Classification report
        st.subheader("Classification Report")

        report = classification_report(
            y_true,
            y_pred,
            labels=model.classes_,
            output_dict=True,
            zero_division=0
        )

        report_df = pd.DataFrame(report).transpose()

        st.dataframe(
            report_df.round(4),
            use_container_width=True
        )

        # Confusion matrix
        st.subheader("Confusion Matrix")

        cm = confusion_matrix(
            y_true,
            y_pred,
            labels=model.classes_
        )

        cm_fig = px.imshow(
            cm,
            x=model.classes_,
            y=model.classes_,
            text_auto=True,
            color_continuous_scale="Blues",
            labels={
                "x": "Predicted Category",
                "y": "Actual Category",
                "color": "Records"
            },
            title="Actual vs Predicted Traffic Categories"
        )

        cm_fig.update_layout(
            xaxis_tickangle=-45
        )

        st.plotly_chart(
            cm_fig,
            use_container_width=True
        )

        st.caption(
            "Weighted precision, recall and F1-score account for "
            "the number of records in each category. The confusion "
            "matrix uses the model's complete 15-class label order."
        )

    else:

        st.warning(
            "No uploaded actual labels matched the model's known categories."
        )
# -----------------------------
# DOWNLOAD RESULTS
# -----------------------------
st.divider()

csv_output = results.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇️ Download Prediction Report",
    data=csv_output,
    file_name="netsentinel_ai_predictions.csv",
    mime="text/csv"
)

st.success("Traffic analysis completed.")