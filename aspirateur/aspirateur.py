class Aspirateur:
    def __init__(self, environnement, capteurs, actionneurs):
        self.environnement = environnement
        self.capteurs = capteurs
        self.actionneurs = actionneurs
        self.position = (0, 0)  # Position initiale de l'agent (coin supérieur gauche)
        self.surface_parcourue = set()  # Ensemble des positions déjà parcourues

    def se_deplacer(self, direction):
        x, y = self.position

        if direction == 'Gauche':
            x -= 1
        elif direction == 'Droite':
            x += 1
        elif direction == 'Haut':
            y -= 1
        elif direction == 'Bas':
            y += 1

        # Vérification des limites de l'espace de déplacement
        if 0 <= x < 3 and 0 <= y < 3:
            self.position = (x, y)
            self.surface_parcourue.add((x, y))
            return True
        else:
            return False

    def aspirer_poussiere(self):
        x, y = self.position
        if (x, y) == (0, 0) and 'poussiere' in self.capteurs:
            return True
        else:
            return False

    def afficher_etat(self):
        x, y = self.position
        etat = 'Propre' if (x, y) not in self.surface_parcourue else 'Sale'
        return etat

    def nettoyer_position(self):
        x, y = self.position
        if (x, y) in self.surface_parcourue:
            self.surface_parcourue.remove((x, y))
            return True
        else:
            return False

    def effectuer_action(self, action):
        if action == 'Gauche' or action == 'Droite' or action == 'Haut' or action == 'Bas':
            return self.se_deplacer(action)
        elif action == 'Aspirer':
            return self.aspirer_poussiere()
        elif action == 'Nettoyer':
            return self.nettoyer_position()
        else:
            return False

    def __str__(self):
        return f"Position: {self.position}, Etat: {self.afficher_etat()}"
