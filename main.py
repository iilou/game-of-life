from iterate import *

init_grid(10, 10)
addCell(3,4)
addCell(4,4)
addCell(3,5)
addCell(4,5)
addCell(3,7)

printMap()

while(True):
    if(input() == "uwu"):
        iterate()
        printMap()
    elif(input() == "x"):
        break