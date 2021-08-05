from iterate import *

init_grid(10, 10)
addCell(0,1)
addCell(0,0)
addCell(0,2)
# addCell(4,5)
# addCell(3,7)

printMap()
printGrid()

while(True):
    if(input() == "uwu"):
        iterate()
        printMap()
        printGrid()
    elif(input() == "x"):
        break