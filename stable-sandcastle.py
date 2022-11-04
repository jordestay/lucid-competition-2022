# jordestay | lucid22
n = int(input())
wall = input().split(' ')
stable = True
diff = 0
count = 1
while count < (len(wall) - 4):
    i = 3
    while i > 0:
        diff += int(wall[count]) - int(wall[i])
        if abs(diff) > 4:
            stable = False
            break
        i -= 1


print(bool(stable))