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
            una_fila.append({ "valor": numpy.random.randint(0, 10), "ocupado_por": None, "activo": False })
      self.puntuacion_1 = 0
      self.puntuacion_2 = 0


# Este proyecto usa la librería curses para implementar la interfaz de usuario
def main(stdscr):
   # Configuramos curses: terminal a color, el color #1 es amarillo sobre negro,
   # #2 es blanco sobre negro, #3 es rojo sobre negro
   curses.start_color()
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
   stdscr.nodelay(False)

   # Iniciamos el ciclo principal
   while True:
      # Renderizamos la cuadrícula
      stdscr.clear()
      stdscr.addstr(0, 0, f"Jugador 1: {estado_juego.puntuacion_1} puntos -- Jugador 2: {estado_juego.puntuacion_2} puntos")

      for indice_Y, una_fila in enumerate(estado_juego.cuadricula):
         for indice_X, una_celda in enumerate(una_fila):
            match una_celda["ocupado_por"]:
               case "P1":
                  color = colores["amarillo"]
               case "P2":
                  color = colores["verde"]
               case _:
                  color = colores["blanco"]
            if una_celda["activo"]: color = colores["rojo"]

            stdscr.addstr(indice_Y+2, indice_X * 2, str(una_celda["valor"]), color)
      
      stdscr.refresh()

      # Recibir el teclazo
      tecla = stdscr.getch()
      match tecla:
         case curses.KEY_LEFT:
            stdscr.addstr(1, 0, "Nos movemos a la izquierda")
         case curses.KEY_RIGHT:
            stdscr.addstr(1, 0, "Nos movemos a la derecha")
         case curses.KEY_UP:
            stdscr.addstr(1, 0, "Nos movemos arriba")
         case curses.KEY_DOWN:
            stdscr.addstr(1, 0, "Nos movemos abajo")
         case ord("q"):
            break
         case ord("Q"):
            break
         case _:
            stdscr.addstr(1, 0, "No hacemos nada")


if __name__ == "__main__":
   curses.wrapper(main)
