from rutenett import Rutenett

class Verden:
    # det er en kostruktøren som har to parameter, og fire instansvariabler.
    def __init__(self, rader, kolonner):
        self._generasjonsnummer=0
        self._rutenett=Rutenett(rader,kolonner)
        self._rutenett.fyll_med_tilfeldige_celler()
        self._rutenett.koble_celler()
# det kalles tegn_rutenett metoden fra Rutenett Klassen, og vises antall_levende celler og generasjonnummer
    def tegn(self):
            
            self._rutenett.tegn_rutenett()
            print("GenerasjonNummer: ",self._generasjonsnummer)
            print("LevendeCeller: ",self._rutenett.antall_levende())
# Det kalles levende naboer, og oppdater status.
    def oppdatering(self):
        allCeller=self._rutenett.hent_alle_celler()
        for teller in allCeller:
           teller.tell_levende_naboer()
           teller.oppdater_status()
           
           
        self._generasjonsnummer+=1
        
           
           



