from datetime import date
import datetime
import random
num = [1]

x = 10
y = 20
print(x + y)

for i in num:
    print(" ")

fav = "Ryan Reynolds"
print(fav)

for i in num:
    print(" ")

s = "lucky"
print(s)

for i in num:
    print(" ")

datum = datetime.datetime.now()
datum = datum.strftime("%w/%m/%Y")
print("Today is " + datum)

for i in num:
    print(" ")
    
r = "Hallo Mensen"
r = r.replace("Hallo Mensen","Hoi Enero",2)
print(r)

for i in num:
    print(" ")

f = r.find("enero")
print(f) 
t = r.find("o")
print(t)
z = r.find(input("Geef een letter of woord op "))
print(z)

for i in num:
    print(" ")

woorden = ["Welkom", "bij" , "ons"]
zin = " ".join(woorden)
print(zin)
zin1 = "_".join(woorden)
print(zin1)

for i in num:
    print(" ")

b = "Hallo Wereld"
woorden = b.split()
print(woorden)
b =  "World,Earth,America,Canada"
woorden = b.split()
print(woorden)
zin = "Hallo allemaal. Ik ben Enero"
woorden = zin.split(".")
print(woorden)

for i in num:
    print(" ")

x = random.randrange(0,100)
print(x)
numb = [1,2,3]
for i in numb:
    print(random.randrange(0,100))
from collections import Counter
numb = []
for i in range(100):
    numb.append(random.randrange(0,100))
counter = Counter(numb)
print(counter)

for i in num:
    print(" ")

x = input("what is your phone number? ")
print("Your number is " + x)
x = input("what is your preffered programming language? ")
print("Your preffered programming language is: " + x)

for i in num:
    print(" ")

clist = ['Canada','USA','Mexico','Australia']
for i in clist:
    print(i)