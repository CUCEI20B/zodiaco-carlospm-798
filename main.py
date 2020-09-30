"""
Carlos Paredes Márquez.
Signos del Zodiaco.
:v
29/09/2020.
"""
dia = int(input("Día de nacimiento en n enteros:    "))
mes = int(input("Mes de nacimiento en n enteros:    "))

if (31>= dia >=21 and mes == 3 ) or (1<= dia <=20 and mes ==4):
    print("aries") #1

if (30>= dia >=21 and mes == 4 ) or (1<= dia <=20 and mes ==5):
    print("tauro") #2

if (31>= dia >=21 and mes == 5 ) or (1<= dia <=21 and mes ==6):
    print("geminis") #3

if (30>= dia >=22 and mes == 6 ) or (1<= dia <=22 and mes ==7):
    print("cancer") #4

if (31>= dia >=23 and mes == 7 ) or (1<= dia <=22 and mes ==8):
    print("leo") #5

if (31>= dia >=23 and mes == 8 ) or (1<= dia <=22 and mes ==9):
    print("virgo") #6

if (30>= dia >=23 and mes == 9 ) or (1<= dia <=22 and mes ==10):
    print("libra") #7

if (31>= dia >=23 and mes == 10 ) or (1<= dia <=22 and mes ==11):
    print("escorpio") #8

if (30>= dia >=23 and mes == 11 ) or (1<= dia <=21 and mes ==12):
    print("sagitario") #9

if (31>= dia >=22 and mes == 12 ) or (1<= dia <=20 and mes ==1):
    print("capricornio") #10

if (31>= dia >=21 and mes == 1 ) or (1<= dia <=18 and mes ==2):
    print("acuario") #11

if (29>= dia >=19 and mes == 2 ) or (1<= dia <=20 and mes ==3):
    print("virgo") #12