import streamlit as st
import pandas as pd

st.title("Explore Disney Princesses")

uploaded_file = st.file_uploader("Upload princesses file (CSV)", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Preview of data:")
    st.dataframe(df)

    st.write("Column selection and filtering:")
    columns = st.multiselect("Select columns to display", df.columns.tolist(), default=df.columns.tolist())
    st.dataframe(df[columns])

    st.write("Search by name:")
    name_query = st.text_input("Enter princess name (partial or full)")
    if name_query:
        filtered_df = df[df['name'].str.contains(name_query, case=False, na=False)]
        st.dataframe(filtered_df)