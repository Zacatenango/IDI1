import importlib.util
import sys
from pathlib import Path


def load_module_from_path(path):
    spec = importlib.util.spec_from_file_location('profinal_mod', path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    # file sits under tareas/tests so go up two levels to repo root
    repo_root = Path(__file__).resolve().parents[2]
    mod_path = repo_root / 'tareas' / 'PROFINAL.py'
    print(f"Loading {mod_path}")
    mod = load_module_from_path(str(mod_path))

    EstadoDelJuego = mod.EstadoDelJuego
    minimax_armar_arbol = mod.minimax_armar_arbol
    minimax_ingenuo = mod.minimax_ingenuo
    ArbolCuaternario = mod.ArbolCuaternario

    # run the simulation similar to pytest test
    from random import seed, choice
    seed(297974)

    juego = EstadoDelJuego(6, 6)

    for step in range(30):
        valid_human = juego.movimientos_validos(juego.posicion_P1)
        if not valid_human:
            print(f"Human no moves at step {step}")
            break
        nueva_human = choice(valid_human)
        juego.tomar(nueva_human, 'P1')

        raiz = ArbolCuaternario(juego.puntuacion_2 - juego.puntuacion_1)
        minimax_armar_arbol(raiz, juego.dificultad, juego, juego.posicion_P2, juego.posicion_P1, es_max=True)
        decision = minimax_ingenuo(raiz, juego.dificultad, es_max=True)

        cpu_valid = juego.movimientos_validos(juego.posicion_P2)
        print(f"Step {step}: P2 pos {juego.posicion_P2}, valid {cpu_valid}, minimax decision: {decision and decision.get('costado')}")

        if (decision is None or decision.get('costado') is None) and cpu_valid:
            print('\nBUG: CPU had valid moves but minimax returned no decision - dumping state:')
            print('Grid values and occupied:')
            for y, fila in enumerate(juego.cuadricula):
                print(''.join(f"{('P2' if c['ocupado_por']=='P2' else ('P1' if c['ocupado_por']=='P1' else '__'))}:{c['valor']:02} " for c in fila))
            return 1

        if decision and decision.get('costado'):
            movement_map = {'arriba': (-1, 0), 'abajo': (1, 0), 'izquierdo': (0, -1), 'derecho': (0, 1)}
            dy, dx = movement_map[decision['costado']]
            nueva_cpu = (juego.posicion_P2[0] + dy, juego.posicion_P2[1] + dx)
            if nueva_cpu not in cpu_valid:
                print(f"BUG: minimax chose an invalid cpu move {nueva_cpu} vs valid {cpu_valid}")
                return 2
            juego.tomar(nueva_cpu, 'P2')

    print('Simulation finished without reproducing the bug within 30 steps')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
