from flask import Flask, render_template, request
from grandpy.parseur import Parseur

app = Flask(__name__)


app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def text_box():
    #return request.form['phrase_utilisateur']
    text = Parseur(request.form['phrase_utilisateur'])
    text.action()
    return render_template("index.html" , message = text.phrase_corige, message_originel = text.phrase_originale, recit = text.recit)


if __name__ == "__main__":
    app.run()


#  AIzaSyAU0ruTznnqHEfl7Yu0nkozg1aJ-6SXfSI  cle API google map

