from random import randint
from celle import Celle

class Rutenett:
    # i kostruktøren er det to parameter og tre instansvariabler
    def __init__(self, rader, kolonner):
        self._ant_rader=rader
        self._ant_kolonner=kolonner
        self._rutenett=self._lag_tomt_rutenett()
# i metoden et det en liste som lages None-verdier.
    def _lag_tom_rad(self):
        raderListe=[]
        for teller in range(self._ant_kolonner):
            raderListe.append(None)
        return raderListe
# der rader settes i en ytreListe.
    def _lag_tomt_rutenett(self):
        ytreListe=[]
        for teller in range(self._ant_rader):
            ytreListe.append(self._lag_tom_rad())
        return ytreListe


    def fyll_med_tilfeldige_celler(self):
        for radTeller in range(self._ant_rader):
            for kolTeller  in range(self._ant_kolonner):
                self.lag_celle(radTeller,kolTeller)

    def lag_celle(self, rad, kol):
        celle1=Celle()
        random=randint(0,2)
        if random==0:
            celle1.sett_levende()
        self._rutenett[rad][kol]=celle1


        
# det finnes celles koordinater og returneres cellen til den gitte posisjonen.
    def hent_celle(self, rad, kol):
        if rad in range(self._ant_rader) and kol in range(self._ant_kolonner):
            return self._rutenett[rad][kol]
        else:
            return None

# i denne metoden skal det vises rutenett.
    def tegn_rutenett(self):
        for radTeller1 in self._rutenett:
            for kolTeller1 in radTeller1:
                print(kolTeller1.hent_status_tegn(),end="")
            print("")
            
        
# det vurderes sannsynlig alle naboene til en celle
    def _sett_naboer(self, rad, kol):
        celle2=self.hent_celle(rad,kol)
        if self.hent_celle(rad-1,kol-1) is not None:
            celle2.legg_til_nabo(self.hent_celle(rad-1,kol-1))
        if self.hent_celle(rad-1,kol) is not None:
            celle2.legg_til_nabo(self.hent_celle(rad-1,kol))
        if self.hent_celle(rad-1,kol+1) is not None:
            celle2.legg_til_nabo(self.hent_celle(rad-1,kol+1))
        if self.hent_celle(rad,kol+1) is not None:
            celle2.legg_til_nabo(self.hent_celle(rad,kol+1))
        if self.hent_celle(rad+1,kol+1) is not None:
            celle2.legg_til_nabo(self.hent_celle(rad+1,kol+1))
        if self.hent_celle(rad+1,kol) is not None:
            celle2.legg_til_nabo(self.hent_celle(rad+1,kol))
        if self.hent_celle(rad+1,kol-1) is not None:
            celle2.legg_til_nabo(self.hent_celle(rad+1,kol-1))

        if self.hent_celle(rad,kol-1) is not None:
            celle2.legg_til_nabo(self.hent_celle(rad,kol-1))



# det kobles naboer
    def koble_celler(self):
        for radTeller2 in range(self._ant_rader):
            for kolTeller2 in range(self._ant_kolonner):
                self._sett_naboer(radTeller2,kolTeller2)
# alle celles tas inn i en liste
    def hent_alle_celler(self):
        celleList=[]
        for rader in self._rutenett:
            for kolonner in rader:
                celleList.append(kolonner)
        return celleList
#  det telles antall_levende celler
    def antall_levende(self):
        antallLevende=0
        for rader in self._rutenett:
            for kolonner in rader:
                if kolonner.er_levende():
                    antallLevende+=1
        return antallLevende
