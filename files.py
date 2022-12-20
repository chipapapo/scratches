import os

os.mkdir("C:\lab7\Bychkar", 0o777)

with open('2.txt') as f:
   text = f.read()
   part1, part2 = text[:len(text)//2], text[len(text)//2:]
with open('2part1.txt', 'x') as f:
   f.write(part1)
with open('2part2.txt', 'x') as f:
   f.write(part2)
