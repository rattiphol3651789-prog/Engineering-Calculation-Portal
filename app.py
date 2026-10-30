
import streamlit as st

st.set_page_config(
    page_title="Engineering Calculator",
    page_icon="🧮",
    layout="wide"
)

st.title("🧮 Engineering Calculator")
st.caption("เครื่องมือคำนวณสำหรับงานวิศวกรรม")

st.write("เลือกหมวดหมู่ที่ต้องการใช้งาน")

st.divider()

col1, col2, col3, col4 = st.columns(4)

with col1:
    with st.container(border=True):
        st.subheader("⚙️ Machining")
        st.write("RPM, Cutting Speed และ Feed Rate")

        if st.button("เข้าสู่เมนู", key="machining", use_container_width=True):
            st.switch_page("pages/1_Machining.py")

with col2:
    with st.container(border=True):
        st.subheader("🔩 Mechanical")
        st.write("เครื่องมือคำนวณทางวิศวกรรมเครื่องกล")

        if st.button("เข้าสู่เมนู", key="mechanical", use_container_width=True):
            st.switch_page("pages/5_Mechanical.py")

with col3:
    with st.container(border=True):
        st.subheader("📏 Quality")
        st.write("Defect Rate, Yield และ PPM")
        st.info("กำลังพัฒนา")

with col4:
    with st.container(border=True):
        st.subheader("🏭 Production")
        st.write("Cycle Time, Takt Time และ OEE")
        st.info("กำลังพัฒนา")
