import pygame 
from os import listdir
from os.path import isfile, join

class Cls_Sprites:
    def fnt_direccion(self,sprites):

        flipped_sprites = []

        for sprite in sprites:
            flipped_sprite = pygame.transform.flip(sprite, True, False)
            flipped_sprites.append(flipped_sprite)

        return flipped_sprites

    def fnt_cargar_sprites(self,ancho,largo,direccion = False):

        self.ruta = 'img/VirtualGuy'

        self.imagenes = []
        for f in listdir(self.ruta):
            if isfile(join(self.ruta, f)):
                self.imagenes.append(f)

        self.todos_sprites = {}

        for imagen in self.imagenes:
            self.hoja_sprites = pygame.image.load(join(self.ruta, imagen)).convert_alpha()

            self.sprites = []

            for i in range(self.hoja_sprites.get_width()//ancho):
                buscar = pygame.Surface((ancho,largo), pygame.SRCALPHA, 32)
                rectangulo = pygame.Rect(i * ancho,0,ancho,largo)
                buscar.blit(self.hoja_sprites, (0,0), rectangulo)
                self.sprites.append(pygame.transform.scale2x(buscar))

            if direccion:
                self.todos_sprites[imagen.replace(".png", "") + "_derecha"] = self.sprites
                self.todos_sprites[imagen.replace(".png", "") + "_izquierda"] = self.fnt_direccion(self.sprites)
            else:
                self.todos_sprites[imagen.replace(".png", "")] = self.sprites
        return self.todos_sprites
    
    