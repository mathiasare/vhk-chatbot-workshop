# Osa 1 - Juturoboti seadistamine

<aside>
🎓 Selles osas seadistame uue Discordi Bot kasutaja kursuse jutukanalisse, et seda hiljem juturobotina kasutada. Et seadistada Discordi juturobotit peame tegema läbi järgmised sammud:

</aside>

### 1. Loo uus rakendus Discordi arendaja portaalis

- Ava arendaja portaal brauseris: [Discord Developer Portal — My Applications](https://discord.com/developers/applications)
- Vali “New Application” paremast nurgast
    
    ![Untitled](Osa%201%20-%20Juturoboti%20seadistamine%203b8e217ce85b4b8fa8cd3e5938642dda/Untitled.png)
    
- Loo endale uus Juturoboti Äpp
    - Vali robotile nimi - esialgu pane nimeks enda eesnimi (omastavas) ja “Bot”. Näiteks “Mathiase Bot”. Hiljem muudame nime ja lisame kirjelduse, kui Boti otstarve on teada.
    - Lisa mingi tore ikoon
    - Kõik muu jäta praegu tühjaks
    - Kopeeri endale APPLICATION ID ja PUBLIC KEY ja salvesta kusagile kättesaadavasse kohta (Notepadi näiteks)
    
    ![Untitled](Osa%201%20-%20Juturoboti%20seadistamine%203b8e217ce85b4b8fa8cd3e5938642dda/Untitled%201.png)
    
- Loo uus Bot kasutaja
    - Liigu alamlehele “Bot”
    - Kopeeri boti TOKEN ka kättesaadavasse kohta. Seda ei saa hiljem uuesti vaadata!
    - Eemalda valik “Public Bot” sektsioonist. See takistab teistel sinu boti kasutamast.
    - Lisa valik “Message Content Intent”. See annab botile loa kasutajate sõnumi sisu näha.
    - Seaded võiks jääda nii:
    
    ![Untitled](Osa%201%20-%20Juturoboti%20seadistamine%203b8e217ce85b4b8fa8cd3e5938642dda/Untitled%202.png)
    
    - Vali kõik õigused TEXT PERMISSIONS kategooriast  ja “Read Messages/View Channels” GENERAL kategooriast. Teised õigused jäta valimata. Kopeeri alt “Permissions Integer”, et pärast kiiremini õigused lisada.
    
    ![Untitled](Osa%201%20-%20Juturoboti%20seadistamine%203b8e217ce85b4b8fa8cd3e5938642dda/Untitled%203.png)
    

### 2. Lisa boti kasutaja serverisse

- Liigu lehele
    
    https://discordapp.com/oauth2/authorize?&client_id=CLIENTID&scope=bot&permissions=PERMISSIONS_INTEGER
    
    kus CLIENT_ID on sinu boti client id ehk varem salvestatud application id.
    
    ja PERMISSIONS_INTEGER on varem salvestatud õiguste number
    

- Vali serveriks “VHK Inseneeria Laager”

### 3. Lisa bot enda jutukanalisse

- Loo endale uus privaatne tekstikanal
    - Vali vasakult serveri tekstikanalite loendist “+” märgi alt “Create channel”
    - Vali kanalile nimi, kuidas ise soovid
    - Vali “Private Channel”
    - Vali liikmete alt enda juturoboti kasutaja
    - Hiljem saad ka lisada siia teisi, et enda robotit neile näidata.

<aside>
🎓 Nüüd kui sinu juturobot on serverisse lisatud, saame proovida kuidas temaga suhtlemine täpsemalt käib. Selleks liigu järgmise juhendi juurde “Osa 2  - programmeerimiskeskonna ettevalmistamine ja esimesed katsetused”.

</aside>