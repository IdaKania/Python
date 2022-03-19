import random

tb = []
tg = []
a = 1
lg = 0
lb = 0
los = random.randint(1, 100)
bot = 0
print("Zgadnij liczbe: ")
liczba = 0

while liczba != los and bot != los:
    if a%2==0:
        print("Kolej bota")
        bot = random.randint(1, 100)
        print(bot)
        tb = tb + [bot]
        lb=lb+1
        
        if bot > los:
            print("Liczba jest za duza")
            print("\n")

        elif bot < los:
            print("Liczb jest za mala")
            print("\n")

    elif a%2==1:
        print("Twoja kolej")
        liczba = int(input())
        tg = tg + [liczba]
        lg=lg+1

        if liczba > los:
            print("Liczba jest za duza")
            print("\n")

        elif liczba < los:
            print("Liczb jest za mala")
            print("\n")
    a=a+1
    
print("Odgadnieto liczbe! To byla liczba ", los)
print("Liczba twoich prob: ", lg)
print("Liczba prob bota: ", lb) 

print("Liczby podane przez bota: ")
for x in tb:
    print(x)

print("Liczby podane przez gracza: ")
for x in tg:
    print(x)


#number = input("Podaj liczbe: ")
#print("Z");
