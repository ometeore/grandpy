import grandpy.parseur as pars
import pytest


@pytest.mark.parametrize("phrase",[
    "test     les noix de cajoux 24 chemin de transoxiane",
    "24 chemin de transoxiane test     les noix de cajoux ",
    "j'ai 1000 fois trop envie d'aller 24 chemin de transoxiane"
])


def test_adresses_classiques_multiples(phrase):
    test = pars.Parseur(phrase)
    test.adresses_classiques_multiples()
    assert test.recit[0] == '24 chemin de transoxiane'

def test_enlever_les_espaces():
    test = pars.Parseur("test     les noix de cajoux")
    test.enlever_les_espaces()
    assert test.phrase_corige == "test les noix de cajoux"


def test_enlever_stop_words():
    test = pars.Parseur("j test bigre absolument ah a   les noix de cajoux")
    test.enlever_stop_words()
    assert test.recit[0] == 'test noix cajoux'


def test_enlever_particule():
    test = pars.Parseur("test et j'suis ta aujourd'hui d'rere")
    test.enlever_particule("test et j'suis ta aujourd'hui d'rere")
    assert test.recit[0] == "test et suis ta aujourd'hui rere"

def test_decomposer_recomposer():
    test = pars.Parseur("je tu il rue des mouettes qui comment")
    test.decomposer_recomposer()
    assert test.recit[0] == " rue des mouettes"


def test_is_a_cap_word():
    test = pars.Parseur(" souhaite Paris pars Londres")
    pass

def test_is_a_postal():
    pass