import time

inventory = []


print("Du vaknar upp på en toalett med en rejäl huvudvärk.")
print("Det är svårt att att kunna se vad som är i toaletten men det luktar inte gott iallafall.")
print("Rummet du befinner dig i är väldigt mörkt. Det finns en taklampa som svagt lyser upp de otvättade väggarna och de smuttsiga golvet.")
print("Handfattet verkar vara rostigt och ha lite mögel och spegeln är helt krossad.")
print("Plötsligt hör du någon knacka på dörren.")
print("Fylld med skräck tänker du inte helt klart, din hjärna värkar välja mellan att [fråga] eller [bajsa], men den kan inte riktigt bestämma sig.")
choice = input("Vill du [fråga] eller [bajsa]: ")
if "fråga" in choice:
    print("")
    print("Du vrålar så högt du kan:")
    print("'VEM FAN ÄR DU OCH VAD FAN VILL DU MIG?!'")
    print("En ung kvinnlig röst svarar tillbaka:")
    print("'Du har varit där inne i 5 timmar, är allting okej? Kan du snälla komma ut så att någon annan kan använda toan?'")
    print("Du svarar tillbaks:")
    print("'Åh, uh... en sekund bara!'")
    print("Du vaggar fram till dörren och lämnar toan.")
elif "bajsa" in choice:
    print("")
    print("Du drar ner dina brallor och lägger dina våta skinkor på den äckliga toan täckt i smuts.")
    print("Du börjar extremt spänna dina magmuskler tills det börjar göra ont, du tar i så hårt att din hjärna nästan får slut på syre.")
    print("Plötsligt släppte smärtan och du känner hur vätskan som var i toan stänker upp på dina skinkor.")
    print("Du torkar dig med det jätte tunna toapappret och spolar.")
    print("Det blir dock toastopp.")
    print("Toan börjar skaka våldsamt.")
    print("Plötsligt börjar det flyga ut några 10 kr ur den.")

    inventory.append("80kr")

    print("Hastigt plockar du om dem och går ut ur toan.")
    print("Du stänger dörren och hör en hög smäll just efteråt.")
    print("Den märkliga toa vätskan börjar långsamt forsa ut från dörrens undersida.")
    print("Du backar lite från dörren och vänder dig om.")
else:
    print("")
    print("Din hjärna kan inte förstå vad du försöker göra så det som händer är att du rapar väldigt högt och du lämnar toaletten.")

print("")
print("Du blir bemött av en tånårig kvinna med en McDonalds klädsel på sig.")
print("Hon verkar vara väldigt förvånad och orolig.")
print("Du vinkar glatt till henne och säger:")
print("'Hejdå!'")
print("Sedan springer du hastigt ut ur McDonalds och ut på den mörka gatan.")
print("Du tar fram din telefon och kollar klockan.")
print("'02:23'")
print("Nästa buss hem kommer alltså om 6 timmar.")
print("Du får panik när du inser att du kommer vara fast i staden i 6 timmar.")
print("Men du kommer på att du skulle kunna ringa någon som kan hämta upp dig.")
print("Du plockar fram din telefon, går till kontakter och just när du skulle ringa din bästa vän så dör telefonen.")
print("Du kan se ditt irriterade och smuttsiga ansikte stirra tillbaks på dig i telefonens reflektion.")
print("")