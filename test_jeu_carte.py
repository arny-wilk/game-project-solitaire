from unittest import TestCase

from solitaire.jeu_carte import les_colonnes, les_foundations


class Test(TestCase):
    def test_les_colonnes(self):
        assert (les_colonnes is not None)
        assert (len(les_colonnes) > 0)

    def test_les_foundations(self):
        assert (les_foundations is not None)
        assert (len(les_foundations) > 0)