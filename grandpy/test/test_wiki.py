from unittest.mock import MagicMock
import grandpy.wiki as wiki
import pytest

#
#@pytest.mark.parametrize("phrase",[
#    "test     les noix de cajoux 24 chemin de transoxiane",
#    "24 chemin de transoxiane test     les noix de cajoux ",
#    "j'ai 1000 fois trop envie d'aller 24 chemin de transoxiane"
#])
#
#
#def test_adresses_classiques_multiples(phrase):
#    test = pars.Parseur("")
#    resultat = test.adresses_classiques_multiples(phrase)
#    assert resultat == '24 chemin de transoxiane'
#
#def test_cut_thousand_word():
#    test = wiki