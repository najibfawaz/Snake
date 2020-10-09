import pygame
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (200, 0, 0)
green = (0, 100, 0)
orange = (255, 165, 0)
dark_violet = (148, 0, 211)

window_size = 750
block_num = 30
square_size = window_size // block_num

score = 0
score_font = pygame.font.Font('freesansbold.ttf', 25)

gameover_font = pygame.font.Font('freesansbold.ttf', 64)

playagain_font = pygame.font.Font('freesansbold.ttf', 20)

score_x = 10
score_y = 10

noob_x = window_size // 2 - 125
noob_y = window_size // 2 - 50

new_buttonx = noob_x + 350
new_buttony = noob_y + 500

dx = 0
dy = 0

delay = 1

fps = 10

pygame.init()

window = pygame.display.set_mode((window_size, window_size))  # size of the window
pygame.display.set_caption('Snake')  # title
background_image = pygame.image.load("snake_bg.png").convert()
window.blit(background_image, [0, 0])

clock = pygame.time.Clock()


class Snake(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


def Snake_coordinates():
    x = random.randrange(0, block_num) * square_size
    y = random.randrange(0, block_num) * square_size
    return x, y


grow = []


def show_score(x, y, txt):
    score_colour = score_font.render(txt, True, black)
    window.blit(score_colour, (x, y))


def game_over():
    gameover_colour = gameover_font.render("NOOB!!!", True, black)
    window.blit(gameover_colour, ((window_size // 2) - 125, (window_size // 2 - 50)))


def play_again():
    playagain_colour = playagain_font.render("New Game", True, black)
    window.blit(playagain_colour, (new_buttonx // 2 + 20, new_buttony // 2 + 10))


def modes():
    easy_colour = playagain_font.render("Easy", True, black)
    window.blit(easy_colour, (new_buttonx // 2 + 50, new_buttony // 2 - 50))

    medium_colour = playagain_font.render("Medium", True, black)
    window.blit(medium_colour, (new_buttonx // 2 + 35, new_buttony // 2 + 10))

    hard_colour = playagain_font.render("Hard", True, black)
    window.blit(hard_colour, (new_buttonx // 2 + 50, new_buttony // 2 + 70))


def random_position():
    x = random.randrange(0, block_num) * square_size
    y = random.randrange(0, block_num) * square_size
    return x, y


def draw_grid():
    for x in range(block_num):
        for y in range(block_num):
            rect = pygame.Rect(x * square_size, y * square_size, square_size, square_size)
            pygame.draw.rect(window, black, rect, 1)


def draw_controlled():
    for obj in grow:
        controlled_surface = pygame.Surface((square_size, square_size))
        controlled_surface.fill(orange)
        window.blit(controlled_surface, (obj.x, obj.y))


def clear_controlled(a, b):
    controlled_surface = pygame.Surface((square_size, square_size))
    controlled_surface.fill(white)
    window.blit(controlled_surface, (a, b))


def draw_apple(a, b):
    # colour a random square
    coloured_surface = pygame.Surface((square_size, square_size))
    coloured_surface.fill(red)
    window.blit(coloured_surface, (a, b))


def clear_apple():
    window.blit(background_image, [0, 0])
    show_score(score_x, score_y, "Score: " + str(score))


def button_new():
    mouse = pygame.mouse.get_pos()
    if new_buttonx / 2 <= mouse[0] <= new_buttonx / 2 + 140 and new_buttony / 2 <= mouse[1] <= new_buttony / 2 + 40:
        pygame.draw.rect(window, orange, [new_buttonx // 2, new_buttony // 2, 140, 40])

    else:
        pygame.draw.rect(window, red, [new_buttonx // 2, new_buttony // 2, 140, 40])


def button_mode():
    mouse = pygame.mouse.get_pos()
    if new_buttonx / 2 <= mouse[0] <= new_buttonx / 2 + 140 and new_buttony / 2 - 60 <= mouse[
        1] <= new_buttony / 2 - 20:
        pygame.draw.rect(window, orange, [new_buttonx // 2, new_buttony // 2 - 60, 140, 40])
    else:
        pygame.draw.rect(window, red, [new_buttonx // 2, new_buttony // 2 - 60, 140, 40])

    if new_buttonx / 2 <= mouse[0] <= new_buttonx / 2 + 140 and new_buttony / 2 <= mouse[1] <= (
            new_buttony / 2 + 40):
        pygame.draw.rect(window, orange, [new_buttonx // 2, new_buttony // 2, 140, 40])
    else:
        pygame.draw.rect(window, red, [new_buttonx // 2, new_buttony // 2, 140, 40])

    if new_buttonx / 2 <= mouse[0] <= new_buttonx / 2 + 140 and new_buttony / 2 + 60 <= mouse[
        1] <= new_buttony / 2 + 100:
        pygame.draw.rect(window, orange, [new_buttonx // 2, new_buttony // 2 + 60, 140, 40])
    else:
        pygame.draw.rect(window, red, [new_buttonx // 2, new_buttony // 2 + 60, 140, 40])


loop = True
mode = True
new = False
first_game = True

randx, randy = random_position()

pygame.display.update()

while loop:
    pygame.display.update()

    if len(grow) == 0 and new and not mode:
        button_new()
        play_again()

    if len(grow) == 0 and (mode or first_game):
        new = False
        button_mode()
        modes()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            # if the mouse is clicked on the
            # button the game is terminated
            if new_buttonx / 2 <= mouse[0] <= new_buttonx / 2 + 140 and new_buttony / 2 <= mouse[
                1] <= new_buttony / 2 + 40 and not mode and new:
                mode = True
                clear_apple()
                button_mode()

            if new_buttonx / 2 <= mouse[0] <= new_buttonx / 2 + 140 and new_buttony / 2 - 60 <= mouse[
                1] <= new_buttony / 2 - 20 and mode and not new:
                first_game = False
                mode = False
                fps = 7
                score = 0
                clear_apple()
                controlledx, controlledy = Snake_coordinates()
                grow.append(Snake(controlledx, controlledy))
                draw_controlled()
                draw_apple(randx, randy)

            if new_buttonx / 2 <= mouse[0] <= new_buttonx / 2 + 140 and new_buttony / 2 <= mouse[1] <= (
                    new_buttony / 2 + 40) and mode and not new:
                first_game = False
                mode = False
                fps = 10
                score = 0
                clear_apple()
                controlledx, controlledy = Snake_coordinates()
                grow.append(Snake(controlledx, controlledy))
                draw_controlled()
                draw_apple(randx, randy)

            if new_buttonx / 2 <= mouse[0] <= new_buttonx / 2 + 140 and new_buttony / 2 + 60 <= mouse[
                1] <= new_buttony / 2 + 100 and mode:
                first_game = False
                mode = False
                fps = 13
                score = 0
                clear_apple()
                controlledx, controlledy = Snake_coordinates()
                grow.append(Snake(controlledx, controlledy))
                draw_controlled()
                draw_apple(randx, randy)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and dx == 0 and len(grow) != 0:
                dx = -square_size
                dy = 0
                break
            elif event.key == pygame.K_RIGHT and dx == 0 and len(grow) != 0:
                dx = square_size
                dy = 0
                break
            elif event.key == pygame.K_DOWN and dy == 0 and len(grow) != 0:
                dx = 0
                dy = square_size
                break
            elif event.key == pygame.K_UP and dy == 0 and len(grow) != 0:
                dx = 0
                dy = -square_size
                break

    if len(grow) != 0:
        if randx == grow[-1].x and randy == grow[-1].y:
            score += 1
            clear_apple()
            randx, randy = random_position()
            draw_apple(randx, randy)
            grow.append(Snake(grow[-1].x + dx, grow[-1].y + dy))

    if dx < 0:
        clear_apple()
        grow.append(Snake(grow[-1].x - square_size, grow[-1].y))
        grow.pop(0)
    if dx > 0:
        clear_apple()
        grow.append(Snake(grow[-1].x + square_size, grow[-1].y))
        grow.pop(0)
    if dy > 0:
        clear_apple()
        grow.append(Snake(grow[-1].x, grow[-1].y + square_size))
        grow.pop(0)
    if dy < 0:
        clear_apple()
        grow.append(Snake(grow[-1].x, grow[-1].y - square_size))
        grow.pop(0)

    if len(grow) != 0:
        if grow[-1].x < -1 or grow[-1].x >= window_size or grow[
            -1].y >= window_size or grow[-1].y < -1:
            grow.clear()
            dx, dy = 0, 0
            clear_apple()
            game_over()
            new = True
            mode = False
            button_new()
            continue
        draw_apple(randx, randy)
        draw_controlled()
        pygame.display.update()

        for i in range(len(grow) - 2):
            if grow[i].x == grow[-1].x and grow[i].y == grow[-1].y:
                grow.clear()
                dx, dy = 0, 0
                clear_apple()
                game_over()
                new = True
                mode = False
                button_new()
                break

    pygame.display.update()
    clock.tick(fps)
