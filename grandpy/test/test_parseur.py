import grandpy.parseur as pars
import pytest


@pytest.mark.parametrize("phrase",[
    "test     les noix de cajoux 24 chemin de transoxiane",
    "24 chemin de transoxiane test     les noix de cajoux ",
    "j'ai 1000 fois trop envie d'aller 24 chemin de transoxiane"
])


def test_adresses_classiques_multiples(phrase):
    test = pars.Parseur("")
    resultat = test.adresses_classiques_multiples(phrase)
    assert resultat == '24 chemin de transoxiane'

def test_enlever_les_espaces():
    test = pars.Parseur("")
    assert test.enlever_les_espaces("test     les noix de cajoux") == "test les noix de cajoux"


def test_enlever_stop_words():
    test = pars.Parseur("")
    resultat = test.enlever_stop_words("j test bigre absolument ah a   les noix de cajoux")
    assert resultat == 'test noix cajoux'


def test_enlever_particule():
    test = pars.Parseur("")
    resultat = test.enlever_particule("test et j'suis ta aujourd'hui d'rere")
    assert resultat == "test et suis ta aujourd'hui rere"

def test_decomposer_recomposer():
    test = pars.Parseur("")
    resultat = test.decomposer_recomposer("je tu il rue des mouettes qui comment")
    assert resultat == " rue des mouettes"


def test_is_a_cap_word():
    pass

def test_is_a_postal():
    pass