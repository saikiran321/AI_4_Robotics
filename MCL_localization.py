# Author : sai kiran
# Montecarlo localization
#

def sense(p,z,pHit,colors):
  q=[]
  ay=[[0.0 for row in range(len(p[0]))] for col in range(len(p))]
  sums=0.0
  # print colors
  for i in range(len(colors)):
      qq=[]
      for j in range(len(colors[i])):
        hit=(z==colors[i][j])
        pp=p[i][j] * (hit * pHit + (1-hit) *(1-pHit))
        ay[i][j]=pp
       
  for i in range(len(colors)):
    sums=sums+sum(ay[i])
  # print sums
  for i in range(len(colors)):
      for j in range(len(colors[0])):
        ay[i][j]=ay[i][j]/sums
        # print i,j
  return ay

def move(p, U,p_move):
    ax=[[0.0 for row in range(len(p[0]))] for col in range(len(p))]
    # print ax
    for i in range(len(p)):
      for j in range(len(p[i])):
        s= p_move * p[(i-U[0]) % len(p)][(j-U[1]) % len(p[0])]+ (1-p_move)*p[i][j]
        ax[i][j]=s
    return ax





def localize(colors,measurements,motions,sensor_right,p_move):
    # initializes p to a uniform distribution over a grid of the same dimensions as colors
    pinit = 1.0 / float(len(colors)) / float(len(colors[0]))
    p = [[pinit for row in range(len(colors[0]))] for col in range(len(colors))]
    # print p
    # >>> Insert your code here <<<
    for i in range(len(measurements)):
      p=move(p,motions[i],p_move)
      p=sense(p,measurements[i],sensor_right,colors)
      
    return p

def show(p):
    rows = ['[' + ','.join(map(lambda x: '{0:.5f}'.format(x),r)) + ']' for r in p]
    print '[' + ',\n '.join(rows) + ']'
    


colors = [['R','G','G','R','R'],
          ['R','R','G','R','R'],
          ['R','R','G','G','R'],
          ['R','R','R','R','R']]
measurements = ['G','G','G','G','G']
motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]
p = localize(colors,measurements,motions,sensor_right = 0.7, p_move = 0.8)
show(p) # displays your answer
