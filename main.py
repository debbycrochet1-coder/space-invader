import pygame
import random

pygame .init()

WIDTH, HEIGHT= 1280, 720
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Collision")

background=pygame.transform.scale(
    pygame.image.load("game.webp"), (WIDTH, HEIGHT)
)


class Sprite(pygame.sprite.Sprite):
    def __init__(self,color):
        super().__init__()
        self.image=pygame.Surface((30,20))
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y

        self.rect.clamp_ip(screen.get_rect())



player = Sprite("Purple")
target = Sprite("Blue")

player.rect.topleft =(
    random.randint(0, WIDTH - 30),
    random.randint(0, HEIGHT - 20)
)

target.rect.topleft =(
    random.randint(0, WIDTH - 30),
    random.randint(0, HEIGHT - 20)
)

sprites = pygame.sprite.Group(player, target)

running = True
won = False
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not won:
        keys = pygame.key.get_pressed()
        x = keys[pygame.K_RIGHT] - keys[pygame.K_LEFT] * 5
        y = keys[pygame.K_DOWN] - keys[pygame.K_UP] * 5

        player.move(x, y)

        if player.rect.colliderect(target.rect):
            sprites.remove(target)
            won = True

    screen.blit(background, (0, 0))
    sprites.draw(screen)

    if won:
        font = pygame.font.SysFont("Comic Sans MS", 72)
        text = font.render("YOU WON!", True, "black")
        screen.blit(text, text.get_rect(center= screen.get_rect().center))


    pygame.display.flip()
    clock.tick(60)

pygame.quit()  
    