print("{:=^20}".format(" 함수 "))

def add(x, y):
    return x + y

print(add(10, 20))
print(add("A", "B"))


def even_odd(num):
    if num % 2 == 1:
        return "odd"
    else:
        return "even"

print(even_odd(10))

print("{:-^20}".format(" 함수의 형태 "))
print("-" * 20)

def say_my_name():
    return "영희"

print(say_my_name())

def print_my_name(name):
    print("my name is " + name)

print_my_name("영희")

def say_hi():
    print("hi")

print(say_hi())

a = [1, 2, 3, 1, 2]
print(a.sort())


print("{:-^20}".format(" 함수의 매개변수 "))
print(1, 2, 3, 4, 5)
print("-" * 20)


def sample_func(a, b, *args):
    print(a)
    print(b)
    print(args)

sample_func(1, 2, 3, 4, 5, "python")


def my_sum(*args):
    total = 0

    for num in args:
        total += num

    return total

print(my_sum(1, 2, 3))
print(my_sum(1, 2, 3, 4, 5, 6))


print("{:-^20}".format(" 함수의 반환값 "))
def sum_sub(a, b):
    return a + b, a - b

print(sum_sub(1, 2))


def sample_2():
    return 2
    print("test")


def say_my_name(name):
    if name.strip() == "":
        return
    print("name", name)


say_my_name("영희")






