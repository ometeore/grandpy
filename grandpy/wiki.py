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
        self.summary = self.cut_thousand_word(self.page.summary)

    def titre_et_resume(self):
        liste_titre_et_resume = {}
        liste_titre_et_resume["title"] = self.title
        liste_titre_et_resume["resume"] = self.cut_thousand_word(self.summary)
        return liste_titre_et_resume

    def cut_thousand_word(self, phrase):
        decompose = phrase.split()
        decompose2 = []
        if (len(decompose)>50):
            decompose = decompose[:50]
        decompose2 =" ".join(decompose)
        print(decompose2)
        return decompose2

