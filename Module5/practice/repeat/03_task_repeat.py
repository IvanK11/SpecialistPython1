# Найдите количество чисел являющихся палиндромами в диапазоне от a до b включительно
# Известно, что a и b целые положительные числа.

def pal_count(a,b):
    numbers = []
    i = 0
    for num in range (a,b+1):
        if str(num) == str(num)[::-1]:
            i += 1
    return i

print (pal_count(10,99))
