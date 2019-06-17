import wikipedia

wikipedia.set_lang("fr")

class Wiki:
    """gère l'interaction avec wikipedia"""

    def __init__(self, phrase):
        self.phrase = phrase
        self.page = wikipedia.page(phrase)
        self.title = self.page.title
        self.url = self.page.url
        self.content = self.page.content
        self.summary = self.page.summary

    def titre_et_resume(self):
        liste_titre_et_resume = {}
        liste_titre_et_resume["title"] = self.title
        liste_titre_et_resume["resume"] = self.summary
        print (liste_titre_et_resume)
        return liste_titre_et_resume


    #ne peut renvoyer des objets non callables

        #liste_titre_et_resume = {}
        #liste_titre_et_resume["title"] = self.title
        #liste_titre_et_resume["resume"] = self.summary