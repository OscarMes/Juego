import pygame 
from script.sprites import Cls_Sprites



class Cls_Personaje(pygame.sprite.Sprite):
    def __init__(self,x,y,ancho,alto,sprite):
        self.rect = pygame.Rect(x,y,ancho,alto)

        self.gravedad = 1
        self.delay_animacion = 3
        self.velocidad_x = 0
        self.velocidad_y = 0
        self.mascara = None
        self.direccion = "izquierda"
        self.contador_animacion = 0
        self.contador_caida = 0
        self.contador_salto = 0
        
        self.SPRITE = sprite



        self.proyectiles = pygame.sprite.Group()

    def disparar(self, imagen_proyectil, velocidad_proyectil):
        if self.direccion == "izquierda":
            velocidad_x = -velocidad_proyectil
        else:
            velocidad_x = velocidad_proyectil



        

    def fnt_dibujar_proyectiles(self, ventana):
        self.proyectiles.draw(ventana)


    def fnt_salto(self):
        self.velocidad_y = -self.gravedad * 8 
        self.contador_animacion = 0
        self.contador_salto += 1
        if self.contador_salto == 1:
            self.contador_caida = 0




    def fnt_colision_terreno(self, terreno_rect):
        if self.rect.colliderect(terreno_rect):
            self.rect.y = terreno_rect.top - self.rect.height
            self.velocidad_y = 0
            self.contador_caida = 0  # Reiniciar el contador de caída
            self.contador_salto = 0
            return True
        return False


    

    def fnt_movimiento(self,direccion_x, direccion_y):
        self.rect.x += direccion_x
        self.rect.y += direccion_y

    def fnt_movimiento_izquierda(self, velocidad):
        self.velocidad_x =  -velocidad
        if self.direccion != "izquierda":
            self.direccion = "izquierda"
            self.contador_animacion = 0

    def fnt_movimiento_derecha(self,velocidad):
        self.velocidad_x =  velocidad
        if self.direccion != "derecha":
            self.direccion = "derecha"
            self.contador_animacion = 0

    def fnt_refrescar(self,fps):
        self.velocidad_y += min(1, (self.contador_caida / fps) * self.gravedad)
        self.fnt_movimiento(self.velocidad_x, self.velocidad_y)

        self.contador_caida += 1

        self.proyectiles.update()

        self.fnt_refrescar_sprite()

    def fnt_refrescar_sprite(self):
        
        #reposo
        hoja_sprites = "idle"

        if self.velocidad_y < 0:
            if self.contador_salto == 1:             
                hoja_sprites = "jump"
            elif self.contador_salto == 2:
                hoja_sprites  = "double_jump"

        elif self.velocidad_y > self.gravedad * 2:
            hoja_sprites = "fall"

        elif self.velocidad_x != 0:
            hoja_sprites = "run"
        
        nombre_hoja_sprites = hoja_sprites + "_" + self.direccion
        sprites  = self.SPRITE[nombre_hoja_sprites]
        indice_sprite = (self.contador_animacion // self.delay_animacion) % len(sprites)
        self.sprite = sprites[indice_sprite]
    
        self.contador_animacion += 1



    
    def fnt_dibujar(self,ventana):
        ventana.blit(self.sprite, (self.rect.x, self.rect.y))




    
