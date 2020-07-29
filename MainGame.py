
from graphics import GraphWin
from Main_Menu import *

def main():
    width = 1000
    height = 600
    win = GraphWin("Check The Board", width, height)
    win.setCoords(0, 0, 100, 100)
    mainMenu(win)


if __name__ == "__main__":
    main()