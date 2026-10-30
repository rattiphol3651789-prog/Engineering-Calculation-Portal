
import streamlit as st

st.set_page_config(
    page_title="Machining Menu",
    page_icon="⚙️",
    layout="wide"
)

st.title("⚙️ Machining Calculator")
st.caption("เลือกเครื่องมือคำนวณที่ต้องการใช้งาน")

if st.button("🏠 กลับหน้าหลัก"):
    st.switch_page("app.py")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    with st.container(border=True):
        st.subheader("🔄 RPM")
        st.write("คำนวณความเร็วรอบเครื่องจักร")

        if st.button("เข้าสู่การคำนวณ", key="rpm", use_container_width=True):
            st.switch_page("pages/2_RPM_Calculator.py")

with col2:
    with st.container(border=True):
        st.subheader("✂️ Cutting Speed")
        st.write("คำนวณความเร็วตัด")

        if st.button("เข้าสู่การคำนวณ", key="cutting", use_container_width=True):
            st.switch_page("pages/3_Cutting_Speed.py")

with col3:
    with st.container(border=True):
        st.subheader("📏 Feed Rate")
        st.write("คำนวณอัตราป้อน")

        if st.button("เข้าสู่การคำนวณ", key="feed", use_container_width=True):
            st.switch_page("pages/4_Feed_Rate.py")
