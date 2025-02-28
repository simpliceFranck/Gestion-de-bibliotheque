# Gestion-de-bibliotheque
C'est une petite application qui permet de gérer certaines tâches d'une bibliothèque notamment :
- Ajouter et supprimer des utilisateurs ;
- Ajouter et supprimer des livres ;
- Rechercher un livre ;
- Mettre à jour un livre ;
- Emprunter et retourner des livres (pour un abonné de la bibliothèque).
  
Il est également possible avec cette application de lister l'ensemble de livres de la bibliothèque
(livres disponibles et empruntés), d'afficher les statistiques (nombre total d'abonnés, nombre total
des livres disponibles, nombre total des livres empruntés ou de sauvegarder les données.

# Matériels utilisés
Pour élaborer cette application, seul Python et ses quelques modules standards ont été nécessaires.
Parmi les modules standards utilisés :
- textwrap.dedent pour supprimer les espaces de début de chaque ligne de texte ;
- os.path.exists pour vérifier si le fichier spécifié existe ou non ;
- itertools.chain pour aplatir des listes imbriquées.
- pickle.load et pickle.dump pour sérialiser et désérialiser des objets Python.
