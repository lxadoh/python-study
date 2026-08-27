from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os
from datetime import datetime
import json
from pydantic import BaseModel
from typing import Any

# 创建FastAPI实例
app = FastAPI(title="汉字谜盒")

# 配置静态文件目录
app.mount("/static", StaticFiles(directory="static"), name="static")

# 创建会话存放的目录 sessions
if not os.path.exists("sessions"):
    os.mkdir("sessions")

# 生成会话标识
def generate_session_id():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# 数据模型
class ApiResponse(BaseModel):
    code: int
    message: str
    data: Any

class ChatRequest(BaseModel):
    session_id: str
    message: str

# 定义路径操作函数
@app.get("/")
def root():
    print("访问项目首页")
    return FileResponse("static/index.html")


# 创建会话
@app.post("/api/sessions")
def create_session():
    print(f"创建会话")
    # 1.生成会话标识
    session_id = generate_session_id()
    # 2.组装会话信息，保存到文件中
    session_data = {
        "current_session": session_id,
        "messages": []
    }
    with open(os.path.join("sessions", f"{session_id}.json"), "w", encoding="utf-8") as f:
        json.dump(session_data, f, ensure_ascii=False, indent=2)

    # 3.返回数据
    return ApiResponse(code=200, message="创建会话成功", data=session_id)


# 与AI交互
@app.post("/api/chat")
def chat(request: ChatRequest) -> ApiResponse:
    print(f"与AI交互: {request.session_id} : {request.message}")
    return ApiResponse(code=200, message="请求成功", data="你好，我是汉字谜盒AI，欢迎来到我的世界。")


# 启动项目
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
