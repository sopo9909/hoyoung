import pygame
import random
pygame.init()

screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("똥 피하기")

clock = pygame.time.Clock()

background = pygame.image.load("C:\\Users\\701\\kdigital\\lecture\\pygame_basic\\background.png")

character = pygame.image.load("C:\\Users\\701\\kdigital\\lecture\\pygame_basic\\character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width/2) - (character_width/2)
character_y_pos = screen_height - character_height

to_x = 0
to_y = 0

character_speed = 0.6

enmey1 = pygame.image.load("C:\\Users\\701\\kdigital\\lecture\\pygame_basic\\enmey.png")
enmey1_size = enmey1.get_rect().size
enmey1_width = enmey1_size[0]
enmey1_height = enmey1_size[1]
enmey1_x_pos = random.randint(0,screen_width-enmey1_width)
enmey1_y_pos = 0
enmey1_speed = 10

enmey2 = pygame.image.load("C:\\Users\\701\\kdigital\\lecture\\pygame_basic\\enmey.png")
enmey2_size = enmey2.get_rect().size
enmey2_width = enmey2_size[0]
enmey2_height = enmey2_size[1]
enmey2_x_pos = random.randint(0,screen_width-enmey2_width)
enmey2_y_pos = 0
enmey2_speed = 10

enmey3 = pygame.image.load("C:\\Users\\701\\kdigital\\lecture\\pygame_basic\\enmey.png")
enmey3_size = enmey3.get_rect().size
enmey3_width = enmey3_size[0]
enmey3_height = enmey3_size[1]
enmey3_x_pos = random.randint(0,screen_width-enmey3_width)
enmey3_y_pos = 0
enmey3_speed = 10

enmey4 = pygame.image.load("C:\\Users\\701\\kdigital\\lecture\\pygame_basic\\enmey.png")
enmey4_size = enmey4.get_rect().size
enmey4_width = enmey4_size[0]
enmey4_height = enmey4_size[1]
enmey4_x_pos = random.randint(0,screen_width-enmey4_width)
enmey4_y_pos = 0
enmey4_speed = 10

game_font = pygame.font.Font(None, 40)
total_time = 10
start_ticks = pygame.time.get_ticks()

running = True
while running:
    dt = clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    character_x_pos += to_x * dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    enmey1_y_pos += enmey1_speed
    enmey2_y_pos += enmey2_speed
    enmey3_y_pos += enmey3_speed
    enmey4_y_pos += enmey4_speed
    if enmey1_y_pos > screen_height:
        enmey1_y_pos=0
        enmey1_x_pos = random.randint(0,screen_width-enmey1_width)
    if enmey2_y_pos > screen_height:
        enmey2_y_pos = 0
        enmey2_x_pos = random.randint(0, screen_width - enmey2_width)
    if enmey3_y_pos > screen_height:
        enmey3_y_pos = 0
        enmey3_x_pos = random.randint(0, screen_width - enmey3_width)
    if enmey4_y_pos > screen_height:
        enmey4_y_pos = 0
        enmey4_x_pos = random.randint(0, screen_width - enmey4_width)


    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enmey1_rect = enmey1.get_rect()
    enmey1_rect.left = enmey1_x_pos
    enmey1_rect.top = enmey1_y_pos

    enmey2_rect = enmey2.get_rect()
    enmey2_rect.left = enmey2_x_pos
    enmey2_rect.top = enmey2_y_pos

    enmey3_rect = enmey3.get_rect()
    enmey3_rect.left = enmey3_x_pos
    enmey3_rect.top = enmey3_y_pos

    enmey4_rect = enmey4.get_rect()
    enmey4_rect.left = enmey4_x_pos
    enmey4_rect.top = enmey4_y_pos

    # 충돌체크
    if character_rect.colliderect(enmey1_rect):
        print("충돌했어요")
        running = False
    if character_rect.colliderect(enmey2_rect):
        print("충돌했어요")
        running = False
    if character_rect.colliderect(enmey3_rect):
        print("충돌했어요")
        running = False
    if character_rect.colliderect(enmey4_rect):
        print("충돌했어요")
        running = False
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enmey1, (enmey1_x_pos, enmey1_y_pos))
    screen.blit(enmey2, (enmey2_x_pos, enmey2_y_pos))
    screen.blit(enmey4, (enmey4_x_pos, enmey4_y_pos))
    screen.blit(enmey3, (enmey3_x_pos, enmey3_y_pos))

    pygame.display.update()