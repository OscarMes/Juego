import pygame

import random


class Cls_Fantasma(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img/enemigo.png").convert_alpha()
        #self.imagen.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(800 - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy  = random.randrange(1, 10)
        self.speedx = random.randrange(-5, 5)

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx

        if self.rect.top > 600 + 10 or self.rect.left < -25 or self.rect.right > 800 + 25 :
            self.rect.x = random.randrange(800 - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 10)