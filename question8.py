# Given s = "AaBbCc", count how many uppercase and lowercase letters are there.

s = "AaBbCc"

upper = 0
lower = 0

for i in s:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower+= 1 

print(upper)
print(lower)
