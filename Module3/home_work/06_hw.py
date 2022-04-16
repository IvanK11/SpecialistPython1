# Данные о товарах на складе хранятся в словаре
items = [
    {
        "name": "Кроссовки",
        "brand": "adidas",
        "price": 3440
    },
    {
        "name": "Кепка",
        "brand": "reebok",
        "price": 3500
    },
    {
        "name": "Рюкзак",
        "brand": "reebok",
        "price": 4800
    },
    {
        "name": "Шорты",
        "brand": "puma",
        "price": 2500
    },
    {
        "name": "Шорты",
        "brand": "adidas",
        "price": 2750
    },
    {
        "name": "Футболка",
        "brand": "puma",
        "price": 1700
    },
]
# TODO: your code here
brands = []
brandlist = []
for el in items:
    brands.append(el["brand"])
for br in brands:
    brandlist = list(set(brands))
print("Товары на складе представлены брэндами: ", ", ".join(brandlist))

# TODO: your code here

brands = []
pairs = []
max = 0
the_list = []
for el in items:
    brands.append(el["brand"])
for br in set(brands):
    pairs.append((br, brands.count(br)))
for p in pairs:
    if p[1]>max:
        max = p[1]
for pair in pairs:
    if pair[1] == max:
        the_list.append(pair[0])

print("На складе больше всего товаров брэнда(ов): ", ", ".join(the_list))

# TODO: your code here

max = 0
max_el = []
brands = []
for el in items:
    if el["price"] > max:
        max = el["price"]
for el in items:
    if el["price"] == max:
        max_el.append(el)
for el in max_el:
    brands.append(el["brand"])
print (brands)

print("На складе самый дорогой товар брэнда(ов): ", ", ".join(brands))

#апдейт, предыдущую версию этого задания можно не смотреть
