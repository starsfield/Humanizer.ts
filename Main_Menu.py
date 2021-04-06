from graphics import GraphWin, Rectangle, Text, Point, color_rgb, Image

def mainMenu (window):

    #Initialize variables
    win = window
    menuObjects = []

    #Background
    background = Image(Point(50,50), "MMBackground.gif")
    background.draw(win)

    #Title Text
    titleBox = Rectangle(Point(10,95), Point(90, 75))
    titleBox.setFill(color_rgb(132,132,130))
    titleBox.setOutline("white")
    menuObjects.append(titleBox)
    titleText = Text(Point(50, 85), "CHECK THE BOARD")
    ti