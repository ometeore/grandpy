import wikipedia

wikipedia.set_lang("fr")
#try exept pour la requete a l'api

class Wiki:
    """gère l'interaction avec wikipedia"""

    def __init__(self, phrase):
        self.phrase = phrase


    def resultat(self):
        try:
            self.page = wikipedia.page(self.phrase)
        except wikipedia.exceptions.PageError as e:
            print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            return None

        self.title = self.page.title
        self.summary =self.page.summary
        return "ok"

    
    def action(self):
        self.summary = self.cut_thousand_word(self.page.summary, 100)
        self.old_people_talk()

    def cut_thousand_word(self, phrase, longeur):
        decompose = phrase.split()
        decompose2 = ""
        if (len(decompose)>longeur):
            decompose = decompose[:longeur]
        decompose2 =" ".join(decompose)
        
        if (decompose2[len(decompose2)-1] != '.'):
            decompose2 = decompose2.split('.')
            del decompose2[-1]
        decompose2 = ".".join(decompose2)
        decompose2 = decompose2 + "."
        return decompose2

    def old_people_talk(self):
        prefix_intro =["Ouh la... laisse moi me souvenir....","Ca remonte a bien longtemps tout ca", "phrase d'accroche numero 27:"]
        self.title = "Ah oui :).... "+ self.title +" .... je me rappèle"
        self.summary = "Laisse moi m'installer dans mon fauteuil, ok?? Très bien c'est parti. "+ self.summary