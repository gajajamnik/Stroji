import os
from stroj import Stroj, Meritev
from datetime import datetime
import time

#seznam vseh strojev
stroji = []

for ime_datoteke in os.listdir('stroji'):
    stroj = Stroj.nalozi_stanje(os.path.join('stroji', ime_datoteke))
    stroji.append(stroj)


#časovni interval, ki nas zanima v desetinkah
for i in range(20):
    now = datetime.now()
    trenuten_cas = now.time()

    #za vse stroje sporocimo temperaturo in poracunamo naslednjo
    for stroj in stroji:
        min_parameter = 10
        stroj.sporoci_temperaturo(trenuten_cas, min_parameter)

    stroj.shrani_stanje(os.path.join('stroji', f'{stroj.ime_stroja}.json'))

    #spremembe se dogajajo na desetinko
    time.sleep(0.100)

