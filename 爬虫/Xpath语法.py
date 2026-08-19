from lxml import html

# 读取html文件
with open("resources/仙逆人物志.html", 'r', encoding='utf-8') as f:
    html_text = f.read()

    # 解析html,返回一个文档对象，可以通过xpath语法提取数据
    document = html.fromstring(html_text)

    # 解析表头 - xpath语法
    # // 表示从文档根节点开始查找
    # / 表示从当前节点开始查找
    # th_list = document.xpath('/table/thead/tr/th/text()')
    # 输出结果 [] 找不到元素
    # th_list = document.xpath('/html/body/div/div/table/thead/tr/th/text()')
    th_list = document.xpath('//table/thead/tr/th/text()')
    print(th_list)

    # tr[1] 表示匹配第一个tr标签
    td_list = document.xpath('//table/tbody/tr[1]/td/text()')
    print(td_list)

    # last() 表示匹配最后一个tr标签
    last_tr = document.xpath('//table/tbody/tr[last()]/td/text()')
    print(last_tr)

    # last()-1 表示匹配倒数第二个tr标签
    last_second_tr = document.xpath('//table/tbody/tr[last()-1]/td/text()')
    print(last_second_tr)

    # p[@class] 表示匹配所有有class属性的p标签
    p_list = document.xpath('//p[@class]/text()')
    print(p_list)

    # p[@class="content"] 表示匹配所有有class属性为content的p标签
    p_list = document.xpath('//p[@class="content"]/text()')
    print(p_list)

    # * 表示匹配任意标签
    th_list = document.xpath('//table/thead/tr/*/text()')
    print(th_list)

    # @src 表示匹配sr属性
    a_list = document.xpath('//td/img/@src')
    print(a_list)
    # @* 表示匹配所有属性
    a_list = document.xpath('//td/img/@*')
    print(a_list)
