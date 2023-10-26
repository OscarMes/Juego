import pygame 
import sys

class Cls_Juego:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Batalla')

        self.ventana = pygame.display.set_mode((800,600))

        self.reloj = pygame.time.Clock()

        self.moviento = [False, False]


    def fnt_bucle_juego(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                self.fnt_movimientos(event)
            pygame.display.update()
            self.reloj.tick(60)

    def fnt_movimientos(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.moviento[0] = True
            if event.key == pygame.K_DOWN:
                self.moviento[1] = True



if __name__ == "__main__":
    obj_juego = Cls_Juego()
    obj_juego.fnt_bucle_juego()



