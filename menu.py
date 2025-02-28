import message

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

    def boucle_de_saisies(self, biblio):
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

# Instance globale de MenuInteractif
menu = MenuInteratif() 