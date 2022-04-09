# Дан список из n элементов, заполненный произвольными целыми числами в диапазоне от -100 до 100.
# Вывести на экран сумму всех положительных элементов кратных двум.

# TODO: your code here
import random
the_list = []
num = 10
i = 1
while i <= num:
    the_list.append (random.randint(-100, 100))
    i += 1
for el in the_list:
    if el > 2 and el % 2 == 0:
        print(el)
