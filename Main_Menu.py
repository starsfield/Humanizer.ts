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
    titleText.setSize(35)
    menuObjects.append(titleText)

    #Start Button
    startBox = Rectangle(Point(30, 65), Point(70, 55))
    startBox.setFill(color_rgb(163,163,161))
    startBox.setOutline("white")
    menuObjects.append(startBox)
    startText = Text(Point(50, 60), "Level Select")
    startText.setSize(20)
    menuObjects.append(startText)

    #Options Button
    optionsBox = Rectangle(Point(30, 50), Point(70, 40))
    optionsBox.setFill(color_rgb(163,163,161))
    optionsBox.setOutline("white")
    menuObjects.append(optionsBox)
    optionsText = Text(Point(50, 45), "Options")
    optionsText.setSize(20)
    menuObjects.append(optionsText)

    #Help Button
    helpBox = Rectangle(Point(30, 35), Point(70, 25))
    helpBox.setFill(color_rgb(163,163,161))
    helpBox.setOutline("white")
    menuObjects.append(helpBox)
    helpText = Text(Point(50, 30), "Help")
    helpText.setSize(20)
    menuObjects.append(helpText)

    #Exit Button
    exitBox = Rectangle(Point(30, 20), Point(70, 10))
    exitBox.setFill(color_rgb(163,163,161))
    exitBox.setOutline("white")
    menuObjects.append(exitBox)
    exitText = Text(Point(50, 15), "Exit")
    exitText.setSize(20)
    menuObjects.append(exitText)

    #Draw in the Main Menu objects
    for i in range(len(menuObjects)):
        menuObjects[i].draw(win)

    #Main Menu Functionality
    clickText = Text(Point(50, 5), " ")
    while True:
        click = win.getMouse()
        clickText.undraw()
        clickText = Text(Point(50, 5), "X: " + str(format(click.getX(), ".2f")) + " " + "Y: " + str(format(click.getY(), ".2f")))
        clickText.setSize(20)
        clickText.setTextColor("red")
        clickText.draw(win)
        if click.getX() >