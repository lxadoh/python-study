import requests
from lxml import html

# 定义url
target_url = "https://www.tiobe.com/tiobe-index/"

# 发送GET请求，获得数据
response = requests.get(target_url)

# # 输出数据
# print(response.text)

# 解析html,返回一个文档对象，可以通过xpath语法提取数据
document = html.fromstring(response.text)

# 解析数据
# 解析表头
th_list = document.xpath('//table[@id="top20"]/thead/tr/th/text()')
print(th_list)

# 解析表格中数据
tr_list = document.xpath('//table[@id="top20"]/tbody/tr')
for tr in tr_list:
    td_list = tr.xpath('./td/text()')
    print(td_list)
