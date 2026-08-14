import streamlit as st
import os
from openai import OpenAI


# 设置页面的配置项
st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="🤖",
    # 布局
    layout="wide",
    # 控制侧边栏
    initial_sidebar_state="expanded",
    menu_items={}
)

# 标题
st.title("AI智能伴侣")

# logo
st.logo("resources/logo.png")

# 系统提示词
system_prompt = "你是一个冷酷的AI智能伴侣，只回答与用户相关的问题，不回答其他问题。"

# 初始化聊天信息
if 'messages' not in st.session_state:
    st.session_state.messages = []

# 显示会话历史
for message in st.session_state.messages: # {"role": "user", "content": prompt}
    st.chat_message(message["role"]).write(message["content"])

# 创建AI大模型交互客户端
client = OpenAI(
    # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx"
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://ws-jb5yoisbhvb75h6l.cn-beijing.maas.aliyuncs.com/compatible-mode/v1",
)

# 消息输入框
prompt = st.chat_input("请输入您的问题：")
if prompt:   # 字符串会自动判断是否为空字符串
    st.chat_message("user").write(prompt)
    print("----------> 调用AI大模型，提示词：", prompt)
    # 添加用户消息到会话历史
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 调用AI大模型
    completion = client.chat.completions.create(
        # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
        model="deepseek-v4-flash-0731",
        messages=[
            {"role": "system", "content": system_prompt},
            *st.session_state.messages,
        ],
        stream=True
    )

    # # 输出AI大模型返回的内容(非流式输出)
    # print("----------> AI大模型返回的内容：", completion.choices[0].message.content)
    # st.chat_message("assistant").write(completion.choices[0].message.content)

    # 输出AI大模型返回的内容(流式输出)
    completion_message = st.chat_message("assistant")
    write_box = completion_message.empty() # 空容器，用于显示AI大模型返回的内容
    full_response = ""
    for chunk in completion:
        if not chunk.choices:
            continue
        if chunk.choices[0].delta.content:
            full_response += chunk.choices[0].delta.content
            write_box.write(full_response)

    # 添加AI大模型返回的内容到会话历史
    st.session_state.messages.append({"role": "assistant", "content": full_response})
