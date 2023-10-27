import pygame 

class Cls_movimiento:
    def __init__(self,juego,tipo_entidad,posicion,tamano):
        self.juego = juego 
        self.tipo_entidad = tipo_entidad
        self.posicion = list(posicion)
        self.tamano = tamano
        self.velocidad = [0,0]

    def fnt_actualizacion(self, movimiento=(0,0)):
        movimento_frame = (movimiento[0] + self.velocidad[0], movimiento[1] + self.velocidad[1])

        self.posicion[0] += movimento_frame[0]
        self.posicion[1] += movimento_frame[1]

    def fnt_renderizar(self, ventana):
        ventana.blit(self.juego.dict_elementos['caballero'], self.posicion)