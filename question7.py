# Problem: Given s = "NEPSE2026", separate letters and digits into two different strings.

s = "NEPSE2026"

aplha = ""
digits = ""

for char in s:
    if char.isalpha():
        aplha += char

    elif char.isdigit():
        digits += char

print("Alphabets:", aplha)
print("Numbers:", digits)