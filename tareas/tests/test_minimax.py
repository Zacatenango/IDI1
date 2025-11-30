import os
import sys

# Ensure parent (tareas/) is on sys.path so we can import PROFINAL when running tests
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PROFINAL import EstadoDelJuego, ArbolCuaternario, minimax_armar_arbol


def make_grid(values):
    # build grid as list of lists of dicts
    return [[{"valor": v, "ocupado_por": None} for v in row] for row in values]


def test_minimax_small_board():
    # 3x3 grid with increasing values for easy tracking
    values = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]
    estado = EstadoDelJuego(3,3)
    # replace cuadricula values and reset ocupados
    estado.cuadricula = make_grid(values)
    # set P2 at (0,0) and P1 at (2,2)
    estado.posicion_P2 = (0,0)
    estado.posicion_P1 = (2,2)
    estado.cuadricula[0][0]["ocupado_por"] = "P2"
    estado.cuadricula[2][2]["ocupado_por"] = "P1"
    estado.puntuacion_2 = estado.cuadricula[0][0]["valor"]
    estado.puntuacion_1 = estado.cuadricula[2][2]["valor"]

    raiz = ArbolCuaternario(estado.puntuacion_2 - estado.puntuacion_1)
    # build tree with 2 levels
    minimax_armar_arbol(raiz, 2, estado, estado.posicion_P2, estado.posicion_P1, es_max=True)

    # After P2 moves he can go right (1) or down (3). From (0,0): (1,0) and (0,1) -> values 3 and 1
    # So top (up) and left are out of bounds, right is 'der', down is 'bot'
    assert raiz.top is None
    assert raiz.izq is None
    assert raiz.der is not None
    assert raiz.bot is not None

    # Check derived values: raiz.valor = 0 - 8 = -8
    assert raiz.valor == -8
    # If P2 moves down to (1,0), advantage becomes -8 + 3 = -5
    assert raiz.bot.valor == -5
    # If P2 moves right to (0,1), advantage becomes -8 + 1 = -7
    assert raiz.der.valor == -7


if __name__ == '__main__':
    test_minimax_small_board()
    print('minimax test OK')
