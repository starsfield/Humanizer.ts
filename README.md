
# Check-The-Board-Game
Check The Board is an indie game solo developed for fun. 

Dev Log

Log 1 (11-15-2021) (Initial Commit):
Created a python file for the main game after deciding that the project would be easier to do in Python than C++. It is too early in the morning to do anything, but creating a project is a huge first step.

Log 2 (11-16-2021) (Added a window that stays open until the user clicks):
Reused some code from an older project to get a widow to appear when the file is run that stays open until a click is detected. The only thing the program can do now is open and close a window at the whim of the user.

Log 3 (11-21-2021) (Created the basic template for the Main Menu):
Created a brand new file to hold everything for the main menu. Currently have the basic outline for the main menu done with makeshift buttons with no functionality yet and a background image.

Log 4 (12-21-2021) (Redid how the objects are drawn, added clickability to the window, finished the 'exit' functionality and started on the 'help' menu):
Created arrays for each group of objects (ex. all of the objects that are shown in the Main Menu) so that they can easily be added and removed from the screen. Made it so clicks are now saved in an object so that their position can be checked to see if the user clicked a button (currently displaying the position). Made it so if the 'Exit' button is clicked the game will close and if the 'Help' button is clicked the Main Menu objects are removed and the Help objects are added (still need to add most of the Help objects).