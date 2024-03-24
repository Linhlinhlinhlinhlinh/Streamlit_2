import streamlit as st
import time
st.title("Điền thông tin giới thiệu bản thân em")
name = st.text_input('Họ và tên')
birthday = st.text_input('Ngày tháng năm sinh')
gender = st.text_input('Giới tính')
s = st.button('Submit')
if s == True:
  if name != '' and gender != "" and birthday != '':
    p = st.progress(0)
    for i in range(100):
      p.progress(i+1)
      time.sleep(0.1)
    st.snow()
    st.empty()
    st.title('Chào mừng em đến với bảng thống kê điểm!')
  else: 
    st.warning('Vui lòng nhập đầy đủ thông tin')
