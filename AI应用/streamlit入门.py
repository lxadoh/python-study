import streamlit as st


# 设置页面的配置项
st.set_page_config(
    page_title="streamlit入门",
    page_icon="🧊",
    # 布局
    layout="wide",
    # 控制侧边栏
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)


# 大标题
st.title("streamlit 入门演示")
st.header("streamlit 一级标题")
st.subheader("streamlit 二级标题")

# 段落文字
st.write("布偶猫是原产于美国的大型宠物猫品种，凭借超高颜值与温顺性格，被誉为“猫中仙女”，是当下最受欢迎的家庭伴侣猫之一。它们体型偏大，体态舒展优雅，全身覆盖蓬松柔软的中长毛，毛发顺滑不易打结，自带温柔氛围感。标志性的湛蓝眼眸清澈透亮，搭配精致的重点色纹路，面部、耳朵、四肢和尾部色彩浓郁，躯干毛色浅淡，颜值十分出众。")
st.write("布偶猫性格温顺黏人、温柔乖巧，脾气极好，几乎没有攻击性，忍耐力极强，即便被拉扯毛发也极少反抗，格外适合有小孩和其他宠物的家庭。它们性情安静软糯，不爱乱叫，喜欢跟随主人身边，互动性极强，擅长撒娇黏人，适配居家饲养。")
st.write("作为长毛猫，布偶猫日常需要梳理毛发预防打结，且肠胃相对敏感，饲养时需清淡喂食、细心照料。它们寿命较长，性格稳定亲人，温柔治愈的特质，让其成为绝佳的陪伴宠物。")

# 图片
# ./ 当前目录
# st.image("./resources/cat.jpg")
st.image("resources/cat.jpg")

# 音频
st.audio("resources/news.mp3")

# 视频
st.video("resources/news.mp4")

# logo
st.logo("resources/logo.png")

# 表格
student_data = {
    "姓名": ["韩立", "南宫婉", "银月"],
    "学号": ["202601", "202602", "202603"],
    "语文": [98, 90, 59],
    "数学": [88, 78, 65],
    "英语": [99, 89, 87],
    "总分": [285, 257, 211]
}
st.table(student_data)

# 输入框
# 普通输入框
name = st.text_input("请输入姓名：")
st.write(f"您输入的姓名为：{name}")

# 密码输入框
password = st.text_input("请输入密码：", type="password")
st.write(f"您输入的密码为：{password}")

# 单选按钮
gender = st.radio("请输入您的性别：", ["男", "女", "未知"])
st.write(f"您的性别为：{gender}")