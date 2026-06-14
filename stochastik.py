import random

print("--- LOTTO SIMULATOR ---")

meine_zahlen = []

#Abfrage der 6 Zahlen nacheinander
zahl1 = int(input("Gib Zahl 1 ein: "))
meine_zahlen.append(zahl1)
zahl2 = int(input("Gib Zahl 2 ein: "))
meine_zahlen.append(zahl2)
zahl3 = int(input("Gib Zahl 3 ein: "))
meine_zahlen.append(zahl3)
zahl4 = int(input("Gib Zahl 4 ein: "))
meine_zahlen.append(zahl4)
zahl5 = int(input("Gib Zahl 5 ein: "))
meine_zahlen.append(zahl5)
zahl6 = int(input("Gib Zahl 6 ein: "))
meine_zahlen.append(zahl6)

print("Deine Zahlen sind:", meine_zahlen)
print("Simulation startet...")

versuche = 0

#Solange wir nicht gewonnen haben
while True:
    versuche = versuche + 1 
    
    # Der Computer zieht 6 zufällige Zahlen
    lotto_ziehung = random.sample(range(1, 50), 6)
    
    # Jetzt wird gezählt, wie viele Treffer wir haben
    richtige = 0
    for zahl in meine_zahlen:
        if zahl in lotto_ziehung:
            richtige = richtige + 1
            
    # Wenn wir 6 Richtige haben, stoppen wir
    if richtige == 6:
        print("JACKPOT nach", versuche, "Versuchen!")
        print("Die Gewinnzahlen waren:", lotto_ziehung)
        break
        
    if versuche == 100000:
        print("Schon 100.000 Mal versucht... nix getroffen.")
    if versuche == 500000:
        print("Schon eine halbe Million Versuche!")