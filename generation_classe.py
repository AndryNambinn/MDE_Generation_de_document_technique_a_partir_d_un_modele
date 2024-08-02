from datetime import date
from typing import List, Optional

class Document:
    def __init__(self, titre: str, auteur: str, date_creation: date):
        self.titre = titre
        self.auteur = auteur
        self.date_creation = date_creation
        self.sections: List['Section'] = []
    
    def ajouter_section(self, section: 'Section'):
        self.sections.append(section)
    
    def afficher(self):
        print(f"Titre: {self.titre}\nAuteur: {self.auteur}\nDate de création: {self.date_creation}")
        for section in self.sections:
            section.afficher()

class Section:
    def __init__(self, titre: str, contenu: str):
        self.titre = titre
        self.contenu = contenu
        self.sous_sections: List['Section'] = []
        self.paragraphes: List['Paragraphe'] = []
        self.lists: List['ListElement'] = []
        self.codes: List['Code'] = []
    
    def afficher(self):
        print(f"\nSection: {self.titre}")
        print(self.contenu)
        for para in self.paragraphes:
            para.afficher()

class Paragraphe:
    def __init__(self, texte: str, annotation: Optional[str] = None):
        self.texte = texte
        self.annotation = annotation
    
    def afficher(self):
        print(f"Paragraphe: {self.texte}")
        if self.annotation:
            print(f"Annotation: {self.annotation}")

class ListElement:
    def __init__(self, type: str, elements: List[str]):
        self.type = type
        self.elements = elements
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

class Table:
    def __init__(self, titre: str, en_tete: List[str], lignes: List[List[str]]):
        self.titre = titre
        self.en_tete = en_tete
        self.lignes = lignes
