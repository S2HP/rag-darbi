import requests
import os
from bs4 import BeautifulSoup as bs
import csv
import time



URL = "https://ss.lv/lv/transport/cars/today-5/sell/"
LAPAS = "lapas/"
DATI = "dati/"

def saglaba(url, datne):
    rezultats = requests.get(url)
    print(rezultats.status_code)
    if rezultats.status_code == 200:
        with open(datne, "w", encoding="utf-8") as f:
            f.write(rezultats.text)
    return


saglaba(URL, LAPAS+"pirma.html")


def dabut_info(datne):
    dati = []
    with open(datne, "r", encoding="utf-8") as f:
        html = f.read()

    zupa = bs(html, 'html.parser')