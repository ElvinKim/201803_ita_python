#1
a = 20180108
a = str(a)

year = a[0:4]
month = a[4:6]
day = a[6:]

print(year + "년 " + month + "월 " + day +"일")

#2
b = "hi SangMook"
print("hello" + b[2:])

#3
print(b.replace("hi", "hello"))

#4
input_str = input("Insert your string : ")
print(input_str[0].upper() + input_str[1:-1].lower() + input_str[-1].upper())

