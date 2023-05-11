# Osa 4 - Sisendi töötlemine, lemmatiseerimine, asjakohasuse hinnang

<aside>
💡 Selles osas keskendume kasutaja kõikvõimalikele küsimustele - täpsemalt nende mõistmisele. Tuleb ju kliendi küsimusest enne aru saada, enne kui saame talle anda rahuldava vastuse. Selleks kasutame mõningaid lihtsamaid keeletehnoloogias kasutatavaid võtteid.

</aside>

### 0. Üldine töö käik

Selles praktikumis teeme läbi kolm tüüpilist etappi loomuliku keele analüüsis. Antud juhul keskendume kasutajate kõikvõimalike sisendite töötlemisele.

Need etapid on:

- Tokeniseerimine ehk sisendi sõnadeks (või ka lauseteks) lammutamine
- Lemmatiseerimine ehk sisendis leiduvate sõnade algvormi viimine
- Informatsiooni sisuline analüüs
- Asjakohasuse hinnangu andmine

NB! Selles osas kirjutame koodi ainult [bot.py](http://bot.py) faili.

### 1. Estnltk teek

Nagu juba mainitud: selleks, et kasutaja sisendit juturobotile loetavaks teha, on vaja seda enne paremale kujule töödelda. Eesti keele töötlemiseks on Pythonis suurepärane teekide kogumik nimega EstNLTK.

**Wikipeedia:** 

> **EstNLTK** on [teekide](https://et.wikipedia.org/wiki/Teek) kogumik, mis on mõeldud eestikeelsete [tekstide töötluseks](https://et.wikipedia.org/wiki/Tekstit%C3%B6%C3%B6tlus). EstNLTK on kirjutatud programmeerimiskeeles [Python](https://et.wikipedia.org/wiki/Python_(programmeerimiskeel)).[[1]](https://et.wikipedia.org/wiki/EstNLTK#cite_note-:0-1)
> 

> EstNLTK on projektipõhiselt koostamisel [Tartu Ülikoolis](https://et.wikipedia.org/wiki/Tartu_%C3%9Clikool) [Sven Lauri](https://et.wikipedia.org/w/index.php?title=Sven_Laur&action=edit&redlink=1) juhtimisel. Projektide tulemuse eesmärgiks on ühendada juba varem loodud eesti keele töötluse programmid uute loodavate ja parandatud versioonidega ning teha ühiselt kättesaadavaks kõigile soovijatele. Arendamist finantseerib [Haridus- ja teadusministeerium](https://et.wikipedia.org/wiki/Haridus-_ja_Teadusministeerium), riikliku programmiga Eesti keeletehnoloogia.[[2]](https://et.wikipedia.org/wiki/EstNLTK#cite_note-:1-2)
> 

Uuri põgusalt Estnltk võimalusi ja syntaxit: [https://github.com/estnltk/estnltk/blob/main/tutorials/basics/introduction_to_nlp_pipeline.ipynb](https://github.com/estnltk/estnltk/blob/main/tutorials/basics/introduction_to_nlp_pipeline.ipynb)

### 2. Tokeniseerimine

Esimese etapina on vaja “lammutada” kasutaja poolt antud sisend eraldi tokeniteks ehk sõnadeks.

Selleks kasuta EstNLTK Text klassi (vaata eelmises punktis antud linki).

<aside>
🔨 **Harjutus 1**

Täienda meetodit **get_words()** ja tagasta kasutaja sisendis olevad sõnad tavalise Pythoni järjendina. Selleks pead ka valmis tegema **get_text()** meetodi, kus töötled Estnltk Text klassiga kasutaja sõnumi.

Näide:  get_words(”Tere maailm!) → [”Tere”, “maailm”, “!”]

</aside>

### 3. Lemmatiseerimine

Teise etapina muudame kasutaja sisendis leiduvad sõnad lemmadeks ehk viime nad algvormi.

Uuri jälle Text klassi ja selle atribuute.

<aside>
🔨 **Harjutus 2**

Täienda meetodit get_lemmas() ja tagasta kasutaja sisendis olevad **************lemmad************** tavalise Pythoni järjendina.

Näide:  get_words(”Läksime õuest joostes tuppa.”) → [”minema”, “õu”, “jooksma”, “tuba”, “.”]

</aside>

### 4. Sisuline analüüs

Hilisemaks API päringu sooritamiseks on sul arvatavasti vaja anda ka mõningaid parameetreid, mis sõltuvad kasutaja sisendist. Selleks on vaja kasutaja sisendit töödelda, et saaksime need parameetrid kätte ning oleksime veendunud nende õigsuses.

Selleks uuri Estnltk õpetusi peatükis “information extraction” siit: [https://github.com/estnltk/estnltk/tree/main/tutorials/nlp_pipeline/D_information_extraction](https://github.com/estnltk/estnltk/tree/main/tutorials/nlp_pipeline/D_information_extraction)

<aside>
🔨 ********************Harjutus 3********************

Täienda järgnevaid meetodeid:

get_location → tagastab lausest sõna mis viitab asukohale

get_time → leiab lausest ajale viitava sõna ja tagastab selle kuupäev + kellajalise väärtuse

get_person → leiab lausest isikule viitava(d) sõnad.

Näited:

get_location(”Minu vanaema elab Vändras”) → “Vändra”

get_time(”Eile õhtul kell 9 oli ilus ilm.”) → “11-05-2023T21:00:00Z”

get_person(”Mis sai Donald Trumpist peale ametiaja lõppu?”) → “Donald Trump”

</aside>

### 5. Asjakohasuse hinnang

Viimaseks on vaja tagastada asjakohasuse hinnang. Selle funktsiooni loogika jääb täiesti sinu mõelda. Tagastada tuleb täisarv vahemikus 0-100, kus suurem number tähendab asjakohasemat kasutaja sisendit. Hinnangut kasutad hiljem, et otsustada kuidas kasutaja sisendile reageerida ning samuti on seda vaja katsetuste osas, kus sinu juturobot ei pruugi enam ainuke tegelane olla 🕵️

<aside>
🔨 ********************Harjutus 4********************

Täienda meetodit **********************************************get_confidence_rating()**********************************************

</aside>

- Vihje 🤫
    
    Hea mõte on kasutada sinu juturoboti valdkonnaga seotud sõnu ja sõnu mis kindlasti esinevad lauses, mis on sinu juturobilt esitatavas sobivas küsimuses sees. Nendest sõnadest saab luua sõnastiku, kus igale sõnale on antud teatav skoor. Samuti on sõnade võrdlemiseks soovitatav kasutada lemmasid.
    

Kui läbisid kõik selle osa punktid, siis oled tõesti suure töö ära teinud! Kiida ennast, siruta vahepeal ja puhka silmi 🤓