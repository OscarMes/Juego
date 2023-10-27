import pygame

class Cls_Terreno:
    def __init__(self,ventana,ancho,alto,pos_x,pos_y,color):

        self.ventana = ventana
        green = (110, 44, 0 )

        ancho_terreno, alto_terreno = ancho, alto
        x_terreno, y_terreno = pos_x, pos_y
        self.terrain_rect = pygame.Rect(x_terreno, y_terreno, ancho_terreno, alto_terreno)
        pygame.draw.rect(self.ventana, color, self.terrain_rect)

        