lst = [21, 42, 23, 14, 5, 66]
lst.sort()
max_num = max(lst)
min_num = min(lst)
print(max_num)
print(min_num)

lst.remove(max_num)
lst.remove(min_num)
print(lst)
