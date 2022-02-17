#

#https://www.trenord.it/rest/cta/tariff?id=79

from time import sleep
import requests
from dhooks import Webhook

hook = Webhook('webhook_url')


def monitor():
    hook.send("Aprica monitor started")
    r = requests.get('https://www.trenord.it/rest/cta/tariff?id=79')

    while (int(r.status_code) == 200):
        try:
            r = requests.get('https://www.trenord.it/rest/cta/tariff?id=79')

            hook.send("Aprica life back in stock\nSTOCK => " + str(r.json()['units']))
        
            sleep(1800)
        except:
            hook.send('ERROR')

    
    hook.send("Aprica monitor stopped")


monitor()
