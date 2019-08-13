from flask import Flask, render_template, request, jsonify, redirect, url_for
from grandpy.parseur import Parseur
from grandpy.wiki import Wiki
from grandpy.api_google_map import Ggmap
from grandpy.key import key
import requests, wikipedia, imghdr


search_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
photos_url = "https://maps.googleapis.com/maps/api/place/photo?parameters"

app = Flask(__name__)


#/search?query=bonjour+grandpy+bot+ou+est+openclassrooms
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']

@app.route('/')
def home():
    return render_template("acceuil.html")

#################################################################################################################
#                                                réponse google map                                             #
#################################################################################################################


@app.route("/wikiRequest/<string:query>")
def api_wiki(query):
    demande = Parseur(query)
    demande.action()
    retour = {}
    wiki = Wiki(demande.phrase_corige)
    module_wiki = wiki.resultat()
    if not module_wiki:
        retour = {"phrase" : "erreur j'ai pas trouvé...", "title": "oups, wiki" , "resume":"papi préfère jouer de la flute, la phrase était:" + demande.phrase_originale +" le parseur a rendu:" + demande.phrase_corige, "latitude": -27.112723, "longitude": -109.3496865, "image": ""}
    else:
        wiki.action()
        ggm = Ggmap(demande.phrase_corige)
        module_map_answer = ggm.resultat()
        if not module_map_answer:
            retour = {"phrase" : "erreur j'ai pas trouvé...", "title": "oups, google map" , "resume":"papi préfère jouer de la flute, la phrase était:" + demande.phrase_originale +" le parseur a rendu:" + demande.phrase_corige, "latitude": -27.112723, "longitude": -109.3496865, "image": ""}
            print(retour)
            return jsonify(retour)
        retour = {"phrase" : demande.phrase_corige, "title": wiki.title, "resume":wiki.summary, "latitude":ggm.latitude, "longitude":ggm.longitude, "image": module_map_answer[0]}
        print(retour)
    return jsonify(retour)



#################################################################################################################
#                                                      404                                                      #
#################################################################################################################

@app.errorhandler(404)
def ma_page_404(error):
    return "Ma jolie page 404", 404





#################################################################################################################
#                                                 page de plantage stylisé                                      #
#################################################################################################################

#@app.route("/sorry")
#def page_de_plantage():
#    return render_template("erreur.html")
#
#@app.route("/sorry", methods=['POST'])
#def redirection():
#    print(request.form['chat'])
#    print(type(request.form['chat']))
#    if request.form['chat'] == "valider":
#        return redirect(url_for('home'))
#    else:
#        return render_template("erreur.html")





if __name__ == "__main__":
    app.run()
