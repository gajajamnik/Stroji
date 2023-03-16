#funkcije, ki se navezujejo na stroje

import json
from datetime import *
from datetime import timedelta
import random

class Stroj:
    def __init__(self, ime_stroja, trenutna_temperatura, toleranca, ure):
        self.ime_stroja = ime_stroja
        self.stanje = 0 #prizgan/ugasnjen (na zacetku nastavimo na ugasnjen, sicer z funkcijo nastavi_trenutno_stanje spremenimo na 1)
        self.trenutna_temperatura = trenutna_temperatura
        self.toleranca = toleranca
        self.ure = ure #seznam seznamov ur ob katerih je prižgan (ce je seznam prazen je vedno ugasnjen)
        self.meritve = [] #ko dodamo stroj je to prazen seznam

    def v_slovar(self):
        return {
            'ime_stroja': self.ime_stroja,
            'trenutna_temperatura': self.trenutna_temperatura,
            'toleranca': self.toleranca,
            'ure': self.ure,
            'meritve': [meritev.v_slovar() for meritev in self.meritve]
        }
    
    def shrani_stanje(self, ime_datoteke):
        with open(ime_datoteke, 'w') as datoteka:
            json.dump(self.v_slovar(), datoteka, ensure_ascii=False, indent=4)

    
    @classmethod
    def iz_slovarja(cls, slovar_stanja):
        ime_stroja = slovar_stanja['ime_stroja']
        trenutna_temperatura = slovar_stanja['trenutna_temperatura']
        toleranca = slovar_stanja['toleranca']
        ure = slovar_stanja['ure']
        self = cls(ime_stroja, trenutna_temperatura, toleranca, ure)
        for m in slovar_stanja['meritve']:
            self.meritve.append(Meritev.iz_slovarja(m))
        return self
        

    @classmethod
    def nalozi_stanje(cls, ime_datoteke):
        with open(ime_datoteke) as datoteka:
            slovar_stanja = json.load(datoteka)
            return Stroj.iz_slovarja(slovar_stanja)

    #glede na trenuten cas nastavi ali je stroj prizgan ali ugasnjen
    def nastavi_trenutno_stanje(self, trenuten_cas):
        #ce smo v casu delovanja in temperatura ne presega tolerance stroj prizgemo
        if self.cas_delovanja(trenuten_cas) and self.trenutna_temperatura <= self.toleranca:
            self.stanje = 1
        #sicer: čas del + nad toler ali ni čas delovanja (ne glede na toleranco) => zapremo
        else:
            self.stanje = 0
        
    #sporoci trenutno temperaturo stroja in poračuna naslednjo
    def sporoci_temperaturo(self, trenuten_cas, min_parameter):
        #temperatura, ki jo bomo sporočili
        temperatura = self.trenutna_temperatura 

        #stroj je prizgan
        if self.stanje:
            #vsako desetinko se temp poveca za 1 z verjet 0.5, zmanjsa za -1 z verj 0.4 in ostane enaka z verj 0.1
            t = random.choices([1, -1, 0], weights=[50, 40, 10])[0]
        #stroj je ugasnjen
        else:
            #vsako desetinko se temperatura zmanjsa za 0.1(vsako sekundo za 1)
            t = -0.1

        #ce temperatura doseže idealno se ne zgodi nič (ne glede na to a je ugasnjen ali prižgan)
        if temperatura + t <= min_parameter and t < 0:
            t = 0

        #nova temperatura
        self.trenutna_temperatura += t

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
            start = datetime.strptime(r[0], '%H:%M:%S.%f').time()
            end = datetime.strptime(r[1], '%H:%M:%S.%f').time()
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