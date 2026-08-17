import streamlit as st
import os
from openai import OpenAI
from datetime import datetime
import json


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


# 保存会话数据
def save_session():
    if st.session_state.current_session:
        # 构建会话数据
        session_data = {
            "nick_name": st.session_state.nick_name,
            "nature": st.session_state.nature,
            "current_session": st.session_state.current_session,
            "messages": st.session_state.messages,
        }
        # 如果会话文件夹不存在，创建它
        if not os.path.exists("sessions"):
            os.mkdir("sessions")

        # 保存会话数据
        with open(f"sessions/{st.session_state.current_session}.json", "w", encoding="utf-8") as f:
            json.dump(session_data, f, ensure_ascii=False, indent=4)


# 加载所有会话列表
def load_sessions():
    sesion_list = []
    # 加载sessions文件夹下的文件
    if os.path.exists("sessions"):
        file_list = os.listdir("sessions")
        for filenmae in file_list:
            if filenmae.endswith(".json"):
                sesion_list.append(filenmae[:-5])
    sesion_list.sort(reverse=True)
    return sesion_list


# 加载指定会话信息
def load_session(session_id):
    try:
        if os.path.exists(f"sessions/{session_id}.json"):
            with open(f"sessions/{session_id}.json", "r", encoding="utf-8") as f:
                session_data = json.load(f)
                st.session_state.nick_name = session_data["nick_name"]
            st.session_state.nature = session_data["nature"]
            st.session_state.current_session = session_data["current_session"]
            st.session_state.messages = session_data["messages"]
    except Exception:
        st.error("加载会话失败!")


# 删除会话信息
def delete_session(session_id):
    try:
        if os.path.exists(f"sessions/{session_id}.json"):
            os.remove(f"sessions/{session_id}.json")
            # 如果删除的会话是当前会话，需要更新信息列表
            if session_id == st.session_state.current_session:
                st.session_state.current_session = generate_session_id()
                st.session_state.messages = []
    except Exception:
        st.error("删除会话失败!")


# 生成会话标识
def generate_session_id():
    # strftime() 方法用于格式化 datetime 对象，将其转换为字符串
    # 例如：2023-12-25_14-30-00
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# 标题
st.title("AI智能伴侣")

# logo
st.logo("resources/logo.png")

# 系统提示词
system_prompt = """
        你叫 %s，现在是用户的真实伴侣，请完全代入伴侣角色。
        规则：
            1. 每次只回1条消息
            2. 禁止任何场景或状态描述性文字
            3. 匹配用户的语言
            4. 回复简短，像微信聊天一样
            5. 有需要的话可以用❤️🌸等emoji表情
            6. 用符合伴侣性格的方式对话
            7. 回复的内容, 要充分体现伴侣的性格特征
        伴侣性格：
            - %s
        你必须严格遵守上述规则来回复用户。
    """

# 初始化聊天信息
# session_state 是 Streamlit 提供的一个全局变量，用于存储用户之间的状态信息
if 'messages' not in st.session_state:
    st.session_state.messages = []

# 昵称
if 'nick_name' not in st.session_state:
    st.session_state.nick_name = "智能伴侣"

# 性格
if 'nature' not in st.session_state:
    st.session_state.nature = "温柔可爱"

# 会话标识
if 'current_session' not in st.session_state:
    st.session_state.current_session = generate_session_id()


# 左侧的侧边栏
with st.sidebar:
    # 会话信息
    st.write("AI控制面板")

    # 新建会话
    if st.button("新建会话", width="stretch", icon="✏️"):
        # 1.保存当前会话信息
        save_session()

        # 2. 创建新的会话
        if st.session_state.messages: # 如果会话历史不为空，True, 则执行新建会话操作
            st.session_state.messages = []
            st.session_state.current_session = generate_session_id()
            save_session()
            st.rerun() # 刷新页面，显示新的会话标识

    # 会话历史
    st.text("会话历史")
    session_list = load_sessions()
    for session in session_list:
        colm1, colm2 = st.columns([4, 1])
        with colm1:
            # 显示会话信息
            if st.button(session, width="stretch", icon="📄", key=f"load_{session}", type="primary" if session == st.session_state.current_session else "secondary"):
                load_session(session)
                st.rerun() # 刷新页面，显示新的会话历史
        with colm2:
            # 删除会话信息
            if st.button("", width="stretch", icon="❌", key=f"delete_{session}"):
                delete_session(session)
                st.rerun() # 刷新页面，显示最新的会话列表

    # 分割线
    st.divider()

    st.subheader("伴侣信息")
    # placeholder的作用：在输入框中显示提示信息，当用户输入内容时，提示信息会自动消失
    # value的作用：设置输入框的默认值
    nick_name = st.text_input("昵称", placeholder="请输入伴侣的昵称", value=st.session_state.nick_name)
    if nick_name:
        st.session_state.nick_name = nick_name
    nature = st.text_input("性格", placeholder="请输入伴侣的性格", value=st.session_state.nature)
    if nature:
        st.session_state.nature = nature

# 显示会话历史
st.text(f"会话名称：{st.session_state.current_session}")
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
        messages=[# 系统提示词占位符，用于填充用户输入的昵称和性格
            {"role": "system", "content": system_prompt % (st.session_state.nick_name, st.session_state.nature)},
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

    # 保存当前会话信息
    save_session()
