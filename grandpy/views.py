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
#                                       réponse POST au formulaire grandy                                       #
#################################################################################################################

@app.route('/contenu_user/<string:phrase>')
def afficher(phrase):

    ggm = Ggmap(phrase_corrige.phrase_corige[0])
    wiki = Wiki(phrase_corrige.phrase_corige[0])

    dico = {"phrase" : phrase_corrige.phrase_corige, "latitude":ggm.latitude, "longitude":ggm.longitude, "titre": wiki.title, "contenu":wiki.summary}
    return jsonify(dico)
#################################################################################################################
#                                                réponse google map                                             #
#################################################################################################################


@app.route("/wikiRequest/<string:query>")
def api_wiki(query):
    phrase_corrige = Parseur(query)
    phrase_corrige.action()
    retour = {}
    wiki = Wiki(query)
    retour.update(wiki.titre_et_resume())
    ggm = Ggmap(query)
    retour["image"] = ggm.resultat()
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
