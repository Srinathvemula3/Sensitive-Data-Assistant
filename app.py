import streamlit as st
from utils import extract_text
from detector import detect_sensitive_data, classify_risk

# ------------------------------
# Page Configuration
# ------------------------------
st.set_page_config(
    page_title="Sensitive Data Detection Assistant",
    page_icon="🔒",
    layout="wide"
)

st.title("🔒 Sensitive Data Detection & Compliance Assistant")

st.write("Upload a PDF, TXT, or CSV file to detect sensitive information.")

# ------------------------------
# File Upload
# ------------------------------
uploaded_file = st.file_uploader(
    "Upload PDF, TXT or CSV",
    type=["pdf", "txt", "csv"]
)

# ------------------------------
# Process File
# ------------------------------
if uploaded_file is not None:

    # Extract text
    text = extract_text(uploaded_file)

    st.success("✅ Document uploaded successfully!")

    # ------------------------------
    # Show Extracted Text
    # ------------------------------
    st.subheader("📄 Extracted Text")

    st.text_area(
        label="Document Content",
        value=text,
        height=300
    )

    # ------------------------------
    # Detect Sensitive Data
    # ------------------------------
    results = detect_sensitive_data(text)

    st.subheader("🔍 Sensitive Data Detected")

    if results:

        for category, values in results.items():

            st.markdown(f"### {category}")

            unique_values = list(set(values))

            for item in unique_values:
                st.write(f"• {item}")

    else:
        st.success("🎉 No Sensitive Data Found")

    # ------------------------------
    # Risk Classification
    # ------------------------------
    risk = classify_risk(results)

    st.subheader("🚨 Risk Classification")

    if "HIGH" in risk:
        st.error(risk)

    elif "MEDIUM" in risk:
        st.warning(risk)

    else:
        st.success(risk)