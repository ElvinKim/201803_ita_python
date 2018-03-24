print('a', 'b', 'c', sep='')
print("{:=^20}".format(" 리스트 자료형 "))

a = [1, 2, 3, 4, 5, 6, 7]
print(a[-1])
print(a + [8, 9, 0])
print([8, 9, 0] * 3)

print("{:-^20}".format(" 리스트 수정 "))
a = [1, 2, 3, 4, 5]
a[0] = 100
a[4] = 500
print(a[2:3])
print(a[2])
a[1:4] = [200, 300, 400, 600]
print(a)

print("{:-^20}".format(" 리스트 삭제 "))
a = [1, 2, 3, 4, 5]
del a[1:4]
print(a)

print("{:-^20}".format(" 리스트 관련 함수 "))
# append
a = [1, 2, 3]
a.append(4)
a.append(5)
print(a)

# sort
print("-" * 20)
a = [5, 2, 3, 1, 4]
b = "aa bb cc"
print(a.sort())
print(a.sort(reverse=True))
print(a)

# reverse
print("-" * 20)
a = [5, 2, 3, 1, 4]
a.reverse()
print(a)

# index
print("-" * 20)
a = [5, 2, 3, 1, 4]
print(a.index(5))

# insert
print("-" * 20)
a = [1, 3, 4, 5, 6]
a.insert(1, 2)
print(a)

# remove
print("-" * 20)
a = [1, 2, 3, 1, 2, 3, 4]
a.remove(3)
print(a.count(3))

# pop
print("-" * 20)
a = [1, 2, 3, 4, 5]
print(a.pop())
print(a.pop(0))

print("{:=^20}".format(" 튜플 자료형 "))
x, y = (10, 20)
print(x)
print(y)

print("{:=^20}".format(" 딕셔너리 자료형 "))
me = {"name": "김상묵", "age": 30, "favorite_foods": ["김치보쌈", "두부김치"]}
print(me["name"])
print(me["favorite_foods"])

me["id"] = 100
print(me)
me["age"] = 20
print(me)
del me["id"]
print(me)

print("{:-^20}".format(" 딕셔너리 관련함수 "))
print(me.keys())
print(me.values())
print(me.items())
print("-" * 20)

print(me["age"])
print(me.get("age"))

#print(me["phone"])
print(me.get("phone"))
print(me.get("phone", 0))


print("{:=^20}".format(" 집합 자료형 "))
a = [1, 2, 3, 4, 1, 2, 1, 2, 4, 5, 6]
a = list(set(a))
print(a[0])

print(tuple(a))
print(list((1, 2, 3)))

input_str = input("aa : ")
print(input_str)










