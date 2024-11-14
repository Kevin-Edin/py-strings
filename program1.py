import time

inventory = []
game_over = False

def input_string(text):
    while True:
        try:
            return str(input(text))
        except:
            print("Det är ett för konstigt namn, testa skriva ett till namn")

while game_over == False:
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
    print("En hög blixt hörs i distansen och det börjar regna tungt.")
    print("Du vill inte bli plaskblöt så du väljer att försöka hitta någonstans att gömma dig från regnet.")
    print("Du ser dig omkring och lägger ögonen på en liten Frasses.")
    print("Du rusar bort till den och kastar dig in genom dörren.")
    print("Du råkar knuffa till någon i processen.")
    print("Personen vänder sig om och det visar sig vara en väldigt gammal gubbe med pytte lite vitt hår kvar på skallen och långt skrunkligt skägg.")
    print("Han frågar dig med en av de snällaste gubbe rösterna du kan tänka dig:")
    print("'Ursäkta mig, vad heter du?'")

    namn = input_string("Skriv ett namn: ")
    namn2 = namn.upper()

    print("Du svarar:")
    print(f"'Jag heter {namn}.'")
    print("Gubbens ton ändras från snäll tomte till vrålande soldat.")
    print(f"'JA DU {namn2}! KANSKE DU VILL TA OCH SE DIG FÖR NÄSTA GÅNG INNAN DU PUTTAR PÅ NÅGON!! DU GJORDE SÅ ATT")
    print("JAG SPILLDE COCA-COLA PÅ MIG SJÄLV OCH NU ÄR MINNA FINGRAR ALDELLES KLADDIG OCH KLIBBIG!!'")
    print("Du pyser ut ett snällt:")
    print("'Förlåt.'")
    print("Den gammla gubben kliar sig i skägget och svarar med den snälla rösten igen:")
    print("'Du är förlåten.'")
    print("Sedan vänder han sig om och börjar ta mera Coca-Cola ur sodamaskinen.")
    print("Du skuttar hastigt förbi gubben och fram till kassan.")
    print("Kassörskan är en ung man.")
    print("Du frågar han:")
    print("'Är det okej om jag stannar här tills min buss kommer? Den kommer om 6 timmar.'")
    print("Kassörskan svarar:")
    print("'Bara om du köper någonting.'")
    print("")

    if "80kr" in inventory:
        print("Du kommer på att du plockade upp några kontanter som flög ur den där äckliga toaletten.")
        print("Du tar dom ur fickan och räknar dom i din hand.")
        print("Du har 80 kr, perfekt nog mycket för ett litet skrovmål.")
        print("Du säger till kassörskan:")
        print("'Ah visst! Jag köper ett skrovmål.'")
        print("Du betalar och får ditt kvitto.")
        print("'Order 32'")
        print("Efter 10 minuter så får du din order och du glufsar i dig skrovmålet.")
        print("Sedan stannar du kvar i Frasses tills en buss hem kommer.")
        print("Du tar bussen hem och lever glatt i resten av dina dagar.")
        game_over = True
    else:
        print("Du sparkar till en bänk och stampar ut ur Frasses.")
        print("Du tänker argt för dig själv:")
        print("'Vilken liten bajsunge alltså.'")
        print("Du ställer dig under ett tak och är beredd på att hålla dig själv vaken tills bussen hem kommer.")
        print("Efter 15 minuter så kommer den gammla gubben från Frasses och frågar dig:")
        print("'Vad sysslar du med då?'")
        print("Du svarar:")
        print("'Väntar bara på en buss hem. Den kommer om 6 timmar.'")
        print("Den gammla gubben frågar:")
        print("'Vill du att jag ska skjutsa dig? Jag gör det gratis!'")
        choice = input("[ja] eller [nej]: ")

        if "ja" in choice:
            print("")
            print("Du svarar:")
            print("'Okej :)'")
            print("Den gammla gubben börjar le och du kan se hans gammla gula tänder.")
            print("Sedan springar han hastigt bort och bakom ett hörn.")
            print("Du hör en motor startas och ett ljus komma från andra sidan hörnet")
            print("Sedan kommer det en vit och skruttig skåpbil.")
            print("Den stannar framför dig och den gammla gubben rullar ner fönstret.")
            print("Han ropar över motorns ljud:")
            print("'Det är bara att hoppa in!'")
            print("Du öppnar sidodörren och hoppar in i skåpbilen.")
            print("När du stänger sidodörren hör du hur gubben låser den och du känner hur han genast börjar köra väldigt snabbt.")
            print("Vägen är guppig och skåpbilen skakar mycket.")
            print("Efter drygt 45 minuter så stannar skåpbilen.")
            print("Sidodörren låses upp och öppnas.")
            print("Den gammla gubben sträcker ut sin hand och säger:")
            print("'Så! Nu är vi framme!'")
            print("Du kliver ut ur bilen och märker att du faktiskt är i din hemma by.")
            print("Du säger till gubben:")
            print("'Tackar så helst mycket!'")
            print("Den gammla gubben ger en tumme upp och du skuttar glatt hem till ditt hus och lever god och glad i resten av dina dagar.")
            game_over = True
        elif "nej" in choice:
            print("")
            print("Du svarar:")
            print("'Nej tack.'")
            print("Den gammla gubben skakar på axlarna och vandrar vidare.")
            print("Du står kvar under taket.")
            print("Det kalla vädret blåser regnet på dig även fast du står under taket.")
            print("Du står där och fryser i 6 timmar tills din buss kommer.")
            print("Du tar den hem och lever sedan glatt i resten av dina dagar.")
            game_over = True
        else:
            print("")
            print("Du får en hjärt attack och dör framför den gammla gubben.")
            game_over = True
print("SLUT!")