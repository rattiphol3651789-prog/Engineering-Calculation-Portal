
import streamlit as st

st.set_page_config(
    page_title="Mechanical Menu",
    page_icon="🔩",
    layout="wide"
)

# หัวข้อหน้า
st.title("🔩 Mechanical Calculator")
st.caption("เลือกเครื่องมือคำนวณที่ต้องการใช้งาน")

# ปุ่มกลับหน้าหลัก
if st.button("🏠 กลับหน้าหลัก"):
    st.switch_page("app.py")

st.divider()

# สร้างการ์ด 3 คอลัมน์
col1, col2, col3 = st.columns(3)

# การ์ดที่ 1 : Torque
with col1:
    with st.container(border=True):
        st.subheader("🔧 Torque")
        st.write("คำนวณแรงบิด (Torque)")

        if st.button(
            "เข้าสู่การคำนวณ",
            key="torque",
            use_container_width=True
        ):
            st.switch_page("pages/6_Torque_Calculator.py")

# การ์ดที่ 2 : Force
with col2:
    with st.container(border=True):
        st.subheader("💪 Force")
        st.write("คำนวณแรง (Force)")

        if st.button(
            "เข้าสู่การคำนวณ",
            key="force",
            use_container_width=True
        ):
            st.switch_page("pages/7_Force_Calculator.py")

# การ์ดที่ 3 : Gear Ratio
with col3:
    with st.container(border=True):
        st.subheader("⚙️ Gear Ratio")
        st.write("คำนวณอัตราทดเกียร์")

        if st.button(
            "เข้าสู่การคำนวณ",
            key="gear_ratio",
            use_container_width=True
        ):
            st.switch_page("pages/8_Gear_Ratio.py")
