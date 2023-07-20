import random
import pygame
from pygame.locals import *
from aspirateur import Aspirateur

# Constants for grid and visualization
GRID_SIZE = 3
CELL_SIZE = 100
WINDOW_SIZE = GRID_SIZE * CELL_SIZE
FPS = 5

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRAY = (128, 128, 128)

def draw_grid(aspirateur):
    for x in range(0, WINDOW_SIZE, CELL_SIZE):
        pygame.draw.line(screen, BLACK, (x, 0), (x, WINDOW_SIZE))
    for y in range(0, WINDOW_SIZE, CELL_SIZE):
        pygame.draw.line(screen, BLACK, (0, y), (WINDOW_SIZE, y))

    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            if (x, y) in aspirateur.surface_parcourue:
                pygame.draw.rect(screen, RED, rect)
            if (x, y) == aspirateur.position:
                pygame.draw.rect(screen, GREEN, rect)
            if ('poussiere', x, y) in aspirateur.environnement:
                pygame.draw.circle(screen, GRAY, rect.center, 10)

def main():
    # Création de l'agent aspirateur avec les informations spécifiées
    aspirateur = Aspirateur(environnement=[('poussiere', 0, 0), ('poussiere', 1, 2)],
                            capteurs=['poussiere', 'camera'], actionneurs=['moteur', 'nettoyer'])

    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        screen.fill(WHITE)
        draw_grid(aspirateur)

        # Choix aléatoire d'une direction
        actions_possibles = ['Gauche', 'Droite', 'Haut', 'Bas', 'Aspirer']
        action = random.choice(actions_possibles)
        aspirateur.effectuer_action(action)
        print(aspirateur)  # Print the agent's position and state

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption("Aspirateur")
    main()
