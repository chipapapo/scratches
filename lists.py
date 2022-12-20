import random

first = []
second = []
third = []
for i in range(random.randint(0,50)):
   first.append((random.randint(-1000, 1000)))
   second.append(int(str(first[i])[-1]))
   third = random.choices(second, k=2*len(second))
print(first)
print(second)
print(third)
