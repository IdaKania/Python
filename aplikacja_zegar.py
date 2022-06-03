import os, time, msvcrt, datetime

clearScreen = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    
czas = 0
pause = False
wyjscie = False
wybor = ''
s = 0
data = datetime.date.today()
raz = 1


def minutnik(s):
        for a in range(s):
            clearScreen()
            print(s, " sekund")
            s=s-1
            time.sleep(1)

while not wyjscie:
    wybor = input("Wybierz: \n •stoper \n •minutnik \n •data \n")

    if wybor=='stoper':
        print('(aby skonczyc kliknij dowolny klawisz)')
        time.sleep(1)
        clearScreen()
        while not pause:
            czas = czas + 1
            clearScreen()
            print(czas)
            time.sleep(1)
            if msvcrt.kbhit():
                print("Wylaczyles program przez wcisniecie", msvcrt.getch())
                pause = True
    
    elif wybor=='minutnik':
        s = input('Ile sekund: ')
        minutnik(int(s))
        clearScreen()
        print("KONIEC CZASU!")
        time.sleep(1)

    elif wybor=='data':
        while not pause:
            if raz==1:
                print('(aby skonczyc kliknij dowolny klawisz)')
                print(data)
                raz=raz-1
            if msvcrt.kbhit():
                print("Wylaczyles program przez wcisniecie", msvcrt.getch())
                pause = True

    else:
        print('Zle wybrano opcje')

    pause = False
    wyjscie = input(" Jesli chcesz wrocic do menu - menu \n Jesli chcesz wyjsc - wyjscie \n")

    if wyjscie=='menu':
        wyjscie = False

    elif wyjscie=='wyjscie':
        wyjscie = True

exit()

