import pygame 
import sys
from script.personaje import Cls_Personaje
from script.sprites import Cls_Sprites
from script.terreno import Cls_Terreno
from script.proyectiles import Cls_Fantasma

class Cls_Juego:
    def __init__(self):
        pygame.init()

        pygame.mixer.init()

        #nombre de la ventana 
        pygame.display.set_caption('Halloween de terror')
        #parametros ancho y largo
        self.ventana = pygame.display.set_mode((800,600))

        #los ticks a los que se moveran los frames 
        self.reloj = pygame.time.Clock()

        self.tiempo = 0
        
        self.vidas = 3


        self.obj_sprites = Cls_Sprites()
        self.sprites = self.obj_sprites.fnt_cargar_sprites(32,32,True)

        self.obj_personaje = Cls_Personaje(100,500,50,62,self.sprites)

        self.velocidad = 5
        
        self.fondo = pygame.image.load("img/fondo.png").convert()
        self.fondo = pygame.transform.scale(self.fondo, (800, 600))

        pygame.mixer.music.load("music\musica.mp3")
        pygame.mixer.music.set_volume(0.1)
        self.vidas = 3
        self.restart_game = False  # Add a restart flag

        # ... (other initialization code)

    # Add a method to reset the game state
    def fnt_reiniciar(self):
        self.segundos = 0
        self.vidas = 3
        self.restart_game = False
        self.obj_personaje = Cls_Personaje(100, 500, 50, 62, self.sprites)

    def fnt_menu_fin_juego(self,tiempo):
        self.fnt_texto("Fin del Juego",400,300,100)
        self.fnt_texto("Presiona cualquier tecla para reiniciar",400,200,40)
        self.fnt_texto(f"Tiempo de supervivencia: {tiempo}",400,500,30)
        pygame.display.flip()
        congelado = True
        while congelado:
            self.reloj.tick(60) 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYUP:
                    congelado = False
                if event.type == pygame.KEYDOWN:
                    self.fnt_reiniciar()  
                    self.inicio = True  
                    self.fin_juego = False
        
    def fnt_menu_inicio(self):
        self.fnt_texto("Bienvenido al Halloween del terror", 400,400,30)
        self.fnt_texto("Presiona cualquier tecla para iniciar", 400,500,30)
        pygame.display.flip()
        congelado = True
        while congelado:
            self.reloj.tick(60) 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYUP:
                    congelado = False
            
    def fnt_bucle_juego(self):


        ticks_iniciales=pygame.time.get_ticks()

        pygame.mixer.music.play(loops= -1)

        self.fin_juego = True

        self.inicio = True
        #Dentro del bucle se estarán actualizando los elementos de la ventana
        while True:
            
            self.segundos=(pygame.time.get_ticks()-ticks_iniciales)/1000
            self.tiempo_texto =  "{:.2f} segundos".format(self.segundos)

            if self.inicio == True:
                self.fnt_menu_inicio()
                self.fnt_elementos()
                self.inicio = False   

            if self.fin_juego == True and self.inicio == False: 
                self.fnt_menu_fin_juego(self.tiempo_texto)
                self.fnt_elementos()
                self.fin_juego = True
                
                
                



            self.reloj.tick(60)

            #self.ventana.fill((14,219,248))

            self.ventana.blit(self.fondo, [0,0])
            #actualizo su posición a 60 cuadro por segundo
            self.obj_personaje.fnt_refrescar(60)
            #Dibujo el personaje en la pantalla 
            self.obj_personaje.fnt_dibujar(self.ventana)


            #prueba
            obj_terreno = Cls_Terreno(self.ventana,800, 50, 0, 550, (8,34,57,255))
            obj_terreno_plataforma = Cls_Terreno(self.ventana,100, 10, 300, 300, (7,23,40,255))
            obj_terreno_plataforma_arbol = Cls_Terreno(self.ventana,100, 10, 650, 100, (7,23,40,255))

            #validar las colisiones con la plataforma
            if self.obj_personaje.fnt_colision_terreno(obj_terreno.terrain_rect) or \
                self.obj_personaje.fnt_colision_terreno(obj_terreno_plataforma.terrain_rect) or \
                self.obj_personaje.fnt_colision_terreno(obj_terreno_plataforma_arbol.terrain_rect):

                self.obj_personaje.velocidad_y = 0  # Detener el movimiento vertical

            colision_fantasmas = pygame.sprite.spritecollide(self.obj_personaje,self.fantasmas,True)
            if colision_fantasmas: 
                self.vidas -=  1
                
                


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w and self.obj_personaje.contador_salto < 2 :
                        self.obj_personaje.fnt_salto()



            self.todos_sprites.update()

            #alimentando de fantasmas la pantalla 
            for colision in colision_fantasmas:
                self.obj_fantasma = Cls_Fantasma()
                self.todos_sprites.add(self.obj_fantasma)
                self.fantasmas.add(self.obj_fantasma)



            self.todos_sprites.draw(self.ventana)
            
            self.fnt_movimientos()

            self.fnt_texto(str("Vidas: ") + str(self.vidas),40, 10,25)
            if self.vidas == 0:
                self.fin_juego = True


            
     
            
        

            pygame.display.flip()
           
    def fnt_elementos(self):
        self.todos_sprites = pygame.sprite.Group()
        self.fantasmas = pygame.sprite.Group()
        self.fin_juego = False
        for i in range(8):
            self.obj_fantasma = Cls_Fantasma()
            self.todos_sprites.add(self.obj_fantasma)
            self.fantasmas.add(self.obj_fantasma)

    def fnt_movimientos(self):
        

        self.obj_personaje.velocidad_x =  0
        self.tecla = pygame.key.get_pressed()

    
        if self.tecla[pygame.K_a]:
            self.obj_personaje.fnt_movimiento_izquierda(self.velocidad)
        if self.tecla[pygame.K_d]:
            self.obj_personaje.fnt_movimiento_derecha(self.velocidad)

    def fnt_texto(self,texto,x,y,tamano):
        fuente = pygame.font.SysFont("serif", tamano)
        texto_ventana = fuente.render(texto, True, (255, 255, 255))
        text_rect = texto_ventana.get_rect()
        text_rect.midtop = (x,y)
        self.ventana.blit(texto_ventana, text_rect)
        


if __name__ == "__main__":
    obj_juego = Cls_Juego()
    obj_juego.fnt_bucle_juego()



