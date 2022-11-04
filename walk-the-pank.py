# from math import pi
import math
print(math.comb(7,3))
get_d_n = input()
d, n = (int(i) for i in get_d_n.split(' '))
area = pi*d**2
clear = area

i=0
while i < n:
    get_obstacle = input()
    obstacle = get_obstacle.split(' ')
    if obstacle[0] == "reef":
        overboard = pi*int(obstacle[-1])**2
        clear -= overboard
    else:
        try_again = pi*int(obstacle[-1])**2
        clear -= try_again
    i += 1
# print('%.3f'%(clear/area))
good = 3*(clear + try_again)
print('%.3f'%(good/7))



# from math import pi
# get_d_n = input()
# d, n = (int(i) for i in get_d_n.split(' '))
# area = pi*d**2
# clear = area

# i=0
# while i <= n:
#     get_obstacle = input()
#     obstacle = (int(i) for i in get_d_n.split(' '))
#     clear -= pi*obstacle[-1]**2
#     i += 1
# print(round(clear // area, 3))