
import pygame
from sys import exit
import random


# game variables

Game_Width = 360
Game_Height = 640

# bird class
bird_x = Game_Width/8
bird_y = Game_Height/3
bird_width = 34
bird_height = 24

class Bird(pygame.Rect):
    def __init__(self, img):
        pygame.Rect.__init__(self, bird_x, bird_y, bird_width, bird_height)
        self.img = img

# Pipe class
pipe_x = Game_Width
pipe_y = 0
pipe_width = 64
pipe_height = 512

class Pipe(pygame.Rect):
    def __init__(self, img):
        pygame.Rect.__init__(self, pipe_x, pipe_y, pipe_width, pipe_height)
        self.img = img
        self.passed = False

# Game image
background_image = pygame.image.load("bg_5.png")
bird_image = pygame.image.load("flappy2.png")
bird_image = pygame.transform.scale(bird_image, (bird_width, bird_height))
top_pipe_image = pygame.image.load("toppipe.png")
top_pipe_image = pygame.transform.scale(top_pipe_image, (pipe_width, pipe_height))
bottom_pipe_image = pygame.image.load("bottompipe.png")
bottom_pipe_image = pygame.transform.scale(bottom_pipe_image, (pipe_width, pipe_height))


# Game Logic
bird = Bird(bird_image)
pipes = []
velocity_x = -2 # move pipes to the left speed (simulates bird moving right )
velocity_y = 0 # move bird up/down speed 
gravity = 0.4
score = 0
game_over = False


def draw():
    window.blit(background_image, (0,0))
    window.blit(bird.img, bird)

    for pipe in pipes:
        window.blit(pipe.img, pipe)

    text_str = str(int(score))
    if game_over:
        text_str = "Game Over: " + text_str



    text_font = pygame.font.SysFont("Comic Sans MS", 45)
    text_rander = text_font.render(text_str, True , "white")
    window.blit(text_rander, (5, 0))

def move():
    global score
    global velocity_y , game_over
    velocity_y += gravity
    bird.y += velocity_y 
    bird.y = max(bird.y, 0)


    if bird.y > Game_Height:
        game_over = True
        return 

    for pipe in pipes:
        pipe.x += velocity_x


        if not pipe.passed and bird.x > pipe.x + pipe_width:
            score += 0.5 # 0.5 because there are 2 pipes! 0.5*2 = 1 , 1 per set of pipes 
            pipe.passed = True

        if bird.colliderect(pipe):
            game_over = True
            return 

    while len(pipes) > 0 and pipes[0].x < -pipe_width:
        pipes.pop(0) # removes first element from the list 

def create_pipes():
    random_pipe_y = pipe_y - pipe_height/4 - random.random()*(pipe_height/2) #0-h/2 

    opening_space = Game_Height/4

    top_pipe = Pipe(top_pipe_image)
    top_pipe.y = random_pipe_y
    pipes.append(top_pipe)

    bottom_pipe = Pipe(bottom_pipe_image)
    bottom_pipe.y = top_pipe.y + top_pipe.height + opening_space
    pipes.append(bottom_pipe)

    #print(len(pipes))


pygame.init()
window = pygame.display.set_mode((Game_Width,Game_Height))

pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()


create_pipes_timer = pygame.USEREVENT + 0
pygame.time.set_timer(create_pipes_timer, 1500) # marks every 1.5 seconds 


while True: # Game Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == create_pipes_timer and not game_over:
            create_pipes()

        if event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_SPACE, pygame.K_x, pygame.K_UP):
                velocity_y = -6

            # Reset game
            if game_over:
                bird.y = bird_y
                pipes.clear()
                score = 0
                game_over = False


    if not game_over:
        move()
        draw()
        pygame.display.update()
        clock.tick(60)  #60 fps


    



