
# requests teek päringute tegemiseks
# requests teegi kohta saab uurida siit: https://docs.python-requests.org/en/latest/index.html
import requests

API_URL = "" # Siia lisa oma valitud API aadress/url.

######################################################

def get_api_response(): # Siia lisa ka vajalikud päringu parameetrid
    """ Funktsioon enda valitud API päringu tegemiseks ja saadud vastuse tagastamiseks """

    res = requests.get(API_URL + "/somePathVariable", params = {
        "someQueryParam" : "someValue"
    })

    data = None
    if res.ok:
        data = res.json() # võtame vastusest JSON objekti - tegelikult on see sõnastik! Prindi kusagil funktsiooni väljund välja ja uuri seda.
    else:
        print(f'Staatus: {res.status_code}, Põhjus: {res.reason}')
    
    return data
    

# print(get_api_response()) # Testida võid jooksutades seda sama faili koos print käsuga (hiljem eemalda see rida)

######################################################
# SIIA LISA TEISTE PÄRINGUTE TEGEMISE FUNKTSIOONID 
# KUI SOOVID MITUT ERINEVAT KASUTADA #