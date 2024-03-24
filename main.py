import streamlit as st
import time

def avg(toan, van, anh):
    if not (toan.isdigit() and van.isdigit() and anh.isdigit()):
        return None
    toan = float(toan)
    van = float(van)
    anh = float(anh)
    diem_trung_binh = (toan + van + anh) / 3
    return diem_trung_binh

st.title("Điền thông tin giới thiệu bản thân em")
name = st.text_input('Họ và tên')
birthday = st.text_input('Ngày tháng năm sinh')
gender = st.text_input('Giới tính')
s = st.button('Submit')

if s:
    if name != '' and gender != "" and birthday != '':
        p = st.progress(0)
        for i in range(100):
            p.progress(i+1)
            time.sleep(0.1)
        st.empty()
        st.title('Chào mừng em đến với bảng thống kê điểm!')
        toan = st.text_input('Nhập điểm toán:')
        van = st.text_input('Nhập điểm văn:')
        anh = st.text_input('Nhập điểm anh:')

        if toan != '' and van != '' and anh != '':
            average = avg(toan, van, anh)
            if average is not None:
                st.success(f"Điểm trung bình của bạn là: {average:.2f}")
            else:
                st.error("Vui lòng nhập điểm hợp lệ (số)")
        else:
            st.warning('Vui lòng nhập đủ thông tin điểm.')
    else:
        st.warning('Vui lòng nhập đầy đủ thông tin.')
