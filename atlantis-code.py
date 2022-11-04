# jordestay | lucid22
input = input()
score = 0
aCt = 0
abCt = 0
cCt = 0

for char in input:
    if char == 'A':
        score += 1
        aCt = 1
    elif char == 'B':
        score += 2
        if aCt == 1:
            score += 2
    elif char == 'C':
        cCt += 1
        aCt = 0

print(score)