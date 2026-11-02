from abc import ABC, abstractmethod
class Composant(ABC):
    @abstractmethod
    def moyenne(self):
        pass

    @abstractmethod
    def nb_etudiants(self):
        pass


    @abstractmethod
    def to_dict(self):
        pass




class Composite(Composant, ABC):
    def __init__(self, nom: str):
        super().__init__(nom)
        self.enfants: list[Composant] = []

    def ajouter_enfant(self, enfant: Composant) -> None:
        self.enfants.append(enfant)

    def moyenne(self) -> float:
        if not self.enfants:
            return 0.0
        return round(sum(e.moyenne() for e in self.enfants) / len(self.enfants), 1)

    def nb_etudiants(self) -> int:
        return sum(e.nb_etudiants() for e in self.enfants)

    def to_dict(self) -> dict:
        enfants_dict = [e.to_dict() for e in self.enfants]
        return {
            "type": "composite",
            "moyenne": self.moyenne(),
            "nb_etudiants": self.nb_etudiants(),
            "enfants": enfants_dict
        }




