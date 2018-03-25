def average(a, b):
    return (a + b) / 2

print(average(10, 20))


def average_lst(lst):
    total = 0
    cnt = 0

    for num in lst:
        total += num
        cnt += 1

    return total / cnt

a = [1, 2, 3, 4, 5]
print(average_lst(a))
print(average_lst((1, 2, 3)))


def average_lst_v2(lst):
    return sum(lst) / len(lst)


