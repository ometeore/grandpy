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
        self.summary = self.cut_thousand_word(self.page.summary, 100)

    def titre_et_resume(self):
        liste_titre_et_resume = {}
        liste_titre_et_resume["title"] = self.title
        liste_titre_et_resume["resume"] = self.cut_thousand_word(self.summary)
        return liste_titre_et_resume

    def cut_thousand_word(self, phrase, longeur):
        decompose = phrase.split()
        decompose2 = []
        if (len(decompose)>longeur):
            decompose = decompose[:longeur]
        decompose2 =" ".join(decompose)
        return decompose2

