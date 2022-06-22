
# Structure for storing coordinates count of remaining obstacle eliminations
class pointLoc:
    def __init__(self,x, y, k):
        self.x = x
        self.y = y
        self.k = k


# Function to perform BFS
def BFS_obs(matrix, source, destination, k):
    ROW = len(matrix)
    COL = len(matrix[0])
    # Direction Vectors
    dir_Row = [-1, 0, 1, 0]
    dir_Col = [0, 1, 0, -1]

    # Stores pointLoc of each cell
    q = []

    # Vector array to store distance of each cell from source cell
    distance = [0 for i in range(ROW)]

    for i in range(len(distance)):
        distance[i] = [0 for i in range(COL)]


    # Vector array to store count of available obstacle eliminations
    obstacles = [0 for i in range(ROW)]
    for i in range(len(obstacles)):
        obstacles[i] = [-1 for i in range(COL)]

    # Push the source cell into queue and use as starting point
    q.append(pointLoc(source.x, source.y, k))

    obstacles_to_remove = []

    # Iterate while queue is not empty
    while (len(q) > 0):

        te = q[0]
        x = te.x
        y = te.y
        tk = te.k

        # If current cell is same as destination then return distance
        if (x == destination.x and y == destination.y):
            return obstacles_to_remove #distance[x][y]

        q = q[1:]

        # If current cell is an obstacle then decrement current value if possible else skip the cell
        node = matrix[x][y]
        if (node.type == 'obstacle'):

            if (tk > 0):
                tk -= 1
                #print(" obs: "+str(x)+" , "+str(y))
                obstacles_to_remove.append((x,y))
            else:
                continue

        # Cell is skipped only if current value is less than previous value of cell
        if (obstacles[x][y] >= tk):
            continue

        # Else update value
        obstacles[x][y] = tk

        # Push all valid adjacent cells into queue
        for i in range(4):

            ax = x + dir_Row[i]
            ay = y + dir_Col[i]

            if (ax < 0 or ay < 0 or ax >= ROW or ay >= COL):
                continue

            q.append(pointLoc(ax, ay, tk))

            # Update distance of current
            # cell from source cell
            distance[ax][ay] = distance[x][y] + 1

    # If not possible to reach destination from source
    return -1


