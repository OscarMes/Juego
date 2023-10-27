# Menús

El juego cuenta con dos menús, para salir de ambos menús y jugar solo hay que presionar cualquier tecla 
- Menú de bienvenida
  
![inicio](https://github.com/OscarMes/Juego/assets/128978144/6d8f232f-9c39-433e-a8be-78e3c236e534)


- Menú de game over
- ![game_over](https://github.com/OscarMes/Juego/assets/128978144/034aff98-79a4-4a2f-b154-e280b8b073be)




# Jugabilidad

El jugador cuenta con 3 vidas, el objetivo del juego es sobrevivir el mayor tiempo posible

![Jugabilidad](https://github.com/OscarMes/Juego/assets/128978144/9ac77198-e5c4-4067-a21e-b62911f1caf6)


# Sprites 

Se hizo uso de sprites para tener un personaje jugable más interactivo 

![image](https://github.com/OscarMes/Juego/assets/128978144/9bc958bb-97a2-4e2c-bdd0-8d5945b881da)



# Desarrollo

Se crearon varios módulos para un desarrollo más limpio, se separaron los elementos y funcionalidades en clases para posteriormente ser llamados en la clase main

![image](https://github.com/OscarMes/Juego/assets/128978144/9aa1af6e-b299-428d-9387-e1662d475b7d)

el módulo main hace llamado a las demás clases y controla la aparición de elementos gracias al bucle principal 

![image](https://github.com/OscarMes/Juego/assets/128978144/6c1f0933-4f3d-4ca2-a0a8-b446f3061584)

para desarrollar al personaje se creó su propia clase en la que se definían las colisiones con el terreno, sus movimientos y sprites 

![image](https://github.com/OscarMes/Juego/assets/128978144/10cf86ab-cba2-45d3-899a-1088fcab521e)


Los sprites fueron iterados con la clase sprites lo que permite que el personaje pueda moverse 

![image](https://github.com/OscarMes/Juego/assets/128978144/fa98e4d2-0f49-4eb0-b753-30262e5635fd)

un terreno simple generado con Rect de pygame

![image](https://github.com/OscarMes/Juego/assets/128978144/ce024c17-9ed9-41e1-a06a-651e1dfb321a)



