from time import sleep
import random
from tabulate import tabulate


class Participant:
    players = []

    def __init__(self):
        self.snames = ['Кайдаш', 'Стрикало', 'Байда', 'Шевченко', 'Класнюк', 'Горишин', 'Саакашвілі', 'Сміт',
                       'Федоченко']
        self.sname = random.choice(self.snames)
        self.sex = random.choice(['чоловік', 'жінка'])
        self.wcat = random.randint(1, 3)
        self.points = random.randint(0, 101)
        self.doping = random.choice([True, False])

        Participant.players.append([self.sname, self.sex, self.wcat, self.points, self.doping])


class Competition:
    def __init__(self, name):
        print('Змагання по {} відкрито'.format(name))
        print('Учасники змагаються')
        for t in range(3):
            print('.', end='')
            sleep(1.5)
        print('\nЗмагання відбулося!\n')

    def tables(self):
        winners1 = []
        winners2 = []
        winners3 = []
        cheaters = []
        for i in Participant.players:
            if i[4]:
                cheaters.append(i)
            elif i[2] == 1:
                winners1.append(i)
            elif i[2] == 2:
                winners2.append(i)
            elif i[2] == 3:
                winners3.append(i)
        winners1.sort(key=lambda p: p[3], reverse=True)
        winners2.sort(key=lambda p: p[3], reverse=True)
        winners3.sort(key=lambda p: p[3], reverse=True)
        print('Переможці першої вагової категорії\n\n' + tabulate(winners1,
                                                                  headers=['Прізвище', 'Стать', 'Вагова категорія',
                                                                           'Бал', 'Допінг']))
        print('\nПереможці другої вагової категорії\n\n' + tabulate(winners2,
                                                                    headers=['Прізвище', 'Стать', 'Вагова категорія',
                                                                             'Бал', 'Допінг']))
        print('\nПереможці третьої вагової категорії\n\n' + tabulate(winners3,
                                                                     headers=['Прізвище', 'Стать', 'Вагова категорія',
                                                                              'Бал', 'Допінг']))
        print('\nШахраї\n\n' + tabulate(cheaters, headers=['Прізвище', 'Стать', 'Вагова категорія', 'Бал', 'Допінг']))


for q in range(15):
    Participant()
Swimming = Competition('плавання')
Swimming.tables()
