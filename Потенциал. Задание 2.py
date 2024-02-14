#2
"""
У вас снова запросили отчет по ошибкам в играх. Теперь отчет необходимо предоставить о количестве багов в каждой игре.
Для этого отсортируйте данные из файла game.txt по столбцу  игры в алфавитном порядке с помощью быстрой сортировки.
После этого предоставьте отчет в формате:
<Игра 1> - количество багов: <count>

….

<Игра N> - количество багов: <count>

Где N - количество уникальных игр.

Не забудьте сделать комментарии к коду согласно стандартам документирования кода выбранного языка.
После выполнения необходимо сделать локальные и удаленные изменения Вашего репозитория 
"""

from random import choice
def Qsort(a):
    '''
   Функция быстрой сортировки

   :param a: неотсортированный массив данных 
   :return: отсортированный массив данных
   '''
    if len(a)<=1: return a
    x = choice(a)
    B1 = []
    BX = []
    B2 = []
    for i in range(len(a)):
        if a[i]<x:
            B1.append(a[i])
        elif a[i] == x:
            BX.append(a[i])
        else:
            B2.append(a[i])
    return Qsort(B1)+BX+Qsort(B2)
fin = open("game.txt", "r", encoding = "utf-8")
title = fin.readline()
gamers = [x.strip().split("$") for x in fin]
fin.close()
gamers = Qsort(gamers)
bag_sum = {}
bag_count = {}
for x in gamers:
    if x[0] in bag_sum:
        bag_sum[x[0]] += 1
    else:
        bag_sum[x[0]] = 1
        bag_count[x[0]] = 0

for i in range(len(gamers)):
    if int(bag_count[gamers[i][0]]) == 0:
        print(f'{gamers[i][0]} - количество багов: {bag_sum[gamers[i][0]]}')
        bag_count[gamers[i][0]]+=1  
