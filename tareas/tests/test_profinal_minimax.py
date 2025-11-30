from tareas.PROFINAL import EstadoDelJuego, minimax_armar_arbol, minimax_ingenuo, ArbolCuaternario


def simulate_until_failure(max_steps=100, seed=297974):
    # Create a game and simulate random legal human moves, then check CPU move selection.
    import random
    random.seed(seed)

    juego = EstadoDelJuego(6, 6)

    # We'll apply some moves by alternating P1 (human) and P2 (cpu) using the functions
    for step in range(max_steps):
        # HUMAN (P1) chooses a random valid move
        valid_human = juego.movimientos_validos(juego.posicion_P1)
        if not valid_human:
            return False, f"Human has no moves at step {step}"
        nueva_human = random.choice(valid_human)
        juego.tomar(nueva_human, 'P1')

        # Build minimax tree for CPU
        raiz = ArbolCuaternario(juego.puntuacion_2 - juego.puntuacion_1)
        minimax_armar_arbol(raiz, juego.dificultad, juego, juego.posicion_P2, juego.posicion_P1, es_max=True)
        decision = minimax_ingenuo(raiz, juego.dificultad, es_max=True)

        # If minimax returned no chosen side but there are valid CPU moves, that's the bug.
        cpu_valid = juego.movimientos_validos(juego.posicion_P2)
        if decision is None or decision.get('costado') is None:
            if cpu_valid:
                return True, f"BUG: CPU had valid moves {cpu_valid} but minimax returned no decision at step {step}"
            else:
                return False, f"CPU had no valid moves at step {step}, which is expected"

        # If we have a valid decision, apply it
        movement_map = {'arriba': (-1, 0), 'abajo': (1, 0), 'izquierdo': (0, -1), 'derecho': (0, 1)}
        dy, dx = movement_map[decision['costado']]
        nueva_cpu = (juego.posicion_P2[0] + dy, juego.posicion_P2[1] + dx)
        if nueva_cpu not in cpu_valid:
            return True, f"BUG: minimax chose {nueva_cpu} which is not valid (valid are {cpu_valid}) at step {step}"
        juego.tomar(nueva_cpu, 'P2')

    return False, "No bug observed within step limit"


def test_minimax_produces_valid_moves():
    # After the fix, minimax should not return a None/invalid decision when CPU
    # has at least one valid move. The test fails if a bug is observed.
    found, msg = simulate_until_failure(max_steps=50)
    assert not found, msg
