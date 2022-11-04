# jordestay | lucid22
tanks = input().split(' ')
print(tanks[0])
print(tanks[len(tanks) - 1])

ascent = 0
units = int(tanks[0])
while ascent < (len(tanks) - 1):
    if units == 0:
        break
    if units < int(tanks[ascent]):
        units = int(tanks[ascent])

    ascent -= 1
print("bool(units)")