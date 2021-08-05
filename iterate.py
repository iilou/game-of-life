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

def get_row():
    return ROW

def get_col():
    return COL

def get_map():
    return map

def printGrid():
    if isInit == False: return False

    for row in map:
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

def checkEdge(r, c, v):
    if r == 0 and c == 0: map[ROW + 1][COL + 1] = v
    elif r == 0 and c == COL - 1: map[ROW + 1][0] = v
    elif r == ROW - 1 and c == 0: map[0][COL + 1] = v
    elif r == ROW - 1 and c == COL - 1: map[0][0] = v

    if r == 0: map[ROW + 1][c + 1] = v
    elif r == ROW - 1: map[0][c + 1] = v
    if c == 0: map[r + 1][COL + 1] = v
    elif c == COL - 1: map[r + 1][0] = v

def addEdges(map):
    for i in range(ROW):
        map[i + 1][0] = map[i + 1][COL]
        map[i + 1][COL + 1] = map[i + 1][1]

    for j in range(COL):
        map[0][j + 1] = map[ROW][j + 1]
        map[ROW + 1][j + 1] = map[1][j + 1]

    map[0][0] = map[ROW][COL]
    map[0][COL + 1] = map[ROW][1]
    map[ROW + 1][0] = map[1][COL]
    map[ROW + 1][COL + 1] = map[1][1]
    
    return map

def addCell(r, c):
    if r < 0 or r >= ROW or c < 0 or c >= COL:
        return False

    checkEdge(r, c, 1)

    map[r + 1][c + 1] = 1
    return True

def killCell(r, c):
    if r < 0 or r >= ROW or c < 0 or c >= COL:
        return False

    map[r + 1][c + 1] = 0
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

    update = addEdges(update)
    map = update
    return update
