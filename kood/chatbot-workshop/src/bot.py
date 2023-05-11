import os
from estnltk import Text
from chatgpt import *
from api import *
from typing import List

CONFIDENCE_PREFIX = "*"
RESPONSE_PREFIX = "$"
KEY_WORDS = []

######################################################################
#ESTNLTK abimeetodid

def get_text(message:str) -> Text:
    """ Funktsioon ESTNLTK töödeldud Text objekti tagastamiseks """
    return

def get_words(message:Text) -> List[str]:
    """ Funktsioon kasutaja sõnumist kõikide sõnade tagastamiseks"""

def get_lemmas(message:Text) -> List[str]:
    """ Funktsioon kasutaja sõnumist lemmade järjendi tagastamiseks """
    return

def get_location(message:Text) -> str:
    """ Funktsioon kasutaja sõnumist asukoha tagastamiseks """
    return

def get_time(message:Text) -> str:
    """ Funktsioon kasutaja sõnumist aja tagastamiseks """
    return

def get_person(message:Text) -> str:
    """ Funktsioon kasutaja sõnumist isiku nime tagastamiseks """
    return

######################################################################

def get_confidence_rating(message:Text) -> int:
    """ Funktsioon tagastab asjakohasuse hinnangu vahemikus 0-100 (0 ja 100 kaasaarvatud). \n
        Suurem number tähendab suuremat asjakohasust.
    """
    return 0

######################################################################

def get_response(question:str, message:Text) -> str:
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