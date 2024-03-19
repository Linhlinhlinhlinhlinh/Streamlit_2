import streamlit as st
import time
st.button(label= 'login')
p = st.progress(0)
for i in range(100):
  p.progress(i+1)
  time.sleep(0.1)
st.balloons()
