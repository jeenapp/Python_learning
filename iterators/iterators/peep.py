def peep(it):
    it_list = list(it)
    first_item = it_list[0]
    remaining_items = iter(it_list[:])
    return first_item, remaining_items

it = iter(range(5))
x, it1 = peep(it)
print(x, list(it1))
