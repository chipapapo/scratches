import random

grades = {'Мельник': random.randint(0,101), 'Шевченко': random.randint(0,101), 'Квач': random.randint(0,101), 'Мазайло': random.randint(0,101), 'Кулеба': random.randint(0,101)}
participants = list(grades.keys())
numbers = list(grades.values())
winners = []
for i in range(3):
   winners.append(participants[numbers.index(max(numbers))])
   participants.remove(participants[numbers.index(max(numbers))])
   numbers.remove(max(numbers))
for i,v in grades.items():
   print(i + ' має ' + str(v) + ' балів.', end=' ')
print('\nПереможці: '+ ', '.join(winners) +'!')

while True:
   ask = input("Впишіть ім'я учасника, щоб перевірити чи він є переможцем ")
   if ask in winners:
       print('Так, він є переможцем!')
   elif ask == 'стоп':
       print('Гаразд...')
       break
   else:
       print('На жаль, ні, він не переможець.')
