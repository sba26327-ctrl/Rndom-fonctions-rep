import random

print("Bine ai venit la jocul 'Ghiceste numarul'!")
numar_secret = random.randint(1,20)

while True:
    incercare = int(input("Ghiceste un numar intre 1 si 20: "))
    if incercare < numar_secret:
        print("Prea mic!")
    elif incercare > numar_secret:
        print("Prea mare!")
    else:
        print("Felicitari! Ai ghicit numarul!")
        break