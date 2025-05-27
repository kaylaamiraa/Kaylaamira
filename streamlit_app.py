import streamlit as st

st.title("kaylaa imuts")
st.write ("kayla amira")


st.image("4B12A221-838D-4FE9-A51F-BF762A87CD1F.jpeg", width=200)

st.tittle("Aplikasi Sederhana")
st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("Tulis sebuah Angka:", value=0, step=1)


if (angka % 2) ==0
  st.write(f"{angka} adalah bilangan genap")
else 
  st.writer(f{angka} adalah bilangan ganjil")
