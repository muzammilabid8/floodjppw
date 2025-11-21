import pandas as pd
import streamlit as st

st.write("## بِسْمِ اللّٰه الرَّحْمٰنِ الرَّحِيْمِ")
st.write("## اپنا ریکارڈ تلاش کریں")
st.write("##### اپنا شناختی کارڈ نمبر بغیر ہائفن کے لکھیں (مثلاً 3630111111111) اور فون نمبر بغیر 0 کے لکھیں (مثلاً 3000900786)")

# GitHub folder raw URLs
github_files = [
    "https://raw.githubusercontent.com/muzammilabid8/floodjppw/main/data_clean.csv",
    "https://raw.githubusercontent.com/muzammilabid8/floodjppw/main/data20.csv",
    "https://raw.githubusercontent.com/muzammilabid8/floodjppw/main/data21.csv",
    "https://raw.githubusercontent.com/muzammilabid8/floodjppw/main/kin.csv",
]

# Load all CSVs into a single DataFrame
df_list = []
for file_url in github_files:
    try:
        temp_df = pd.read_csv(file_url)
        temp_df['source_file'] = file_url.split('/')[-1]  # Optional: track source file
        df_list.append(temp_df)
    except Exception as e:
        st.warning(f"Could not load {file_url}: {e}")

df = pd.concat(df_list, ignore_index=True)

# Search input
query = st.text_input("Enter Name, CNIC, or Phone")
search_btn = st.button("Search")

st.write("یہ فہرست جلالپور پیر والا کے لوگوں پر مشتمل ہے جن کے کارڈ کیمپ میں موصول ہو چکے ہیں یا فنڈ منظور ہو چکا ہے۔ نئے نام روزانہ شامل کیے جائیں گے۔")
st.write(" کے تحت ظاہر ہوتا ہے تو براہ کرم اے سی آفس جائیں تاکہ یہ جان سکیں کہ آیا آپ کی درخواست قبول ہوئی ہے یا نہیں۔  PLRA Not Verified اگر آپ کا نام ")
st.write("میں آ جائے تو اس کا مطلب ہے کہ آپ کی درخواست زمین کی وراثتی مسائل کی وجہ سے مسترد ہو گئی ہے۔ kin.csv اگر آپ کا نام")

# Search functionality
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
            st.error("اس وقت کوئی ریکارڈ نہیں ملا۔ انتظار کریں، ان شاء اللہ آپ کا فنڈ منظور ہو جائے گا۔")







