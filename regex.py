import re


import random
import re

text = "An American in Paris"

print(text.replace("a","*"))
print(text.replace("A","*"))

print(text.replace("a","*").replace("A","*"))

text = text.replace("a","*")
text = text.replace("A","*")
print(text)

text = "An Amer1ican 2in Pari2s3"

print(re.sub('[aeiou]',"*",text, flags=re.I))
print(re.sub('[a-zA-Z]',"*",text))
print(re.sub('[0-9]',"*",text))
print(re.sub(r'[^\d]',"*",text))

txt = '123456789'
print(re.sub("[123,123456789]",'*',txt))

starWars = "Star Wars2: Episode " + (" " * random.randint(1, 9)) + str(random.randint(1, 70)) + " - A New Hope"

print(starWars)
print(starWars[-14])
print(re.sub('[a-zA-Z :-]',"", starWars))
print(re.sub(r'[^\d]',"", starWars))
print(re.sub(r'[^\d]',"", starWars.split('Episode')[1]))