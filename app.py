import streamlit as st

# ตั้งค่าหน้าตาเว็บไซต์
st.set_page_config(
    page_title="My Streamlit Projects Hub",
    page_icon="🚀",
    layout="wide"
)

# ส่วน หัวข้อหลัก
st.title("🚀 My Streamlit Projects")
st.write("รวมผลงานแอปพลิเคชันและโมเดล Machine Learning ทั้งหมด")
st.divider()

# ข้อมูลโครงการทั้ง 6 งาน (แก้ไขรูปภาพ, ชื่อ, และคำอธิบายตรงนี้ได้เลย)
projects = [
    {
        "title": "KNN with Heart",
        "description": "โมเดลวิเคราะห์และทำนายด้วยอัลกอริทึม K-Nearest Neighbors",
        "image": "https://images.unsplash.com/photo-1505751172876-fa1923c5c528?w=600&q=80",
        "url": "https://knnwithheart-otgfaanixrepowwjwrfs2q.streamlit.app/"
    },
    {
        "title": "Decision Tree App",
        "description": "การจำแนกข้อมูลและวิเคราะห์ต้นไม้ตัดสินใจ",
        "image": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&q=80",
        "url": "https://decisiontree-apjtjdnsphgyalfoiimpxy.streamlit.app/"
    },
    {
        "title": "Streamlit App Project 3",
        "description": "แอปพลิเคชันวิเคราะห์ข้อมูลประมวลผลบน Streamlit",
        "image": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=600&q=80",
        "url": "https://tvdwfxyqu48e4af2veepky.streamlit.app/"
    },
    {
        "title": "Streamlit App Project 4",
        "description": "แอปพลิเคชันแสดงผลข้อมูลแบบ Interactive",
        "image": "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=600&q=80",
        "url": "https://4u4kaz4xbjr9dfbqomvat8.streamlit.app/"
    },
    {
        "title": "Regression Model",
        "description": "โมเดลการถดถอยพยากรณ์ข้อมูลเชิงปริมาณ",
        "image": "https://images.unsplash.com/photo-1543286386-713bdd548da4?w=600&q=80",
        "url": "https://regression-dn8txr3qernzhhnczecmsa.streamlit.app/"
    },
    {
        "title": "Random Forest Model",
        "description": "โมเดลจำแนกประเภทข้อมูลโดยใช้ Random Forest",
        "image": "https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?w=600&q=80",
        "url": "https://randomforest-rdafgcqmqhclbqncxyjvg3.streamlit.app/"
    }
]

# จัดแสดงเป็น Grid 3 คอลัมน์ (จะปรับเปลี่ยนเป็น 2 คอลัมน์บนหน้าจอขนาดเล็กอัตโนมัติ)
cols = st.columns(3)

for idx, project in enumerate(projects):
    with cols[idx % 3]:
        # ใช้ container ล้อมรอบเพื่อทำเป็นกรอบการ์ด
        with st.container(border=True):
            # แสดงภาพปก
            st.image(project["image"], use_container_width=True)
            
            # หัวข้อและคำอธิบาย
            st.subheader(project["title"])
            st.caption(project["description"])
            
            # ปุ่มลิงก์เปิดเว็บ
            st.link_button("เปิดใช้งานเว็บ ➔", project["url"], use_container_width=True)