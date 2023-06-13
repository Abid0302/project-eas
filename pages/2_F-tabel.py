import streamlit as st
from scipy.stats import f

def hitung_ftabel(dfn, dfd, alpha):
    ftabel = f.ppf(1 - alpha, dfn, dfd)
    return ftabel

st.title("Kalkulator F-Tabel")

dfn = st.number_input("Derajat kebebasan numerator (dfn)", min_value=1, value=2, step=1)
dfd = st.number_input("Derajat kebebasan denominator (dfd)", min_value=1, value=10, step=1)
alpha = st.slider("Tingkat signifikansi (alpha)", min_value=0.01, max_value=0.10, step=0.01, value=0.05)

if st.button("Hitung F-Tabel"):
    ftabel = hitung_ftabel(dfn, dfd, alpha)
    st.write("F-Tabel:", ftabel)