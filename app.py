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
DEV_NAME = "นายปกานต์ วงษ์ท่าเรือ"           # แก้ไข ชื่อ-นามสกุล
DEV_ROLE = "664245056 66/44" # แก้ไข ตำแหน่ง

DEV_GITHUB = "https://github.com/your-username" # 👈 เพิ่มลิงก์ส่วนตัวตรงนี้ (นำ URL มาใส่)

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
        
        # 👈 เพิ่มปุ่มลิงก์ส่วนตัวตรงนี้
        st.link_button("🌐 โปรไฟล์ GitHub ผู้พัฒนา", DEV_GITHUB)

# ==========================================
# 2. ข้อมูลโครงการทั้ง 6 งาน 
# (ระบุแค่ชื่อไฟล์ไม่ต้องใส่นามสกุล เช่น 'knn', 'decisiontree')
# สามารถนำ URL GitHub มาวางแทนที่ '#' ได้ในภายหลัง
# ==========================================
projects = [
    {
        "title": "KNN with Heart",
        "description": "โมเดลวิเคราะห์และทำนายด้วยอัลกอริทึม K-Nearest Neighbors",
        "img_name": "knn",
        "url": "https://knnwithheart-otgfaanixrepowwjwrfs2q.streamlit.app/",
        "github": "https://github.com/littlepakan/knnwithheart/blob/main/KnnwithHeart.py"  # 👈 นำลิงก์ GitHub มาแก้ตรงนี้
    },
    {
        "title": "Decision Tree Classifier",
        "description": "การจำแนกข้อมูลและวิเคราะห์ต้นไม้ตัดสินใจ",
        "img_name": "decisiontree",
        "url": "https://decisiontree-apjtjdnsphgyalfoiimpxy.streamlit.app/",
        "github": "https://github.com/littlepakan/decisiontree/blob/main/app.py"  # 👈 นำลิงก์ GitHub มาแก้ตรงนี้
    },
    {
        "title": "FlatFoot Filter App (SVM Classifier Version)",
        "description": "แอปพลิเคชันวิเคราะห์ข้อมูลและจำแนกประเภทโดยใช้ SVM Classifier ในหัวข้อโรคเท้าแบน",
        "img_name": "svm",
        "url": "https://tvdwfxyqu48e4af2veepky.streamlit.app/",
        "github": "https://github.com/littlepakan/pesplanussvm/blob/main/app.py"  # 👈 นำลิงก์ GitHub มาแก้ตรงนี้
    },
    {
        "title": "K-Means Clustering App",
        "description": "แอปพลิเคชันแสดงผลข้อมูลแบบ Clustering โดยใช้ K-Means Algorithm",
        "img_name": "kmean",
        "url": "https://4u4kaz4xbjr9dfbqomvat8.streamlit.app/",
        "github": "https://github.com/littlepakan/kmean/blob/main/streamlit_app.py"  # 👈 นำลิงก์ GitHub มาแก้ตรงนี้
    },
    {
        "title": "Regression Model",
        "description": "โมเดลการถดถอยพยากรณ์ข้อมูลเชิงปริมาณ",
        "img_name": "regression",
        "url": "https://regression-dn8txr3qernzhhnczecmsa.streamlit.app/",
        "github": "https://github.com/littlepakan/regression/blob/main/app.py"  # 👈 นำลิงก์ GitHub มาแก้ตรงนี้
    },
    {
        "title": "Random Forest Model",
        "description": "โมเดลจำแนกประเภทข้อมูลโดยใช้ Random Forest",
        "img_name": "randomforest",
        "url": "https://randomforest-rdafgcqmqhclbqncxyjvg3.streamlit.app/",
        "github": "https://github.com/littlepakan/randomforest/blob/main/app.py"  # 👈 นำลิงก์ GitHub มาแก้ตรงนี้
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
            
            # ปุ่มลิงก์เปิดเว็บ และ ลิงก์ GitHub แบบวางคู่กัน
            btn_col1, btn_col2 = st.columns(2)
            with btn_col1:
                st.link_button("เปิดเว็บ ➔", project["url"], use_container_width=True)
            with btn_col2:
                st.link_button("💻 GitHub", project["github"], use_container_width=True)