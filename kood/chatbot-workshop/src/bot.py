import os
from estnltk import Text
from chatgpt import *
from api import *

CONFIDENCE_PREFIX = "*"
RESPONSE_PREFIX = "$"
KEY_WORDS_TABLE = {
    "ilm": 70,
    "temperatuur": 40,
    "soe" : 15,
    "külm" : 15
}

######################################################################

def get_lemmas(message:str):
    """ Funktsioon kasutaja sõnumi töötlemiseks ja "lemmade" tagastamiseks.
    """
    text = Text(message)
    text.tag_layer()

    return [sublist[0] for sublist in text.lemma]


######################################################################

def get_confidence_rating(message:str) -> int:
    """ Funktsioon tagastab asjakohasuse hinnangu vahemikus 0-100 (0 ja 100 kaasaarvatud). \n
        Suurem number tähendab suuremat asjakohasust.
    """
    confidence = 0
    lemmas = get_lemmas(message)

    for word in KEY_WORDS_TABLE.keys():
        if word in lemmas:
            confidence += KEY_WORDS_TABLE[word]

    return min(100, confidence)

######################################################################

def get_response(message:str) -> str:
    """ Funktsioon kasutaja sõnumile vastamiseks. Otsustab vastavalt kasutaja sisendile, mida teha tuleks. """
    location = get_location(message)
    print(location)
    api_res = get_api_response(location)
    if api_res == None:
        return "Unable to get data from API"
    res = get_response_from_gpt(api_res, message)
    return res
    

    
######################################################################

def decide_action(message:str):
    """ Funktsioon otsustab kasutaja sisendile reageerimiseks järgmiste tegevuste vahel:
        1. asjakohasuse hinnangu saatmine
        2. kasutaja päringule vastamine
        3. sõnumile vastamata jätmine
    """
    confidence = get_confidence_rating(message)

    if message[0] == CONFIDENCE_PREFIX:
        print(confidence)
        return confidence

    if message[0] != RESPONSE_PREFIX:
        return ""
    
    if confidence > 50:
        return get_response(message[1:])
    else:
        return "Ma jään kahjuks vastuse võlgu!"

######################################################################

######## SIIA LISA ENDA TEHTUD ABIFUNKTSIOONID (KUI ON VAJA) #########

def get_location(message:str):
    text = Text(message)
    text.tag_layer('ner')
    return [row.lemma for row in text.ner if row.nertag == 'LOC'][0][0][0]


def get_time(message:str):
    text = Text(message)
    text.tag_layer('timexes')
    return [(row.text, row.value) for row in text.timexes][0][1]


def get_person(message:str):
    text = Text(message)
    text.tag_layer('ner')
    return [row.enclosing_text for row in text.ner if row.nertag == 'PER'][0]    


######################################################################