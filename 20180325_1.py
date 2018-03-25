print("{:=^20}".format(" 제어문 "))
print("{:-^20}".format(" if문 "))

# if 문
print("-" * 20)
if 1 > 10:
    print("test")
    print("test")
    if 1 < 20:
        print("test")

if True:
    print("aaa")

# if - else 문
print("-" * 20)
a = 10

if a % 2 == 0:
    print("짝수")
else:
    print("홀수")


# if - elif - else 문
print("-" * 20)
a = -10

if a > 0:
    print("양수")
elif a < 0:
    print("음수")
else:
    print("zero")
print("-" * 10)
if 10 > 1:
    print("test")
elif 20 > 1:
    print("test") 
elif 30 > 1:
    print("test")

# 연산자
print("-" * 20)
print((1 > 10) and (1 < 10))

x = 6
if 1 < x < 10:
    print("test")

# in 연산자
print("-" * 20)
print("a" not in ["a", 'b', 'c'])
print("a" in "abc")

# 자료형의 True/False
print("-" * 20)
if "python":
    print("test")
if 10:
    print("test")

if None:
    print("aaaa")


print("{:-^20}".format(" while문 "))

# while 문
print("-" * 20)
i = 0
while i < 10:
    print("hello")
    i += 1 # i = i + 1

# break 문
x = 0
print("-" * 20)
while True:
    if 3 * x > 56:
        break
    x += 1
print(x)

x = 0
while x < 100:
    if x > 20:
        break
    print(x)
    x += 1


# continue 문
a = 0
while a <= 20:
    a = a + 1
    if a % 2 == 1:
        continue
    print(a)


print("{:-^20}".format(" for문 "))
print("-" * 20)
a = [1, 2, 3, 4, "python"]

for x in a:
    print(x)

for x in "ABCDEF":
    print(x)


# range 객체
for n in range(3, 10):
    print(n)


# for - continue
for x in range(20):
    if x % 2 == 1:
        continue
    print(x)


# 구구단
print("-" * 20)
for x in range(2, 10):
    for y in range(1, 10):
        print("{} * {} = {}".format(x, y, x * y))
    print("-" * 10)

# 리스트 컴프리헨션
print("-" * 20)
square_lst = []

for num in range(1, 11):
    square_lst.append(num ** 2)
print(square_lst)

square_lst_2 = [num ** 2 for num in range(1, 11)]
print(square_lst_2)


# 리스트 zip
print("-" * 20)
lst1 = [10, 'b', 'c']
lst2 = ['A', 'B', 'C', 'D', 'E']
lst3 = [3, 4, 5, 6, 7]

for x, y, z in zip(lst1, lst2, lst3):
    print(x, y, z)
    print("-" * 10)


# enumerate
print("-" * 20)
lst = ["A", "B", "C", "D", "A", "B"]

i = 0
for x in lst:
    print(i, x)
    i += 1

print("-" * 10)
for i, x in enumerate(lst):
    print(i, x)











