import pandas as pd
import streamlit as st

# Load data
df = pd.read_csv("data (1).csv")

st.title("Search Your Record")

# Message
st.write("### Pray for Flood Affecties")
st.write(" #### This list contains the people from Jalalpur Pirwala whose cards have been received in the camp or the Fund is approved. Missing names will be added daily. If your name appears under “PLRA  Not Verified,” please visit the AC office to check whether your application has been rejected or not.")
st.write("## Enter CNIC without hyphen - like(3630111111111) and phone number without 0 like (3000900786)")
query = st.text_input("Enter Name, CNIC, or Phone")
search_btn = st.button("Search")

if search_btn:
    if query.strip() == "":
        st.warning("Please type something to search.")
    else:
        q = query.lower()
        results = df[df.apply(lambda row: row.astype(str).str.lower().str.contains(q).any(), axis=1)]
        
        if len(results) > 0:
            st.success(f"{len(results)} record(s) found")
            st.write(results)
        else:
            st.error("No record found.")
