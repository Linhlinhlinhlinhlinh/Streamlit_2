import streamlit as st
import time
st.title("Điền thông tin giới thiệu bản thân em")
st.text_input('Họ và tên')
st.text_input('Ngày tháng năm sinh')
st.text_input('Giới tính')
s = st.button('Submit')
if s == True:
  p = st.progress(0)
  for i in range(100):
    p.progress(i+1)
    time.sleep(0.1)
  st.balloons()
