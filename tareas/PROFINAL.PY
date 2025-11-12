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


# Este proyecto usa la librería curses para implementar la interfaz de usuario
def main(stdscr):
   # Configuramos curses: terminal a color, el color #1 es amarillo sobre negro,
   # #2 es blanco sobre negro
   curses.start_color()
   curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
   curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)

   # Configuramos nuestro juego
   estado_juego = EstadoDelJuego(ARGUMENTOS["-x"], ARGUMENTOS["-y"])






if __name__ == "__main__":
   curses.wrapper(main)
