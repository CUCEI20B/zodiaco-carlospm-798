"""
Carlos Paredes Márquez.
Signos del Zodiaco.
29/09/2020.
"""
dia = int(input("Día de nacimiento en n enteros:    "))
mes = int(input("Mes de nacimiento en n enteros:    "))

if (31>= dia >=21 and mes == 3 ) or (1<= dia <=20 and mes ==4):
    print("Aries") #1

elif (30>= dia >=21 and mes == 4 ) or (1<= dia <=20 and mes ==5):
    print("Tauro") #2

elif (31>= dia >=21 and mes == 5 ) or (1<= dia <=21 and mes ==6):
    print("Geminis") #3

elif (30>= dia >=22 and mes == 6 ) or (1<= dia <=22 and mes ==7):
    print("Cáncer") #4

elif (31>= dia >=23 and mes == 7 ) or (1<= dia <=22 and mes ==8):
    print("Leo") #5

elif (31>= dia >=23 and mes == 8 ) or (1<= dia <=22 and mes ==9):
    print("Virgo") #6

elif (30>= dia >=23 and mes == 9 ) or (1<= dia <=22 and mes ==10):
    print("Libra") #7

elif (31>= dia >=23 and mes == 10 ) or (1<= dia <=22 and mes ==11):
    print("Escorpio") #8

elif (30>= dia >=23 and mes == 11 ) or (1<= dia <=21 and mes ==12):
    print("Sagitario") #9

elif (31>= dia >=22 and mes == 12 ) or (1<= dia <=20 and mes ==1):
    print("Capricornio") #10

elif (31>= dia >=21 and mes == 1 ) or (1<= dia <=18 and mes ==2):
    print("Acuario") #11

elif (29>= dia >=19 and mes == 2 ) or (1<= dia <=20 and mes ==3):
    print("virgo") #12