from enum import Enum;

class Types(Enum):
    boer = 'B'
    wolf = 'W'
    geit = 'G'
    kool = 'K'

class Ding():
    # maak hier even een lijst van
    links = ""
    rechts = ""
    state = ""
    for x in Types:
        links+=x.value

    state = links + "||" + rechts

    if Types.geit.value+Types.kool.value in links:
        print("OH NEE")

    if Types.geit.value+Types.kool.value in rechts:
        print("OH NEE RECHTS")

    print(state)
