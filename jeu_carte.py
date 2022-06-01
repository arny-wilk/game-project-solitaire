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

    @property
    def retirer_carte(self):
        if len(self.colonne) == 0:
            print("Il n'y a aucune carte dans la pile")
        else:
            return self.colonne.pop()

    @property
    def afficher_premiere_carte(self) -> dict:
        if len(self.colonne) == 0:
            print("Il n'y a aucun carte dans la pile")
        else:
            return self.colonne[-1]

    def afficher_pile(self):
        print(self.colonne)


class Foundation(Colonne):
    def __init__(self, name: str, numero: int, foundation=None):
        super().__init__(numero)
        self.name = name
        if foundation is None:
            self.foundation = []

    def ajouter_carte(self, carte=None):
        self.foundation.append(carte)


""" Distribution des cartes sur 7 colonnes. La première carte est toujours visible """
les_colonnes = [Colonne(numero=1), Colonne(numero=2), Colonne(numero=3), Colonne(numero=4), Colonne(numero=5),
                Colonne(numero=6), Colonne(numero=7)]

les_foundations = [Foundation('Pique', 0), Foundation('Coeur', 1), Foundation('Carreaux', 2),
                   Foundation('Trefle', 3)]


def commencer_solitaire():
    for colonne in les_colonnes:
        for _ in range(colonne.numero):
            colonne.ajouter_carte()
        colonne.afficher_pile()


def choisir_carte() -> Foundation:
    for colonne in les_colonnes:
        for _ in range(colonne.numero):
            for foundation in les_foundations:
                if colonne.afficher_premiere_carte.keys() == str(foundation.numero):
                    carte = colonne.retirer_carte
                    foundation.ajouter_carte(carte)
                return foundation


""" Pile des cartes (fondations) par couleur """
""" couleurs: card.suit -> 0=pique , 1=coeur, 2=carreaux, 3=trefle  """

if __name__ == '__main__':
    commencer_solitaire()
    print(choisir_carte())
