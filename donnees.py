
from models.composant import Composite
from models.feuille import Feuille


def construire_programme() -> Composite:

    # --- Étudiants ---
    alice   = Feuille("Alice",   "Tremblay", {"TP1": 78, "TP2": 85, "Examen": 91})
    bob     = Feuille("Bob",     "Nguyen",   {"TP1": 65, "TP2": 70, "Examen": 74})
    carla   = Feuille("Carla",   "Diaz",     {"TP1": 92, "TP2": 88, "Examen": 95})
    david   = Feuille("David",   "Chen",     {"TP1": 55, "TP2": 62, "Examen": 68})
    fatima  = Feuille("Fatima",  "Roy",      {"TP1": 80, "TP2": 75, "Examen": 77})
    gabriel = Feuille("Gabriel", "Côté",     {"TP1": 71, "TP2": 69, "Examen": 73})
    hana    = Feuille("Hana",    "Park",     {"TP1": 88, "TP2": 91, "Examen": 89})
    ivan    = Feuille("Ivan",    "Leblanc",  {"TP1": 60, "TP2": 58, "Examen": 64})

    # --- 3D3 — Automne 2026 ---
    groupe_3d3_01 = Composite("Groupe 01")
    groupe_3d3_01.ajouter_enfant(alice)
    groupe_3d3_01.ajouter_enfant(bob)

    groupe_3d3_02 = Composite("Groupe 02")
    groupe_3d3_02.ajouter_enfant(carla)
    groupe_3d3_02.ajouter_enfant(david)

    session_3d3_a26 = Composite("Automne 2026")
    session_3d3_a26.ajouter_groupe(groupe_3d3_01)
    session_3d3_a26.ajouter_groupe(groupe_3d3_02)

    # --- 3D3 — Automne 2025 ---
    groupe_3d3_a25_01 = Composite("Groupe 01")
    groupe_3d3_a25_01.ajouter_enfant(Feuille("Eva", "Martin", {"TP1": 85, "TP2": 90, "Examen": 88}))

    session_3d3_a25 = Composite("Automne 2025")
    session_3d3_a25.ajouter_groupe(groupe_3d3_a25_01)

    cours_3d3 = Composite("3D3 — Programmation orientée objet")
    cours_3d3.ajouter_session(session_3d3_a26)
    cours_3d3.ajouter_session(session_3d3_a25)

    # --- 3R1 — Automne 2026 ---
    groupe_3r1_01 = Composite("Groupe 01")
    groupe_3r1_01.ajouter_enfant(fatima)
    groupe_3r1_01.ajouter_enfant(gabriel)
    groupe_3r1_01.ajouter_enfant(hana)
    groupe_3r1_01.ajouter_enfant(ivan)

    session_3r1_a26 = Composite("Automne 2026")
    session_3r1_a26.ajouter_groupe(groupe_3r1_01)

    cours_3r1 = Composite("3R1 — Réseaux informatiques")
    cours_3r1.ajouter_session(session_3r1_a26)

    # --- Programme ---
    programme = Composite("Techniques de l'informatique")
    programme.ajouter_cours(cours_3d3)
    programme.ajouter_cours(cours_3r1)

    return programme
