class Celle:
    # Konstruktør som har tre instansvariabler.
    def __init__(self):
        self._status="doed"
        self._naboer=[]
        self._ant_levende_naboer=0
        
    # det lages to metoder for de to status slik levende og doed
    def sett_doed(self):
        self._status="doed"
        # return self._status
        

    def sett_levende(self):
        self._status="levende"
        # return self._status

        
#  det er en method som har en parameter som legges til i listen_naboer
    def legg_til_nabo(self, nabo):
        self._naboer.append(nabo)
        return self._naboer
# Her returneres celles status hvis cellen er levende returneres True ellers False.
    def er_levende(self):
        if self._status=="levende":
            return True
        else:
            return False
        
# Her returneres celles status iallefall
    def hent_status(self):
        return self._status
        
# i denne metoden returneres "O" dersom statusen er levende ellers returneres ".".
    def hent_status_tegn(self):
        if self._status=="levende":
            return "O"
        else:
            return "."
        
# her sjekkes alle naboer, og telles antall levende naboer
    def tell_levende_naboer(self):
       self._ant_levende_naboer=0
       for teller in self._naboer:
              if teller.er_levende():
                  self._ant_levende_naboer+=1
              else:
                  self._ant_levende_naboer=self._ant_levende_naboer
        
       return self._ant_levende_naboer

        
    
    def oppdater_status(self):
      if  self._status=="doed":
         if self._ant_levende_naboer== 3:
            self.sett_levende()
      else:
          if self._ant_levende_naboer < 2 or self._ant_levende_naboer > 3:
              self.sett_doed()
          else:
               self.sett_levende()