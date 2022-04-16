# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    ch = str(ticket_number)
    i = 0
    half = int(len(ch) / 2)
    end = len(ch)
    summa = 0
    summa2 = 0
    if end != 6: return False
    while i < half:
        summa += int(ch[i])
        i += 1
    while half < end:
        summa2 += int(ch[half])
        half += 1
    return summa == summa2

# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
