from verden import Verden

def hovedprogram():
    # Det er to variabler som bestemmes av brukeren, og de er parameter i Verden klassen.
    raderBrukeren=int(input("Skriv talle av rader:"))
    kolBrukeren=int(input("Skriv talle av kolonner:"))
    verdenBrukeren=Verden(raderBrukeren,kolBrukeren)
# Programmet oppretters sjøl til brukeren skal trykker 'q'.
#  Det kalles to metoden fra klassen Verden for å tegne og å oppdatere Celle-verden.q 

    teller=1
    while teller!=0:
         brukerenVilje=input("Hvis du trykker mellomrom, forsetter programmet// Hvis du trykker 'q', slutter programmet:")
         if brukerenVilje==" ":
            verdenBrukeren.tegn()
            verdenBrukeren.oppdatering()
         elif brukerenVilje.lower()=="q":
            teller=0
         else:
            print("Uvedkommende karakter")


# starte hovedprogrammet
hovedprogram()