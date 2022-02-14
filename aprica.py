#https://discord.com/api/webhooks/941441827104506026/8l60_KxXE2WeEcjuNThZ0ydYEq-4ctfEsFbIuiI8evGhlFOOrhVMITM0VsMd1XRe7De2

#https://www.trenord.it/rest/cta/tariff?id=79

from time import sleep
import requests
from dhooks import Webhook

hook = Webhook('https://discord.com/api/webhooks/941441827104506026/8l60_KxXE2WeEcjuNThZ0ydYEq-4ctfEsFbIuiI8evGhlFOOrhVMITM0VsMd1XRe7De2')


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