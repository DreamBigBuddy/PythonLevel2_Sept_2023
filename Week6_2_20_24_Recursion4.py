def list_sum(ls):
    if len(ls) == 1:
        return ls[0]

    else:
        return ls[0] + list_sum(ls[1:])

print(list_sum([1, 2, 3, 4, 5]))
