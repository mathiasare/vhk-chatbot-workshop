import os
from estnltk import Text
from chatgpt import *
from api import *

CONFIDENCE_PREFIX = "*"
RESPONSE_PREFIX = "$"
KEY_WORDS = []

######################################################################

def parse_message(message:str) -> Text:
    """ Funktsioon kasutaja sõnumi töötlemiseks. """
    return message

######################################################################

def get_confidence_rating(message:str) -> int:
    """ Funktsioon tagastab asjakohasuse hinnangu vahemikus 0-100 (0 ja 100 kaasaarvatud). \n
        Suurem number tähendab suuremat asjakohasust.
    """
    return 0

######################################################################

def get_response(message:str) -> str:
    """ Funktsioon kasutaja sõnumile vastamiseks. Otsustab vastavalt kasutaja sisendile, mida teha tuleks. """
    confidence = get_confidence_rating(message)

    if confidence == 100:
        return "Oled ikka enesekindel!"
    else:
        return "Ma jään kahjuks vastuse võlgu. Ciao!"
    
######################################################################

def decide_action(message:str):
    """ Funktsioon otsustab kasutaja sisendile reageerimiseks järgmiste tegevuste vahel:
        1. asjakohasuse hinnangu saatmine
        2. kasutaja päringule vastamine
        3. sõnumile vastamata jätmine
    """
    pass

######################################################################

######## SIIA LISA ENDA TEHTUD ABIFUNKTSIOONID (KUI ON VAJA) #########