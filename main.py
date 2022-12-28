from game import Game
import sys
import pygame
pygame.init()

# charger la classe Game
game = Game()

# afficher la fenetre
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Morpion')

# la boucle du jeu
running = True

# couleur blanche
WHITE = (254, 254, 254)


# création de la grille du jeu
def show_grid():

    for i in range(1, 3):
        pygame.draw.line(screen, WHITE, (400 / 3 * i, 0), (400 / 3 * i, 400), 6)
        pygame.draw.line(screen, WHITE, (0, 400 / 3 * i), (400, 400 / 3 * i), 6)


def draw_circle(x, y):
    pygame.draw.circle(screen, WHITE, (x, y), 50, 7)


def if_collide_with_mouse():
    if pygame.mouse.get_pressed()[0]:

        for rect in game.rect_collisions:
            pos = pygame.mouse.get_pos()
            if pygame.Rect(game.rect_collisions[rect]).collidepoint(pos):
                x_position = game.rect_position_x[rect]
                y_position = game.rect_position_y[rect]
                draw_circle(x_position, y_position)
                pygame.time.wait(200)


game.rect_collide()
while running:
    # afficher la grille de jeu
    show_grid()

    # vérifier si une case a été cliquée
    if_collide_with_mouse()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()
sys.exit()
