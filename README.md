# Machines

The program simulates changes in machine temperatures. Each machine has a current temperature, an on/off state, a schedule specifying when it should be on, and a maximum temperature tolerance. The machines’ temperatures and states change according to the following rules:

* If the machine is **on**, its temperature:

  * increases by 1 every 0.1 seconds with a **probability of 0.5**,
  * decreases by 1 with a **probability of 0.4**, and
  * stays the same with a **probability of 0.1**.

* If the machine is **on** and its temperature **exceeds the tolerance**, it turns **off**.

* If the **current time** falls within the scheduled operation time but the machine is currently **off due to overheating**, it will **turn back on** as soon as the temperature drops below the tolerance.

* If the **current time is outside the scheduled operation period**, the machine remains **off regardless of temperature**.

* While the machine is **off**, its temperature decreases by 1 every **1 second**.

* The temperature **cannot drop below the ideal temperature** (minimum parameter). Once this temperature is reached, it does not decrease further.

The machine configurations are stored in JSON files inside the `stroji` folder. The `stroj.py` file contains two Python classes: `Stroj` and `Meritev`, which include all the functions needed to calculate the next temperature and state based on the current time and the machine’s current temperature.

The `main.py` file reads the configuration data from the JSON files and runs the temperature simulation for the machines. The simulated temperatures, along with their corresponding timestamps, are recorded **in the same JSON files** from which the configuration was originally loaded.

The `stroji` folder contains configuration files for five different machines:

* **stroj1**: On from 8:00–10:00 and 12:00–14:00; initial temperature is 41, which is above its tolerance (40).
* **stroj2**: Always off; initial temperature is 11. During simulation, the machine remains off, the temperature drops to 10, then stays constant.
* **stroj3**: Always on; initial temperature is 20.
* **stroj4**: On from 23:00–10:00; initial temperature is 15.
* **stroj5**: On from 15:00–12:00; initial temperature is 39.

You run the program using the `main.py` file.




-----------------------
# Stroji
Program simulira spreminjanje temperature strojev. Vsak stroj ima podano trenutno temperaturo, stanje prižgan/ugasnjen, cas, ko je prižgan in toleranco najvišje temperature. Temperatura strojev in stanje se spreminja po naslednjih pravilih:
- če je stroj prižgan se mu temperatura vsako desetinko sekunde poveča za 1 z verjetnostjo 0.5, zmanjša za 1 z verjetostjo 0.4 in ostane enaka z verjetnostjo 0.1
- če je stroj prižgan in temperatura preseže toleranco stroja se ta ugasne
- če trenuten čas ustreza obdobju, ko je stroj prižgan, vendar je trenutno stroj ugasnjen zaradi temperature nad toleranco, se ta prižge takoj ko temperatura pade pod toleranco
- če trenuten čas ne ustreza obdobju, ko je stroj v delovanju je stroj ves čas ugasnjen ne glede na temperaturo
- v času ko je stroj ugasnjen se stroju temperatura vsako sekundo zmanjša za 1
- ne glede na to ali je stroj prižgan ali ugasnjen se temperatura ne spusti pod idealno; ko stroj doseže idealno temperaturo (minimalni parameter) se ta ne manjša več

Konfiguracije strojev so zapisane v json datotekah in shranjene v mapi stroji. Program stroj.py vsebuje dva Pythonova razreda: Stroj in Meritev, ki vsebujeta vse funkcije za izračun naslednje temperature in stanja glede na trenuten čas in trenutno temperaturo stroja. V programu main.py izvedemo izpis podatkov iz konfiguracijskih datotek ter simulacijo zapisov temperatur strojev. Temperature strojev skupaj s časom v katerem so bile izmerjene se zapisujejo v iste json datoteke iz katerih smo prebrali podatke.

V mapi stroji so zapisane konfiguracije petih različnih strojev:
- stroj1: stroj je prižgan 8.00-10.00 in 12.00-14.00, zacetna temperatura je nastavljena na 41, kar je nad toleranco(40)
- stroj2: stroj je ves čas ugasnjen, začetna temperatura je nastavljena na 11; ob simulaciji stroj ostane ugasnjen, temperatura pa se niža do 10 in potem ostane enaka
- stroj3: stroj je ves čas prižgan, začetna temperatura je nastavljena na 20
- stroj4: stroj je prižgan 23.00 - 10.00, začetna temperatura je nastavljena na 15  
- stroj5: stroj je prižgan 15.00- 12.00, zacetna temperatura je 39

Program poženemo z datoteko main.py.
