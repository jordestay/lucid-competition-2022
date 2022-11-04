# jordestay | lucid22
fish = ['halibut', 'mackerel', 'salmon', 'snapper', 'squid', 'tuna']
count = [0,0,0,0,0,0,0]

scrambled = input()
for char in scrambled:
    if char == 'h':
        count[0] += 1
    elif char == 'k':
        count[1] += 1
    elif char == 'o':
        count[2] += 1
    elif char == 'p':
        count[3] += .5
    elif char == 'q':
        count[4] += 1
    elif char == 't':
        count[5] += 1

i = 0
while i < len(fish):
    print("%s:%s"%(fish[i], int(count[i])))
    i += 1