"""
Carlos Paredes Márquez.
Signos del Zodiaco.
29/09/2020.
"""
dia = int(input("Día de nacimiento en n enteros:    "))
mes = int(input("Mes de nacimiento en n enteros:    "))

if (31>= dia >=21 and mes == 3 ) or (1<= dia <=20 and mes ==4):
    signo = "aries" #1

elif (30>= dia >=21 and mes == 4 ) or (1<= dia <=20 and mes ==5):
    signo = "tauro" #2

elif (31>= dia >=21 and mes == 5 ) or (1<= dia <=21 and mes ==6):
    signo = "geminis" #3

elif (30>= dia >=22 and mes == 6 ) or (1<= dia <=22 and mes ==7):
    signo = "cancer" #4

elif (31>= dia >=23 and mes == 7 ) or (1<= dia <=22 and mes ==8):
    signo = "leo" #5

elif (31>= dia >=23 and mes == 8 ) or (1<= dia <=22 and mes ==9):
    signo = "virgo" #6

elif (30>= dia >=23 and mes == 9 ) or (1<= dia <=22 and mes ==10):
    signo = "libra" #7

elif (31>= dia >=23 and mes == 10 ) or (1<= dia <=22 and mes ==11):
    signo = "escorpio" #8

elif (30>= dia >=23 and mes == 11 ) or (1<= dia <=21 and mes ==12):
    signo = "sagitario" #9

elif (31>= dia >=22 and mes == 12 ) or (1<= dia <=20 and mes ==1):
    signo = "capricornio" #10

elif (31>= dia >=21 and mes == 1 ) or (1<= dia <=18 and mes ==2):
    signo = "acuario" #11

elif (29>= dia >=19 and mes == 2 ) or (1<= dia <=20 and mes ==3):
    signo = "virgo" #12

else:
    signo = "Error.\n"

print(signo)