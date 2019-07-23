import grandpy.parseur as pars
import pytest



def test_adresses_classiques_multiples(phrase):
    test = pars.Parseur("")
    resultat = test.adresses_classiques_multiples(phrase)
    assert resultat == '24 chemin de transoxiane'