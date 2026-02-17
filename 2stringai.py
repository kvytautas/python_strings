# print ("*********** Užduotis1 ************")
#Sukurti du kintamuosius. Jiems priskirti savo mylimo aktoriaus vardą ir pavardę kaip stringus (Jonas Jonaitis). Atspausdinti trumpesnį stringą.

# name = "Johnny"
# last_name = "Depp"
#
# if len(name)>len(last_name):
#     print(name)
# elif len(name)<len(last_name):
#     print(last_name)
# else: print(name, last_name)
#
# print ("*********** Užduotis2 ************")
#Sukurti du kintamuosius. Jiems priskirti savo mylimo aktoriaus vardą ir pavardę kaip stringus. Vardą atspausdinti tik didžiosiom raidėm, o pavardę tik mažosioms. (LEONARDO dicaprio)

# print(name.upper(), last_name.lower())
#
# print ("*********** Užduotis3 ************")
#Sukurti du kintamuosius. Jiems priskirti savo mylimo aktoriaus vardą ir pavardę kaip stringus. Sukurti trečią kintamąjį ir jam priskirti stringą, sudarytą iš pirmų vardo ir pavardės kintamųjų reikšmių raidžių. Jį atspausdinti.

# var3 = name[0] + last_name[0]
#
# print(var3.upper())
#
# print ("*********** Užduotis4 ************")
#Sukurti du kintamuosius. Jiems priskirti savo mylimo aktoriaus vardą ir pavardę kaip stringus. Sukurti trečią kintamąjį ir jam priskirti stringą, sudarytą iš trijų paskutinių vardo ir pavardės kintamųjų raidžių. Jį atspausdinti.

# var4 = name[-3:] + last_name[-3:]
#
# print(var4.upper())

# print ("*********** Užduotis5 ************")
# # Sukurti kintamąjį su stringu: "An American in Paris". Jame vis`as “a” (didžiąsias ir mažąsias) pakeisti žvaigždutėm “*”.  Rezultatą atspausdinti.
#
#
# var5 = "An American in Paris"
# #var5 = var5.replace("a", "*").replace("A", "*")
# print(var5.replace("a", "*").replace("A", "*"))

# print ("*********** Užduotis6 ************")
# Sukurti kintamąjį su stringu: "An American in Paris". Jame ištrinti visas balses. Rezultatą atspausdinti. Kodą pakartoti su stringais: "Breakfast at Tiffany's", "2001: A Space Odyssey" ir "It's a Wonderful Life".


# var6 = "Breakfast at Tiffany's"
# var66 = "2001: A Space Odyssey"
# var666 = "It's a Wonderful Life"
#
# vowels = "aeyuioAEYUIO"
# result5 = "".join(ch for ch in var5 if ch not in vowels)
# print(result5)
# print("".join(ch for ch in var6 if ch not in vowels))
# print("".join(ch for ch in var66 if ch not in vowels))
# print("".join(ch for ch in var666 if ch not in vowels))

# print ("*********** Užduotis7 ************")
#
# import random
#
# starWars = "Star Wars: Episode " + (" " * random.randint(1, 9)) + str(random.randint(1, 7)) + " - A New Hope"
# print(starWars)
#
# var7 = "".join(ch for ch in starWars if ch.isdigit())
# print(var7)
#
# print("*********** Užduotis8 ************")
#
# var8 = starWars # "starWars"
# if var8[0] == var8[-1]:
#     print("Sutampa")
# else:
#     print("Nesutampa")
#
# print("*********** Užduotis9 ************")
# # Sukurk kintamąjį su bet kokiu žodžiu.
# #  Atspausdink tą patį žodį, bet visos raidės išskyrus pirmą ir paskutinę turi būti pakeistos į _.
# #  Pvz. Python → P____n.
#
# # vowels = "aeyuioAEYUIO"
# input9 = vowels
# var9 = input9[0] + "_" * (len(input9) - 2) + input9[-1]
# print(var9)

print("*********** Užduotis10 ************")

text = "Man 24 metai"
print(text)

print("Yra skaičių" if any(ch in "0123456789" for ch in text) else "Tik raidės")

print("*********** Papildoma. Užduotis11 ************")

var11 = "Don't Be a Menace to South Central While Drinking Your Juice in the Hood"
print(var11)
count11 = sum(len(word) <= 5 for word in var11.split())
print(count11)

var11e = "Tik nereikia gąsdinti Pietų Centro, geriant sultis pas save kvartale"
print(var11e)
count11e = sum(len(word) <= 5 for word in var11e.split())
print(count11e)

print("*********** Papildoma. Užduotis12 ************")
# Parašyti kodą, kuris generuotų atsitiktinį stringą iš lotyniškų mažųjų raidžių. Stringo ilgis 3 simboliai.

import random
import string

rnd_str = ''.join(
    random.choice(string.ascii_lowercase)
    for _ in range(3)
)
print("random string of three",rnd_str)

print("*********** Papildoma. Užduotis12 ************")
#Parašykite kodą, kuris generuotų atsitiktinį stringą su 10 atsitiktine tvarka išdėliotų žodžių, o žodžius generavimui imtų iš 11-me uždavinyje pateiktų dviejų stringų. Žodžiai neturi kartotis. (reikės masyvo)

words1 = var11.split()
words2 = var11e.split()

all_words = words1 + words2
print("all_words",all_words)
random.shuffle(all_words)
# print("var12",var12)
random_words = all_words[:10]

print("random_words",random_words)

