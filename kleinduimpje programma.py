dictio = {
    "begin":{
        "text": """Kleinduimpje woont samen met zijn broertjes in het bos. Omdat er te weinig eten is thuis, worden ze in het bos achtergelaten. Kleinduimpje heeft gelukkig witte steentjes in zijn zak zitten die hij op de route achterlaat waardoor hij weer terug komt. Ze komen terug thuis, maar hun ouders willen hen weg hebben dus brengt de vader ze nog een keer weg. 
    Je wordt weg gebracht naar het midden van het bos. Neem je iets mee? Keuzes: brood, blaadjes, niks. """, 
        "choices": {
            "brood": "brood stukjes",
            "blaadjes": "blaadjes",
            "niks": "leeg"
            }
        },
    
    "brood stukjes": {
        "text": """Je scheurt stukjes brood af terwijl je aan het lopen bent, ze vallen op de grond als een soort route. Je komt in het midden van het bos aan. Het is donker en je kunt niet ver zien. Je vader zegt dat hij even iets gaat halen en dat jullie hier moeten blijven. Jullie gaan zitten op de grond en wachten even. Je vader lijkt niet terug te komen, wat doe je? Keuzes: blijven zitten en wachten, je spoor terug volgen. """,
        "choices": {
            "blijven zitten en wachten": "blijven",
            "je spoor terug volgen": "spoor brood"
            }
        },
    
    "blaadjes": {
        "text": """Je pakt snel een hand vol met gevallen blaadjes en stopt die in je zak. Je laat ze vallen op de grond terwijl je achter je vader aanloopt. Je komt in het midden van het bos aan. Het is donker en je kunt niet ver zien. Je vader zegt dat hij even iets gaat halen en dat jullie hier moeten blijven. Jullie gaan zitten op de grond en wachten even. Je vader lijkt niet terug te komen, wat doe je? Keuzes: blijven zitten en wachten, je spoor proberen te volgen terug.""",
        "choices": {
            "blijven zitten en wachten": "blijven",
            "spoor terug volgen": "spoor blaadjes"
            }
        },
    
    "leeg": {
        "text": """Je loopt achter je vader aan. Je komt in het midden van het bos aan. Het is donker en je kunt niet ver zien. Je vader zegt dat hij even iets gaat halen en dat jullie hier moeten blijven. Jullie gaan zitten op de grond en wachten even. Je vader lijkt niet terug te komen, wat doe je? Keuzes: blijven zitten en wachten, opzoek naar mensen. """,
        "choices": {
            "blijven zitten en wachten": "blijven",
            "opzoek naar mensen": "mensen"
            }
        },
    "blijven": {
        "text": """De nacht is aan gebroken en je maakt een vuurtje met je broertjes om warm te blijven. Je valt inslaap. De volgende ochtend als je wakker wordt is je vader er nog steeds niet. Wat doe je? Keuzes: blijven zitten en wachten, spoor terug volgen.""",
        "choices": {
            "blijven zitten en wachten": "blijven",
            "spoor terug volgen": "spoor blaadjes"
            }
        },
    "spoor brood": {
        "text": """De eerste paar stukjes brood zie je al op de grond liggen. Maar als je een maal op weg bent kun je de stukjes niet meer op de grond vinden. Ze zijn op gegeten door de dieren in het bos. Je bent verdwaald. Wat doe je? Keuzes: Terug lopen naar waar je vandaan komt, op zoek naar mensen. """,
        "choices": {
            "terug lopen naar waar je vandaan komt": "terug",
            "opzoek naar mensen": "mensen"
            }
        },
    
    "spoor blaadjes": {
        "text": """Het is herfst en dus liggen er een hele hoop blaadjes op de grond. Je raakt verward en weet niet meer welke blaadjes jij hebt laten vallen. Je bent verdwaald. Wat doe je? Keuzes: Terug lopen naar waar je vandaan komt, op zoek naar mensen. """,
        "choices": {
            "terug lopen naar waar je vandaan komt": "blijven",
            "opzoek naar mensen": "mensen"
            }
        },
        
    "mensen": {
        "text": """Na een paar uur ronddwalen in het bos zie je in de verte een lichtje. Je volgt de route naar het licht en ziet een huisje staan. Je hoort stemmen uit het huisje komen; er zijn mensen thuis! Wat doe je? Keuzes: Je klopt aan bij het huis, je loopt verder. """,
        "choices": {
            "Je klopt aan bij het huis": "aankloppen",
            "je loopt verder": "verder"
            }
        },
    
    "terug": {
        "text": """Je vind de plek terug waar je hebt geslapen. Je hebt honger je ziet een bos met bessen. Wat doe je? Keuzes: Eet de bes, eet de bes niet""",
        "choices": {
            "eet de bes": "bes",
            "eet de bes niet": "niet bes"
            }
        },
    
    "bes": {
        "text": """De bes is giftig, je wordt er ziek van. Je hebt geen toegang tot een dokter of tegengif dus je gaat dood.""",
        "choices": {
           
            }
        },
    
    "niet bes": {
        "text": """Je hebt nog steeds honger dus je gaat opzoek naar iets anders te eten maar kunt niks vinden. Wat doe je? Keuzes: opzoek naar mensen, je loopt rond""",
        "choices": {
            "opzoek naar mensen": "mensen",
            "rond lopen": "rondlopen"
            }
        },
    
    "rondlopen": {
        "text": """Je kunt geen eten vinden en je energie is op. Je valt neer en ligt op de grond. Je kunt niet overeind komen en gaat dood.""",
        "choices": {
           
            }
        },
    
    "verder": {
        "text": """Je dwaalt door het bos maar ziet niks anders. Je weet wel de weg naar waar je vandaan kwam en het huisje. Wat doe je? Keuzes: Huisje, terug """,
        "choices": {
            "naar het huisje": "huisje",
            "terug gaan naar waar je vandaan kwam": "terug"
            }
        },
    
    "aankloppen": {
        "text": """Je klopt aan en een oud vrouwtje doet de deur open. Ze nodigt je uit voor een kopje thee. Je loopt naar binnen en hoort de deur achter je in het slot vallen. Je gaat aan de tafel zitten en de vrouw zet een kopje voor je neer. Je kijkt rond in het huisje en ziet allemaal kooien, je voelt je niet op je gemak. Je probeert naar buiten te lopen maar de deur is dicht. Je zit gevangen. Je kunt proberen de deur in te trappen of uit het raam klimmen. Wat doe je? Keuzes: deur, raam""",
        "choices": {
            "door het raam": "raam",
            "door de deur": "deur"
            }
        },
    "raam": {
        "text": """Het raam staat op een kier en je probeert je er tussen te wurmen. Het is moeilijk maar je komt er door heen. Je komt aan de andere kant van het huisje uit en je ziet een ander licht van een dorpje. Daar loop je naar toe. Je vindt een herberg en kan hier slapen. Je start een nieuw leven. Je leeft nog lang en gelukkig.""",
        "choices": {
            
            }
        },
    
    "deur": {
        "text": """Je probeert de deur in te trappen maar de deur is te sterk. De vrouw ziet je en stopt je in een kooi, de sleutel gooit ze in een ijzeren pot boven het vuur. De sleutel smelt. Je zit hier vast. Je blijf hier voor de rest van je leven zitten.""",
        "choices": {
            
            }
        },
}

def inputcheck(inp, keuzes):
    if inp in keuzes:
        return keuzes[inp]
    
staat = 'begin'

while True:
    print(dictio[staat]["text"])
    for i in dictio[staat]["choices"]:
        print(i)
    richting = None
    
    while richting == None:
        richting = input("Waar ga je heen?").lower()
    print(richting)
    staat = inputcheck(richting,dictio[staat]["choices"])
    print(staat)
   
    
