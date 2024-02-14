#4
"""
При просмотре логов вы увидели, что в одной игре может быть несколько ошибок.
Вам необходимо добавить счетчик того, сколько ошибок выявлено в игре.
Реализуйте методы/функции, которые будут считать количество упоминаний какой-либо игры.
Полученный список игр необходимо отсортировать в порядке возрастания.
При занесении данных в csv файл, счетчик необходимо применить ко всем строкам.

“Starfield, Mila, MВКJ:537, 1233-11-19” → “ Starfield, Mila, MВКJ:537, 1233-11-19, 9”

На вход подается файл game.txt, который необходимо записать в список, добавить счетчик для каждого элемента,
после чего дополнить список счетчиками. Последним этапом полученный список записать в новый game_counter.csv  файл.
Назвать новый столбец “counter" 
"""

fin = open("game.txt", "r", encoding = "utf-8")
title = fin.readline()
gamers = [x.strip().split("$") for x in fin]
fin.close()
bag_sum = {}
for x in gamers:
    if x[0] in bag_sum:
        bag_sum[x[0]] += 1
    else:
        bag_sum[x[0]] = 1
sm = 0
fout = open("game_counter.csv", "w", encoding = "utf-8")
title = title.split("$")
title = ",".join(title)
fout.write(title.strip() + ", counter" + "\n")
for x in gamers:
    sm = x[0]
    x = ", ".join(x)
    x = x + f', {bag_sum[sm]}' + "\n"
    fout.write(x)
fout.close()
