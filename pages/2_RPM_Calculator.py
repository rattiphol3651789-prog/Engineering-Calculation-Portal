
import streamlit as st

st.set_page_config(
    page_title="RPM Calculator",
    page_icon="⚙️",
    layout="wide"
)

st.title("🔄 RPM Calculator")
st.caption("เครื่องคำนวณความเร็วรอบเครื่องจักร")

if st.button("⬅️ กลับหน้า Machining"):
    st.switch_page("pages/1_Machining.py")

st.divider()

st.subheader("กรอกข้อมูลสำหรับคำนวณ")

col1, col2 = st.columns(2)

with col1:
    cutting_speed = st.number_input(
        "Cutting Speed (Vc) : m/min",
        min_value=0.0,
        value=100.0,
        step=10.0
    )

with col2:
    diameter = st.number_input(
        "Diameter (D) : mm",
        min_value=0.0,
        value=10.0,
        step=1.0
    )

if diameter > 0:
    rpm = (1000 * cutting_speed) / (3.14159 * diameter)
    st.success(f"ความเร็วรอบ = {rpm:,.0f} RPM")
else:
    st.warning("กรุณากรอก Diameter มากกว่า 0 mm")

st.divider()

st.subheader("สูตรคำนวณ")
st.latex(r"RPM = \frac{1000 \times Vc}{\pi \times D}")

st.caption("Vc = Cutting Speed (m/min) | D = Diameter (mm)")
