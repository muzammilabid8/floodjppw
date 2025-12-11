import pandas as pd
import streamlit as st
import time

st.write("## بِسْمِ اللّٰه الرَّحْمٰنِ الرَّحِيْمِ")
st.write("### اپنا ریکارڈ تلاش کریں")
st.write("##### اپنا شناختی کارڈ نمبر بغیر ہائفن کے لکھیں (مثلاً 3630111111111) ")
st.write("##### فون نمبر بغیر 0 کے لکھیں (مثلاً 3000900786)")

# GitHub folder raw URLs
github_files = [
    
    "https://raw.githubusercontent.com/muzammilabid8/floodjppw/main/data_clean.csv",
    "https://raw.githubusercontent.com/muzammilabid8/floodjppw/main/data20.csv",
    "https://raw.githubusercontent.com/muzammilabid8/floodjppw/main/data21.csv",
    "https://raw.githubusercontent.com/muzammilabid8/floodjppw/main/kin.csv",
    "https://raw.githubusercontent.com/muzammilabid8/floodjppw/main/calls21.csv",
    "https://raw.githubusercontent.com/muzammilabid8/floodjppw/main/calls23.csv",
    "https://raw.githubusercontent.com/muzammilabid8/floodjppw/main/calls24.csv",
    "https://raw.githubusercontent.com/muzammilabid8/floodjppw/main/calls25.csv",
    "https://raw.githubusercontent.com/muzammilabid8/floodjppw/main/calls26.csv",
    "https://raw.githubusercontent.com/muzammilabid8/floodjppw/main/calls27.csv",
    "https://raw.githubusercontent.com/muzammilabid8/floodjppw/main/calls28.csv",
     "https://raw.githubusercontent.com/muzammilabid8/floodjppw/main/calls02.csv",
    "https://raw.githubusercontent.com/muzammilabid8/floodjppw/main/calls03.csv",
    "https://raw.githubusercontent.com/muzammilabid8/floodjppw/main/master2400.csv",
    "https://raw.githubusercontent.com/muzammilabid8/floodjppw/main/MASTER2411.csv",
    
]

# Load CSVs
df_list = []
for file_url in github_files:
    try:
        temp_df = pd.read_csv(file_url)
        temp_df['source_file'] = file_url.split('/')[-1]
        df_list.append(temp_df)
    except Exception as e:
        st.warning(f"Could not load {file_url}: {e}")

df = pd.concat(df_list, ignore_index=True)

# Search input
query = st.text_input("Enter Name, CNIC, or Phone")
search_btn = st.button("Search")


if search_btn:
    if query.strip() == "":
        st.warning("Please type something to search.")
    else:

        # ------- BIG CUSTOM LOADER -------
        loading_html = """
        <div style="text-align:center; margin-top:20px;">
            <div class="loader"></div>
            <h2 style="color:#444; font-size:20px; margin-top:20px;">
                 انتظار کریں، آپ کا ریکارڈ تلاش کیا جا رہا ہے...
            </h2>
        </div>

        <style>
        .loader {
          border: 12px solid #f3f3f3;
          border-top: 12px solid #3498db;
          border-radius: 50%;
          width: 60px;
          height: 60px;
          animation: spin 1s linear infinite;
          margin: auto;
        }

        @keyframes spin {
          0% { transform: rotate(0deg); }
          100% { transform: rotate(360deg); }
        }
        </style>
        """

        loader_placeholder = st.markdown(loading_html, unsafe_allow_html=True)
        time.sleep(1.5)

        # ------- SEARCH LOGIC -------
        q = query.lower()
        results = df[df.apply(lambda row: row.astype(str).str.lower().str.contains(q).any(), axis=1)]

        # Remove loader
        loader_placeholder.empty()

        if len(results) > 0:
            st.success(f"{len(results)} record(s) found")
            st.write("### 🎉 مبارک ہو! آپ کی امداد منظور ہو چکی ہے۔")
            st.write(results)
        else:
            st.error("اس وقت کوئی ریکارڈ نہیں ملا۔ انتظار کریں، ان شاء اللہ آپ کا فنڈ منظور ہو جائے گا۔")

st.write("یہ فہرست جلالپور پیر والا کے لوگوں پر مشتمل ہے جن کے کارڈ کیمپ میں موصول ہو چکے ہیں یا فنڈ منظور ہو چکا ہے۔ نئے نام روزانہ شامل کیے جائیں گے۔")
st.write("kin.csv")
st.write("اور")
st.write("plra not verified")
st.write("میں اگر آپ کا نام آ جائے تو اس کا مطلب ہے کہ آپ کی درخواست زمین کی وراثتی مسائل کی وجہ سے مسترد ہو گئی ہے۔ پٹواری سے رابطہ کریں اور وراثت منتقل کریں۔")





