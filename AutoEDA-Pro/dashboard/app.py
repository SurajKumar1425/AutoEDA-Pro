import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(
    page_title="AutoEDA Pro",
    layout="wide"
)


def load_csv(file):
    encodings = [
        "utf-8",
        "utf-8-sig",
        "latin1",
        "cp1252"
    ]

    separators = [
        ",",
        ";",
        "\t"
    ]

    for encoding in encodings:
        for sep in separators:
            try:
                file.seek(0)

                df = pd.read_csv(
                    file,
                    encoding=encoding,
                    sep=sep,
                    on_bad_lines="skip"
                )

                return df

            except Exception:
                continue

    return None


st.title("🚀 AutoEDA Pro Dashboard")


uploaded_file = st.file_uploader(
    "Upload CSV Dataset",
    type=["csv"]
)


if uploaded_file:

    df = load_csv(uploaded_file)

    if df is None:
        st.error(
            "Unable to read this CSV file. The file may be corrupted or unsupported."
        )
        st.stop()


    st.success("Dataset Loaded Successfully")


    st.subheader("Dataset Preview")
    st.dataframe(df.head())


    st.subheader("Dataset Information")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Rows",
            df.shape[0]
        )

    with col2:
        st.metric(
            "Columns",
            df.shape[1]
        )


    st.subheader("Missing Values Analysis")

    missing = pd.DataFrame({
        "Missing Values": df.isnull().sum(),
        "Percentage (%)": (
            df.isnull().mean() * 100
        ).round(2)
    })

    missing = missing[
        missing["Missing Values"] > 0
    ]


    if missing.empty:
        st.success(
            "No missing values found"
        )

    else:
        st.dataframe(missing)


    st.subheader("Numerical Distribution")


    numeric_cols = df.select_dtypes(
        include="number"
    ).columns


    if len(numeric_cols) > 0:

        column = st.selectbox(
            "Select Numerical Column",
            numeric_cols
        )


        fig, ax = plt.subplots(
            figsize=(8, 4)
        )


        sns.histplot(
            df[column].dropna(),
            kde=True,
            ax=ax
        )


        st.pyplot(fig)


    else:
        st.warning(
            "No numerical columns found"
        )


    st.subheader("Correlation Heatmap")


    if len(numeric_cols) > 1:

        corr = df[numeric_cols].corr()


        fig, ax = plt.subplots(
            figsize=(10, 6)
        )


        sns.heatmap(
            corr,
            annot=True,
            cmap="coolwarm",
            ax=ax
        )


        st.pyplot(fig)


    else:
        st.warning(
            "At least 2 numerical columns are required for correlation analysis"
        )


    st.success(
        "AutoEDA Analysis Completed Successfully"
    )
