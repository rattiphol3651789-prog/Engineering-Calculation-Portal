
import streamlit as st

st.set_page_config(
    page_title="Force Calculator",
    page_icon="💪",
    layout="wide"
)

st.title("💪 Force Calculator")
st.caption("เครื่องคำนวณแรงตามกฎข้อที่ 2 ของนิวตัน")

if st.button("⬅️ กลับหน้า Mechanical"):
    st.switch_page("pages/5_Mechanical.py")

st.divider()

st.subheader("กรอกข้อมูลสำหรับคำนวณ")

col1, col2 = st.columns(2)

with col1:
    mass = st.number_input(
        "Mass (m) : มวล (kg)",
        min_value=0.0,
        value=10.0,
        step=1.0
    )

with col2:
    acceleration = st.number_input(
        "Acceleration (a) : ความเร่ง (m/s²)",
        min_value=0.0,
        value=2.0,
        step=0.5
    )

# คำนวณแรง
force = mass * acceleration

st.divider()

st.subheader("ผลการคำนวณ")

st.success(f"แรง (Force) = {force:,.2f} N")

st.divider()

st.subheader("สูตรคำนวณ")

st.latex(r"F = m \times a")

st.write("F = Force (N)")
st.write("m = Mass (kg)")
st.write("a = Acceleration (m/s²)")

st.info("หมายเหตุ: เป็นการคำนวณแรงลัพธ์ตามกฎข้อที่ 2 ของนิวตัน")

