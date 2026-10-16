print("Quiz: Programmeringens samhällspåverkan")
print("Svara på frågorna med a, b eller c.")
print()

fragor = [
    ["Vem var Ada Lovelace?",
     "a) Programmerare", "b) Sångare", "c) Fotbollsspelare", "a"],

    ["Vem arbetade Ada Lovelace med?",
     "a) Albert Einstein", "b) Charles Babbage", "c) Isaac Newton", "b"],

    ["Vad är programmering?",
     "a) Att laga mat", "b) Att måla", "c) Att skriva instruktioner till datorer", "c"],

    ["Vad används programmering till?",
     "a) Att skapa appar", "b) Bara att spela fotboll", "c) Bara att läsa böcker", "a"],

    ["Vad är en algoritm?",
     "a) En dator", "b) Steg för att lösa ett problem", "c) En skärm", "b"],

    ["Vad är en dator?",
     "a) Ett djur", "b) Ett fordon", "c) En maskin som kan behandla information", "c"],

    ["Vad gjorde Ada Lovelace?",
     "a) Skrev instruktioner till en beräkningsmaskin", "b) Byggde bilar", "c) Uppfann telefonen", "a"],

    ["Vad betyder AI?",
     "a) Automatisk internet", "b) Artificiell intelligens", "c) All information", "b"],

    ["Hur påverkar programmering samhället?",
     "a) Den används inte längre", "b) Den stoppar all teknik", "c) Den hjälper oss med många saker", "c"],

    ["Vad kan programmering hjälpa sjukvården med?",
     "a) Att analysera information", "b) Att bygga fotbollsplaner", "c) Att laga mat", "a"],

    ["Varför är programmering viktigt idag?",
     "a) Ingen använder datorer", "b) Många saker använder datorprogram", "c) Det finns inga appar", "b"],

    ["Kan programmering skapa problem?",
     "a) Nej, aldrig", "b) Bara i skolan", "c) Ja, till exempel problem med säkerhet", "c"]
]

poang = 0

for fraga in fragor:
    print()
    print(fraga[0])
    print(fraga[1])
    print(fraga[2])
    print(fraga[3])

    svar = input("Ditt svar: ").lower()

    if svar == fraga[4]:
        print("Rätt svar!")
        poang = poang + 1
    else:
        print("Fel svar!")
        print("Rätt svar är", fraga[4])

print()
print("Du fick", poang, "av", len(fragor), "poäng.")

if poang >= 9:
    print("Bra jobbat!")
elif poang >= 6:
    print("Bra försök!")
else:
    print("Öva lite till!")