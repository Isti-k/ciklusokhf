def feladat():
    cv: int = 0
    while(cv <= 21):
        if cv % 3 == 0:
            print(f"{cv}", end=" ")
        cv += 1

def feladat2():
    cv: int = 10
    while(cv >= 1):
            print(f"{cv}", end="; ")
            cv -= 1

def feladat3():
    szam: int = int(input("Adjon meg egy 5-tel osztható számot:"))
    if szam % 5 == 0:
         print(f"{szam} a szám 5-tel osztható.")
    else:
        print("Ez a szám nem osztható 5-tel, próbálja újra!")

def feladat4():
    cv: int = 0
    while(cv <= 53):
        if cv % 3 == 0:
            print(f"BUMM", end="; ")
        elif cv % 2 == 0:
            print(f"BUMM", end="; ")
        elif cv:
            print(f"{cv}", end="")
        cv += 1