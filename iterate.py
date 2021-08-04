ROW, COL = (0,0)

map = [[]]
isInit = False
nrow = [1,1,1,0,0,-1,-1,-1]
ncol = [1,0,-1,1,-1,1,0,-1]

def init_grid(r, c):
    global isInit
    global map
    global ROW, COL

    ROW, COL = (r, c)

    map = [[0 for i in range(COL + 2)] for j in range(ROW + 2)]
    isInit = True
    return map

def printGrid(arr):
    if isInit == False: return False

    for row in arr:
        print (row)

    return True

def printMap():
    print(str(ROW) + " " + str(COL))
    if isInit == False: return False

    for i in range(ROW):
        currentOutput = ""

        for j in range(COL):
            if map[i + 1][j + 1] == 1:
                currentOutput += "o"
            else:
                currentOutput += "."
        
        print(currentOutput)

    return True

def addCell(r, c):
    if r < 0 or r >= ROW or c < 0 or c >= COL:
        return False

    map[r + 1][c + 1] = 1
    return True

def iterate(): 
    global map

    update = [[0 for i in range(COL + 2)] for j in range(ROW + 2)]

    for i in range(ROW):
        for j in range(COL):
            neighbours = 0
            for k in range(8):
                neighbours += map[i + nrow[k] + 1][j + ncol[k] + 1]

            if(map[i + 1][j + 1] == 1):
                if(neighbours == 2 or neighbours == 3):
                    update[i + 1][j + 1] = 1

            else:
                if(neighbours == 3):
                    update[i + 1][j + 1] = 1

    map = update
    return update
