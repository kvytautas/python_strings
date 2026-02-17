print ("*********** Užduotis1 ************")

name="Johnny"
last_name="Depp"

if len(name)>len(last_name):
    print(name)
elif len(name)<len(last_name):
    print(last_name)
else: print(name, last_name)

print ("*********** Užduotis2 ************")

print(name.upper(), last_name.lower())

print ("*********** Užduotis3 ************")

var3=name[0] + last_name[0]

print(var3.upper())

print ("*********** Užduotis4 ************")

var4=name[-3:] + last_name[-3:]

print(var4.upper())

