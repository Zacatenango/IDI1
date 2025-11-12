import curses
import random

def main(stdscr):
    # Initialize colors
    curses.start_color()
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
    
    # Create 6x6 grid of random numbers
    grid = [[random.randint(0, 9) for _ in range(6)] for _ in range(6)]
    highlighted = set()  # Store positions of highlighted cells
    
    # Clear screen
    stdscr.clear()
    stdscr.nodelay(False)
    
    while True:
        # Render grid
        stdscr.clear()
        stdscr.addstr(0, 0, "Press SPACE to highlight random cell, Q to quit\n\n")
        
        for i in range(6):
            for j in range(6):
                color = curses.color_pair(1) if (i, j) in highlighted else curses.color_pair(2)
                stdscr.addstr(i + 2, j * 2, str(grid[i][j]), color)
        
        stdscr.refresh()
        
        # Get user input
        key = stdscr.getch()
        
        if key == ord(' '):
            # Highlight random cell
            pos = (random.randint(0, 5), random.randint(0, 5))
            highlighted.add(pos)
        elif key == ord('q') or key == ord('Q'):
            break

if __name__ == "__main__":
    curses.wrapper(main)
