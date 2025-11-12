import curses

# Este proyecto usa la librería curses para implementar la interfaz de usuario. La configuramos aquí
stdscr = curses.initscr()
curses.noecho()  # Presionar una tecla hará que no se refleje en la terminal
curses.cbreak()  # La aplicación debe reaccionar instantáneamente a las teclas sin presionar Enter
stdscr.keypad(True)  # Habilitamos las flechillas del teclado

# Para terminar la aplicación
curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()
