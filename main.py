#simulacija temperatur strojev glede na vhodne podatke: cas_interval, min_parameter

import os
from stroj import Stroj, Meritev
from datetime import datetime
import time


def simulacija(cas_interval, min_parameter):
    #cas_interval = cas, ki ga opazujemo za simulacijo v desetinkah
    #min_parameter = idealna temperatura stroja

    #IZPIS IZ KONFIGURACIJSKIH DATOTEK
    stroji = []
    for ime_datoteke in os.listdir('stroji'):
        stroj = Stroj.nalozi_stanje(os.path.join('stroji', ime_datoteke))
        stroji.append(stroj)


    #SIMULACIJA
    for i in range(cas_interval):
        now = datetime.now()
        trenuten_cas = now.time()
        print(f'Trenuten cas je {trenuten_cas}')
        print('----------------------------------')
 
        for stroj in stroji:
            print(f'ime stroja: {stroj.ime_stroja}')
            print(f'stanje stroja: {stroj.stanje}')
            print(f'temperatura: {stroj.trenutna_temperatura}')

            #nastavimo ali je stroj prižgan ali ugasnjen
            stroj.nastavi_trenutno_stanje(trenuten_cas)
            print(f'novo stanje stroja: {stroj.stanje}')

            #za vse stroje sporocimo temperaturo in poracunamo naslednjo
            stroj.sporoci_temperaturo(trenuten_cas, min_parameter)
            print(f'nova temperatura: {stroj.trenutna_temperatura}')

            stroj.shrani_stanje(os.path.join('stroji', f'{stroj.ime_stroja}.json'))
            print(f'shranjujem stanje stroja {stroj.ime_stroja}')
            print('----------------------------------------')

        #notranja zanka potrbuje cca 0.003000 s
        d = 0.003

        #spremembe se dogajajo na desetinko
        time.sleep(0.100 - d)


simulacija(20, 10)