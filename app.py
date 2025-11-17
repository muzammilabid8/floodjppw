import pandas as pd
import streamlit as st

# Load data
df = pd.read_csv("data.csv")

st.title("Search Your Record")

query = st.text_input("Enter Name, CNIC, or Phone")

if query:
    query = query.lower()
    results = df[df.apply(lambda row: row.astype(str).str.lower().str.contains(query).any(), axis=1)]
    
    if len(results) > 0:
        st.write(results)
    else:
        st.write("Sorry! No record found.")
