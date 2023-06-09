# Osa 6 - ChatGPT ja väljundi loomine

<aside>
💡 Nüüd lähme viimaks selle tõeliselt lõbusa osa juurde! Kasutame ChatGPT-d et teha API päringuga tagastatud vastus inimesele paremini loetavaks.

</aside>

### 1. Küsi juhendajalt ChatGPT võti

Salvesta see .env failis sisalduva OPENAI_KEY muutujasse.

### 2. Valmista ette ChatGPT-le saadetav sisend

Selleks täienda [chatgpt.py](http://chatgpt.py) failis olevat **get_prompt()** funktsiooni. Antud funktsioon peaks tagastama sõne, mis sisaldab kogu ChatGPT-le antavat tööjuhendit, kasutaja küsimust ja API päringust saadud vastust.

Eduka “prompti” näide:

---

<aside>
🧠 Please answer my question based on the JSON response of the

open-meteo weather forecast API provided below. Assume the API response is about the location user asked about. If my question is not about current weather or weather forecast in general please respond with 'Vabandust! Ma ei oska sellele küsimusele vastata.'

My question: { question }

Open-meteo API response: { response }

Please answer my question in Estonian language!

</aside>

---

<aside>
‼️ Sisendi katsetamiseks kasuta ChatGPT veebilehte: [https://chat.openai.com/](https://chat.openai.com/)

Kindlasti ära esialgseks katsetamiseks kasuta praegust programmi ja OpenAPI tokenit. See kulutab asjata selle töötoa jaoks antud päringute limiiti.

</aside>

### 3. Tokenite arv

Tee valmis meetod get_token_count(), mis tagastab gpt-le saadetava promptis leiduva tokenite arvu. Selleks võid kasutada juba varem valmis tehtud funktsiooni get_words().

### 4. Uuri OpenAI teegi kasutamist ja tee päring

Uuri seda juhendit: [https://medium.com/geekculture/a-simple-guide-to-chatgpt-api-with-python-c147985ae28](https://medium.com/geekculture/a-simple-guide-to-chatgpt-api-with-python-c147985ae28)

Täienda meetodit ****************get_response_from_gpt()**************** mis kasutab get_prompt() funkstiooni tagastust, et saata GPT mudelile juhised ning tagastab GPT-lt saadud vastuse.

<aside>
⚠️ NB! Funktsioonis peab olema kontroll, et ei saadetaks korraga rohkem kui 2000 tokenit! Muidu saab kasutaja rahaline limiit liiga ruttu täis.

</aside>

Kui tokenite arv tuleb lubatust suurem, siis on vaja prompti ja arvatavasti API päringu tagastuse pikkust vähendada. Küsi selleks vajadusel juhendaja abi!

### 5. Viimistle kogu loogikat ja tee juturobot valmis

Muuda juturoboti loogikat nii, et API päringu vastuse asemel vastatakse kasutaja küsimusele ChatGPT-lt saadud vastusega.

Viimistle vajadusel kogu rakenduse toimimise loogikat, et kasutaja küsimused saaksid võimalikult hästi vastatud.

<aside>
🥳 Ja ongi selleks korraks kõik!! Või kas on ikka…

</aside>