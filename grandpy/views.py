from flask import Flask, render_template
from grandpy.parseur import Parseur

app = Flask(__name__)


app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def text_box():
    text = Parseur(request.form['phrase_utilisateur'])
    text.action()
    return render_template("index.html" , message = text.phrase_corige )


if __name__ == "__main__":
    app.run()

############### FAIRE DU TDD 

#if __name__ == '__main__':
#    def main():
#        """Hello world"""
#        phrase = input("Veuillez entrer une phrase\n\n")
#        if phrase == "1":
#            test1 = Parseur("Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?")
#            test1.action()
#        else:
#            test = Parseur(phrase)
#            test.action()
