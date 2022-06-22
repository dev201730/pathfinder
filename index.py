import math, sys
import random
import collections
from a_star import *
from bfs_w_e import *

rows = 10
cols = 10
grid = []
start = None
end = None
obs_count = 0



def create_grid():
  global grid, start, end
  grid, start, end = [], None, None

  for i in range(rows):
    row_nodes = []
    for j in range(cols):
      node = Node(grid, j, i)
      row_nodes.append(node)
    grid.append(row_nodes)



def update_node_type(x, y, node_type):
  global start, end

  row = y
  col = x
  node = grid[row][col]

  if row < 0 or col < 0 or row >= rows or col >= cols or node.type == 'obstacle' or node == start or node == end:
    return
  elif node_type == 'endpoint' and start and end:
    return

  if node_type == 'obstacle':
    grid[row][col].type = 'obstacle'
  elif node_type == 'endpoint':
    if not start:
      start = node
    elif not end:
      end = node


def pathfind(the_obstacles_list):
  global obs_count
  path = a_star(grid, start, end)
  if not path:
    k = 1
    new_ob_list = []
    while not path and k < obs_count:
      print('Unable to reach delivery point')
      if(BFS_obs(grid, start, end, k) != -1):
        new_ob_list = BFS_obs(grid, start, end, k)
        print("SUGGESTED OBSTACLES to keep:")
        main_list = list(set(the_obstacles_list) - set(new_ob_list))
        print(main_list)
        return 
      else:
        k = k + 1      
    
  else:
    distance = round(path[-1].f_score, 2)
    if distance % 1 == 0:
      distance = int(distance)
    print('Path found with distance ' + str(distance) + '.')
  
    path_nodes_list = []
    for node in path:
      if node != start and node != end:
        node.type = 'path'
        path_nodes_list.append((node.x,node.y))
    print(path_nodes_list)
    return

            




def main():

    global obs_count

    
    
    # phase 1 & 2
    create_grid()

    endpoints_list = [(0,0), (9, 9)]
    for endpoint in endpoints_list:
        update_node_type(endpoint[0], endpoint[1], 'endpoint')

    obstacles_list = [(9,7), (8,7), (6,7), (6,8)]
    for obs in obstacles_list:
        update_node_type(obs[0], obs[1], 'obstacle')

    
    # phase 2 , add an additional 20 randomly placed obstacles
    # print obstacle locations in the format [ (x1,y1), (x2,y2), ...]
    # the obstacles should not overlap existing ones and should not be places at the start and end points.
    c = 0
    while c < 20:
        x1 = random.randint(0,9)
        y1 = random.randint(0,9)

        if ( (x1,y1) not in obstacles_list ) and ( (x1,y1) not in endpoints_list ):
            obstacles_list.append((x1,y1))
            update_node_type(x1, y1, 'obstacle')
            c += 1
    
    print("Current OBSTACLES:")
    print(obstacles_list)
    obs_count = len(obstacles_list)

    pathfind(obstacles_list)

    print("----------- END OF PHASE 2 -----------")
    



    # bonus
    #identify which obstacles to be removed in order for vehicle to reach its destination.
    #the algorithm should suggest the least amount of obstacles using the format [(x1,y1), (x2,y2) ...]

    create_grid()

    endpoints_list = [(0,0), (9, 9)]
    for endpoint in endpoints_list:
        update_node_type(endpoint[0], endpoint[1], 'endpoint')

    obstacles_list = [(9,7), (8,7), (6,7), (6,8) , (8,9), (9,8), (8,8)]
    for obs in obstacles_list:
        update_node_type(obs[0], obs[1], 'obstacle')

    print("Current OBSTACLES:")
    print(obstacles_list)
    obs_count = len(obstacles_list)

    pathfind(obstacles_list)



    print("----------- END OF PHASE 3 (BONUS) -----------")








if __name__ == '__main__':
    main()

