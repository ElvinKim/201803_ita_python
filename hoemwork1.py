# problem 1
a = 20180123
year = int(a / 10000)
month = int((a % 10000) / 100)
day = a % 100
print("{:04d}.{:02d}.{:02d}".format(year, month, day))

# problem 2
input_str = input("insert your string : ")
print(input_str[0] + "_" * (len(input_str) - 1))

# problem 3
input_str = input("insert your string : ")
word_lst = input_str.split()
print(word_lst[0], word_lst[-1])

# problem 4
score_dict = {"Korean": 80, "Math": 88, "English": 100}

# problem 5
score_str = input("insert your score : ")
score_lst = score_str.split()

score_dict = {"Korean": score_lst[0],
              "Math": score_lst[1],
              "English": score_lst[2]}
