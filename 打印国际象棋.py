#打印国际象棋棋盘 ■ □
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            print("■", end="  ")
        else:
            print("□", end="  ")
    print()