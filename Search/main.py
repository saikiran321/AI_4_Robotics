# -----------
#Dijkshtra path planning
# ----------

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # ----------------------------------------
    # modify code below
    # ----------------------------------------
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    expand = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    parent=  [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    action=  [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed[init[0]][init[1]] = 1
    x = init[0]
    y = init[1]
    g = 0
    xi=0
    open = [[g, x, y]]
    found = False  
    resign = False # flag set if we can't find expand

    while not found and not resign:
        if len(open) == 0:
            resign = True
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            
            x = next[1]
            y = next[2]
            g = next[0]
            expand[x][y]=xi
            xi+=1
            
            if x == goal[0] and y == goal[1]:
                found = True
            else:
                for i in range(len(delta)):
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            open.append([g2, x2, y2])
                            parent[x2][y2]=[x,y]
                            closed[x2][y2] = 1
                            action[x2][y2]=i
    # print parent
    print expand
    return action

action=search(grid,init,goal,cost)
for i in action:
    print i

print "-----------------"
route=[[' ' for row in range(len(grid[0]))] for col in range(len(grid))]

x=goal[0]
y=goal[1]
route[x][y]='*'
i=0

while x!=init[0] or y!=init[1] :
    x2=x-delta[action[x][y]][0]
    y2=y-delta[action[x][y]][1]
    route[x2][y2]=delta_name[action[x][y]]
    x=x2
    y=y2
 


for i in  route:
    print i