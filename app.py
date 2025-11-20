import pandas as pd
import streamlit as st

st.write("## بِسْمِ اللّٰه الرَّحْمٰنِ الرَّحِيْمِ")

# Load data
df = pd.read_csv("combined20112025.csv")

# Title and instructions
st.markdown(
    "<div style='text-align: right;'>"
    "## اپنا ریکارڈ تلاش کریں - Search Your Record<br>"
    "##### اپنا شناختی کارڈ نمبر بغیر ہائفن کے لکھیں (مثلاً 3630111111111) اور فون نمبر بغیر 0 کے لکھیں (مثلاً 3000900786)"
    "</div>",
    unsafe_allow_html=True
)

# Input box
query = st.text_input("نام، شناختی کارڈ نمبر، یا فون نمبر درج کریں - Enter Name, CNIC, or Phone")
search_btn = st.button("Search")

# Message about flood affectees
st.markdown(
    "<div style='text-align: right;'>"
    "### سیلاب متاثرین کے لیے دعا کریں - Pray For Flood Affectees<br>"
    "یہ فہرست جلالپور پیر والا کے اُن لوگوں پر مشتمل ہے جن کے کارڈ کیمپ میں موصول ہو چکے ہیں یا جن کا فنڈ منظور ہو چکا ہے۔ "
    "نئے نام روزانہ شامل کیے جائیں گے۔ "
    "اگر آپ کا نام 'PLRA Not Verified' کے تحت آتا ہے تو براہِ کرم اے سی آفس جائیں اور تصدیق کریں کہ آیا آپ کی درخواست منظور ہوئی ہے یا مسترد۔"
    "</div>",
    unsafe_allow_html=True
)

# Search functionality
if search_btn:
    if query.strip() == "":
        st.markdown(
            "<div style='text-align: right;'>براہِ کرم تلاش کرنے کے لیے کچھ لکھیں۔ - Please type something to search</div>",
            unsafe_allow_html=True
        )
    else:
        q = query.lower()
        results = df[df.apply(lambda row: row.astype(str).str.lower().str.contains(q).any(), axis=1)]
        
        if len(results) > 0:
            st.success(f"{len(results)} record(s) found")
            st.write(results)
        else:
            st.markdown(
                "<div style='text-align: right;'>"
                "اس وقت کوئی ریکارڈ نہیں ملا۔ انتظار کریں، ان شاء اللہ آپ کا فنڈ منظور ہو جائے گا۔ - Sorry, No record found"
                "</div>",
                unsafe_allow_html=True
            )
