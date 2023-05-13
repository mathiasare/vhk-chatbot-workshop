import os
from chatgpt import *
from api import *
import nltk

nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")


CONFIDENCE_PREFIX = "*"
RESPONSE_PREFIX = "$"
KEY_WORDS = []

######################################################################
#NLTK abimeetodid

def get_tokens(message):
    """ Funktsioon tokenite ehk sõnade tagastamiseks """
    return

def get_lemmas(tokens):
    """ Funktsioon kasutaja sõnumist lemmade järjendi tagastamiseks """
    return

def get_location(tokens) -> str:
    """ Funktsioon kasutaja sõnumist asukoha tagastamiseks """
    return

def get_time(tokens) -> str:
    """ Funktsioon kasutaja sõnumist aja tagastamiseks """
    return

def get_person(tokens) -> str:
    """ Funktsioon kasutaja sõnumist isiku nime tagastamiseks """
    return

######################################################################

def get_confidence_rating(lemmas) -> int:
    """ Funktsioon tagastab asjakohasuse hinnangu vahemikus 0-100 (0 ja 100 kaasaarvatud). \n
        Suurem number tähendab suuremat asjakohasust.
    """
    return 0

######################################################################

def get_response(question, lemmas) -> str:
    """ Funktsioon kasutaja sõnumile vastamiseks. Otsustab vastavalt kasutaja sisendile, mida teha tuleks. """
    confidence = get_confidence_rating(lemmas)

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
