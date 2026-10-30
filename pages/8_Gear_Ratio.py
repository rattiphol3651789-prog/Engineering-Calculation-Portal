
import streamlit as st

st.set_page_config(
    page_title="Gear Ratio Calculator",
    page_icon="⚙️",
    layout="wide"
)

st.title("⚙️ Gear Ratio Calculator")
st.caption("เครื่องคำนวณอัตราทดเกียร์")

if st.button("⬅️ กลับหน้า Mechanical"):
    st.switch_page("pages/5_Mechanical.py")

st.divider()

st.subheader("กรอกข้อมูลจำนวนฟันของเฟือง")

col1, col2 = st.columns(2)

with col1:
    driver_teeth = st.number_input(
        "Driver Gear : จำนวนฟันเฟืองขับ",
        min_value=1,
        value=20,
        step=1
    )

with col2:
    driven_teeth = st.number_input(
        "Driven Gear : จำนวนฟันเฟืองตาม",
        min_value=1,
        value=60,
        step=1
    )

# คำนวณอัตราทด
gear_ratio = driven_teeth / driver_teeth

st.divider()

st.subheader("ผลการคำนวณ")

st.success(f"Gear Ratio = {gear_ratio:.2f} : 1")

st.divider()

st.subheader("สูตรคำนวณ")

st.latex(r"Gear\ Ratio = \frac{N_{Driven}}{N_{Driver}}")

st.write("N Driven = จำนวนฟันเฟืองตาม")
st.write("N Driver = จำนวนฟันเฟืองขับ")

st.info(
    "หมายเหตุ: การคำนวณนี้ใช้กับชุดเฟืองภายนอก 2 ตัว "
    "โดยอัตราทดความเร็วรอบเป็นอัตราส่วนผกผันกับจำนวนฟัน"
)
