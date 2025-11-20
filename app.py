import pandas as pd
import streamlit as st
st.write( "## بِسْمِ اللّٰه الرَّحْمٰنِ الرَّحِيْمِ")
# Load data
df = pd.read_csv("combined20112025.csv")
st.write("## اپنا ریکارڈ تلاش کریں")
st.write("##### اپنا شناختی کارڈ نمبر بغیر ہائفن کے لکھیں (مثلاً 3630111111111) اور فون نمبر بغیر 0 کے لکھیں (مثلاً 3000900786)")


query = st.text_input("Enter Name, CNIC, or Phone")
search_btn = st.button("Search")

# Message
st.write("### سیلاب متاثرین کے لیے دعا کریں")
st.write("یہ فہرست جلالپور پیروالا کے اُن لوگوں پر مشتمل ہے جن کے کارڈ کیمپ میں موصول ہو چکے ہیں یا جن کا فنڈ منظور ہو چکا ہے۔ گمشدہ نام روزانہ شامل کیے جائیں گے۔ اگر آپ کا نام 'PLRA Not Verified' کے تحت آتا ہے تو براہِ کرم اے سی آفس جائیں اور تصدیق کریں کہ آپ کی درخواست منظور ہوئی ہے یا مسترد۔")


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






