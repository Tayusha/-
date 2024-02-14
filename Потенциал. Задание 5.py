#5
"""
Когда мы начали исправлять ошибки, оказалось, что поиск по названию игры и персонажа неэффективен.
Необходимо составить хэш-таблицу, в которой будет выстроено соответствие название игры + имя персонажа и значения их хэша.
На основании этого необходимо составить хэш-таблицу, добавить полученный хэш нулевым столбом, результат записать в csv файл.

Строка для хэша генерируется следующим образом: Название игры + Имя персонажа
Примечание: в названии игры необходимо убрать все пробелы
Название игры: Starfield  Персонаж: Mila → StarfieldMila


Для данного задания рекомендуется взять p = 65. 

26*2 – кол-во букв в английском алфавите строчных и прописных

10 – кол-во цифр.

2 – символы “:”,”-“, которые могут встретиться в названии игры.

1 – т.к. считаем не с 0.

m = 10**9+9

На вход подается файл game.txt результаты необходимо записать в новый game_with_hash.csv файл. 
"""
def hash(s):
    '''
  Функция создаёт хэш для строки
   :param s: строка
   :return: хэш-строка
   '''
    p = 65
    m = 10**9+9
    a = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM12345:-'.67890"
    hash_name = 0
    d = {}
    for ind, symbol in enumerate(a, 1):
        d[symbol] = ind
    for i in range(len(s)):
        hash_name += d[s[i]]*p**i
    return hash_name%m
fin = open("game.txt", "r", encoding = "utf-8")
title = fin.readline()
gamers = [x.strip().split("$") for x in fin]
fin.close()

fout = open("game_with_hash.csv", "w", encoding = "utf-8")
title = title.split("$")
title = "hash, " + ",".join(title)
fout.write(title)
k = ""
for x in gamers:
    k = str(x[0]+x[1])
    k = k.replace(" ", "")
    x = [str(hash(k))] + x
    x = ",".join(x)+"\n"
    fout.write(x)
fout.close()

    
        
