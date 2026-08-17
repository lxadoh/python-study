import requests

# 定义url
target_url = "https://www.tiobe.com/tiobe-index/"

# 发送GET请求，获得数据
response = requests.get(target_url)

# 输出数据
print(response.text)
