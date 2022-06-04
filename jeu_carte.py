from deck_of_cards import deck_of_cards
from deck_of_cards.deck_of_cards import DeckOfCards

"""On instancie le paquet de carte avec la librairie deck_of_cards"""

deck_obj: DeckOfCards = deck_of_cards.DeckOfCards()
deck_obj.shuffle_deck()
print("\nLes cartes sont melangees !\n")

"""On range les cartes par colonnes """


class Colonne:
    def __init__(self, numero: int, colonne: list = None):
        self.numero = numero
        if colonne is None:
            self.colonne = []

    def ajouter_carte(self):
        card = deck_obj.give_random_card()
        carte: dict[str, int] = {str(card.suit): card.value}
        self.colonne.append(carte)
        return carte

    def retirer_carte(self):
        if len(self.colonne) == 0:
            print("Il n'y a aucune carte dans la pile")
        else:
            return self.colonne.pop()

    def afficher_premiere_carte(self) -> dict:
        if len(self.colonne) == 0:
            print("Pas de carte ici !")
        else:
            return self.colonne[-1]

    def afficher_pile(self):
        print(self.colonne)


class Foundation(Colonne):
    def __init__(self, name: str, numero: int, foundation: list = None):
        super().__init__(numero)
        self.name = name
        if foundation is None:
            self.foundation = []

    def ajouter_carte_de_la_colonne(self, carte: dict):
        self.foundation.append(carte)


class Tapis(Colonne):
    def __init__(self, liste=None, numero=None):
        super(Tapis, self).__init__(numero)
        if liste is None:
            self.liste = []


""" Distribution des cartes sur 7 colonnes. La première carte est toujours visible """
les_colonnes = [Colonne(numero=1), Colonne(numero=2), Colonne(numero=3), Colonne(numero=4), Colonne(numero=5),
                Colonne(numero=6), Colonne(numero=7)]

les_foundations = [Foundation('Pique', numero=1), Foundation('Coeur', numero=2),
                   Foundation('Carreaux', numero=3),
                   Foundation('Trefle', numero=4)]

le_tapis = Tapis(numero=1)


def commencer_solitaire() -> list:
    for colonne in les_colonnes:
        for _ in range(colonne.numero):
            colonne.ajouter_carte()
        colonne.afficher_pile()


def selection_carte() -> list:
    couleur = {'0', '1', '2', '3'}
    carte_candidates = []
    for colonne in les_colonnes:
        for (key, value) in colonne.afficher_premiere_carte().items():
            if key in couleur and value == 1:
                carte_candidates.append(colonne.retirer_carte())
    print(carte_candidates)


""" Pile des cartes (fondations) par couleur """
""" couleurs: card.suit -> 0=pique , 1=coeur, 2=carreaux, 3=trefle  """

if __name__ == '__main__':
    commencer_solitaire()
    selection_carte()
