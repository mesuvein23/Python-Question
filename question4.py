# Problem: Given s = "apple,banana-mango;pineapple", split it into a list of fruits using multiple separators (,, -, ;).
import re

s = "apple,banana-mango;pineapple"

fruits = re.split(r'[,-;]', s)
print(fruits)