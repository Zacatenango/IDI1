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
      # Player 1 starts bottom-right, player 2 starts top-left
      self.posicion_P2 = (0, 0)
      self.posicion_P1 = (self.dimension_Y - 1, self.dimension_X - 1)
      self.turno_P1 = True

      # Claim initial positions
      # If both start in same square (very small boards), only first player claims
      if self.posicion_P2 == self.posicion_P1:
         self.cuadricula[self.posicion_P1[0]][self.posicion_P1[1]]["ocupado_por"] = "P1"
         self.puntuacion_1 += self.cuadricula[self.posicion_P1[0]][self.posicion_P1[1]]["valor"]
      else:
         self.cuadricula[self.posicion_P2[0]][self.posicion_P2[1]]["ocupado_por"] = "P2"
         self.puntuacion_2 += self.cuadricula[self.posicion_P2[0]][self.posicion_P2[1]]["valor"]
         self.cuadricula[self.posicion_P1[0]][self.posicion_P1[1]]["ocupado_por"] = "P1"
         self.puntuacion_1 += self.cuadricula[self.posicion_P1[0]][self.posicion_P1[1]]["valor"]

   def _in_bounds(self, pos):
      y, x = pos
      return 0 <= y < self.dimension_Y and 0 <= x < self.dimension_X

   def get_adjacent_positions(self, pos):
      y, x = pos
      adjacents = [ (y-1, x), (y+1, x), (y, x-1), (y, x+1) ]
      return [p for p in adjacents if self._in_bounds(p)]

   def get_valid_moves(self, pos):
      # Valid moves are adjacent squares that are not occupied
      return [p for p in self.get_adjacent_positions(pos)
              if self.cuadricula[p[0]][p[1]]["ocupado_por"] is None]

   def claim(self, pos, player):
      # Set the square's occupant and increase the player's score
      y, x = pos
      if self.cuadricula[y][x]["ocupado_por"] is not None:
         raise ValueError("Square already occupied")
      self.cuadricula[y][x]["ocupado_por"] = player
      if player == "P1":
         self.puntuacion_1 += self.cuadricula[y][x]["valor"]
         self.posicion_P1 = (y, x)
      else:
         self.puntuacion_2 += self.cuadricula[y][x]["valor"]
         self.posicion_P2 = (y, x)


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
      # If either player has no valid moves, end the game
      valid_moves_P1 = estado_juego.get_valid_moves(estado_juego.posicion_P1)
      valid_moves_P2 = estado_juego.get_valid_moves(estado_juego.posicion_P2)
      if len(valid_moves_P1) == 0 or len(valid_moves_P2) == 0:
         # Determine winner
         if estado_juego.puntuacion_1 > estado_juego.puntuacion_2:
            mensaje = f"Juego terminado: Gana Jugador 1 ({estado_juego.puntuacion_1} - {estado_juego.puntuacion_2}). Presiona 'q' para salir o 'r' para reiniciar."
         elif estado_juego.puntuacion_2 > estado_juego.puntuacion_1:
            mensaje = f"Juego terminado: Gana Jugador 2 ({estado_juego.puntuacion_2} - {estado_juego.puntuacion_1}). Presiona 'q' para salir o 'r' para reiniciar."
         else:
            mensaje = f"Juego terminado: Empate ({estado_juego.puntuacion_1} - {estado_juego.puntuacion_2}). Presiona 'q' para salir o 'r' para reiniciar."
         # Render final state and wait for quit/restart
         stdscr.clear()
         stdscr.addstr(0, 0, f"Jugador 1: {estado_juego.puntuacion_1} puntos -- Jugador 2: {estado_juego.puntuacion_2} puntos")
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
         tecla = stdscr.getch()
         if tecla == ord('q'):
            break
         elif tecla == ord('r'):
            estado_juego = EstadoDelJuego(ARGUMENTOS["-x"], ARGUMENTOS["-y"])  # restart
            mensaje = ""
            continue
      # Renderizamos la cuadrícula
      stdscr.clear()
      turno_text = "1" if estado_juego.turno_P1 else "2"
      stdscr.addstr(0, 0, f"Jugador 1: {estado_juego.puntuacion_1} puntos -- Jugador 2: {estado_juego.puntuacion_2} puntos    Turno: Jugador {turno_text}")
      
      # Mostramos el mensaje de movimiento
      if mensaje:
         stdscr.addstr(1, 0, mensaje)
      else:
         stdscr.addstr(1, 0, "Controles: W/A/S/D moverse, r reiniciar, q salir")

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
      
      if tecla in (ord('w'), ord('a'), ord('s'), ord('d')):
         # Determine move vector
         if tecla == ord('w'):
            delta = (-1, 0)
            dir_text = "arriba"
         elif tecla == ord('s'):
            delta = (1, 0)
            dir_text = "abajo"
         elif tecla == ord('a'):
            delta = (0, -1)
            dir_text = "izquierda"
         else:  # tecla == ord('d')
            delta = (0, 1)
            dir_text = "derecha"

         # Evaluate attempted move for the active player
         if estado_juego.turno_P1:
            pos_actual = estado_juego.posicion_P1
            player_label = "P1"
         else:
            pos_actual = estado_juego.posicion_P2
            player_label = "P2"

         nueva_pos = (pos_actual[0] + delta[0], pos_actual[1] + delta[1])
         valid_moves = estado_juego.get_valid_moves(pos_actual)
         if nueva_pos in valid_moves:
            # Claim and change turn
            estado_juego.claim(nueva_pos, player_label)
            mensaje = f"{('Jugador 1' if player_label=='P1' else 'Jugador 2')} se movió {dir_text} y reclamó {estado_juego.cuadricula[nueva_pos[0]][nueva_pos[1]]['valor']} puntos"
            # Toggle turn
            estado_juego.turno_P1 = not estado_juego.turno_P1
         else:
            if not estado_juego._in_bounds(nueva_pos):
               mensaje = "Movimiento fuera de los límites"
            elif estado_juego.cuadricula[nueva_pos[0]][nueva_pos[1]]["ocupado_por"] is not None:
               mensaje = "Casilla ocupada, no puedes moverte ahí"
            else:
               mensaje = "Movimiento inválido"
      elif tecla == ord("q"):
         break
      elif tecla == ord('r'):
         estado_juego = EstadoDelJuego(ARGUMENTOS["-x"], ARGUMENTOS["-y"])  # restart
         mensaje = ""
      elif tecla == -1:  # No key pressed (timeout)
         mensaje = ""
      
      time.sleep(0.1)  # Small delay to keep message visible
      
      


if __name__ == "__main__":
   curses.wrapper(main)
