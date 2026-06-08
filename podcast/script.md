# Statnice na uši - podcast k bakalářským státnicím (Informatika / UI / Strojové učení)
# Formát: dva moderátoři. MÁRA = klidný expert s přirovnáními. TERKA = zvědavá studentka ve stresu.
# Math je psaná slovy, aby to šlo přečíst nahlas. Pokrývá zkouškové okruhy přehledově.

## Kapitola 1: Jak na to a proč se nebát
MÁRA: Vítej u Statnic na uši. Já jsem Mára a se mnou je Terka, která má za pět týdnů státnice.
TERKA: A momentálně mírnou paniku. Mám se naučit půlku bakaláře za pár večerů, Máro.
MÁRA: Dobrá zpráva: nemusíš umět všechno. Zkouška je přehledová. Chtějí přesné definice, hlavní myšlenky a terminologii, ne dlouhé důkazy.
TERKA: Jak to vypadá konkrétně?
MÁRA: Dostaneš osm otázek. Dvě z matematiky, dvě z informatiky a čtyři ze specializace, což je u tebe umělá inteligence a strojové učení. Každá otázka je za nula až tři body.
TERKA: A kolik potřebuju, abych prošla?
MÁRA: Dvanáct bodů celkem na trojku. Ale pozor, jsou dvě podmínky: aspoň pět bodů ze společných okruhů a aspoň sedm ze specializace.
TERKA: Takže specializace je důležitější.
MÁRA: Přesně. Sedm z dvanácti je víc než pět z dvanácti, takže tam dej většinu času. A nejdůležitější trik: vyhni se nulám.
TERKA: Jak myslíš vyhni se nulám?
MÁRA: U skoro každé otázky se první ptají na definici. Když umíš přesnou definici, máš skoro jistý bod. Když z žádné otázky nedostaneš nulu, projdeš skoro určitě.
TERKA: Takže definice nadrtit, specializaci pochopit, a u společných stačí breadth.
MÁRA: Krásně shrnuto. A pak udělat pár starých zkoušek na čas. To je nejlepší poslední krok. Pojďme na matiku.

## Kapitola 2: Společná matematika bez slz
TERKA: Matematická analýza. Limity, derivace, integrály. Začni intuicí, prosím.
MÁRA: Limita je odpověď na otázku: kam se hodnoty blíží, když se k něčemu přibližuju. Posloupnost má limitu L, když od nějakého místa jsou všechny členy libovolně blízko L.
TERKA: A derivace?
MÁRA: Okamžitá rychlost změny, sklon tečny. Když je derivace kladná, funkce roste. Druhá derivace kladná znamená, že je funkce konvexní, tedy jako miska.
TERKA: A integrál je plocha pod grafem, že?
MÁRA: Ano. A kouzlo je, že derivace a integrál jsou opačné operace. To je základní věta analýzy. Geometrická řada se taky hodí: součet jedna plus kvocient plus kvocient na druhou a tak dál je jedna děleno jedna mínus kvocient, pokud je kvocient v absolutní hodnotě menší než jedna.
TERKA: Lineární algebra. Tam se vždycky ztratím v maticích.
MÁRA: Mysli geometricky. Vektorový prostor je prostor směrů. Báze je nejmenší sada směrů, ze kterých složíš všechno. Počet těch směrů je dimenze.
TERKA: A vlastní čísla a vlastní vektory?
MÁRA: Vlastní vektor je směr, který matice nezmění, jenom ho natáhne nebo smrskne. O kolik ho natáhne, to je vlastní číslo. Najdeš je z charakteristického polynomu, tedy z podmínky, že determinant matice A mínus lambda krát jednotková je nula.
TERKA: Diskrétní matematika?
MÁRA: Tam jde o počítání a struktury na konečných množinách. Ekvivalence je relace, která je reflexivní, symetrická a tranzitivní, a rozdělí množinu na třídy. A z kombinatoriky znej binomickou větu a princip inkluze a exkluze, což je jen chytré odečítání dvojího započítání.
TERKA: Teorie grafů prý bývá vděčná.
MÁRA: Je. Strom je souvislý graf bez kružnic a má o jednu hranu míň než vrcholů. Bipartitní graf poznáš tak, že nemá lichou kružnici. A toky v sítích: představ si potrubí s kapacitami, ptáš se kolik proteče, a platí, že maximální tok se rovná minimálnímu řezu, tedy nejužšímu hrdlu.
TERKA: Pravděpodobnost?
MÁRA: Bayesova věta převrací podmíněnou pravděpodobnost: pravděpodobnost A za podmínky B je pravděpodobnost B za podmínky A krát pravděpodobnost A, děleno pravděpodobností B. Střední hodnota je dlouhodobý průměr a je lineární vždycky. A centrální limitní věta říká, proč se všude objevuje normální rozdělení: průměr mnoha nezávislých vlivů je zhruba normální.
TERKA: A logika, ať to máme.
MÁRA: Rozlišuj tautologii, což je pravda ve všech modelech, a splnitelnost, což je pravda aspoň v jednom. A rezoluce dokazuje spor: z klauzulí postupně odvozuješ, až vyrobíš prázdnou klauzuli.
TERKA: Dobrý, matika oddýchaná.

## Kapitola 3: Společná informatika
TERKA: Automaty a jazyky. Co si mám zapamatovat?
MÁRA: Hierarchii. Regulární jazyky umí konečný automat a regulární výrazy. Bezkontextové umí zásobníkový automat, ten má navíc paměť v podobě zásobníku. A nejsilnější je Turingův stroj, který umí všechno vyčíslitelné, ale narazí na nerozhodnutelné problémy, třeba problém zastavení.
TERKA: Složitost. Pé a en pé.
MÁRA: Třída pé jsou problémy řešitelné v polynomiálním čase. Třída en pé jsou ty, kde umíš v polynomiálním čase aspoň ověřit správné řešení. En pé úplný problém je nejtěžší v en pé, převedeš na něj všechny ostatní.
TERKA: Algoritmy obecně?
MÁRA: Znej rozděl a panuj a kuchařkovou větu na odhad složitosti. Z grafových algoritmů prohledávání do šířky a do hloubky, Dijkstru na nejkratší cesty s nezápornými délkami, a minimální kostru.
TERKA: Programovací jazyky. Já jsem se učila C sharp, ne Javu.
MÁRA: Perfektní, drž se C sharp. Měj jasno v objektovém programování: třída, rozhraní, dědičnost, polymorfismus. Hodnotové versus referenční typy. Garbage collector, který uklízí paměť. A vlákna a synchronizaci, kde hrozí souběh.
TERKA: Architektura a operační systémy?
MÁRA: Reprezentace čísel ve dvojkovém doplňku, privilegovaný režim a jádro. A hlavně virtuální paměť: adresa se dělí na číslo stránky a offset, a tabulka stránek to přeloží na fyzický rámec.
TERKA: A synchronizace?
MÁRA: Kritická sekce, vzájemné vyloučení, zámky a semafory. Klasika je producent konzument: semafor počítá volná a obsazená místa v bufferu.

## Kapitola 4: Základy umělé inteligence
TERKA: Tak, specializace. Tady musím zazářit.
MÁRA: Začni prohledáváním. Máš stavový prostor a hledáš cestu k cíli. Prohledávání do šířky, do hloubky, a hvězda A. Hvězda A je optimální, když je heuristika přípustná, tedy nikdy nenadhodnotí vzdálenost do cíle.
TERKA: Splňování podmínek, to CSP.
MÁRA: Proměnné, domény hodnot a omezení. Algoritmus AC tři zajistí hranovou konzistenci: pro každou hodnotu jedné proměnné musí existovat slučitelná hodnota u sousedů, jinak ji vyškrtneš.
TERKA: Pravděpodobnostní uvažování a Bayesovské sítě.
MÁRA: Bayesovská síť je orientovaný acyklický graf, kde každý uzel je náhodná proměnná a hrany jsou závislosti. Krása je, že místo obří sdružené tabulky stačí pro každý uzel pravděpodobnost vzhledem k jeho rodičům.
TERKA: A skryté Markovské modely?
MÁRA: Představ si řetězec skrytých stavů, které nevidíš, a pozorování, která vidíš. Filtrace je odhad současného skrytého stavu z pozorování. A Viterbiho algoritmus najde nejpravděpodobnější posloupnost skrytých stavů.
TERKA: Markovské rozhodovací procesy, ty MDP.
MÁRA: Agent ve stavech, dělá akce, dostává odměny a nejistě přechází dál. Hledáš strategii s nejvyšší očekávanou odměnou. Klíč je Bellmanova rovnice, a řešíš ji iterací hodnot nebo iterací strategií.
TERKA: A hry?
MÁRA: Minimax: já maximalizuju, soupeř minimalizuje, a alfa beta prořezávání ti ušetří prohledávání větví, které stejně nemají smysl. A znej Nashovo ekvilibrium, stav, kde se nikomu nevyplatí změnit strategii samostatně.

## Kapitola 5: Strojové učení, srdce specializace
MÁRA: Tady padá nejvíc bodů, tak pozor. Učení s učitelem: z dvojic vstup a správný výstup hledáš funkci, která funguje i na nových datech.
TERKA: A pořád slyším přeučení a regularizace.
MÁRA: Přeučení je, když se model naučí šum trénovacích dat. Pozná se tak, že má malou chybu na tréninku a velkou na nových datech. Regularizace tomu brání tím, že trestá moc velké váhy. El dvě je hladí, el jedna navíc dělá řídké váhy, čili rovnou vybírá příznaky.
TERKA: Lineární a logistická regrese.
MÁRA: Lineární regrese prokládá daty přímku metodou nejmenších čtverců. Logistická regrese je navzdory názvu klasifikace: lineární skóre protlačíš sigmoidou, a vyjde pravděpodobnost třídy mezi nulou a jedničkou.
TERKA: Support vector machines, ten es vé em.
MÁRA: Nejhezčí přirovnání: mezi dvě třídy chceš proložit co nejširší ulici. Hranice vede středem té ulice. Body na okraji jsou podpůrné vektory a jen ty určují hranici. A jádro umožní oddělit i data, co nejdou oddělit přímkou, jako bys je nadzvedl do vyšší dimenze.
TERKA: Rozhodovací stromy a lesy.
MÁRA: Strom klade otázky typu je příznak větší než práh a dělí data tak, aby skupiny byly co nejčistší, podle entropie nebo Giniho indexu. Náhodný les je hromada stromů, co hlasují, a je překvapivě robustní.
TERKA: Učení bez učitele?
MÁRA: Tam nemáš správné odpovědi. K means rozdělí data do k shluků: opakovaně přiřaď body nejbližšímu centru a přepočítej centra. A analýza hlavních komponent, PCA, najde směry, kde se data nejvíc mění, a tam je promítne, takže ubereš dimenze.
TERKA: A hodnocení modelů?
MÁRA: Matice záměn a z ní přesnost, preciznost a úplnost. Když máš nevyvážené třídy, samotná přesnost klame, proto se dívej na F jedna. A nikdy nelaď model podle testovacích dat, na to je validační sada.

## Kapitola 6: Poslední rady před zkouškou
TERKA: Cítím se líp. Co mám dělat těch pět týdnů?
MÁRA: Nejdřív se nauč u všech témat aspoň definici. Pak dotáhni specializaci do hloubky, abys uměla vysvětlit a načrtnout. Společné okruhy ber na šířku, definice plus jeden typový výpočet.
TERKA: A pak ty staré zkoušky.
MÁRA: Ano. Udělej dvě tři stará zadání na čas a koukni, jestli se vejdeš do limitů. To ti řekne víc než jakýkoliv odhad.
TERKA: A když se zaseknu?
MÁRA: Napiš aspoň definici a hlavní myšlenku. Parciální body se sčítají. Lepší tři rozjeté otázky než jedna dokonalá a dvě prázdné.
TERKA: Dík, Máro. Jdu drtit.
MÁRA: Držím palce. A pamatuj: cílem není výborně, cílem je v klidu projít. Měj se a hodně štěstí u státnic.
