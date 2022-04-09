# Дан список имен.
# Найдите самое длинное имя, если таких имен несколько - выведи любое их них

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]

# TODO: your code here
the_longest = names [0]
for name in names:
    if len (name) > len (the_longest):
        the_longest = name
print(the_longest)
