from fastapi import FastAPI

# 创建FastAPI应用
app = FastAPI()

# 定义API接口 -> 该函数的返回值就是API接口的响应内容，接口的路径就是/，请求方法就是GET
@app.get("/")
def read_root():
    return {"Hello": "World"}


# 定义API接口
@app.get("/users")
def get_users():
    return [
        {"id": 1, "name": "张三"},
        {"id": 2, "name": "李四"},
        {"id": 3, "name": "王五"},
    ]


# 启动服务 -> 启动FastAPI应用，监听8000端口
# uvicorn 是FastAPI的默认服务器，用于启动FastAPI应用，监听指定的主机和端口
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
# fastapi dev "FastAPI入门.py"
