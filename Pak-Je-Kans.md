# Wat wordt er gemaakt
---
We willen een omgeving maken op Mijn Amsterdam genaamd Pak Je Kans voorzieningencheck, in deze omgeving kunnen mensen met een laag inkomen de voorzieningen zien waar ze recht op hebben. Deze voorzieningen worden zo persoonlijk mogelijk gefilterd. Dit doen we met de gegevens die we van de burger hebben en krijgen, als de burger toestemming geeft dat we zijn of haar egevens gebruiken om deze voorzieningen te laten zien. Ons doel met deze omgeving is de burger inzicht geven welke voorzieningen zij kunnen aanvragen. De burgers kunnen het ook direct aanvragen, dit kunnen zij doen door op een link te klikken die we meegeven.

# Wat moet er gemaakt worden in de Back-End
---
* Er moeten files worden gemaakt met voorzieningen en voorwaarden erin.
* Er moeten functies komen die deze voorwaarden toepassen op de voorzieningen en deze doorgeven aan de front end waar nodig is.
* Er moet een docker container worden gemaakt.
* Ook moeten er tests worden geschreven om te checken of het allemaal werkt.
* Certificaten om te checken of het veilig is.
* jenkins file voor Build en Deploy.
* Kibana en Sentry logging views op de NUC.
* Netwerkconnectiviteit + bijbehorende env variabelen om connectie te maken met de bron api.

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

* Editor
* Browser 
* Python libraries
    1. objectpath
    2. os
    3. unittest
    4. blinker
    5. urllib3
    6. Werkzeug
    7. python-dateutil
    8. Flask
    9. connexion
    10. PyYAML

Deze als voorbeeld maar er zijn er nog meer.
* Command prompt 
* GitHub
