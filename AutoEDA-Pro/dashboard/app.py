
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="AutoEDA Pro",
    layout="wide"
)

st.title("AutoEDA Pro Dashboard")

uploaded_file = st.file_uploader(
    "Upload CSV Dataset",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.success("Dataset Loaded Successfully")

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.subheader("Dataset Information")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Rows", df.shape[0])

    with col2:
        st.metric("Columns", df.shape[1])


    st.subheader("Missing Values")

    missing = pd.DataFrame({
        "Missing": df.isnull().sum(),
        "Percentage":
        df.isnull().mean()*100
    })

    st.dataframe(
        missing[missing["Missing"] > 0]
    )


    st.subheader("Numerical Distribution")

    numeric_cols = df.select_dtypes(
        include="number"
    ).columns


    if len(numeric_cols) > 0:

        column = st.selectbox(
            "Select Numerical Column",
            numeric_cols
        )

        fig, ax = plt.subplots()

        sns.histplot(
            df[column],
            kde=True,
            ax=ax
        )

        st.pyplot(fig)


    st.subheader("Correlation Heatmap")

    if len(numeric_cols) > 1:

        corr = df[numeric_cols].corr()

        fig, ax = plt.subplots(
            figsize=(8,5)
        )

        sns.heatmap(
            corr,
            annot=True,
            cmap="coolwarm",
            ax=ax
        )

        st.pyplot(fig)


    st.success(
        "AutoEDA Analysis Completed"
    )
