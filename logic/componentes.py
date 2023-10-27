import pygame 

img_path = "img/"

def fnt_imagenes(direccion):
    img = pygame.image.load(img_path + direccion).convert_alpha()
    #img = img.convert_alpha()
    #img.set_colorkey((0,0,0))
    return img