import random
print("Qatar World Cup 2022")
GA = ["Qatar", "Ecuador", "Senegal", "Netherlands"]
GB = ["England", "Iran", "USA", "Wales"]
GC = ["Argentina", "Saudi Arabia", "Mexico", "Poland"]
GD = ["France", "Australia", "Denmark", "Tunisia"]
GE = ["Spain", "Costa Rica", "Germany", "Japan"]
GF = ["Belgium", "Canada", "Morocco", "Croatia"]
GG = ["Brazil", "Serbia", "Switzerland", "Cameroon"]
GH = ["Ghana", "South Korea", "Portugal", "Uruguay"]

print("************Group A************")
for i in GA:
    print(i)
    
print("\n************Group B************")
for i in GB:
    print(i)
    
print("\n************Group C************")
for i in GC:
    print(i)

print("\n************Group D************")
for i in GD:
    print(i)
    
print("\n************Group E************")
for i in GE:
    print(i)
    
print("\n************Group F************")
for i in GF:
    print(i)
    
print("\n************Group G************")
for i in GG:
    print(i)
    
print("\n************Group H************")
for i in GH:
    print(i)

print("\nChaimpionship of Group Match")
GAC = random.sample(GA, 2)
print("\nChampion from Group A : ")
for i in GAC:
    print(i)
    
GBC = random.sample(GB, 2)
print("\nChampion from Group B : ")
for i in GBC:
    print(i)

GCC = random.sample(GC, 2)
print("\nChampion from Group C : ")
for i in GCC:
    print(i)

GDC = random.sample(GD, 2)
print("\nChampion from Group D : ")
for i in GDC:
    print(i)
    
GEC = random.sample(GE, 2)
print("\nChampion from Group E : ")
for i in GEC:
    print(i)
    
GFC = random.sample(GF, 2)
print("\nChampion from Group F : ")
for i in GFC:
    print(i)
    
GGC = random.sample(GG, 2)
print("\nChampion from Group G : ")
for i in GGC:
    print(i)
    
GHC = random.sample(GH, 2)
print("\nChampion from Group H : ")
for i in GHC:
    print(i)
    
print("\n************* Round of 16 *************\n")
G16A = random.choice(GAC)
print("Round 16 A : ", G16A)

G16B = random.choice(GBC)
print("Round 16 B : ", G16B)

G16C = random.choice(GCC)
print("Round 16 C : ", G16C)

G16D = random.choice(GDC)
print("Round 16 D : ", G16D)

G16E = random.choice(GEC)
print("Round 16 E : ", G16E)

G16F = random.choice(GFC)
print("Round 16 F : ", G16F)

G16G = random.choice(GGC)
print("Round 16 G : ", G16G)

G16H = random.choice(GHC)
print("Round 16 H : ", G16H)

print("\n************* Quarter Final *************\n")
Q1 = G16A, G16B
QFA = random.choice(Q1)
print(f"Quarter Final between {G16A} & {G16B} \nWinner : {QFA}")

Q2 = G16C, G16D
QFB = random.choice(Q2)
print(f"\nQuarter Final between {G16C} & {G16D} \nWinner : {QFB}")

Q3 = G16E, G16F
QFC= random.choice(Q3)
print(f"\nQuarter Final between {G16E} & {G16F} \nWinner : {QFC}")

Q4 = G16G, G16H
QFD = random.choice(Q4)
print(f"\nQuarter Final between {G16G} & {G16H} \nWinner : {QFD}")

print("\n************* Semi Final *************\n")
S1 = QFA, QFB
SFA = random.choice(S1)
print(f"Semi Final between {QFA} & {QFB}\nWinner : {SFA}")

S2 = QFC, QFD
SFB = random.choice(S2)
print(f"\nSemi Final between {QFC} & {QFD}\nWinner : {SFB}")

print("")
print("****************************************")
print("***    Qatar World Cup 2022 Final    ***")
print("****************************************")

FIFAFinal = SFA, SFB
QATARWCF = random.choice(FIFAFinal)
print(f"\n*** {SFA} VS {SFB} ***\n")
print("*******************************************")
print(f"***Winner***    {QATARWCF}    ***Winner***")
print("*******************************************")




