# MACHINE LEARNING OPGAVE 3
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from sklearn.datasets import fetch_mldata
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn.metrics import confusion_matrix

print ("Laden van de data en zetten van de X en de y")
mnist = fetch_mldata('MNIST original')
X,y = mnist['data'], mnist['target']

test_waarde = 36000
some_digit = X[test_waarde] #dit is een 5

pass

# ========================  OPGAVE 1 ======================== 
# Teken het plaatje dat hoort bij de data op regel 36000 (die we hierboven
# al in de variabel some_digit hebben gezet). Net als in weet 2 moet je 
# hiervoor deze vector omzetten in een matrix van 28×28 (maak hiervoor
# gebruik van de methode reshape). Vervolgens kun je pyplot.imgshow()
# gebruiken om het plaatje weer te geven. Voor het beste effect geef
# je de parameter cmap de waarde cm.binary en zet je de interpolation
# op 'nearest'. Als het goed is, krijg je een plaatje te zien van een 5 
# (dat is het plaatje dat staat op positie 36000).

# Experimenteer met verschillende waarden van some_digit om een idee te 
# krijgen van de verschillende vormen van de cijfers in deze dataset.

img = some_digit.reshape(28,28)
plt.imshow(img, cmap=matplotlib.cm.binary, interpolation="nearest")
plt.show()


# ========== ONDERVERDELEN VAN DE DATA IN EEN ==============
# ============= TRAINING- EN EEN TEST-SET ================== 
# In de regels hieronder wordt de dataset onderverdeeld in een trainings-set (de 
# eerste zestigduizend plaatjes) en een test-set (de laatste tienduizend plaatjes).
# Vervolgens schudden we de trainings-set, omdat SGD de neiging heeft om trainings-
# data te 'onthouden. Dit doen we met behulp van de NumPy-functie random.permutation().

X_train, X_test, y_train, y_test = X[:60000], X[60000:], y[:60000], y[60000:] 
print ("schudden van de trainings-set...")
shuffle_idx = np.random.permutation(60000)
X_train, y_train = X_train[shuffle_idx], y_train[shuffle_idx]

input ("Druk op een toets om verder te gaan.")


# ========================  OPGAVE 2 ======================== 
# Maak twee variabelen, y_train_5 en y_test_5, die bestaan uit een array die True
# is voor alle waarden van de oorspronkelijke training- en test-set wanneer dit 
# een 5 is, en False voor alle andere waarden.

#YOUR CODE HERE - deel 1
y_train_5 = 0
y_test_5 = 0

# Maak vervolgens een SGDClassifier aan. Deze classifier is afhankelijk van een
# bepaalde 'randomness' tijdens het trainen; je moet dus een parameter random_state
# meegeven. Om duidelijke wijsgerige redenen geven we die parameter meestal de 
# waarde 42.

#YOUR CODE HERE - deel 2
sgd_clf = 0

# Deze classifier heeft een methode 'fit' die twee arrays verwacht: één met de 
# training samples en één met de target values.  Bedenk wat in dit geval wat is, 
# en stuur de betreffende arrays mee als actuele parameters. Op deze manier 
# trainen we de classifier om een 5 uit de volledige dataset te voorspellen 
# (we trainen hem dus om te voorspellen of een gegeven input een 5 is of niet)
# (deel 3). We testen dit op de variabel some_digit die we hierboven hebben
# aangemaakt.

#YOUR CODE HERE - deel 3
#sgd_clf.fit() 
print ("Voorspellen van digit nummer {}: dit zou een 5 moeten opleveren.".format(test_waarde))
print ( sgd_clf.predict([some_digit]) ) 

# Tenslotte gebruiken we de methode cross_val_score() om de accuratesse van 
# onze classifier te bepalen. Deze methode heeft een parameter cv (voor cross-
# validation) waarmee je kunt aangeven in hoeveel delen de data geknipt moet 
# worden. Geef deze parameter een waarde van 3, en experimenteer met verschillende
# waarden hiervoor. Geef de scoring-parameter de waarde 'accuracy'.
# Zorg ervoor dat deze cross-validatie score wordt afgedrukt.

#YOUR CODE HERE - deel 4
y_train_pred = 0;
print ("Bepalen van de cross-validatie-score:")
print (y_train_pred)


# ========================  OPGAVE 3 ======================== 
# Gebruik de methode confusion_matrix om de confusion matrix van het netwerk
# dat je hierboven hebt getraind te bepalen: onthoudt dat dit gaat om de 
# voorspelde waarden en de actuele waarden (wat zit er in welke variabele?). 
# Gebruik vervolgens deze matrix om de variabelen TN, FP, FN en TP te 
# bepalen, en aan de hand daarvan de verschillende verhoudingen (zie de 
# opgave op Blackboard voor specifieke info hierover).

#YOUR CODE HERE
cm = None
print ("De confusion matrix van deze classifier:");
print (cm)

#YOUR CODE HERE

print ("TPR: {}; PPV: {}, TNR: {}, FPR: {}".format(TPR, PPV, TNR, FPR))


# ========================  OPGAVE 4 ======================== 
# Gebruik de volledige data-set om de classifier te trainen. Maak vervolgens
# gebruik van dezelfde methode als de vorige opgave om de confusion matrix 
# uit te rekenen. Wat kun je op basis van deze matrix zeggen over de 
# accuratesse van de classifier? Waar zou je eventueel nog verbeteringen in
# kunnen aanbrengen?

#YOUR CODE HERE


