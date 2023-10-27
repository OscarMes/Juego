import pygame 
import sys

from logic.componentes import fnt_imagenes
from logic.movimiento import Cls_movimiento

class Cls_Juego:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Batalla')
        self.ventana = pygame.display.set_mode((800,600))
        self.reloj = pygame.time.Clock()
        self.moviento = [False, False]

        self.dict_elementos = {
            'caballero': fnt_imagenes('caballero_reposo/golden knight animation idle breathing_00001.png')
        }

        self.personaje = Cls_movimiento(self,"caballero", (50,50),(1,1))

    def fnt_bucle_juego(self):

        #Dentro del bucle se estarán actualizando los elementos de la ventana
        while True:

            self.ventana.fill((14,219,248))
            self.personaje.fnt_actualizacion((self.moviento[1] - self.moviento[0], 0))
            self.personaje.fnt_renderizar(self.ventana)



            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                self.fnt_movimientos(event)
            pygame.display.update()
            self.reloj.tick(60)



    def fnt_movimientos(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.moviento[0] = True
            if event.key == pygame.K_d:
                self.moviento[1] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                self.moviento[0] = False
            if event.key == pygame.K_d:
                self.moviento[1] = False 



if __name__ == "__main__":
    obj_juego = Cls_Juego()
    obj_juego.fnt_bucle_juego()



