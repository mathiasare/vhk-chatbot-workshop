
# requests teek päringute tegemiseks
# requests teegi kohta saab uurida siit: https://docs.python-requests.org/en/latest/index.html
import requests

WEATHER_API_URL = "https://api.open-meteo.com/v1/forecast?" # Siia lisa oma valitud API aadress/url.
LOCATION_API_URL = "https://nominatim.openstreetmap.org/search.php"

######################################################

def get_api_response(location:str): # Siia lisa ka vajalikud päringu parameetrid
    """ Funktsioon enda valitud API päringu tegemiseks ja saadud vastuse tagastamiseks """
    coords =  get_coordinates(location)
    if (coords == None):
        return None
    (lat, lon) = coords
    res = get_weather_response(lat, lon)
    return f'Weather in {location}: \n {res}'

#print(get_api_response()) # Testida võid jooksutades seda sama faili koos print käsuga (hiljem eemalda see rida)

######################################################
# SIIA LISA TEISTE PÄRINGUTE TEGEMISE FUNKTSIOONID 
# KUI SOOVID MITUT ERINEVAT KASUTADA #

def get_coordinates(location:str):
    res = requests.get(LOCATION_API_URL,params= {
        "q": location,
        "format": "jsonv2"
    }).json()

    if len(res) == 0:
        print("Ei leidnud kordinaate!")
        return None
    coords = (res[0]["lat"], res[0]["lon"])
    print(coords)
    return coords


def get_weather_response(lat, lon):
    res = requests.get(WEATHER_API_URL,params= {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True,
        "hourly": "temperature_2m,relativehumidity_2m"
    }).json()
    return res