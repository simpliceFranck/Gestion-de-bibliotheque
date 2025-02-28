import pickle, os

from textwrap import dedent
from itertools import chain

import message
from models import Utilisateur, LivrePapier, LivreNumerique
from menu import menu

message.SYMBOLE
message.ESPACE


   
class Bibliotheque:
    '''Classe sigleton.'''
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Bibliotheque, cls).__new__(cls, *args, **kwargs)
        return cls._instance
    
    
    def __init__(self) -> None:
        self.__nom = 'Bibliothèque François Villon'
        self.__adresse = '81, boulevard de la Villette, 75010 Paris'
        self.__data_utilisateurs = {}
        self.__data_livres_disponibles = {}
        self.__data_livres_empruntes = {}
        # On remet dans le script les données stockées.
        self.restituer_donnees()
    

    def __lire_data_utilisateurs(self):
        '''Lire les données utilisateurs stockées.'''
        try:
            if os.path.exists('utilisateurs_data.pickle'):
                with open('utilisateurs_data.pickle', 'rb') as f:
                    self.__data_utilisateurs = pickle.load(f)
        except Exception as e:
            raise ValueError(e)
    

    def __lire_data_livres_disponibles(self):
        '''lire les données livres disponibles stockées.'''
        try:
            if os.path.exists('livres_disponibles_data.pickle'):
                with open('livres_disponibles_data.pickle', 'rb') as f:
                    self.__data_livres_disponibles = pickle.load(f)
        except Exception as e:
            raise ValueError(e)
    

    def __lire_data_livres_empruntes(self):
        '''Lire les données livres empruntés stockées.'''
        try:
            if os.path.exists('livres_empruntes_data.pickle'):
                with open('livres_empruntes_data.pickle', 'rb') as f:
                    self.__data_livres_empruntes = pickle.load(f)
        except Exception as e:
            raise ValueError(e)
    

    def restituer_donnees(self):
        '''Restitue dans le script toutes les données stockées.'''
        self.__lire_data_utilisateurs()
        self.__lire_data_livres_disponibles()
        self.__lire_data_livres_empruntes()
    

    def is_user_exist(self, nom):
        '''Vérifie si l'utilisateur existe dans 'data_utilisateurs'
        et retourne 'True' ou 'False'.'''
        return self.__data_utilisateurs.get(nom) is not None
    

    def is_book_exist(self, isbn):
        '''Vérifie si l'Isbn existe dans 'data_livres_disponibles'
        et retourne 'True' ou 'False'.'''
        return self.__data_livres_disponibles.get(isbn) is not None

    
    def ajouter_utilisateur(self, nom, statut):
        '''Ajoute un utilisateur dans le dictionnaire 'data_utilisateurs'.'''
        usager = Utilisateur(nom, statut)

        if nom not in self.__data_utilisateurs:
            self.__data_utilisateurs[nom] = usager
            menu.afficher_message(message.ADD_USER)
        else:
            menu.afficher_message(message.USER_NOT_FOUND)

    
    def supprimer_utilisateur(self, nom):
        '''Supprime un utilisateur du dictionnaire 'data_utilisateurs'.'''
        if nom in self.__data_utilisateurs:
            del self.__data_utilisateurs[nom]
            menu.afficher_message(message.SUPPRESSION_USAGER_REUSSIE)
        else:
            menu.afficher_message(message.USER_NOT_EXIST)

    
    def ajouter_livre(self, titre, auteur, isbn, statut):
        '''Ajoute un livre dans le dictionnaire 'data_livres_empruntes'.'''
        if isbn not in self.__data_livres_disponibles:
            if statut == '3':
                livre = LivrePapier(titre, auteur, isbn)
            elif statut == '4':
                livre = LivreNumerique(titre, auteur, isbn) 
            self.__data_livres_disponibles[isbn] = livre
            menu.afficher_message(message.ADD_BOOK)
        else:
            menu.afficher_message(message.BOOK_EXIST)

    
    def supprimer_livre(self, isbn):
        '''Supprime un livre par isbn.'''
        if isbn in self.__data_livres_disponibles:
            del self.__data_livres_disponibles[isbn]
            menu.afficher_message(message.SUPPRESSION_LIVRE_REUSSIE)
        else:
            menu.afficher_message(message.BOOK_NOT_EXIST)
    

    def rechercher_livre(self, titre="", auteur="", isbn=""):
        '''Recherche un livre soit par 'titre', soit par 'auteur', soit par 'isbn'.'''
        if titre: # trouver par titre
            for livre in self.__data_livres_disponibles.values():
                if livre.get_titre() == titre:
                    print()
                    livre.description()
                    break
            else:    
                menu.afficher_message(message.BOOK_NOT_FOUND)
        elif auteur: # trouver par auteur
            for livre in self.__data_livres_disponibles.values():
                if livre.get_auteur() == auteur:
                    print()
                    livre.description()
                    break
            else:    
                menu.afficher_message(message.BOOK_NOT_FOUND)
        elif isbn: # trouver par isbn
            if isbn in self.__data_livres_disponibles:
                livre = self.__data_livres_disponibles.get(isbn)
                print()
                livre.description()
            else:
                menu.afficher_message(message.OPERATION_IMPOSSIBLE)
    

    def emprunter_livre(self, nom_emprunteur, isbn):
        '''Emprunter un livre en utilisant le nom de l'emprunteur
        et l'isbn du livre à emprunté.'''
        if not self.is_user_exist(nom_emprunteur):
            raise ValueError(message.BORROWER_NOT_EXIST)
        
        if not self.is_book_exist(isbn):
            raise ValueError(message.OPERATION_IMPOSSIBLE)

        livre = self.__data_livres_disponibles.get(isbn)
        # Pour qu'un utilisateur piusse emprunter plus d'un livre
        if self.__data_livres_empruntes.get(nom_emprunteur, None) is None:
            self.__data_livres_empruntes[nom_emprunteur] = [livre]
        else:
            self.__data_livres_empruntes.get(nom_emprunteur, None).append(livre)
        print(self.__data_livres_empruntes)
        del self.__data_livres_disponibles[isbn]
        menu.afficher_message(message.EMPRUNT_LIVRE_REUSSI)
    

    def retourner_livre(self, nom_emprunteur, isbn):
        '''Retourner un livre en utilisant le nom de l'emprunteur
        et l'isbn du livre emprunté.'''
        if nom_emprunteur not in self.__data_livres_empruntes:
            raise ValueError(message.BORROWER_NOT_EXIST)
        
        for livre in chain(*(self.__data_livres_empruntes.values())):
            if livre.get_isbn() == isbn:
                self.__data_livres_disponibles[isbn] = livre
                if len(self.__data_livres_empruntes.get(nom_emprunteur)) == 1: 
                    del self.__data_livres_empruntes[nom_emprunteur]
                else:
                    self.__data_livres_empruntes.get(nom_emprunteur).remove(livre)
                menu.afficher_message(message.RETOUR_LIVRE_REUSSI)
                break
        else:
            menu.afficher_message(message.RETOUR_IMPOSSIBLE)
        

    def lister_livres(self):
        '''Afficher les détails de tous les livres disponibles à l'emprunt
        et de ceux déjà empruntés.'''
        menu.afficher_message("Livres disponibles : ")
        if len(self.__data_livres_disponibles) != 0:
            for ind, livre in enumerate(self.__data_livres_disponibles.values()):
                menu.afficher_message(f"{ind + 1}°/")
                livre.description()
        else:
            menu.afficher_message("0")
        print()
        menu.afficher_message("Livres empruntés : ")
        if len(self.__data_livres_empruntes) != 0:
            for ind, livre in enumerate(chain(*(self.__data_livres_empruntes.values()))):
                menu.afficher_message(f"{ind + 1}°/")
                livre.description()
        else:
            menu.afficher_message("0")


    def mettre_a_jour_livre(self, nouveau_titre, nouveau_auteur, ancien_titre, ancien_auteur):
        '''Mettre à jour le titre ou le nom de l'auteur d'un livre.'''
        for liv in self.__data_livres_disponibles.values():
            if all((liv.get_titre() == ancien_titre, liv.get_auteur() == ancien_auteur)):
                liv.mise_a_jour(nouveau_titre, nouveau_auteur)
                menu.afficher_message(message.UPDATE_OK)
                break
        else:
            menu.afficher_message(message.MISE_A_JOUT_IMPOSSIBLE)
    

    def generer_statistiques(self):
        '''Générer les statistiques de la bibliothèque.'''
        menu.afficher_message(dedent(f"""\
                    Total utilisateurs       : {len(self.__data_utilisateurs)}
                    Total libres disponibles : {len(self.__data_livres_disponibles)}
                    Total livres empruntés   : {len(self.__data_livres_empruntes)}"""))
    

    def __stocker_data_utilisateurs(self):
        '''Stocker les données utilisateurs sur un fichier.pickle'''
        try:
            with open('utilisateurs_data.pickle', 'wb') as f:
                pickle.dump(self.__data_utilisateurs, f)
        except Exception as e:
            raise ValueError(e)
    

    def __stocker_data_livres_disponibles(self):
        '''Stocker les données livres disponibles sur un fichier.pickle'''
        try:
            with open('livres_disponibles_data.pickle', 'wb') as f:
                pickle.dump(self.__data_livres_disponibles, f)
        except Exception as e:
            raise ValueError(e)
        
    
    def __stocker_data_livres_empruntes(self):
        '''Stocker les données livres empruntés sur un fichier.pickle'''
        try:
            with open('livres_empruntes_data.pickle', 'wb') as f:
                pickle.dump(self.__data_livres_empruntes, f)
        except Exception as e:
            raise ValueError(e)
    

    def sauvegarder_donnees(self):
        '''Sauvegarder l'ensemble de données de la bibliothèque.'''
        self.__stocker_data_utilisateurs()
        self.__stocker_data_livres_disponibles()
        self.__stocker_data_livres_empruntes()


if __name__ == '__main__':
    biblio = Bibliotheque()
    menu.boucle_de_saisies(biblio)