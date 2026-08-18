from lxml import html

# 读取html文件
with open("resources/仙逆人物志.html", 'r', encoding='utf-8') as f:
    html_text = f.read()

    # 解析html,返回一个文档对象，可以通过xpath语法提取数据
    document = html.fromstring(html_text)

    # 解析表头 - xpath语法
    th_list = document.xpath('//table/thead/tr/th/text()')
    print(th_list)

    # 解析表格数据 - xpath语法
    # # 获取所有数据，但输出在一个列表中，每个元素是一个元组
    # td_list = document.xpath('//table/tbody/tr/td/text()')
    # print(td_list)

    # # 如果只需要第一行数据
    # first_row = document.xpath('//table/tbody/tr[1]/td/text()')
    # print(first_row)

    # 获取所有行数据
    tr_list = document.xpath('//table/tbody/tr')
    for tr in tr_list:
        td_list = tr.xpath('./td/text()')
        print(td_list)
