import streamlit as st
from scipy.stats import t

def hitung_ttabel(df, alpha, tails):
    if tails == "One":
        ttabel = t.ppf(1 - alpha, df)
    else:
        ttabel = t.ppf(1 - alpha / 2, df)
    return ttabel

st.title("Kalkulator T-Tabel")

df = st.number_input("Derajat kebebasan (df)", min_value=1, value=10, step=1)
alpha = st.slider("Tingkat signifikansi (alpha)", min_value=0.01, max_value=0.10, step=0.01, value=0.05)
tails = st.selectbox("Bilah ekor", ["One", "Two"])

if st.button("Hitung T-Tabel"):
    ttabel = hitung_ttabel(df, alpha, tails)
    st.write("T-Tabel:", ttabel)