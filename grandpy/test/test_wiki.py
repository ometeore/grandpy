from unittest.mock import MagicMock
from grandpy.wiki import Wiki
import pytest

#fonction de Mock qui retourne un objet avec un attribut title et summary donc une partie de ce que fait wikipedia.page
def Mock(self):
    class Test:
        def __init__(self):
            self.title = 'test'
            self.summary = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras dui enim, aliquet imperdiet tellus quis, consectetur pretium ligula. Nullam dapibus libero et quam blandit, at facilisis orci faucibus. Nulla facilisi. Donec vitae lorem vitae arcu pharetra rutrum. Sed ut efficitur leo, eget tincidunt mauris. Vestibulum id ex justo. Vivamus at magna quam. Cras dignissim mi suscipit erat efficitur mattis. Etiam dignissim leo a mauris pharetra, nec euismod metus gravida. Ut gravida ex sed varius sagittis. In pellentesque ullamcorper urna sed suscipit. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Nullam ac tempus velit. Nullam malesuada risus nec mi ultrices, at luctus lorem dapibus. Sed quis accumsan erat. Integer dolor nisi, imperdiet quis quam convallis, aliquet viverra urna. Maecenas eros elit, aliquet quis ornare ac, condimentum sed ligula. Suspendisse vitae ornare magna, ut tristique odio. Quisque accumsan eu nibh sed congue. Vestibulum ante ipsum primis"
    return Test()


def test_wiki_cut_thousand_word(monkeypatch):
    monkeypatch.setattr('wikipedia.page', Mock)
    test = Wiki('phrase')
    test.summary = test.cut_thousand_word(test.summary, 10)
    assert test.summary == "Lorem ipsum dolor sit amet, consectetur adipiscing elit."

def test_wiki_old_people_talk(monkeypatch):
    monkeypatch.setattr('wikipedia.page', Mock)
    test = Wiki('test')
    test.summary = test.cut_thousand_word(test.summary, 10)
    test.old_people_talk()
    assert test.title == "Ah oui :).... test .... je me rappèle"
    assert test.summary == "Laisse moi m'installer dans mon fauteuil, ok?? Très bien c'est parti. Lorem ipsum dolor sit amet, consectetur adipiscing elit."