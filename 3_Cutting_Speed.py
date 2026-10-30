
import streamlit as st

st.set_page_config(
    page_title="Cutting Speed Calculator",
    page_icon="✂️",
    layout="wide"
)

st.title("✂️ Cutting Speed Calculator")
st.subheader("เครื่องคำนวณความเร็วตัด")

if st.button("⬅️ กลับหน้า Machining"):
    st.switch_page("pages/1_Machining.py")

st.divider()

st.write("กรอกความเร็วรอบและเส้นผ่านศูนย์กลางของชิ้นงานหรือเครื่องมือตัด")

col1, col2 = st.columns(2)

with col1:
    rpm = st.number_input(
        "Spindle Speed (RPM)",
        min_value=0.0,
        value=1000.0,
        step=100.0
    )

with col2:
    diameter = st.number_input(
        "Diameter (mm)",
        min_value=0.0,
        value=10.0,
        step=1.0
    )

if diameter > 0:
    cutting_speed = (3.14159 * diameter * rpm) / 1000

    st.success(
        f"Cutting Speed = {cutting_speed:,.2f} m/min"
    )
else:
    st.warning("กรุณากรอก Diameter มากกว่า 0 mm")

st.divider()

st.markdown("### สูตรคำนวณ")

st.latex(r"Vc = \frac{\pi \times D \times RPM}{1000}")

st.caption("Vc = Cutting Speed (m/min) | D = Diameter (mm) | RPM = ความเร็วรอบ")
