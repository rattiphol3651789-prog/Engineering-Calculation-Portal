
import streamlit as st

st.set_page_config(
    page_title="Feed Rate Calculator",
    page_icon="📏",
    layout="wide"
)

st.title("📏 Feed Rate Calculator")
st.subheader("เครื่องคำนวณอัตราป้อนสำหรับ CNC Milling")

if st.button("⬅️ กลับหน้า Machining"):
    st.switch_page("pages/1_Machining.py")

st.divider()

st.write("กรอกข้อมูล Cutting Tool และความเร็วรอบของเครื่องจักร")

col1, col2 = st.columns(2)

with col1:
    rpm = st.number_input(
        "Spindle Speed (RPM)",
        min_value=0.0,
        value=1000.0,
        step=100.0
    )

    teeth = st.number_input(
        "Number of Teeth (Z)",
        min_value=1,
        value=4,
        step=1
    )

with col2:
    feed_per_tooth = st.number_input(
        "Feed per Tooth (fz) : mm/tooth",
        min_value=0.0,
        value=0.05,
        step=0.01,
        format="%.3f"
    )

st.divider()

feed_rate = rpm * teeth * feed_per_tooth

st.success(f"Feed Rate = {feed_rate:,.2f} mm/min")

st.markdown("### สูตรคำนวณ")

st.latex(r"Feed\ Rate = RPM \times Z \times f_z")

st.caption(
    "RPM = ความเร็วรอบ | Z = จำนวนฟัน | fz = อัตราป้อนต่อฟัน"
)
