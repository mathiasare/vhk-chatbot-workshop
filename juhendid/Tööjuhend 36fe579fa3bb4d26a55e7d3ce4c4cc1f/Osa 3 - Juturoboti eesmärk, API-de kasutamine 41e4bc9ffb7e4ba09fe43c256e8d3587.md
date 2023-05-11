# Osa 3 - Juturoboti eesmärk, API-de kasutamine

<aside>
🎓 Selles osas tuleb sul välja mõelda oma juturoboti eesmärk! Selleks on vaja välja valida endale avalik API, millest saadud infot saab kasutajale kättesaadaval kujul edastada tema küsimustele vastates.

</aside>

### 1.  API valimine

Uuri järgnevate avalike API-de nimekirja: [https://mixedanalytics.com/blog/list-actually-free-open-no-auth-needed-apis/](https://mixedanalytics.com/blog/list-actually-free-open-no-auth-needed-apis/)

Teine sobiv nimekiri kategooriate järgi (vali nende seast kus on märgitud Auth = NO):

[The Public APIs List, a curated list for the public web Apis](https://apislist.com/)

Mida tähele panna sobiva API otsingul?

- Info võiks olla mitmekülgne ehk sellega saaks vastata mitmele erinevale küsimusele
- Üldjuhul väldi “suvaliste andmete” genereerijaid
- Pilte saatvad API-d on ka võimalik kasutada, aga vaata, et oleks ka mingit muud tekstilist infot päringu vastuses, mida saaks kasutajale kuvada.
- Võib ka valida mitu API-t kui tuleb mõni hea idee. Mitme API implementeerimine ei võta oluliselt kauem aega. Väga hea on kasutada mõne “sisukama” API kasutamise hõlpsustamiseks mõnda täiendavat API-t.
    
    Näide:
    
    Ilma ennustamise API jaoks on vaja asukoha kordinaate, samas kasutaja ei tea peast asukohtade kordinaate ning neid on tüütu ise otsida.
    
    Lahendus: 
    
    Kasutaja küsib asukohapõhist ilma, näiteks “Mis ilm on praegu Tartus?” → [Nominatum](https://nominatim.org/release-docs/latest/api/Overview/) API pakub asukohale (Tartu) vastavad kordinaadid → Programm kasutab saadud kordinaate, et pärida ilma vastavalt API-lt. 
    

Küsi julgesti juhendajalt, kui peaks küsimusi tekkima või oleks tarvis soovitusi.

Minu isiklikud lemmikud:

- Quote Garden - Kuulsate tsitaatide andmebaas
- [Nominatum](https://nominatim.org/release-docs/latest/api/Overview/)  - Asukohad ja aadressid
- Open Meteo - Ilma info
- [Ball Dont Lie](https://www.balldontlie.io/) - NBA mängijate info
- [Open Library](https://openlibrary.org/developers/api) - Raamatute info

<aside>
🤔 NB! Kõige praktilisem viis aru saada, et millist infot tegelikult mõni API pakub on teha päring. Päringute tegemiseks tee läbi selle osa ülesanne 2. Võid alati ülesande 1 juurde pärast tagasi pöörduda.

</aside>

### 2.  Päringute tegemine

Päringute tegemiseks on vaja sellist tööriista nagu REST client. Sisuliselt on tegemist programmiga, mis oskab suhelda API endpointidega (juhul kui nad kasutavad REST arhitektuuri ja HTTP(s) protokolli).

- Selleks lisa endale Thunder Client laiendus (extention) VS Codiumis.
- Vali vasakult menüüst Thunder Client -i kasutajaliides
- Vormista päring kasutajaliideses ja vajuta “Send”

Päringu vormistamisel on olulised paar järgnevat asja:

**Päringu meetod:** 

REST arhitektuur lubab üldjuhul kasutada 5 päringu meetodit (GET, POST, UPDATE, PATCH, DELETE).

Siin kursusel läheb sul üldiselt vaja **GET** meetodit, mis ongi mõeldud info saamiseks API-lt.

**API url ehk aadress:** aadress, mille poole pöördutakse, et infot pärida.

**Aadressi muutujad (Path variables): Päringu aadressile järgnevad muutujad, enamasti täisarvud.**

Nende puhul ei kasutata muutuja nime ehk järjekord on oluline.

**Päringu parameetrid (Query parameters):** Päringu aadressile järgnevad parameetrid koos väärtusega. Nende puhul pole järjekorral vahet.

Kokkuvõttes:

![Untitled](Osa%203%20-%20Juturoboti%20eesma%CC%88rk,%20API-de%20kasutamine%2041e4bc9ffb7e4ba09fe43c256e8d3587/Untitled.png)

Päringu vastuse saad üldjuhul, kas JSON või XML formaadis. Neid õpime peagi Pythoniga sisse lugema ja töötlema.

Päringu vastusega tuleb kaasa ka päringu staatuse arv. See annab märku, kas päring oli edukas või läks midagi valesti.

**Kiire spikker:**

- 200 - OK
- 400 - Päringu viga, ilmselt tegid midagi valesti.
    - 401 - Unauthorized - ehk pead sisse logima kusagile
    - 403 - Forbidden - sa arvatavasti ei peaks selle URLi pihta isegi pärgingut tegema või praegust REST meetodit kasutama
    - 404 - Not found - Sellist aadressi ei eksisteeri (või pole antud REST meetodit kasutusel)
    - 405 - I’m a teapot! - Oled teepott, mis parata…
- 500 - Serveri viga - Sina tegid kõik õigesti, aga serveri poolel on asjad jamasti 🤯

### 3.  Eesmärgi seadmine ja dokumenteerimine

Nüüd kui plaan on enam-vähem paigas mine uuesti [Discord Developer Portal](https://discord.com/developers/) lehele ja muuda oma juturoboti nimi selliseks, et oleks aru saada, mis valdkonnaga tal pistmist on. Samuti lisa väike kokkuvõtte äppi kirjeldusse (Description väli).

Samuti võiksid rääkida korra oma plaanist mulle (kui sa seda juba teinud pole), et saaksin kinnitada, et see on päriselt ka tehtav ja võib-olla mõne soovituse anda.

Kui see on tehtud siis mine juhendi järgmise osa juurde. Hea töö! Keep it up!! 💪