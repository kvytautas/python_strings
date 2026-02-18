import re


text = "An American in Paris"

print(re.sub( '[aeiou]',  "*", text, flags=re.I))
print(re.sub( '[a-z,A-Z]', "*", text))
print(re.sub( '[0-9]',  "*", text))
print(re.sub( '[^\d]', "*", text))