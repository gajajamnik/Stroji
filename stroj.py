#funkcije, ki se navezujejo na stroje

import json
from datetime import *
from datetime import timedelta
import random

class Stroj:
    def __init__(self, ime_stroja, stanje, trenutna_temperatura, toleranca, ure):
        self.ime_stroja = ime_stroja
        self.stanje = stanje #prizgan/ugasnjen
        self.trenutna_temperatura = trenutna_temperatura
        self.toleranca = toleranca
        self.ure = ure #seznam seznamov ur ob katerih je prižgan (ce je seznam prazen je vedno ugasnjen)
        self.meritve = [] #ko dodamo stroj je to prazen seznam

    def v_slovar(self):
        return {
            'ime_stroja': self.ime_stroja,
            'stanje': self.stanje,
            'trenutna_temperatura': self.trenutna_temperatura,
            'toleranca': self.toleranca,
            'ure': self.ure,
            'meritve' : self.meritve.v_slovar()
        }
    
    def shrani_stanje(self, ime_datoteke):
        with open(ime_datoteke, 'w') as datoteka:
            json.dump(self.v_slovar(), datoteka, ensure_ascii=False, indent=4)

    
    @classmethod
    def iz_slovarja(cls, slovar_stanja):
        ime_stroja = slovar_stanja['ime_stroja']
        stanje = slovar_stanja['stanje']
        trenutna_temperatura = slovar_stanja['trenutna_temperatura']
        toleranca = slovar_stanja['toleranca']
        ure = slovar_stanja['ure']
        self = cls(ime_stroja, stanje, trenutna_temperatura, toleranca, ure)
        for m in slovar_stanja['meritve']:
            self.meritve.append(Meritev.iz_slovarja(m))
        return self
        

    @classmethod
    def nalozi_stanje(cls, ime_datoteke):
        with open(ime_datoteke) as datoteka:
            slovar_stanja = json.load(datoteka)
            return Stroj.iz_slovarja(slovar_stanja)
        
    #stroj je prižgan
    def sporoci_temperaturo(self, trenuten_cas, min_parameter):
        #temperatura, ki jo bomo sporočili
        temperatura = self.trenutna_temperatura 

        #stroj je prizgan
        if self.stanje:
            #poračuna novo temperatura (in ugasne stroj)
            t = random.choice([1, -1, 0], weights=[50, 40, 10])

        #stroj je ugasnjen
        else:
            #vsako sekundo se temperatura zmanjsa za 1
            t = -0.1

        #ce temperatura doseže idealno se ne zgodi nič
        if temperatura <= min_parameter and t == -1:
            t = 0

        #nova temperatura
        self.trenutna_temperatura += t

        #ce nova temperatura presega toleranco stroj ugasnemo
        if self.trenutna_temperatura > self.toleranca:
            self.stanje = 0

        #ce je stroj ugasnjen, a v casu delovanja in ne presega tolerance se prižge
        if self.cas_delovanja(trenuten_cas) and self.trenutna_temperatura <= self.toleranca:
            self.stanje = 1

        #belezimo novo meritev
        meritev = Meritev(trenuten_cas, temperatura)
        self.meritve.append(meritev)
    

    #vrne true ali false glede na to a je stroj v delovanju glede na trenuten čas
    def cas_delovanja(self, trenutni_cas):
        t = False
        #ce je stroj ves cas ugasnjen je seznam ur prazen
        if self.ure == []:
            return False
        for r in self.ure:
            start = r[0]
            end = r[1]
            #ce je stroj ves cas prizgan bo start = end in eden od naslednjih pogojev bo izpolnjen
            if start <= end and start <= trenutni_cas and trenutni_cas <= end:
                t = True
            elif end <= start and (start <= trenutni_cas or trenutni_cas <= end):
                t = True
        return t




class Meritev:
    def __init__(self, cas, temperatura):
        self.cas = cas
        self.temperatura = temperatura

    def v_slovar(self):
        return{
            'cas': self.cas.strftime('%H:%M:%S.%f'),
            'temperatura': self.temperatura
        }

    @classmethod
    def iz_slovarja(cls, slovar):
        cas = datetime.strptime(slovar['cas'], '%H:%M:%S.%f').time()
        temperatura = slovar['temperatura']
        self = cls(cas, temperatura)

        return self