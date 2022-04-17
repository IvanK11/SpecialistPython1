# Дано общее количество объектов для отображения на веб-сайте и количество объектов на каждой странице.
# Вычислите, сколько объектов будет отображаться на последней странице сайта.

def pagination(num_items, items_on_page):
    last = num_items % items_on_page
    if last == 0:
        return items_on_page
    else: return last

res = pagination(177, 16)
print (res)
