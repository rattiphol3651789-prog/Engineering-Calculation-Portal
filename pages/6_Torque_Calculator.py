
import streamlit as st

st.set_page_config(
    page_title="Torque Calculator",
    page_icon="🔧",
    layout="wide"
)

st.title("🔧 Torque Calculator")
st.caption("เครื่องคำนวณแรงบิดทางวิศวกรรม")

if st.button("⬅️ กลับหน้า Mechanical"):
    st.switch_page("pages/5_Mechanical.py")

st.divider()

st.subheader("กรอกข้อมูลสำหรับคำนวณ")

col1, col2 = st.columns(2)

with col1:
    force = st.number_input(
        "Force (F) : แรงที่กระทำ (N)",
        min_value=0.0,
        value=100.0,
        step=10.0
    )

with col2:
    lever_arm = st.number_input(
        "Lever Arm (L) : ระยะแขนแรง (mm)",
        min_value=0.0,
        value=200.0,
        step=10.0
    )

# แปลงระยะจาก mm เป็น m
lever_arm_m = lever_arm / 1000

# คำนวณแรงบิด
torque = force * lever_arm_m

st.divider()

st.subheader("ผลการคำนวณ")

st.success(f"แรงบิด (Torque) = {torque:,.2f} N·m")

st.divider()

st.subheader("สูตรคำนวณ")

st.latex(r"T = F \times L")

st.write("T = Torque (N·m)")
st.write("F = Force (N)")
st.write("L = Lever Arm (m)")

st.info("หมายเหตุ: สูตรนี้ใช้กรณีแรงกระทำตั้งฉากกับแขนแรง")

