# Inleiding
---
In dit bestand ga ik uitleggen wat er gemaakt moet worden. Ook ga ik beschrijven wat dit betekend voor de back end. Ik zal ook de benodigdheden zoals informatie en tools die handig zijn noemen en beschrijven. Zo kan ik het PIO project beter inzien.

# Wat wordt er gemaakt
---
 De Pak Je Kans Voorzieningencheck is een functionaliteit op Mijn Amsterdam, welke nog in ontwikkeling is. In deze omgeving kunnen mensen met een laag inkomen de persoonlijke voorzieningen zien waar ze recht op hebben. Deze voorzieningen worden zo persoonlijk mogelijk gefilterd. Dit doen we met de gegevens die we van de burger hebben en krijgen, als de burger toestemming geeft dat we zijn of haar gegevens gebruiken om deze voorzieningen te laten zien. Ons doel met deze omgeving is de burger inzicht geven welke voorzieningen zij kunnen aanvragen. De burgers kunnen het ook direct aanvragen, dit kunnen zij doen door op een link te klikken die we meegeven.

# Beschrijving van de Back-End
---
* Files met een beschrijving van de voorziening en de bijbehorende voorwaarden.
* Functies die deze voorwaarden toepassen op de voorzieningen en deze doorgeven aan de front end waar nodig is.
* Tests om te checken of het allemaal werkt.
* Certificaten om te checken of de security in orde is.

# Benodigdheden
---

### informatie

* Voorzieningen : Wigger
    1. Welke voorzieningen zijn er.
    2. Wat zijn de voorwaarden van de voorzieningen.
* Design : Bram
    1. Hoe gaat het er algemeen uit komen te zien.
    2. Wat moet waar komen te staan.
* Rule engine : Johan
    1. Verzamelen en organiseren van data voor rules, bepalen van voorwaarden zodat de rules gefilterd kunnen worden.
    2. De rule engine gebruiken om deze voorzieningen te tonen.
* Rule file : Enero
    1. Alle rules in een JSON file zetten, met de regels erbij zetten.
* Front end : Tim
    1. Welke informatie moet je doorgeven aan de front end om ervoor te zorgen dat elke voorziening op de goeie plaats komt te staan met de juiste tekst en linkjes erin.
    2. Hoe moet je deze informatie noemen, zodat het op de goed gefilterd kan worden.

### Tools 

* Editor (Visual Studio Code)
* Browser (gebruikt om info op te zoeken)
* Python libraries
    1. objectpath (Wordt gebruikt om regels in een string te zetten)
    2. os (Wordt gebruikt om met directories te werken)
    3. unittest (Wordt gebruikt om tests uit te voeren)
    4. Flask (Is een framework voor Python)

Deze als voorbeeld maar er zijn er nog meer.
* Command prompt 
* GitHub
