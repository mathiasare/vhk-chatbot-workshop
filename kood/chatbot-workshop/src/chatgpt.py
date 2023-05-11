import os
import openai

OPENAI_KEY = os.getenv('OPENAI_KEY')
openai.api_key = OPENAI_KEY
openai.organization = "org-nyfQqCyXaWnevASZBYqd4JAf"

######################################################################

### abimaterjal: https://medium.com/geekculture/a-simple-guide-to-chatgpt-api-with-python-c147985ae28

def get_response_from_gpt(input:str) -> str:
    """ Funktsioon saadab ChatGPT-le päringu ja tagastab selle sobiva vastuse. """
    pass

######################################################################

def get_prompt(input:str) -> str:
    """ Abifunktsioon ChatGPT sisendi 'prompti' vormistamiseks. """
    pass


######################################################################
######## SIIA LISA ENDA TEHTUD ABIFUNKTSIOONID (KUI ON VAJA) #########