import pygame
import random
pygame.init()
screen = pygame.display.set_mode((736, 414))
pygame.display.set_caption("Harry Potter - the boy,who lived...")

hp = pygame.image.load('IMG_6229.JPG')
player = pygame.image.load('avatar.png')
hat = pygame.image.load('hat (2).png')
music = pygame.mixer.Sound('21071.mp3')
music.play()
grifindor = pygame.mixer.Sound('Распределяющая - Шляпа (www.hotplayer.ru).mp3')
slytherin = pygame.mixer.Sound('Распределяющая шляпа - Слизерин (www.hotplayer.ru).mp3')
kogtevran = pygame.mixer.Sound('Распределяющая шляпа — Когтевран (www.lightaudio.ru).mp3')
puff = pygame.mixer.Sound('Распределяющая шляпа — Пуффедуй (www.lightaudio.ru).mp3')

def a(x):
    if x == 1:
        pygame.mixer.Sound.play(grifindor)
    elif x == 2:
        pygame.mixer.Sound.play(slytherin)
    elif x == 3:
        pygame.mixer.Sound.play(kogtevran)
    elif x == 4:
        pygame.mixer.Sound.play(puff)

player_speed = 0.5
player_x = 0

running = True
while running:

    screen.blit(hp, (0, 0))
    screen.blit(player, (player_x, 200))
    screen.blit(hat, (250, 15))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    elif keys[pygame.K_RIGHT]:
        player_x += player_speed

    if player_x == 250:
        x = random.randint(1, 4)
        a(x)


    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
