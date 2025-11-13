#! /home/usuario/programacion/ITESO/semestre1/IDI1/tareas/bin/python

"""
Proyecto final de IDI 1 de Acoyani Garrido Sandoval

Usage: PROFINAL.PY [-x <dimension_x>] [-y <dimension_y>]

-x <dimension_x>     Dimensión horizontal de la cuadrícula, 6 por default
-y <dimension_y>     Dimensión vertical de la cuadrícula, 6 por default
"""

import json
import curses
import numpy
import time
from docopt import docopt


ARGUMENTOS = docopt(__doc__)
numpy.random.seed(297974)


class EstadoDelJuego():
   def __init__(self, dimension_X, dimension_Y):
      self.dimension_X = dimension_X if dimension_X is not None else 6
      self.dimension_Y = dimension_Y if dimension_Y is not None else 6
      self.cuadricula = [ [] for _ in range(self.dimension_Y) ]
      for una_fila in self.cuadricula:
         for X in range(self.dimension_X):
            una_fila.append({ "valor": numpy.random.randint(0, 10), "ocupado_por": None })
      self.puntuacion_1 = 0
      self.puntuacion_2 = 0
      self.posicion_P1 = (0,0)
      self.posicion_P2 = (0,0)
      self.turno_P1 = True


# Este proyecto usa la librería curses para implementar la interfaz de usuario
def main(stdscr):
   # Configuramos curses: terminal a color, el color #1 es amarillo sobre negro,
   # #2 es blanco sobre negro, #3 es rojo sobre negro
   curses.start_color()
   curses.cbreak()
   curses.noecho()
   curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
   curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
   curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
   curses.init_pair(4, curses.COLOR_GREEN, curses.COLOR_BLACK)

   colores = \
   {
      "blanco": curses.color_pair(2),
      "amarillo": curses.color_pair(1),
      "verde": curses.color_pair(4),
      "rojo": curses.color_pair(3)
   }

   # Configuramos nuestro juego
   estado_juego = EstadoDelJuego(ARGUMENTOS["-x"], ARGUMENTOS["-y"])
   
   # Iniciando el programa, preparamos nuestra pantalla
   stdscr.clear()
   stdscr.nodelay(True)
   stdscr.keypad(True)
   stdscr.timeout(100)  # 100ms timeout for getch()

   mensaje = ""
   
   # Iniciamos el ciclo principal
   while True:
      # Renderizamos la cuadrícula
      stdscr.clear()
      stdscr.addstr(0, 0, f"Jugador 1: {estado_juego.puntuacion_1} puntos -- Jugador 2: {estado_juego.puntuacion_2} puntos")
      
      # Mostramos el mensaje de movimiento
      if mensaje:
         stdscr.addstr(1, 0, mensaje)

      for indice_Y, una_fila in enumerate(estado_juego.cuadricula):
         for indice_X, una_celda in enumerate(una_fila):
            match una_celda["ocupado_por"]:
               case "P1":
                  color = colores["amarillo"]
               case "P2":
                  color = colores["verde"]
               case _:
                  color = colores["blanco"]
            stdscr.addstr(indice_Y+2, indice_X * 2, str(una_celda["valor"]), color)
      
      stdscr.refresh()
      
      # Recibir el teclazo
      tecla = stdscr.getch()
      
      if tecla == ord("w"):
         mensaje = "Nos movemos arriba"
      elif tecla == ord("a"):
         mensaje = "Nos movemos a la izquierda"
      elif tecla == ord("s"):
         mensaje = "Nos movemos abajo"
      elif tecla == ord("d"):
         mensaje = "Nos movemos a la derecha"
      elif tecla == ord("q"):
         break
      elif tecla == -1:  # No key pressed (timeout)
         mensaje = ""
      
      time.sleep(0.1)  # Small delay to keep message visible
      
      


if __name__ == "__main__":
   curses.wrapper(main)
