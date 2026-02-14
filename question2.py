# Problem: Given s = "hello world", print the first character, last character, and the middle character (if length is odd).

s = "hello world"

print(s[0])
print(s[-1])

length = len(s)
# print(s)

if length % 2 == 0:
    pass
else:
    middle_char = length // 2
    print(s[middle_char]) #standard print
    print({s[middle_char]}) #fstring 
 