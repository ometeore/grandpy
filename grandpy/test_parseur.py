import grandpy.parseur as script

def test_enlever_les_espaces():
    test = script.Parseur("j'aime     les noix de cajoux")
    test.enlever_les_espaces()

    assert test.phrase_corige == "j'aime les noix de cajoux"

def test_adresses_classiques_multiples():
    test = script.Parseur("j'aime     les noix de cajoux 24 chemin de transoxiane")
    test.adresses_classiques_multiples()
    assert test.recit[0] == '24 chemin de transoxiane'

def test_enlever_stop_words():
    test = script.Parseur("j aime bigre absolument ah a   les noix de cajoux")
    test.enlever_stop_words()
    assert test.recit[0] == ['aime','noix', 'cajoux'] 

def test_decomposer_recomposer():
    test = script.Parseur("je rentre mais je ne serai pas disponible avant bientôt")
