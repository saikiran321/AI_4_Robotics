# ----------
# User Instructions:
# 
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal. 
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def compute_value(grid,goal,cost):
    # ----------------------------------------
    # insert code below
    # ----------------------------------------
    val=[[99 for i in grid[0]] for j in grid]
    closed=[[0 for i in grid[0]] for j in grid]
    action=[[-1 for i in grid[0]] for j in grid]
    route=[[' ' for i in grid[0]] for j in grid]

    x=goal[0]
    y=goal[1]
    f=0
    open=[[0,x,y]]
    closed[x][y]=1
    val[x][y]=0
    route[x][y]='*'
    while True:
        if len(open) == 0:
            break
        open.sort()
        open.reverse()
        new_val=open.pop()
        x=new_val[1]
        y=new_val[2]
        f=new_val[0]

        for d in range(len(delta)):
            x2=x-delta[d][0]
            y2=y-delta[d][1]
            if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                if closed[x2][y2]==0 and grid[x2][y2] == 0:
                    f2 = f + cost
                    open.append([f2, x2, y2])
                    val[x2][y2]=f2
                    closed[x2][y2] = 1
                    action[x2][y2]=d
                    route[x][y]=delta_name[d]

    return route

# route=[['' for i in grid[0]] for j in grid]
route=compute_value(grid,goal,cost)
for r in route:
    print r
# x=goal[0]
# y=goal[1]
# route[x][y]='*'
# i=0
# init=[0,0]
# print action
# while x!=init[0] or y!=init[1] :
#     x2=x-delta[action[x][y]][0]
#     y2=y-delta[action[x][y]][1]
#     route[x2][y2]=delta_name[action[x][y]]
#     x=x2
#     y=y2
 


# for i in  route:
#     print i