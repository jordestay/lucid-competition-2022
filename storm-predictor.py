# jordestay | lucid22
count = 0
i=0
while i < 4:
    forecast = input()
    forecast = forecast.split(' ')
    if forecast[-1] == "true":
        count += 1
    i += 1

if count < 3:
    print('Go fishing!')
else:
    print('Wait for the storm to pass.')