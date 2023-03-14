from stroj import Stroj
import os
import time

#stroj1 = Stroj('stroj1', 0, 25, 40, [], [])

#stroj1.shrani_stanje(os.path.join('stroji', f'{stroj1.ime_stroja}.json'))

#testni_stroj = Stroj.nalozi_stanje(os.path.join('stroji', 'test.json'))

from datetime import datetime
now = datetime.now()
print(f'čas je {now.time()}')