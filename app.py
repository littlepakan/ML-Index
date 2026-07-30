import streamlit as st
import os

# ตั้งค่าหน้าตาเว็บไซต์
st.set_page_config(
    page_title="My Streamlit Projects Hub",
    page_icon="🚀",
    layout="wide"
)

# ==========================================
# 1. ส่วนข้อมูลผู้พัฒนา (แก้ไข ชื่อ-นามสกุล และรูปตรงนี้)
# ==========================================
DEV_NAME = "นายสมชาย ใจดี"           # แก้ไข ชื่อ-นามสกุล
DEV_ROLE = "นักพัฒนา Machine Learning / Data Science" # แก้ไข ตำแหน่ง/คำอธิบาย
DEV_IMAGE = "img/profile.png"          # ภาพโปรไฟล์ผู้พัฒนา (อยู่ในโฟลเดอร์ img/)

# แสดงผลส่วนผู้พัฒนา
with st.container(border=True):
    col_dev_img, col_dev_info = st.columns([1, 4], vertical_alignment="center")
    
    with col_dev_img:
        # เช็คว่ามีไฟล์รูปไหม ถ้าไม่มีจะแสดงข้อความแทนเพื่อไม่ให้โค้ดพัง
        if os.path.exists(DEV_IMAGE):
            st.image(DEV_IMAGE, use_container_width=True)
        else:
            st.info("📌 ใส่รูปโปรไฟล์ที่ `img/profile.png`")
            
    with col_dev_info:
        st.subheader("👨‍💻 ผู้พัฒนาผลงาน")
        st.title(DEV_NAME)
        st.write(DEV_ROLE)

st.write("") # เว้นบรรทัด
st.divider()

# ==========================================
# 2. ข้อมูลโครงการทั้ง 6 งาน (ดึงรูปจากโฟลเดอร์ img/)
# ==========================================
projects = [
    {
        "title": "KNN with Heart",
        "description": "โมเดลวิเคราะห์และทำนายด้วยอัลกอริทึม K-Nearest Neighbors",
        "image": "img/knn.png",
        "url": "https://knnwithheart-otgfaanixrepowwjwrfs2q.streamlit.app/"
    },
    {
        "title": "Decision Tree App",
        "description": "การจำแนกข้อมูลและวิเคราะห์ต้นไม้ตัดสินใจ",
        "image": "img/decision_tree.png",
        "url": "https://decisiontree-apjtjdnsphgyalfoiimpxy.streamlit.app/"
    },
    {
        "title": "Streamlit App Project 3",
        "description": "แอปพลิเคชันวิเคราะห์ข้อมูลประมวลผลบน Streamlit",
        "image": "img/project3.png",
        "url": "https://tvdwfxyqu48e4af2veepky.streamlit.app/"
    },
    {
        "title": "Streamlit App Project 4",
        "description": "แอปพลิเคชันแสดงผลข้อมูลแบบ Interactive",
        "image": "img/project4.png",
        "url": "https://4u4kaz4xbjr9dfbqomvat8.streamlit.app/"
    },
    {
        "title": "Regression Model",
        "description": "โมเดลการถดถอยพยากรณ์ข้อมูลเชิงปริมาณ",
        "image": "img/regression.png",
        "url": "https://regression-dn8txr3qernzhhnczecmsa.streamlit.app/"
    },
    {
        "title": "Random Forest Model",
        "description": "โมเดลจำแนกประเภทข้อมูลโดยใช้ Random Forest",
        "image": "img/random_forest.png",
        "url": "https://randomforest-rdafgcqmqhclbqncxyjvg3.streamlit.app/"
    }
]

# ==========================================
# 3. จัดแสดงการ์ดผลงานเป็น Grid 3 คอลัมน์
# ==========================================
st.subheader("📦 รวมผลงานทั้งหมด")

cols = st.columns(3)

for idx, project in enumerate(projects):
    with cols[idx % 3]:
        with st.container(border=True):
            # แสดงภาพปก
            if os.path.exists(project["image"]):
                st.image(project["image"], use_container_width=True)
            else:
                st.warning(f"ยังไม่มีรูป ` {project['image']} `")
            
            # หัวข้อและคำอธิบาย
            st.subheader(project["title"])
            st.caption(project["description"])
            
            # ปุ่มลิงก์เปิดเว็บ
            st.link_button("เปิดใช้งานเว็บ ➔", project["url"], use_container_width=True)