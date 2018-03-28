#car path planning using DPP

forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # go right
forward_name = ['up', 'left', 'down', 'right']

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space 
grid = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]

init = [4, 3, 0] # given in the form [row,col,direction]
                 # direction = 0: up
                 #             1: left
                 #             2: down
                 #             3: right
                
goal = [2, 0] # given in the form [row,col]

cost = [2, 1, 16] 



def optimum_policy2D(grid,init,goal,cost):
    policy2D=[[' ' for i in range(len(grid[0]))] for j in range(len(grid))]
    value=[[[999 for i in range(len(grid[0]))] for j in range(len(grid))],
            [[999 for i in range(len(grid[0]))] for j in range(len(grid))],
            [[999 for i in range(len(grid[0]))] for j in range(len(grid))],
            [[999 for i in range(len(grid[0]))] for j in range(len(grid))]]
    policy=[[[' ' for i in range(len(grid[0]))] for j in range(len(grid))],
            [[' ' for i in range(len(grid[0]))] for j in range(len(grid))],
            [[' ' for i in range(len(grid[0]))] for j in range(len(grid))],
            [[' ' for i in range(len(grid[0]))] for j in range(len(grid))]]
    policy2D=[[' ' for i in range(len(grid[0]))] for j in range(len(grid))]
    # open_list=[]
    # open_list.append([0,init[0],init[1],init[2]])
    change=True
    while change:
        change=False
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                for th in range(4):
                    # print x,y,th
                    if x==goal[0] and y==goal[1]:
                        if value[th][x][y]>0:
                            value[th][x][y]=0
                            policy[th][x][y]='*'
                            change=True

                    elif grid[x][y]==0:

                        for j in range(3):
                            o2=(th+action[j])%4
                            x2=x+forward[o2][0]
                            y2=y+forward[o2][1]
                            if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]) and grid[x2][y2]==0:
                                # print o2,x2,y2
                                v2=value[o2][x2][y2]+cost[j]
                                if v2 < value[th][x][y]:
                                    change=True
                                    value[th][x][y]=v2
                                    policy[th][x][y]=action_name[j]
    print policy
    x=init[0]
    y=init[1]
    th=init[2]
    policy2D[x][y]=policy[th][x][y]
    while policy[th][x][y]!='*':
        if policy[th][x][y]=="#":
            o2=th
        elif policy[th][x][y]=="R":
            o2=(th-1)%4
        elif policy[th][x][y]=="L":
            o2=(th+1)%4
        x=x+forward[o2][0]
        y=y+forward[o2][1]
        th=o2
        policy2D[x][y]=policy[th][x][y]

                              



    return policy2D

policy2D=optimum_policy2D(grid,init,goal,cost)
for i in policy2D:
    print i