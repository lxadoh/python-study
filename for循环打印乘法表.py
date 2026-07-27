# 打印 9×9 乘法表
for i in range(1, 10):
    for j in range(1, 1+i):
        print(f"{j} × {i} = {j * i}", end="\t")
    print()