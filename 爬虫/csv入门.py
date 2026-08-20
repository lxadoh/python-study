# csv操作 -方式一
# 写
with open("csv_data/01.csv", 'w', encoding='utf-8-sig') as f:
    # 英文逗号分隔
    f.write("姓名,年龄,性别,爱好\n")
    f.write("张三,18,男,篮球\n")
    f.write("李四,19,女,足球\n")
    f.write("王五,20,男,跑步\n")
    f.write("赵六,21,女,篮球\n")

# 读
with open("csv_data/01.csv", 'r', encoding='utf-8') as f:
    for line in f:
        # strip():去掉换行符
        print(line.strip())


# csv操作 -方式二 csv模块
# import csv
#
# # # 写
# # # 调用open函数时,会自动添加换行符,newline='': 表示不添加换行符  默认添加换行符
# with open("csv_data/02.csv", 'w', encoding='utf-8', newline='') as f:
#     # fieldnames: 表示表头字段名
#     writer = csv.DictWriter(f, fieldnames=['姓名', '年龄', '性别', '爱好'])
#     writer.writeheader() # 写入表头
#     # writerow(): 写入一行数据  参数: 一个字典
#     writer.writerow({'姓名': '张三', '年龄': '18', '性别': '男', '爱好': '篮球'})
#     writer.writerow({'姓名': '李四', '年龄': '19', '性别': '女', '爱好': '足球'})
#     writer.writerow({'姓名': '王五', '年龄': '20', '性别': '男', '爱好': '跑步'})
#     writer.writerow({'姓名': '赵六', '年龄': '21', '性别': '女', '爱好': '篮球'})
    # writerows(): 写入多行数据  参数: 一个字典列表
    writer.writerows([{'姓名': '王二', '年龄': '22', '性别': '男', '爱好': '跑步'},
                      {'姓名': '赵二', '年龄': '23', '性别': '女', '爱好': '篮球'}])
#
# # 读
# with open("csv_data/02.csv", 'r', encoding='utf-8') as f:
#     # DictReader(): 读取csv文件,返回一个字典列表
#     reader = csv.DictReader(f)
#     for row in reader:
#         print(row)
