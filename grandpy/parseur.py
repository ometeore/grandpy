import re

# les majuscules UPER_CASE <-

### --> Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?

class Parseur:
    """Mise en place et interfaçage d'une base de données MySQL"""
    def __init__(self, phrase):
        self.phrase_originale = phrase
        self.phrase_corige = phrase
        self.recit = []

    def action(self):
        """ effectue les differentes méthodes sur la chaine d'entrée puis stoque le meilleur résultat dans phrase_corige"""
        self.enlever_les_espaces()
        self.enlever_particule()
        self.adresses_classiques_multiples()
        
        self.enlever_stop_words()
        self.decomposer_recomposer()
        print("le print du parseur")
        print(self.recit)
        self.phrase_corige = self.recit
        #self.presentation()

    def presentation(self): 
        """ print les attributs """
        print ("\n\n phrase originale: " + self.phrase_originale+"\n\nphrase corigée: " + self.phrase_corige + "\n\nliste de tentatives:")


    def enlever_les_espaces(self):
        """ enleve les espaces surnuméraire"""
        self.phrase_corige = ' '.join(self.phrase_corige.split())
        
    #def adresses_classiques_multiples(self):
    #    """ extrait une adresse type par regex int(XX) (TEXT) <-> 23 rue des bouquetins """
    #    regex = "[0-9]{1,3}(?:(?:[,. ]){1}[-a-zA-Zàâäéèêëïîôöùûüç]+)+"
    #    pattern = re.compile(regex)
    #    if pattern.search(self.phrase_corige) is not None:
    #        result = pattern.findall(self.phrase_corige)
    #        if len(result) == 1:
    #            self.recit.append(result[0])
    #        if len(result)>1:
    #            print("\n\nveuillez ne saisir qu'une adresse")
    
    def adresses_classiques_multiples(self):
        decompose = self.phrase_originale.split()
        for word in decompose:
            try: 
                int(word)
                index = decompose.index(word)
                decompose2 = decompose[index:(index+4)]
                decompose2 =" ".join(decompose2)
                self.recit.append(decompose2)
            except:
                pass

    def enlever_stop_words(self):
        """ enleve une liste de stop words cf OC"""
        decompose = self.phrase_originale.split()
        stop_words = ["Grandpy","je","tu","il","elle","on","nous","vous","ils","elles","ont", "a","abord","absolument","afin","ah","ai","aie","ailleurs","ainsi","ait","allaient","allo","allons","allô","alors","anterieur","anterieure","anterieures","apres","après","as","assez","attendu","au","aucun","aucune","aujourd","aujourd'hui","aupres","auquel","aura","auraient","aurait","auront","aussi","autre","autrefois","autrement","autres","autrui","aux","auxquelles","auxquels","avaient","avais","avait","avant","avec","avoir","avons","ayant","b","bah","bas","basee","bat","beau","beaucoup","bien","bigre","boum","bravo","brrr","c","car","ce","ceci","cela","celle","celle-ci","celle-là","celles","celles-ci","celles-là","celui","celui-ci","celui-là","cent","cependant","certain","certaine","certaines","certains","certes","ces","cet","cette","ceux","ceux-ci","ceux-là","chacun","chacune","chaque","cher","chers","chez","chiche","chut","chère","chères","ci","cinq","cinquantaine","cinquante","cinquantième","cinquième","clac","clic","combien","comme","comment","comparable","comparables","compris","concernant","contre","couic","crac","d","da","dans","de","debout","dedans","dehors","deja","delà","depuis","dernier","derniere","derriere","derrière","des","desormais","desquelles","desquels","dessous","dessus","deux","deuxième","deuxièmement","devant","devers","devra","different","differentes","differents","différent","différente","différentes","différents","dire","directe","directement","dit","dite","dits","divers","diverse","diverses","dix","dix-huit","dix-neuf","dix-sept","dixième","doit","doivent","donc","dont","douze","douzième","dring","du","duquel","durant","dès","désormais","e","effet","egale","egalement","egales","eh","elle","elle-même","elles","elles-mêmes","en","encore","enfin","entre","envers","environ","es","est","et","etant","etc","etre","eu","euh","eux","eux-mêmes","exactement","excepté","extenso","exterieur","f","fais","faisaient","faisant","fait","façon","feront","fi","flac","floc","font","g","gens","h","ha","hein","hem","hep","hi","ho","holà","hop","hormis","hors","hou","houp","hue","hui","huit","huitième","hum","hurrah","hé","hélas","i","il","ils","importe","j","je","jusqu","jusque","juste","k","l","la","laisser","laquelle","las","le","lequel","les","lesquelles","lesquels","leur","leurs","longtemps","lors","lorsque","lui","lui-meme","lui-même","là","lès","m","ma","maint","maintenant","mais","malgre","malgré","maximale","me","meme","memes","merci","mes","mien","mienne","miennes","miens","mille","mince","minimale","moi","moi-meme","moi-même","moindres","moins","mon","moyennant","multiple","multiples","même","mêmes","n","na","naturel","naturelle","naturelles","ne","neanmoins","necessaire","necessairement","neuf","neuvième","ni","nombreuses","nombreux","non","nos","notamment","notre","nous","nous-mêmes","nouveau","nul","néanmoins","nôtre","nôtres","o","oh","ohé","ollé","olé","on","ont","onze","onzième","ore","ou","ouf","ouias","oust","ouste","outre","ouvert","ouverte","ouverts","o|","où","p","paf","pan","par","parce","parfois","parle","parlent","parler","parmi","parseme","partant","particulier","particulière","particulièrement","pas","passé","pendant","pense","permet","personne","peu","peut","peuvent","peux","pff","pfft","pfut","pif","pire","plein","plouf","plus","plusieurs","plutôt","possessif","possessifs","possible","possibles","pouah","pour","pourquoi","pourrais","pourrait","pouvait","prealable","precisement","premier","première","premièrement","pres","probable","probante","procedant","proche","près","psitt","pu","puis","puisque","pur","pure","q","qu","quand","quant","quant-à-soi","quanta","quarante","quatorze","quatre","quatre-vingt","quatrième","quatrièmement","que","quel","quelconque","quelle","quelles","quelqu'un","quelque","quelques","quels","qui","quiconque","quinze","quoi","quoique","r","rare","rarement","rares","relative","relativement","remarquable","rend","rendre","restant","reste","restent","restrictif","retour","revoici","revoilà","rien","s","sa","sacrebleu","sait","sans","sapristi","sauf","se","sein","seize","selon","semblable","semblaient","semble","semblent","sent","sept","septième","sera","seraient","serait","seront","ses","seul","seule","seulement","si","sien","sienne","siennes","siens","sinon","six","sixième","soi","soi-même","soit","soixante","son","sont","sous","souvent","specifique","specifiques","speculatif","stop","strictement","subtiles","suffisant","suffisante","suffit","suis","suit","suivant","suivante","suivantes","suivants","suivre","superpose","sur","surtout","t","ta","tac","tant","tardive","te","tel","telle","tellement","telles","tels","tenant","tend","tenir","tente","tes","tic","tien","tienne","tiennes","tiens","toc","toi","toi-même","ton","touchant","toujours","tous","tout","toute","toutefois","toutes","treize","trente","tres","trois","troisième","troisièmement","trop","très","tsoin","tsouin","tu","té","u","un","une","unes","uniformement","unique","uniques","uns","v","va","vais","vas","vers","via","vif","vifs","vingt","vivat","vive","vives","vlan","voici","voilà","vont","vos","votre","vous","vous-mêmes","vu","vé","vôtre","vôtres","w","x","y","z","zut","à","â","ça","ès","étaient","étais","était","étant","été","être","ô"]
        decompose2 = [word for word in decompose if len(word) > 2 and word not in stop_words]
        decompose2 =" ".join(decompose2)
        self.recit.append(decompose2)


    def decomposer_recomposer(self):
        decompose = self.phrase_originale.split()
        lieu = ["rue","boulevard","chemin","avenue","route","allée","allee","ruelle","adresse","chateau","gare","Esplanade"]
        i = 0
        rue = ""
        ponctuation = ["!","?",".",","]
        compteur_ponctuation = 0
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


    def enlever_particule(self):
        """ defait les particules d' l' a' des mots """
        decompose = self.phrase_originale.split()
        decompose2 = []
        for word in decompose:
            if len(word) > 1 and word[1] == "'":
                word = word[2:]
            decompose2.append(word)        
        decompose2 =" ".join(decompose2)
        self.recit.append(decompose2)
#return ' '.join([w for w in word.split("'") if len(w) > 1]) 