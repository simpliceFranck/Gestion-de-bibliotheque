import pickle, os

from textwrap import dedent
from itertools import chain

import message


message.SYMBOLE
message.ESPACE



class Livre():
    '''Livre est la classe mère.'''
    def __init__(self, titre, auteur, isbn) -> None:
        self._titre = titre
        self._auteur = auteur
        self._isbn = isbn


    def description(self):
        '''Affiche les détails d'un livre'''
        menu.afficher_message(dedent(f"""\
                                        Titre  : {self._titre}
                                        Auteur : {self._auteur}
                                        Isbn   : {self._isbn}"""))


    def mise_a_jour(self, nouveau_titre, nouveau_auteur):
        self._titre = nouveau_titre
        self._auteur = nouveau_auteur


    def get_titre(self):
        return self._titre
    
    
    def get_auteur(self):
        return self._auteur
    
    
    def get_isbn(self):
        return self._isbn



class LivrePapier(Livre):
    '''Classe fille de la classe livre avec un attribut supplémentaire 'type'.'''
    def __init__(self, titre, auteur, ibsn, type='Livre papier') -> None:
        super().__init__(titre, auteur, ibsn)
        self.__type = type
    

    def description(self):
        '''Affiche les détails d'un livre papier'''
        super().description()
        print(f"Type   : {self.__type}")



class LivreNumerique(Livre):
    def __init__(self, titre, auteur, ibsn) -> None:
        super().__init__(titre, auteur, ibsn)
        self.__type = 'Livre numérique'
    

    def description(self):
        '''Affiche les détails d'un livre numérique'''
        super().description()
        print(f"Type   : {self.__type}")



class Utilisateur:
    '''Cette classe implémente des usagers de la bibliothèque.'''
    def __init__(self, nom, statut) -> None:
        self.__nom = nom
        self.__statut = statut
    

    def is_admin(self):
        '''Retourne 'True' si l'usager a le statut d'administrateur.'''
        return self.__statut == 'Admin'
    

    def get_nom(self):
        '''Elle permet d'accéder à l'attribut nom de l'extérieur.'''
        return self.__nom



        
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


class MenuInteratif:

    def afficher_message(self, message):
        '''Affiche le message qu'elle prend en paramètre'''
        print(message)

    
    def __contrôler_la_validite_de_isbn(self):
        '''Vérifie la validité de l'isbn saisi par l'utilisateur
        et retourne la valeur.'''
        while True:
            isbn = input("Isbn : ")
            if isbn.isdigit() and len(isbn) == 13:
                break
            self.afficher_message(message.VALIDITE_ISBN)
        return isbn


    def __indiquer_statut_usager(self):
        '''Récupère le statut de l'utilisateur et le retourne.'''
        while True:
            choix_statut = input(message.STATUT_USAGER)
            if choix_statut == '1':
                statut = 'Admin'
                break
            elif choix_statut == '2':
                statut = 'Abonné'
                break
        return statut


    def __indiquer_isbn_et_type_du_livre(self):
        '''Récupère l'isbn et le type du livre et les retourne.'''
        isbn = self.__contrôler_la_validite_de_isbn()
        while True:
            choix_type = input(message.TYPE_DE_LIVRE)
            if choix_type not in ['3', '4']:
                self.afficher_message("Tapez '3' ou '4' !")
            else:
                type = choix_type
                break
        return isbn, type
    

    def __indiquer_titre_et_auteur_du_livre(self):
        '''Récupère titre et auteur du livre, puis les retourne.'''
        titre = input("Titre : ").lower().title()
        auteur = input("Auteur : ").lower().title()
        return titre, auteur


    def __indiquer_isbn_du_livre_et_nom_de_emprunteur(self):
        '''Récupère l'isbn et le nom de l'emprunteur du livre, puis
        les retourne.'''
        isbn = self.__contrôler_la_validite_de_isbn()
        nom = input("Nom de l'emprunteur : ").lower().title()
        return isbn, nom 


    def boucle_de_saisies(self):
        '''Elle permet d'intéragir avec l'utilisateur.'''       
        while True:
            self.afficher_message(message.MENU)
            choix = input('Choisissez une option : ')

            if choix == '1': # Ajouter utilisateur
                self.afficher_message(message.AJOUT_USAGER)
                nom = input("Nom de l'utilisateur : ").lower().capitalize()
                statut = self.__indiquer_statut_usager()
                biblio.ajouter_utilisateur(nom, statut)

            elif choix == '2': # Supprimer utilisateur
                self.afficher_message(message.SUPPRESSION_USAGER)
                nom = input("Nom de l'utilisateur à supprimer : ").lower().capitalize()
                biblio.supprimer_utilisateur(nom)

            elif choix == '3': # Ajouter un livre
                self.afficher_message(message.AJOUT_LIVRE)
                titre, auteur = self.__indiquer_titre_et_auteur_du_livre()
                isbn, type = self.__indiquer_isbn_et_type_du_livre()
                biblio.ajouter_livre(titre, auteur, isbn, type)

            elif choix == '4': # Supprimer un livre
                self.afficher_message(message.SUPPRESSION_LIVRE)
                while True:
                    isbn = input("Isbn du livre à supprimer : ")
                    if isbn.isdigit() and len(isbn) == 13:
                        break
                    self.afficher_message(message.VALIDITE_ISBN)
                biblio.supprimer_livre(isbn)

            elif choix == '5': # Rechercher un livre
                self.afficher_message(message.RECHERCHER_LIVRE)
                choix = input("\nVotre choix : ")
                if choix == '5':
                    titre = input("Titre : ").lower().title()
                    biblio.rechercher_livre(titre=titre)
                elif choix == '6':
                    auteur = input("Auteur : ").lower().title()
                    biblio.rechercher_livre(auteur=auteur)
                elif choix == '7':
                    while True:
                        isbn = input("Isbn : ")
                        if isbn.isdigit() and len(isbn) == 13:
                            break
                        self.afficher_message(message.VALIDITE_ISBN)
                    biblio.rechercher_livre(isbn=isbn)

            elif choix == '6': # Emprunter un livre
                self.afficher_message(message.EMPRUNT_LIVRE)
                isbn, nom_emprunteur = self.__indiquer_isbn_du_livre_et_nom_de_emprunteur()
                biblio.emprunter_livre(nom_emprunteur, isbn)

            elif choix == '7': # Retourner un livre
                self.afficher_message(message.RETOUR_LIVRE)
                isbn, nom_emprunteur = self.__indiquer_isbn_du_livre_et_nom_de_emprunteur()
                biblio.retourner_livre(nom_emprunteur, isbn)

            elif choix == '8': # Lister les livres
                self.afficher_message(message.LISTE_LIVRE)
                biblio.lister_livres()
            
            elif choix == '9': # Mettre à jour un livre
                self.afficher_message(message.UPDATE_BOOK)
                nouveau_titre = input("Nouveau titre   : ").lower().title()
                nouveau_auteur = input("Nouveau auteur  : ").lower().title()
                
                ancien_titre = input("Ancien titre  : ").lower().title()
                ancien_auteur = input("Ancien auteur : ").lower().title()

                biblio.mettre_a_jour_livre(nouveau_titre, nouveau_auteur, ancien_titre, ancien_auteur)

            elif choix == '10': # Générer les statistiques
                self.afficher_message(message.STATISTIQUES)
                biblio.generer_statistiques()
            
            elif choix == '11': # Quitter le programme après avoir sauvegarder les données.
                biblio.sauvegarder_donnees()
                break


if __name__ == '__main__':
    biblio = Bibliotheque()
    menu = MenuInteratif()
    menu.boucle_de_saisies()

# dico = {1: [], 2: []}
# for i in chain(*(dico.values())):
#     if i == 5:
#         print(i)
#         break