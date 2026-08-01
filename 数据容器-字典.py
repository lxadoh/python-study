# 字典
# # 定义字典
# dict1 = {"a": 23, "b": 42, "c": 44, "d": 234}
# # dict1 = {"a": 23, "b": 42, "c": 44, "d": 234, "a": 55}
# print(dict1)      # key不能重复，如果重复，后面的值会覆盖前面的值
# # key必须是不可变类型(str, int, float, tuple)，不可以是list, set, dict
#
# # 字典访问
# print(dict1["a"])  # 获取
# dict1["b"] = 33   # 修改
# print(dict1)
#
#
# # 字典操作
# # 添加
# dict1["e"] = 45
# print(dict1)
#
# # 修改
# dict1["a"] = 11
# print(dict1)
#
# # 查询
# print(dict1["a"])   # 根据key获得vaule
# print(dict1.get("a"))   # 根据key获得vaule
#
# print(dict1.keys())    # 获得所有key
# print(dict1.values())    # 获得所有value
# print(dict1.items())    # 获得所有键值对 key|value
#
# # 删除
# score = dict1.pop("b")
# print(score)
# print(dict1)
#
# del dict1["c"]
# print(dict1)
#
# # 遍历
# for k in dict1.keys():
#     print(k)
#
# for v in dict1.values():
#     print(v)
#
# for item in dict1.items():
#     print(f"{item[0]}: {item[1]}")
#
# for k,v in dict1.items():
#     print(f"{k}: {v}")
