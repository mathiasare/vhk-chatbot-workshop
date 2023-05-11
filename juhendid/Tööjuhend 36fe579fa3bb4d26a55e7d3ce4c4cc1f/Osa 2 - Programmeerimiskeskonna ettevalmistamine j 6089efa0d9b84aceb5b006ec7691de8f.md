# Osa 2  - Programmeerimiskeskonna ettevalmistamine ja esimesed katsetused

<aside>
🎓 Selles osas seame valmis kõik vajaliku, et saaksime hakkata lõpuks koodi kirjutama. Veel seda tüütut seadistamist… aga ole mureta - selle osa lõpus saame oma juturoboti käima panna!

</aside>

### 1. Seadista VS Codium ja tutvu sellega

- Ava VS Codium
- Ülevalt ribast vali File → Open Folder → Vali kaust kuhu salvestasid kursuse materjalid
- Vasakult menüüst vali Extentions ja lae alla järgnev laiendus (suure tõenäosusega see juba on olemas):
    - Python
- Taaskäivita VSCodium, kui ta seda nõuab laienduse toimimiseks.
- Liigu tagasi “Explorer” valikule vasakust menüüst

### 2. Ava kursuse projekt VSCodiumis

- Vali ülevalt menüüst File → Open Folder
- Vali avanenud File Exploreri aknas allalaetud kursuse failide kaust

### 3. Seadista kursuse pythoni projekt

- Ava uus terminaliaken. Ülevalt Terminal → New Terminal
- Liigu kausta /kood/chatbot-workshop. Selleks jooksuta käsk (kirjuta käsk terminalis ja vajuta Enter):
    
    ```bash
    cd kood/chatbot-workshop
    ```
    
- jooksuta käsk:
    
    ```bash
    poetry --version
    ```
    
    Kontrolli kas saad vastuseks (kui ei siis anna juhendajale märku):
    
    ```bash
    Poetry (version 1.4.2)
    ```
    
- jooksuta käsk:
    
    ```bash
    poetry install
    ```
    

Oota kuni teekide installimine on lõpuni jõudnud. Kui kõik õnnestus, siis nüüd peaks olema sinu pythoni projekt seadistatud ehk seda on võimalik jooksutada, muuta ja testida.

### 4. Seadista .env fail

<aside>
📎 .env fail ehk ”dotenv” on programmeerimises kasutusel abifailina, mis sisaldab globaalseid muutujaid ning paroole.

</aside>

- Ava editoris fail **.env.example**
- Lisa enda discordi boti token muutujale **DISCORD_TOKEN**
    
    Tulemus võiks näha välja nii:
    
    ```bash
    DISCORD_TOKEN=SINUTOKENONLISATUDSIIA
    ```
    
- Muuda faili nimi **********.env********** -ks. Selleks vali vasakult menüüst praegune fail ja vajuta **F2 (**või parem klikk ja Rename)

### 5. Tutvu projekti sisuga

Kohe saad jooksutada oma uut boti rakendust ja äratada oma juturobot ellu! Enne võõra koodi jooksutamist võiks aga enne koodiga tutvuda - muidu kes teab, mida see teha võib 🤪

Uuri **chatbot-workshop** kausta sisu. Peale äsja loodud .env failidele on kaustas veel mõned failid.

Lühidalt seletades:

.gitignore - versioonikontrolli programmi Git jaoks (ehk seda sul ei ole vaja veel osata)

poetry.lock ja pyproject.toml - need failid aitasid sul hõlpsalt laadida alla projektis vajaminevad teegid. Oluline on lihtsalt teada, et **nende muutmisel või eemaldamisel ei pruugi enam kood tööle minna**.

[README.md](http://README.md) - kausta sisu info fail. Kah pole praegu eriti oluline.

Nüüd ava **src** kaust. “src” on lühend sõnast “source” või “source code” ehk siin kaustas on kogu projektis olevad pythoni koodifailid. Selle kaustas juba olemasolevate failide kallal hakkadki selle kursuse jooksul tööle, et oma juturobot või õigemini tema teadmised ja oskused valmis meisterdada.

### 6. Hello, world!

<aside>
🎓 Lõpuks on kätte jõudnud see hetk, et äratada oma juturobot ellu!

</aside>

- Selleks ava uus terminali aken või kasuta juba avatud terminali.
- Veendu, et oled terminaliga kaustas ********************************src.******************************** Kui mitte, siis liigu eelnevalt mainitud käsuga sinna kausta.
- Jooksuta käsk (sellega saad ka hiljem käivitada oma rakendust):

```bash
poetry run python main.py
```

Sellise käsuga saad ka hiljem teisi selle projekti pythoni faile jooksutada, kui on vaja funktsioonide toimimist katsetada.

Nüüd võiksid näha terminali akna väljundi viimasel real tervitust oma juturobotilt!

Samuti kui vaatad oma discordi kanalisse, siis sinu bot kasutaja peaks olema “online”.

Kui mitte, siis kontakteeru juhendajaga!

### 6. Paneme juturoboti rääkima!

Kedagi ellu äratada on tore, aga mis kasu sellest on sinu robot rääkida ei oska.

Parandame selle probleemi kohe!

Ava ****************[main.py](http://main.py)** fail. Uurides faili lähemalt, näed, et antud programmis luuakse discordi “client” objekt koos talle antud õigustega, luuakse funktsioon nimega “on_ready” ja käivitatakse rakendus käsuga client.run(TOKEN) (kus antakse ka sisendiks juturoboti token).

Siinkohal on oluline aru saada sellest samast “on_ready” funktsioonist ning selle eripärasest süntaksist.

```python
@client.event
async def on_ready():
    print(f'Tere, maailm! Minu nimi on {client.user}.')
```

Antud funktsiooni kohal oleva **@client.event** tähisega määrame funktsiooni meie boti jaoks nö “event listener” funktsiooniks. See tähendab, et kui toimub mingi teatav sündmus, siis jooksutatakse antud funktsiooni. Funktsiooni “on_ready” jooksutav sündmus, nagu nimigi vihjab, on hetk kui meie programm on juturoboti ära seadistanud ja juturobot on valmis edasisi käske täitma.

Et robot rääkima saada, peame sarnaselt eelnevale funktsioonile looma funktsiooni, mis reageeriks kasutajate sõnumitele. Selleks on Discordi teegil olemas funktsioon nimega “on_message”, mis võtab parameetri nimega “message”, kus sisaldubki kasutaja saadetud sõnum. 

“message” on objekt (omamoodi sõnastik), mis sisaldab lisaks sõnumile endale ka muud kasulikku infot. Näiteks sõnumi autor, kuulatava kanali nimi ja serveri nimi. Et seda infot kasutada on vaja programmis lihtsalt nendele objekti atribuutidele viidata:

```python
message.author # sõnumi autor
message.author.name # sõnumi autori nimi
message.channel # sõnumi kanal
message.guild # server
message.content # sõnumi sisu
```

Erinevalt sõnastikule saab aga objektidel olla ka oma funktsioone, mida saab välja kutsuda.

Meile on kasulik sõnumi küljes oleva “channel” ehk kanali objekti küljes olev funktsioon “send”, millega saab sellesse kanalisse sõnumi saata. 

Ehk nii:

```python
await message.channel.send('Vastus')
```

Kindlasti märkasid ka viimases koodireas sõna “await”. See on antud funktsooni juures oluline, sest tegemist on asünkroonse ehk taustal toimuva funktsiooniga. Asünkroonseid funktsioone me sellel kursusel pikemalt ei käsitle, aga võta lihtsalt teadmiseks, et neid kasutatakse olukordades, kus mingi osa koodist võib võtta kaua aega või sõltub välistest teguritest (antud juhul Discordi serveritest) ning targem on seda osa teha taustal nii, et muu osa programmist jätkaks oma tööd.

Eelnevast infost võime kokku panna järgneva funktsiooni:

```python
@client.event
async def on_message(message):
    await message.channel.send('Tere, ' + message.author.name + '!')
```

**NB!** Selle programmi loogika juures aga on üks teatav probleem. Kas sa oled mõelnud, mis juhtub, kui meie bot ise saadab sõnumi kanalisse? Kas antud juhul saadab “on_message” uue sõnumi ja tekib lõpmatu tsükkel? Kui me selle küsimuse siin niimoodi tõstatasime, siis sa ilmselt tead juba vastust!

Probleemi saab lahendada, lisades funktsiooni algusesse kiire kontrolli:

```python
if message.author == client.user:
		return
```

Nii lõpetab funktsioon boti enda sõnumile reageerides töö enne, kui see jõuab hakkata pahandust tekitama.

Samuti võiksid lisada ka järgneva kontrolli, et bot reageeriks sõnumitele esialgu ainult sinu kanalis:

```python
if message.channel.name != "kanali-nimi":
    return
```

Nüüd aga peaks olema asi korras ning saad asuda katsetuse juurde! Pane oma juturobot sinu sõnumile vastama! (Pro tip: eelmist käsklust saad terminalis kasutada, kui vajutad peale terminali valimist “nool üles” klahvi).

Kui said sellega hakkama ja juturobot vastas peale seda kui olid oma kanalisse sõnumi saatnud, siis on see osa töötoast sinu jaoks lõppenud!

Tubli töö! 🙌