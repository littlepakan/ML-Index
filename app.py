import streamlit as st
import os

# ตั้งค่าหน้าตาเว็บไซต์
st.set_page_config(
    page_title="My Streamlit Projects Hub",
    page_icon="🚀",
    layout="wide"
)

# ---------------------------------------------------------
# ฟังก์ชันช่วยหา Path รูปภาพแบบสแกนนามสกุล (.png, .jpg, .jpeg)
# ---------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_image_path(filename_without_ext):
    """
    รับชื่อไฟล์ (เช่น 'knn' หรือ 'profile') แล้วค้นหาว่ามีนามสกุลไหนอยู่ในโฟลเดอร์ img/
    """
    extensions = ['', '.png', '.jpg', '.jpeg', '.PNG', '.JPG', '.JPEG', '.webp']
    for ext in extensions:
        full_path = os.path.join(BASE_DIR, "img", f"{filename_without_ext}{ext}")
        if os.path.exists(full_path):
            return full_path
    return None

# ==========================================
# 1. ส่วนข้อมูลผู้พัฒนา
# ==========================================
DEV_NAME = "นายสมชาย ใจดี"           # แก้ไข ชื่อ-นามสกุล
DEV_ROLE = "นักพัฒนา Machine Learning / Data Science" # แก้ไข ตำแหน่ง

profile_img_path = get_image_path("profile")

with st.container(border=True):
    col_dev_img, col_dev_info = st.columns([1, 4], vertical_alignment="center")
    
    with col_dev_img:
        if profile_img_path:
            st.image(profile_img_path, use_container_width=True)
        else:
            st.info("📌 ใส่รูปโปรไฟล์ชื่อ `profile` ไว้ในโฟลเดอร์ `img`")
            
    with col_dev_info:
        st.subheader("👨‍💻 ผู้พัฒนาผลงาน")
        st.title(DEV_NAME)
        st.write(DEV_ROLE)

st.write("") 
st.divider()

# ==========================================
# 2. ข้อมูลโครงการทั้ง 6 งาน 
# (ระบุแค่ชื่อไฟล์ไม่ต้องใส่นามสกุล เช่น 'knn', 'decision_tree')
# ==========================================
projects = [
    {
        "title": "KNN with Heart",
        "description": "โมเดลวิเคราะห์และทำนายด้วยอัลกอริทึม K-Nearest Neighbors",
        "img_name": "knn",
        "url": "https://knnwithheart-otgfaanixrepowwjwrfs2q.streamlit.app/"
    },
    {
        "title": "Decision Tree App",
        "description": "การจำแนกข้อมูลและวิเคราะห์ต้นไม้ตัดสินใจ",
        "img_name": "decision_tree",
        "url": "https://decisiontree-apjtjdnsphgyalfoiimpxy.streamlit.app/"
    },
    {
        "title": "Streamlit App Project 3",
        "description": "แอปพลิเคชันวิเคราะห์ข้อมูลประมวลผลบน Streamlit",
        "img_name": "project3",
        "url": "https://tvdwfxyqu48e4af2veepky.streamlit.app/"
    },
    {
        "title": "Streamlit App Project 4",
        "description": "แอปพลิเคชันแสดงผลข้อมูลแบบ Interactive",
        "img_name": "project4",
        "url": "https://4u4kaz4xbjr9dfbqomvat8.streamlit.app/"
    },
    {
        "title": "Regression Model",
        "description": "โมเดลการถดถอยพยากรณ์ข้อมูลเชิงปริมาณ",
        "img_name": "regression",
        "url": "https://regression-dn8txr3qernzhhnczecmsa.streamlit.app/"
    },
    {
        "title": "Random Forest Model",
        "description": "โมเดลจำแนกประเภทข้อมูลโดยใช้ Random Forest",
        "img_name": "random_forest",
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
            # ค้นหาไฟล์รูปในโฟลเดอร์ img/
            img_path = get_image_path(project["img_name"])
            
            # แสดงภาพปก
            if img_path:
                st.image(img_path, use_container_width=True)
            else:
                st.warning(f"⚠️ ไม่พบรูปชื่อ `{project['img_name']}` ในโฟลเดอร์ img")
            
            # หัวข้อและคำอธิบาย
            st.subheader(project["title"])
            st.caption(project["description"])
            
            # ปุ่มลิงก์เปิดเว็บ
            st.link_button("เปิดใช้งานเว็บ ➔", project["url"], use_container_width=True)