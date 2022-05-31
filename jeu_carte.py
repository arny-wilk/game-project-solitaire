from deck_of_cards import deck_of_cards

"""On instancie le paquet de carte avec la librairie deck_of_cards"""

deck_obj = deck_of_cards.DeckOfCards()
deck_obj.shuffle_deck()
print("\nLes cartes sont melangees !\n")

"""On range les cartes par colonnes """


class Colonne:
    def __init__(self, colonne=None) -> list:
        if colonne is None:
            self.colonne = []

    def ajouter_carte(self):
        card = deck_obj.give_random_card()
        carte = {str(card.suit): card.value}
        self.colonne.append(carte)

    def retirer_carte(self):
        if len(self.colonne) == 0:
            print("Il n'y a aucune carte dans la pile")
        else:
            return self.colonne.pop()

    def afficher_premiere_carte(self):
        if len(self.colonne) == 0:
            print("Il n'y a aucun carte dans la pile")
        else:
            return self.colonne[-1]

    def afficher_pile(self):
        print(self.colonne)


class Foundation(Colonne):
    def __init__(self, name, couleur, foundations=None):
        self.name = name
        self.couleur = couleur
        if foundations is None:
            foundations = []
        super(Foundation, self).__init__()

    def afficher_foundation(self):
        print(f'{self.foundation}')


""" Distribution des cartes sur 7 colonnes. La première carte est toujours visible """

colonne_1 = Colonne()
colonne_1.ajouter_carte()
colonne_1.afficher_pile()

colonne_2 = Colonne()
for _ in range(3):
    colonne_2.ajouter_carte()
colonne_2.afficher_pile()

colonne_3 = Colonne()
for _ in range(4):
    colonne_3.ajouter_carte()
colonne_3.afficher_pile()

colonne_4 = Colonne()
for _ in range(5):
    colonne_4.ajouter_carte()
colonne_4.afficher_pile()

colonne_5 = Colonne()
for _ in range(6):
    colonne_5.ajouter_carte()
colonne_5.afficher_pile()

colonne_6 = Colonne()
for _ in range(7):
    colonne_6.ajouter_carte()
colonne_6.afficher_pile()

colonne_7 = Colonne()
for _ in range(8):
    colonne_7.ajouter_carte()
colonne_7.afficher_pile()

""" Pile des cartes (fondations) par couleur """
""" couleurs: card.suit -> 0=pique , 1=coeur, 2=carreaux, 3=trefle  """

foundation_pique = Foundation('Pique', '0')
foundation_pique.afficher_pile()

foundation_coeur = Foundation('Coeur', '1')
foundation_coeur.afficher_pile()

foundation_carreaux = Foundation('Carreaux', '2')
foundation_carreaux.afficher_pile()

foundation_trefle = Foundation('Trefle', '3')
foundation_trefle.afficher_pile()
