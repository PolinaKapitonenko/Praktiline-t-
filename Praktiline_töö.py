
from math import *
from random import *

#1
number= int(input("Enter a number: "))
if number >= 0:
    if number % 2 == 0:
        print("isegi")
else:
    print("kummaline")

#2
number1 = int(input("Esimene numer: "))
number2 = int(input("teine number: "))
number3 = int(input("KOlmas number: "))
if number1 > 0 and number2 > 0 and number3 > 0:
    if number1 + number2 + number3 == 180:
        # Check if the triangle is equilateral, isosceles, or scalene
        if number1 == number2 and number2 == number3:
            print("Arvud tähistavad võrdkülgse kolmnurga nurki.")
        elif number1 == number2 or number1 == number3 or number2 == number3:
            print("Arvud tähistavad võrdhaarse kolmnurga nurki.")
        else:
            print("Numbrid näitavad kolmnurga nurki.")
    else:
        print("mitte juures")
else:
    print("viga!")

#3
kusimus = input("Kas soovite teada nädalapäeva? ")
if kusimus.lower() == "jah":
  number = input("Sisestage arv vahemikus 1 kuni 7: ")
  if number.isdigit() and 1 <= int(number) <= 7:
    days = ("Esmaspäev Teisipäev Kolmapäev Neljapäev Reede Laupäev Pühapäev")
    print(f"nädalapäev: (days(int(number)-1))")
  else:
    print("viga!")
else:
  print("Head aega")








