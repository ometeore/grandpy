import re
from .views import app

# Si il y a un numero chercher regex num + rue /chemin / ect + adresse
# enlever la ponctuation (sauf ' )
# si la ponctuation est ? si ! 
# les majuscules <-

#types d'adresse 
# avenue Charles de gaule
# Paris
# gare de rennes
# restaurant picasiette
# Chez Paul?

### --> Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?

class Parseur:
    """Mise en place et interfaçage d'une base de données MySQL"""
    def __init__(self, phrase):
        self.phrase_originale = phrase
        self.phrase_corige = phrase
        self.recit = []


############### FAIRE DU TDD


    def action(self):
        self.enlever_les_espaces()
        self.adresses_classiques_multiples()
        self.decomposer_recomposer()
        if len(self.recit) == 1:
            self.phrase_corige = self.recit[0]
        self.presentation()

    def presentation(self): 
        print ("\n\n phrase originale: " + self.phrase_originale+"\n\nphrase corigée: " + self.phrase_corige + "\n\nliste de tentatives:")
        print(self.recit)

    def enlever_les_espaces(self):
        self.phrase_corige = ' '.join(self.phrase_corige.split())
        
    def adresses_classiques_multiples(self):
        regex = "[0-9]{1,3}(?:(?:[,. ]){1}[-a-zA-Zàâäéèêëïîôöùûüç]+)+"
        pattern = re.compile(regex)
        if pattern.search(self.phrase_corige) is not None:
            result = pattern.findall(self.phrase_corige)
            if len(result) == 1:
                self.recit.append(result[0])
    
    #peut etre a ce moment faire des tests sur l'api ggmap

            if len(result)>1:
                print("\n\nveuillez ne saisir qu'une adresse")
    
    def decomposer_recomposer(self):
        decompose = self.phrase_originale.split()
        lieu = ["rue","boulevard","chemin","avenue","route","allée","allee","ruelle","adresse","chateau","gare","Esplanade"]
        i = 0
        rue = ""
        ponctuation = ["!","?",".",","]
        compteur_ponctuation = 0
        conjuguaison = ["je","tu","il","elle","on","nous","vous","ils","elles","ont"]
        conjonctions = ["que","qui","quoi","comment","ou"]
        for element in decompose:
            for chemin in lieu:
                if (element == chemin):
                    i = 3
            for point in ponctuation:
                if (element == point):
                    i=0
            
            if i > 0:                       
                rue = rue + " " + element
                i = i - 1

        if rue is not "":
            self.recit.append(rue)        

