from textwrap import dedent

SYMBOLE = '-'
ESPACE = ' '

UPDATE_OK = "\nMise à jour effectuée avec succès."
BORROWER_NOT_EXIST = "\nL'emprunteur n'est pas connu de nos services."
BOOK_NOT_FOUND = "\nLe livre n'a pas été trouvé."
USER_NOT_FOUND = "L'utilisateur n'a pas été trouvé."
VALIDITE_ISBN = "L'isbn doit être une suite de treize chiffres."
ADD_USER = "\nL'utilisateur a été ajouté avec succès."
ADD_BOOK = "\nLe livre a été ajouté avec succès."
BOOK_EXIST = "\nAjout impossible : le livre existe déjà."
USER_EXIST = "\nAjout impossible : l'utilisateur existe déjà."
USER_NOT_EXIST = "\nSuppression impossible : l'utilisateur n'existe pas."
BOOK_NOT_EXIST = "\nSuppression impossible : le livre n'existe pas."
NOT_ADMIN = "\nVotre statut ne vous permet pas d'effectuer cette opération."
STATUT_USAGER = "Statut de l'usager (tapez 1 pour 'Admin' ou 2 pour 'Abonné'): "
OPERATION_IMPOSSIBLE = "\nÉchec : aucun livre ne correspond à l'Isbn !"
SUPPRESSION_USAGER_REUSSIE = "\nL'utilisateur a été supprimé avec succès."
SUPPRESSION_LIVRE_REUSSIE = "\nLe livre a été supprimé avec succès."
EMPRUNT_LIVRE_REUSSI ="\nL'emprunt a été effectué avec succès."
RETOUR_LIVRE_REUSSI = "\nL'opération 'retour livre' s'est effectuée avec succès."
AJOUT_USAGER_IMPOSSIBLE = "\nAjout impossible : Vous n'êtes pas connu de nos services."
RETOUR_IMPOSSIBLE = "\nÉchec : le livre retourné ne correspond pas à celui emprunté."
MISE_A_JOUT_IMPOSSIBLE = "\nÉchec : l'ancien livre sur lequel effectué la mise à jour n'existe pas."


MENU = dedent(f"""
                {SYMBOLE*22}MENU ITERATIF{SYMBOLE*22}
                Ajouter un utilisateur{ESPACE*25}: tapez 1
                Supprimer un utilisateur{ESPACE*23}: tapez 2
                Ajouter un livre{ESPACE*31}: tapez 3
                Supprimer un livre{ESPACE*29}: tapez 4
                Rechercher un livre{ESPACE*28}: tapez 5                        
                Emprunter un livre{ESPACE*29}: tapez 6
                Retourner un livre{ESPACE*29}: tapez 7
                Lister les livres{ESPACE*30}: tapez 8
                Mettre à jour des informations d'un livre{ESPACE*5} : tapez 9
                Statistiques{ESPACE*35}: tapez 10                        
                Quitter{ESPACE*40}: tapez 11\n""")

RECHERCHER_LIVRE = dedent(f"""
                            {SYMBOLE*18}RECHERCHE D'UN LIVRE{SYMBOLE*18}
                            La recherche d'un livre peut se faire :
                            - Par Titre (tapez 5)
                            - Par Auteur (tapez 6)
                            - Par Isbn (tapez 7).""")

AJOUT_USAGER = f"\n{SYMBOLE*17}AJOUT D'UN UTILISATEUR{SYMBOLE*17}"
SUPPRESSION_USAGER = f"\n{SYMBOLE*14}SUPPRESSION D'UN UTILISATEUR{SYMBOLE*14}"
AJOUT_LIVRE = f"\n{SYMBOLE*20}AJOUT D'UN LIVRE{SYMBOLE*20}"
SUPPRESSION_LIVRE = f"\n{SYMBOLE*17}SUPPRESSION D'UN LIVRE{SYMBOLE*17}"
TYPE_DE_LIVRE = "Type du livre (tapez 3 pour 'Livre papier' ou 4 pour 'Livre numérique') :"
EMPRUNT_LIVRE = f"\n{SYMBOLE*19}EMPRUNT D'UN LIVRE{SYMBOLE*19}"
RETOUR_LIVRE = f"\n{SYMBOLE*17}RESTITUTION D'UN LIVRE{SYMBOLE*17}"
LISTE_LIVRE = f"\n{SYMBOLE*20}LISTE DE LIVRES{SYMBOLE*20}"
UPDATE_BOOK = f"\n{SYMBOLE*17}MISE A JOUR D'UN LIVRE{SYMBOLE*17}"
STATISTIQUES = f"\n{SYMBOLE*20}LES STATISTIQUES{SYMBOLE*20}"