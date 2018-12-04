
Theorie exploratie

Opdracht 1
a) Verzin een zenderinrichting voor de Oekraïne. Iedere provincie moet een zendertype hebben, geen enkele twee aangrenzende provincies mogen hetzelfde zendertype hebben. Verzin een zenderinrichting voor het hele land, en hoe minder zendertypes je gebruikt, hoe beter.

Zenderinrichting is te vergelijken met het kleuren van een landkaart. Beide zijn namelijk planaire grafen. Er bestaat een doorgerekend bewijs dat elke landkaart is te kleuren met 4 kleuren.

1 kleur is al triviaal voor 2 aangrenzende landen.
2 kleuren is niet toelaatbaar als er een cykel is.
3 kleuren zijn al veel landkaarten te kleuren. Landkaarten zijn niet 3 kleurbaar als er een punt is met oneven graad (>=3) en de buren een gesloten wandeling vormen.
4 kleurbaar is elke graaf uit de theorie.

Hieruit concluderen we dat er maximaal 4 kleuren nodig zijn. We checken of er een mogelijkheid is om 3 kleurbaar is, zo niet passen we 4 kleuren algoritme toe.

https://nl.wikipedia.org/wiki/Vierkleurenstelling
We kleuren de graaf met Kempe n-color theorem http://www.cs.princeton.edu/~appel/Color.pdf


b) Doe hetzelfde voor China, de USA en uiteindelijk voor moedertje Rusland. Hoe minder zenderypes, hoe beter.

Idem voor hierboven

c) De produktie van zenders wordt in Rusland uiteraard ook door de overheid beregeld. Het is het goedkoper om minder zendertypes te hebben, maar ook om van alle zendertypes ongeveer evenveel te hebben. Probeer voor ieder land met ieder minimumaantal zendertypes te bepalen hoe een evenwichtige verdeling eruit zou zien, en kijk of een inrichting mogelijk is met zo'n verdeling.

- kempe heuristic toepassen. Ipv random kleur aan node toepassen, kleur toepassen die minst is gebruikt. Dus door middel van lijst bijhouden hoevaak een kleur al is gebruikt.
Iteratief algortime op toelaatbare oplossing die aan constraints voldoet. Een node met de kleur die het vaakst is gebruikt, de kleur geven die het minst is gebruikt en checken of oplossing nof steeds toelaatbaar is.

----------------------------------------------------------------------------------------------------------------------------------------------

Opdracht 2
Er zijn vier mogelijke kostenschema's bekend geworden. Bekijk voor ieder land welk kostenschema de voordeligste inrichting oplevert.

Zendertype	Kosten 1	Kosten 2	Kosten 3	Kosten 4
    A      	  12	     19	       16	        3
    B	        26	     20	       17	       34
    C 	      27	     21	       31	       36
    D	        30	     23	       33	       39
    E	        37	     36	       36	       41
    F	        39	     37	       56	       43
    G	        41	     38	       57	       58

Branch and bound.
Lastige van het probleem is dat wanneer je 1 zendertype toevoegd die duurder is, je misschien heel vaak eentje kan gebruiken die goedkoop is.
Idee is misschien om node met hoogste graad een duurdere kleur te geven.

----------------------------------------------------------------------------------------------------------------------------------------------

Advanged
Omdat production in numbers goedkoper is, wordt iedere geplaatste zender van een type 10% goedkoper dan de vorige van hetzelfde type. Vind, met je algoritmes, opnieuw de beste oplossing voor de landen. Hoe vergelijken ze met de oplossingen van opgaven 1 en 2?

----------------------------------------------------------------------------------------------------------------------------------------------

State Space

De statespace voor RadioRussia is gemakkelijk te berekenen, er zijn in totaal 7 verschillende zendtypes die per provincie geplaatst kunnen worden. De formule van de upperbound wordt hierdoor gemakkelijk berekend:

State Space (losse punten) = aantal zendtypes ^ aantal provincies

Maar in ons geval van constraints waarbij aanliggende provincies niet hetzelfde zendtype mogen hebben, word de statespace een stuk lager. De eerste provincie heeft 7 mogelijke opties en de daarop volgende provincies steeds 6 verschillende zentypes waaruit ze kunnen kiezen. De  formule wordt hieroor:

State Space (aanliggende punten) =  aantal zendtypes * (aantal zendtypes - 1) ^ (aantal provincies - 1)

Als we deze twee voor een land als Ukraine berekenen:
losse punten: 1.3 * 10^21
aanliggende punten: 2.2 * 10^19

Rusland:
losse punten: 7^82 = 1.986 * 10^69
aanliggende punten: 7.5 * 10^63

Wanneer de constaints worden toegepast wordt de state space gellijk een stuk kleiner.
