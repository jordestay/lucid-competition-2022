# jordestay | lucid22
n = int(input())
x, y = (int(i) for i in input().replace("(","").replace(")","").split(','))
x1, y1 = 0, 0
count = n - 2
while count > 0:
    instructions = input().split(' ')
    direction, paces = instructions[1], int(instructions[2])
    if direction == "east":
        x1 += paces
    elif direction == "west":
        x1 -= paces
    elif direction == "north":
        y1 += paces
    elif direction == "south":
        y1 -= paces
    count -= 1

l = 0
if x1 == 0 and y1 == 0:
    l = 0
elif x1 == 0:
    l = y
elif y1 == 0:
    l = x
else:
    l = int(x/x1)
print(abs(l))