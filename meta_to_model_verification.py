from datetime import date
from generation_classe import Document, Section, Paragraphe

# Création d'un document (modèle)
doc = Document("Manuel d'utilisateur", "John Doe", date.today())

# Création de sections
introduction = Section("Introduction", "Bienvenue dans le manuel.")
installation = Section("Installation", "Voici comment installer le produit.")
utilisation = Section("Utilisation", "Comment utiliser le produit.")
conclusion = Section("Conclusion", "Merci de votre lecture.")

# Ajout de paragraphes
para1 = Paragraphe("Ce manuel vous guidera à travers les étapes d'installation.")
para2 = Paragraphe("Assurez-vous de lire toutes les sections avant de commencer.")

# Ajout des paragraphes à la section 'Introduction'
introduction.paragraphes.append(para1)
introduction.paragraphes.append(para2)

# Ajout des sections au document
doc.ajouter_section(introduction)
doc.ajouter_section(installation)
doc.ajouter_section(utilisation)
doc.ajouter_section(conclusion)

# Afficher le document (optionnel)
doc.afficher()
