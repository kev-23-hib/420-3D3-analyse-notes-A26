from models.composant import Composant
from abc import ABC

class Feuille(Composant, ABC):
    def __init__(self, prenom: str, nom: str, notes: dict[str, float]):
        self.prenom = prenom
        self.nom = nom
        self.notes = notes
    pass