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
    titleBox.set