# Osa 5 - Rakenduse loogika, API kasutamine vastavalt sisendile

<aside>
🎓 Selles osas teed valmis suurema osa oma juturoboti rakenduse “äriloogikast”. Vaja on panna juturobot reageerima õigesti kasutaja sisendile. Samuti kasutame “requests” teeki, et koostada kasutaja sisendile vastav API päring.

</aside>

## 1. Tegevuse valimine

Tee valmis funktsioon **************************decide_action************************** (bot.py) ****************************************************vastavalt tema päises esitatud kirjeldusele:

```python
def decide_action(message:str):
    """ Funktsioon otsustab kasutaja sisendile reageerimiseks järgmiste tegevuste vahel:
        1. asjakohasuse hinnangu saatmine - kui kasutaja sisendi esimene sümbol == CONFIDENCE_PREFIX
        2. kasutaja päringule vastamine - kui kasutaja sisendi esimene sümbol == RESPONSE_PREFIX
            - Sellisel juhul tagasta meetodi get_response() väljund aga ainult siis kui asjakohasuse hinnang > 50
        3. sõnumile vastamata jätmine
    """
```

## 2. Vastuse tagastamine

Tee valmis funktsioon get_response().

Selle väljund võiks olla [api.py](http://api.py) failis leiduv **********************get_api_response()********************** tagastus (mille juurde alles jõuame).

Samuti võiks selles meetodis lugeda muutujatesse kõik kasutaja sisendist välja loetud API päringuks vajalikud parameetrid (kasuta get_location(), get_person(), get_time() ja enda tehtud abifunktsioone). Lisa need muutujad **get_api_response** funktsiooni parameetriteks.

## 3. API päringu tegemine

Et aega säästa on sulle antud **********get_api_response()********** juba pooleldi valmis kujul.

Siin on kasutatud requests teeki, et teha juba varem mainitud GET päring.

Täienda seda funktsiooni nii, et see teeks sinu valitud API pihta õige päringu,

Vajadusel loo sarnase kujuga abimeetodeid, kui sul oli plaan kasutada mitut API otspunkti.

## 4. Juturoboti kasutamine

Viimaseks täienda [main.py](http://main.py) failis juba varem loodud **on_message()** funktsiooni, et see saadaks **************************************decide_action()************************************** funktsiooniga tagastatud väljundi.

Proovi nüüd juturobotiga suhelda läbi erinevate sõnumite oma Discordi kanalis.

Juturobot võiks reageerida vastusega ainult siis, kui sõnumi esimene sümbol on “*” või “$”.

Samuti peaks juturobot vastama API päringust saadud vastusega ainult siis, kui su küsimus oli piisavalt asjakohane.

Kui kõik töötas ilusti siis patsuta endale õlale! Sinu juturobot on peaaegu valmis! 💥