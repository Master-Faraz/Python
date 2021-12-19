a_string = "0abc 155 def 23"


numbers = []
total = 0

for word in a_string.split():

    if word.isdigit():
        numbers.append(int(word))


for i in range(0, len(numbers)):
    total += numbers[i]

print(a_string)
print(numbers)
print(total)

# s = input()
# s1 = ''
# for i in s:
#     if type(i) != int:
#         s1+=i

# print(s1)