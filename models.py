from textwrap import dedent
from menu import menu


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
        # Le name mangling je ne suis pas convaincu.
    

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