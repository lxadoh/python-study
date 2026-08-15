import json

# 写入json文件
user = {
    "name": "张三",
    "age": 18,
    "gender": "男",
    "hobby": ["篮球", "足球"]
}
with open("resources/user.json", "w", encoding="utf-8") as f:
    # json.dump(user, f)：将字典user写入文件f
    # ensure_ascii=False：不使用转义字符，直接写入中文（默认是True，会使用转义字符表示中文）
    # indent=2：会在json文件中每个键值对的值前缩进2个空格
    json.dump(user, f, ensure_ascii=False, indent=2)

# 读取json文件
with open("resources/user.json", "r", encoding="utf-8") as f:
    # json.load(f)：从文件中读取json数据，返回一个字典
    user = json.load(f)
    print(user)
