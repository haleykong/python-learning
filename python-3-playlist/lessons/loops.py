# FOR LOOPS
ninjas = ['ryu', 'crystal', 'yoshi', 'ken']

for ninja in ninjas:
    print(ninja)

# Cycle through portion of list
for ninja in ninjas[1:3]:
    print(ninja)

for ninja in ninjas:
    if ninja == 'yoshi':
        print(f'{ninja} - black belt')
        break
    else:
        print(ninja)

# WHILE LOOPS
age = 25
num = 0

while num < age:
    if num == 0:
        num += 1
        continue  # Continue with next iteration
    if num % 2 == 0:
        print(num)
    if num > 10:
        break
    num += 1
