from datetime import datetime
from datetime import date 


def currentlytime ():
    print("today:", datetime.today())
    print("now:", datetime.now())
    print("utcnow:", datetime.utcnow())


def naptime ():
    print(21, 00, 00)

def waketime ():
    print(7, 00, 00)

currentlytime()
naptime()
waketime()