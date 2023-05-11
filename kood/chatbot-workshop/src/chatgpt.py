import os
import openai
from dotenv import load_dotenv

load_dotenv()
OPENAI_KEY = os.getenv('OPENAI_KEY')

openai.organization = "org-nyfQqCyXaWnevASZBYqd4JAf"
openai.api_key = OPENAI_KEY

######################################################################

### abimaterjal: https://medium.com/geekculture/a-simple-guide-to-chatgpt-api-with-python-c147985ae28

def get_response_from_gpt(content:str, question:str) -> str:
    """ Funktsioon saadab ChatGPT-le päringu ja tagastab selle sobiva vastuse. """
    messages = [{"role": "system", "content" : "You’re a kind helpful weather forcast presenting assistant"}]
    content = get_prompt(content, question)
    messages.append({"role": "user", "content": content})

    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
    )

    chat_response = completion.choices[0].message.content
    if chat_response == None:
        return ""
    return chat_response
    

######################################################################

def get_prompt(content:str, question:str) -> str:
    """ Abifunktsioon ChatGPT sisendi 'prompti' vormistamiseks. """
    return f"""
        Please answer my question based on the JSON response of the 
        open-meteo weather forecast API provided below. Assume the API response is about the location user asked about. If my question is 
        not about current weather or weather forecast in general 'Vabandust! Ma ei oska sellele küsimusele vastata.'

        My question: {question}

        Open-meteo API response: { content }

        Please answer my question in Estonian language!
    """


######################################################################
######## SIIA LISA ENDA TEHTUD ABIFUNKTSIOONID (KUI ON VAJA) #########