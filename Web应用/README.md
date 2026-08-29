# 🪄 汉字谜盒

一个基于 **FastAPI + 阿里云百炼大模型** 的汉字字谜互动小游戏。

AI 会随机出一道字谜，你输入答案进行猜测；答对了它会夸你并揭晓谜底，答错了会给提示但绝不剧透，直到你主动说"公布答案"或"不知道"。所有对局都会以 JSON 文件的形式保存在本地，可随时回看或删除。

> 本项目是 Python Web 学习的实战练习，代码以"能跑通、好读懂"为第一目标。

---

## 📋 目录

- [功能特性](#功能特性)
- [技术栈](#技术栈)
- [目录结构](#目录结构)
- [快速开始](#快速开始)
  - [1. 安装依赖](#1-安装依赖)
  - [2. 配置 API Key](#2-配置-api-key)
  - [3. 启动服务](#3-启动服务)
- [使用方式](#使用方式)
- [API 接口文档](#api-接口文档)
- [数据流与会话存储](#数据流与会话存储)
- [前端结构说明](#前端结构说明)
- [常见问题 FAQ](#常见问题-faq)
- [后续优化方向](#后续优化方向)

---

## ✨ 功能特性

| 特性 | 说明 |
| --- | --- |
| 🎲 随机出题 | AI 每次出的字谜完全随机，会话内不重复 |
| ✅ 智能判题 | 只回复一个字即视为作答，AI 自动判断对错 |
| 💡 分层提示 | 答错只给线索不剧透；说"提示一下"给更明确的线索 |
| 🙈 主动揭晓 | 只有说"公布答案"或"不知道"时才揭晓谜底并解释 |
| 💾 多会话管理 | 支持新建、切换、删除游戏记录，刷新页面不丢失 |
| 🌓 主题切换 | 白色 / 暗黑两套主题，选择保存在浏览器 localStorage |
| 📝 统一响应 | 所有接口返回 `{code, message, data}` 结构，异常统一兜底 |
| 📊 运行日志 | 使用 `logging` 输出带时间、级别、文件名、行号的日志 |

---

## 🛠 技术栈

**后端**
- **Python 3.12**
- **FastAPI** —— Web 框架，自动生成接口文档
- **Uvicorn** —— ASGI 服务器
- **Pydantic** —— 请求体 / 响应体数据校验
- **OpenAI SDK** —— 以 OpenAI 兼容模式调用阿里云百炼大模型

**前端**
- 原生 **HTML + CSS + JavaScript**（无框架、无构建工具）
- `fetch` 调用后端接口，`localStorage` 保存主题偏好

**AI 模型**
- 模型名：`deepseek-v4-flash-0731`
- 接口地址：`https://ws-jb5yoisbhvb75h6l.cn-beijing.maas.aliyuncs.com/compatible-mode/v1`
- 参数：`stream=False`、`temperature=1.5`（提高出题随机性）

---

## 📁 目录结构

```
Web应用/
├── main.py                 # 主程序（FastAPI 应用、接口路由、AI 调用、异常处理器）
├── FastAPI入门.py          # FastAPI 最小示例，适合先跑这个感受框架
├── static/                 # 前端静态资源（通过 /static 路径对外提供）
│   ├── index.html          # 页面结构：三栏布局
│   ├── style.css           # 样式：含白色 / 暗黑两套主题
│   └── app.js              # 交互逻辑：会话管理、消息渲染、主题切换
├── sessions/               # 会话存档目录（首次启动自动创建）
│   └── 2026-08-28_13-16-49.json
└── README.md
```

---

## 🚀 快速开始

### 1. 安装依赖

```bash
pip install fastapi uvicorn openai pydantic
```

> `starlette` 会作为 FastAPI 的依赖自动安装，无需单独指定。

（可选）把依赖固化成文件，方便换机器复现：

```bash
pip freeze > requirements.txt
```

### 2. 配置 API Key

程序通过环境变量 `DASHSCOPE_API_KEY` 读取密钥：

```python
api_key=os.getenv("DASHSCOPE_API_KEY")
```

**Windows CMD（仅当前窗口有效）：**

```bat
set DASHSCOPE_API_KEY=sk-你的密钥
```

**PowerShell（仅当前窗口有效）：**

```powershell
$env:DASHSCOPE_API_KEY="sk-你的密钥"
```

**Linux / macOS：**

```bash
export DASHSCOPE_API_KEY=sk-你的密钥
```

**永久配置（Windows 推荐）：**

```powershell
[System.Environment]::SetEnvironmentVariable("DASHSCOPE_API_KEY", "sk-你的密钥", "User")
```

设置完成后**重启终端和 IDE** 才会生效。若未设置，`os.getenv` 会返回 `None`，调用大模型时会直接报错。

### 3. 启动服务

> ⚠️ **必须在 `Web应用/` 目录下启动**。代码中 `StaticFiles(directory="static")` 和 `sessions/` 都是相对路径，工作目录不对会报 `RuntimeError: Directory 'static' does not exist`。

```bash
cd Web应用
```

**方式一：直接运行（推荐新手）**

```bash
python main.py
```

**方式二：uvicorn 命令（支持热重载）**

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**方式三：fastapi 命令**

```bash
fastapi dev main.py
```

服务默认监听 `http://localhost:8000`。

---

## 🎮 使用方式

1. 浏览器打开 <http://localhost:8000> 进入游戏首页。
2. 首次进入会自动创建一个新会话，AI 主动打招呼并出第一道题。
3. 在输入框中输入你的答案（**通常只输入一个字**），回车或点击 ➤ 发送。
4. 常用指令：

| 你输入 | AI 反应 |
| --- | --- |
| 一个汉字 | 视为作答，判断对错 |
| `提示一下` | 给出线索，不公布答案 |
| `公布答案` / `不知道` | 揭晓谜底 + 解释，询问是否再来一题 |
| `换一题` / `再来一题` | 立即更换新字谜 |

5. 左侧「游戏记录」可切换历史对局，点击 ❌️ 删除。
6. 点击右上角 🎨 切换白色 / 暗黑主题，偏好会保存在浏览器中。

**自动生成的接口文档：**

| 地址 | 说明 |
| --- | --- |
| <http://localhost:8000/docs> | Swagger UI，可直接在页面上调试接口 |
| <http://localhost:8000/redoc> | ReDoc 风格文档 |
| <http://localhost:8000/openapi.json> | OpenAPI 规范 JSON |

---

## 📡 API 接口文档

所有接口的响应体统一为 `ApiResponse` 结构：

```json
{
  "code": 200,
  "message": "提示信息",
  "data": "业务数据"
}
```

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `code` | `int` | `200` 成功，`500` 服务器内部错误 |
| `message` | `str` | 提示信息 |
| `data` | `Any` | 会话 ID / 会话列表 / 会话内容 / AI 回复文本 |

---

### `GET /` —— 首页

返回 `static/index.html` 页面。

**响应：** HTML 文件流

---

### `POST /api/sessions` —— 创建会话

无需请求体。

**响应示例：**

```json
{
  "code": 200,
  "message": "创建会话成功",
  "data": "2026-08-28_13-16-49"
}
```

**处理流程：**
1. 用 `datetime.now().strftime("%Y-%m-%d_%H-%M-%S")` 生成会话 ID
2. 在 `sessions/` 下写入 `{session_id}.json`，初始内容为 `{"current_session": id, "messages": []}`
3. 返回新会话 ID

---

### `GET /api/sessions` —— 获取会话列表

**响应示例：**

```json
{
  "code": 200,
  "message": "获得会话列表成功",
  "data": ["2026-08-28_13-53-21", "2026-08-28_13-16-49"]
}
```

> 列表通过文件名去扩展名后 `sort(reverse=True)` 得到。因为文件名格式是 `年-月-日_时-分-秒`，字符串倒序正好等价于**时间倒序**，最新会话排在最前。

---

### `GET /api/sessions/{session_id}` —— 获取指定会话

**路径参数：** `session_id`，例如 `2026-08-28_13-16-49`

**响应示例：**

```json
{
  "code": 200,
  "message": "获取会话信息成功",
  "data": {
    "current_session": "2026-08-28_13-16-49",
    "messages": [
      { "role": "user", "content": "王" },
      { "role": "assistant", "content": "太棒了！就是'王'字！" }
    ]
  }
}
```

---

### `DELETE /api/sessions/{session_id}` —— 删除指定会话

**路径参数：** `session_id`

**响应示例：**

```json
{
  "code": 200,
  "message": "删除会话信息成功",
  "data": null
}
```

文件不存在时也会正常返回成功（代码中有 `os.path.exists` 判断）。

---

### `POST /api/chat` —— 与 AI 对话（核心接口）

**请求体：**

```json
{
  "session_id": "2026-08-28_13-16-49",
  "message": "王"
}
```

| 字段 | 类型 | 说明 |
| --- | --- | --- |
| `session_id` | `str` | 会话标识，格式 `%Y-%m-%d_%H-%M-%S` |
| `message` | `str` | 用户的答案或指令 |

**响应示例：**

```json
{
  "code": 200,
  "message": "请求成功",
  "data": "太棒了！就是'王'字！要不要再来一题？"
}
```

**处理流程（对应 `main.py` 中的 7 步注释）：**

```
1. 读取 sessions/{session_id}.json 加载历史消息
2. 组装 messages = [系统提示词] + 历史消息 + 本次用户输入
3. 调用大模型：model="deepseek-v4-flash-0731", temperature=1.5
4. 取 completion.choices[0].message.content 作为 AI 回复
5. 移除系统提示词，把 AI 回复追加进消息列表
6. 写回 sessions/{session_id}.json
7. 返回 AI 回复文本
```

> **设计要点**：系统提示词（角色设定、出题规则、判题规则）**不落盘**，只存在于 `main.py` 的 `SYSTEM_PROMPT` 常量中，每次请求时临时拼到消息列表最前面。这样既能随时修改人设而不影响已有会话，也避免了提示词污染历史记录。

---

### 全局异常处理

```python
@app.exception_handler(Exception)
def exception_handler(request: Request, exc: Exception):
    logging.error(f"处理异常，请求路径: {request.url}， 捕获到异常: {exc}")
    return JSONResponse(content={"code": 500, "message": "服务器内部错误，请联系管理员", "data": None})
```

任何未捕获的异常都会被记录到日志，并向前端返回统一的 `code: 500` 响应。

---

## 🔄 数据流与会话存储

```
浏览器 (static/index.html + app.js)
   │
   │  fetch('/api/...')
   ▼
FastAPI (main.py)
   │
   ├─► 读/写  sessions/{session_id}.json   ← 历史消息持久化
   │
   └─► OpenAI SDK ──► 阿里云百炼大模型 (deepseek-v4-flash-0731)
```

**一次完整对话的时序：**

1. 页面加载 → `GET /api/sessions` 拉列表 → 无会话则 `POST /api/sessions` 新建
2. 用户发送消息 → `POST /api/chat`
3. 后端加载历史 → 拼接系统提示词 → 调用大模型 → 保存新消息 → 返回回复
4. 前端渲染气泡并滚动到底部

**会话文件格式** `sessions/{session_id}.json`：

```json
{
  "current_session": "2026-08-28_13-16-49",
  "messages": [
    { "role": "user", "content": "一加一不是二，打一字" },
    { "role": "assistant", "content": "猜猜看，是什么字呢？" },
    { "role": "user", "content": "王" },
    { "role": "assistant", "content": "太棒了！就是'王'字！" }
  ]
}
```

| 字段 | 说明 |
| --- | --- |
| `current_session` | 会话 ID（与文件名一致） |
| `messages` | 消息数组，`role` 为 `user` 或 `assistant` |

> **隐私提醒**：`sessions/` 里是真实对话记录。如果要上传 GitHub，建议在 `.gitignore` 中加入 `sessions/`，避免提交个人数据。

---

## 🎨 前端结构说明

页面采用三栏布局（见 `static/index.html`）：

| 区域 | 内容 |
| --- | --- |
| 左侧 `.sidebar` | 「新建游戏」按钮 + 游戏记录列表 `#sessionList` |
| 中间 `.chat-container` | 标题栏 + 消息区 `#chatMessages` + 输入框 `#chatInput` / 发送键 `#sendBtn` + 主题切换 |
| 右侧 `.info-sidebar` | 游戏简介：核心玩法、特色功能、适合人群 |

`static/app.js` 的核心模块：

| 模块 | 主要函数 |
| --- | --- |
| 全局状态 | `state = { currentSession, messages, isLoading }` |
| 初始化 | `init()` → `bindEventListeners()` → `loadSessionList()` → `createNewSession()` |
| 会话管理 | `loadSessionList` / `renderSessionList` / `loadSession` / `createNewSession` / `deleteSession` |
| 消息渲染 | `renderMessages` / `appendMessageToUI` / `showLoading` / `hideLoading` / `scrollToBottom` |
| 聊天发送 | `sendMessage()` |
| 主题切换 | `bindThemeSwitcher` / `applyTheme` / `loadSavedTheme` |
| 工具函数 | `escapeHtml`（防 XSS）/ `showError` |

**用户体验细节：**
- 输入框 `Enter` 发送，`Shift + Enter` 换行
- 发送后立刻显示用户气泡 + 三点点加载动画，不等服务端返回
- 请求失败时回滚最后一条消息（`state.messages.pop()`）并重新渲染
- `isLoading` 标志防止重复提交
- 当前会话为空消息时点「新建游戏」会提示"当前游戏尚未开始，无需创建新游戏"

---

## ❓ 常见问题 FAQ

**Q1：启动时报 `RuntimeError: Directory 'static' does not exist`**

工作目录不对。代码用的是相对路径，必须先 `cd` 到 `Web应用/` 目录再启动；或者在 PyCharm 的运行配置里把 *Working directory* 设为 `.../pystudy/Web应用`。

**Q2：聊天时返回 `code: 500` 或日志中出现鉴权错误**

`DASHSCOPE_API_KEY` 未设置或无效。用 `echo %DASHSCOPE_API_KEY%`（CMD）或 `echo $env:DASHSCOPE_API_KEY`（PowerShell）确认能否读到值。设置环境变量后记得重启终端和 IDE。

**Q3：页面样式全丢、控制台报 404**

检查 `index.html` 中引用的 `/static/style.css`、`/static/app.js` 是否与 `app.mount("/static", ...)` 的路径前缀一致。若你把挂载路径改成了别的（如 `/data`），前端引用也要同步修改。

**Q4：修改了 `SYSTEM_PROMPT` 后没有生效**

如果只改了文件没重启，用 `python main.py` 启动的需手动重启；用 `uvicorn --reload` 或 `fastapi dev` 的会自动重载。另外系统提示词不落盘，修改不会影响已有的历史会话。

**Q5：会话列表为空但 `sessions/` 目录里有文件**

接口只识别文件名能去掉 `.json` 后缀的条目。若目录里混入了非 JSON 文件（如 `.DS_Store`），会被一起列进会话列表。可在 `get_sessions()` 中加 `endswith(".json")` 过滤。

**Q6：同一秒内创建多个会话会冲突吗？**

会。会话 ID 精确到秒，同一秒内重复创建会覆盖同一个 JSON 文件。学习项目影响不大；若要更严谨，可在 ID 后追加随机数或 `uuid4().hex[:6]`。

**Q7：如何更换 AI 模型？**

修改 `main.py` 中 `client.chat.completions.create(model="deepseek-v4-flash-0731", ...)` 的 `model` 参数即可。可用模型列表见[阿里云百炼文档](https://help.aliyun.com/zh/model-studio/getting-started/models)。

**Q8：能让回复流式输出（打字机效果）吗？**

可以。把 `stream` 改为 `True` 并改用 SSE（`StreamingResponse`）向前端推送；`AI应用/ai_partner_2.py` 中有 Streamlit 版的流式实现可供参考。

**Q9：为什么前端没有做路由/框架？**

本项目定位是 FastAPI 后端学习，前端刻意保持零依赖，便于聚焦接口交互本身。

---

## 🔧 后续优化方向

- [ ] 新增 `requirements.txt` 固化依赖版本
- [ ] 会话 ID 改用 `uuid` 避免同秒冲突
- [ ] `get_sessions()` 增加 `.json` 后缀过滤
- [ ] 相对路径改为基于 `__file__` 的绝对路径，彻底摆脱工作目录依赖
- [ ] 为 `POST /api/chat` 增加 AI 调用超时与重试
- [ ] 回复改为流式（SSE）实现打字机效果
- [ ] 会话存储由 JSON 文件切换到 SQLite / Redis
- [ ] 增加简单的用户体系与接口鉴权
- [ ] 补充 `pytest` 接口测试

---

## 📚 相关学习材料

- 同目录下的 [`FastAPI入门.py`](FastAPI入门.py) —— 只有 27 行的最小可运行示例，建议先跑它
- 上级目录 [`AI应用/`](../AI应用/) —— Streamlit 版 AI 对话应用的 4 个演进版本

---

<div align="center">

Made with ❤️ while learning Python

</div>
