import numpy as np
import matplotlib.pyplot as plt


def plotNumber(nrVector):
    # OPGAVE 1
    # Maak gebruik van de methode reshape om de vector om te zetten in een 
    # 20 × 20 matrix.

    # Let op: de manier waarop de data is opgesteld vereist dat je gebruik maakt
    # van de Fortran index-volgorde – de eerste index verandert het snelst, de 
    # laatste index het langzaamst; als je dat niet doet, wordt het plaatje 
    # gespiegeld en geroteerd. Je kunt dit doen door de parameter 'order' van
    # de reshape-methode op 'F' te zetten (order='F').

    # Maak gebruik van een plt.cm.gray om een grayscale plaatje te maken van
    # de vector nrVector die als parameter wordt meegegeven.
    # print(nrVector)

    vector = nrVector.reshape((20, 20), order='F')
    plt.imshow(vector, cmap=plt.cm.gray)






def sigmoid(z):
    #OPGAVE 2
    # Maak de code die de sigmoid van de input z teruggeeft. Zorg er hierbij 
    # voor dat de code zowel werkt wanneer z een getal is als wanneer z een
    # vector is.  
    # Je kunt gebruik maken van de methode exp() in NumPy.

    1 / (1 + np.exp(-z))
    pass


def predictNumber(Theta1, Theta2, X):
    #OPGAVE 3
    # Deze methode moet een vector teruggeven waarin de index staat van de 
    # output-node (0-9) die de hoogste waarde heeft bij elke regel uit de 
    # input-matrix X. 

    # De matrices Theta1 en Theta2 corresponderen met het gewicht tussen de 
    # input-laag en de verborgen laag, en tussen de verborgen laag en de 
    # output-laag, respectievelijk. Deze matrices zijn al getraind (er wordt
    # geen gebruik gemaakt van back-propagation).

    # Een mogelijk stappenplan kan zijn:

    #    1. voeg enen toe aan de gegeven matrix X; dit is de input-matrix a1
    #    2. roep de sigmoid-functie van hierboven aan met a1 als actuele
    #       parameter: dit is de variabele a2
    #    3. voeg enen toe aan de matrix a2, dit is de input voor de laatste
    #       laag in het netwerk
    #    4. roep de sigmoid-functie aan op deze a2; dit is het uiteindelijke
    #       resultaat (de output)
    #    5. gebruik de methode argmax() van NumPy om te bepalen op welke index
    #       van deze output het grootste getal staat; dit is het getal dat 
    #       correspondeert met het cijfer van het huidige sample (let er daarbij
    #       op dat de indexen zero-based zijn)


    # Voeg enen toe aan het begin van elke stap en reshape de uiteindelijke 
    # vector zodat deze dezelfde dimensionaliteit heeft als y in de exercise.
    pass
