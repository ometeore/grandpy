import grandpy.parseur as script


class Test_Parseur:
    def test_enlever_les_espaces(self):
        test = script.Parseur("test     les noix de cajoux")
        test.enlever_les_espaces()
        assert test.phrase_corige == "test les noix de cajoux"

    def test_adresses_classiques_multiples(self):
        test = script.Parseur("test     les noix de cajoux 24 chemin de transoxiane")
        test.adresses_classiques_multiples()
        assert test.recit[0] == '24 chemin de transoxiane'

    def test_enlever_stop_words(self):
        test = script.Parseur("j test bigre absolument ah a   les noix de cajoux")
        test.enlever_stop_words()
        assert test.recit[0] == ['test','noix', 'cajoux'] 


    def test_enlever_particule(self):
        test = script.Parseur("test et j'suis ta aujourd'hui d'rere")
        test.enlever_particule("test et j'suis ta aujourd'hui d'rere")
        assert test.recit[0] == "test et suis ta aujourd'hui rere"

    def test_decomposer_recomposer(self):
        test = script.Parseur("je tu il rue des mouettes qui comment")
        test.decomposer_recomposer()
        assert test.recit[0] == " rue des mouettes"


     