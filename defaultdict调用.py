# collections模块的defaultdict类
from collections import defaultdict

# defaultdict 属于 collections 模块，是普通 dict（字典）的子类，专门解决一个痛点：
# 普通字典访问不存在的 key 会直接报错 KeyError，而 defaultdict 不会。
# defaultdict 会在访问不存在的 key 时，自动创建一个默认值，而不是报错。
d = defaultdict(list)   # 初始化一个 defaultdict 对象，list 是默认值的类型
# "a"不存在 → 自动创建 mp["a"] = [] → 然后执行 [].append("s")
d["a"].append("hello")
d["c"].append("python")
d["b"].append("world")
# "a"存在 → 直接执行 [].append("sdfg")
d["a"].append("sdfg")
print(list(d.values()))
print(d.values())


# 普通字典
x = {"a": 1, "b": 2, "c": 3}
print(list(x.keys()))
print(x.values())
