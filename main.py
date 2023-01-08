from game import Game
import sys
import pygame
pygame.init()

# charger la classe Game
game = Game()

# cercle ou croix
# circle_or_cross = 0

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


def draw_cross(x, y):
    for i in range(1, 3):
        pygame.draw.line(screen, WHITE, (x + 50, y - 50), (x - 50, y + 50), 7)
        pygame.draw.line(screen, WHITE, (x - 50, y - 50), (x + 50, y + 50), 7)


def if_collide_with_mouse():
    if pygame.mouse.get_pressed()[0]:
        for rect in game.rect_collisions:
            pos = pygame.mouse.get_pos()
            if pygame.Rect(game.rect_collisions[rect]).collidepoint(pos):
                x_position = game.rect_position_x[rect]
                y_position = game.rect_position_y[rect]
                if game.crosses[rect] == 'None':
                    if game.circles[rect] == 'None':
                        game.i += 1
                        pygame.time.wait(60)

                        if (game.i % 2) == 0:
                            game.circles[rect] = 'circle'
                            game.circles_x[rect] = x_position
                            game.circles_y[rect] = y_position

                        else:
                            game.crosses[rect] = 'cross'
                            game.crosses_x[rect] = x_position
                            game.crosses_y[rect] = y_position

                    pygame.time.wait(60)
                    print(game.circles)
                    print(game.crosses)


def if_inline_symbols(symbol):
    for i in range(1, 4):
        num = 0
        for x in range(1, 4):
            for circle in game.circles:
                num += 1
                if game.circles[circle] == num:
                    game.win += 1

                if game.win == 3:
                    print(f"win de {symbol}")


game.rect_collide()

for i in range(1, 10):
    game.crosses[i] = 'None'
    game.circles[i] = 'None'

print(game.crosses)
print(game.circles)

while running:
    # afficher la grille de jeu
    show_grid()

    # vérifier si une case a été cliquée
    if_collide_with_mouse()

    # dessiner les croix et les cercles
    for circle in game.circles:
        if not game.circles[circle] == 'None':
            draw_circle(game.circles_x[circle], game.circles_y[circle])

    for cross in game.crosses:
        if not game.crosses[cross] == 'None':
            draw_cross(game.crosses_x[cross], game.crosses_y[cross])

    # vérifier si on a un alignement de symboles
    # if_inline_symbols("cross")

    # vérifier si des cercles ou des croix sont alignées
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()
sys.exit()
