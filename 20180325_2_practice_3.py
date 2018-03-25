def my_average(*args):
    #return sum(args) / len(args)
    total = 0
    cnt = 0

    for num in args:
        total += num
        cnt += 1
    return total / cnt

print(my_average(1, 2, 3, 4, 5))


def my_concat(c, *args):
    return c.join(args)

print(my_concat("-", "ab", 'cd', 'ef'))

def my_concat_2(*args):
    temp_lst = list(args)
    c = temp_lst.pop(0)
    return c.join(temp_lst)

print(my_concat_2("-", "ab", 'cd', 'ef'))