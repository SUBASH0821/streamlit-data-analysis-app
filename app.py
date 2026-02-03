import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# App title
st.set_page_config(page_title="Streamlit Data App", layout="wide")
st.title("📊 Streamlit Data Analysis App")

# File upload
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read CSV
    df = pd.read_csv(uploaded_file)

    st.success("File uploaded successfully!")

    # Show dataset
    st.subheader("📄 Dataset Preview")
    st.dataframe(df.head())

    # Dataset info
    st.subheader("ℹ️ Dataset Info")
    st.write("Rows:", df.shape[0])
    st.write("Columns:", df.shape[1])

    # Select column
    numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns
    selected_col = st.selectbox("Select a numeric column", numeric_columns)

    # Plot
    st.subheader("📈 Column Distribution")
    fig, ax = plt.subplots()
    ax.hist(df[selected_col], bins=20)
    ax.set_xlabel(selected_col)
    ax.set_ylabel("Count")
    st.pyplot(fig)

else:
    st.info("👆 Upload a CSV file to get started")
