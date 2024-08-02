from datetime import date
from typing import List, Optional

class Document:
    def __init__(self, titre: str, auteur: str, date_creation: date):
        self.titre = titre
        self.auteur = auteur
        self.date_creation = date_creation
        self.sections: List['Section'] = []
        self.lists: List['List'] = []

class Section:
    def __init__(self, titre: str, contenu: str):
        self.titre = titre
        self.contenu = contenu
        self.sous_sections: List['Section'] = []
        self.paragraphes: List['Paragraphe'] = []
        self.lists: List['List'] = []
        self.codes: List['Code'] = []

class Paragraphe:
    def __init__(self, texte: str, annotation: Optional[str] = None):
        self.texte = texte
        self.annotation = annotation

class List:
    def __init__(self, type: str, element: List[str]):
        self.type = type
        self.element = element
        self.figures: List['Figure'] = []
        self.tables: List['Table'] = []

class Code:
    def __init__(self, langage: str, contenu: str, description: Optional[str] = None):
        self.langage = langage
        self.contenu = contenu
        self.description = description

class Figure:
    def __init__(self, titre: str, chemin_acces: str, description: Optional[str] = None):
        self.titre = titre
        self.chemin_acces = chemin_acces
        self.description = description

from typing import List

class Table:
    def __init__(self, titre: str, en_tete: List[str], ligne: List[List[str]]):
        self.titre = titre
        self.en_tete = en_tete
        self.ligne = ligne

