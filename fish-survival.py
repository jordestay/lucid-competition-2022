get_params = input()
pop, num_events = (int(i) for i in get_params.split(' '))

i = 0
while i < num_events:
    get_input = input()
    t, x = get_input.split(' ')
    if t == "G":
        pop += int(x)
    elif t == "P":
        pop -= pop % int(x)
    i += 1

print(pop)