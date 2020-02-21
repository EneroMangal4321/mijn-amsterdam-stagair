from datetime import date
import datetime
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
