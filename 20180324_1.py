print("{:=^20}".format(" 문자형 자료형 "))
print("{:-^20}".format(" 따옴표 넣기 "))
print('I\'m SangMook')
print("-" * 20)
print("Life is too short\nYou need Python")

print("{:-^20}".format(" 문자열 연산자 "))
print("ABC" + "DEF")
print("A" * 20)

print("{:-^20}".format(" 문자열 인덱싱 "))
a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(a[2])
print(a[-2])

print("{:-^20}".format(" 문자열 슬라이싱 "))
print(a[20:-1])
print(a[20:])

print("{:-^20}".format(" 문자열 포매팅(1) "))
name_format = "제 이름은 %s 입니다."
age_format = "제 나이는 %d 입니다."
name_age_format = "제 이름은 %s 이고 제 나이는 %d 입니다."
name_age_format_v2 = "제 이름은 %s 이고 제 나이는 %s 입니다."
print(name_format % "김상묵")
print(age_format % 20)
print(name_age_format % ("김상묵", 20))
print(name_age_format_v2 % ("김상묵", str(20)))
# str(20) == "20"

print("{:-^20}".format(" 문자열 관련 함수 "))
# count
a = "ABCABCABC"
print(a.count("A"))
print(a.count("AB"))
print("ABCABCABC".count("AB"))

# index
print("ABCABCABC".index("C"))
# find
print("ABCABCABC".find("C"))

# join
a = "ABC"
print("-".join(a))

# upper & lower
print("ADSDEadfaefADFASF".upper())
print("ADSDEadfaefADFASF".lower())

# strip
print("       ABC        ".lstrip())
print("       ABC        ".rstrip())
print("       ABC        ".strip())

# replace
print("ABC ABC AA CC DD".replace("ABC", "QQQ"))

# split
print("ABC ABC AA CC DD".split())
print("ABC ABC,AA CC DD".split(","))

print("{:-^20}".format(" 문자열 포매팅(2) "))

name_format = "나의 이름은 {}입니다."
name_age_format = "나의 이름은 {1}이고 나이는 {0}입니다."
name_age_format_v2 = "나의 이름은 {name}이고 나이는 {age}입니다."
print(name_format.format("김상묵"))
print(name_age_format.format(20, "김상묵"))
print(name_age_format_v2.format(name="김상묵", age=20))

print("{:*<20}".format(" 문자열 포매팅(2) "))
print("{:*>20}".format(" 문자열 포매팅(2) "))

print("-" * 20)
a = int(input("Input your a: "))
b = int(input("Input your b: "))
print(a + b)












