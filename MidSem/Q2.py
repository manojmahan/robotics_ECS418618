# -*- coding: utf-8 -*-
import math

init_rob = (10, 10)
rob_area = 0.4
vel = 5

C1 = [(0,0), (10, 0), (0, 40), (10, 40)]
C2 = [(10,34), (11.7, 34), (10, 40), (11.7, 40)]
C3 = [(11.7,20), (24, 20), (11.7, 40), (24, 40)]
C4 = [(11.7,7), (24, 7), (11.7, 20), (24, 20)]
C5 = [(24,7), (30, 7), (24, 40), (30, 40)]
C6 = [(30,34), (32, 34), (30, 40), (32, 40)]
C7 = [(32,0), (40, 0), (32, 40), (40, 40)]
C8 = [(10,0), (32, 0), (10, 7), (32, 7)]



def dist_fn(x, y):
    d = math.sqrt((x[0] - y[0])**2 + (x[1] + y[1])**2)
    return d

def center_cell(cell):
    c = (cell[0][0] + cell[1][0]) / 2, (cell[0][1] + cell[2][1]) / 2
    return c

def move_cell(cell, rob_area):
    
    area_cell = abs(cell[0][0] - cell[1][0]) * abs(cell[0][1] - cell[2][1])
    distance = area_cell / rob_area
    
    total_dist = distance
    return total_dist
lowest = []
tot_dist = 0

L = [C1, C2, C3, C4, C5, C6, C7, C8]
L2 = [C2, C1, C8, C7, C6, C4, C5, C3]
L3 = [C3, C4, C5, C6, C7, C8, C1, C2]
L4 = [C4, C5, C4, C8, C1, C2, C3,  C5]
L5 = [C5, C4, C6, C7,C8, C1, C2,  C3]
L6 = [C6, C7,C8, C1, C2, C3, C4,  C5]
L7 = [C7, C8, C1, C2, C3, C4, C5, C6]
L8 = [C8, C7, C6, C4, C5, C3, C2, C1]

    



for i in range(len(L)-1):
    ds = 0
    
    d1 = dist_fn(init_rob, L[i+1][1])
    d2 = move_cell(L[i], rob_area)
    ds = d1 + d2
    
    tot_dist += ds
    init_rob = L[i][-1]
lowest.append(tot_dist)
    
tot_dist = 0
for i in range(len(L2)-1):
    ds = 0
    
    d1 = dist_fn(init_rob, L2[i+1][1])
    d2 = move_cell(L2[i], rob_area)
    ds = d1 + d2
    
    tot_dist += ds
    init_rob = L2[i][-1]
lowest.append(tot_dist)
tot_dist = 0
for i in range(len(L3)-1):
    ds = 0
    d1 = dist_fn(init_rob, L3[i+1][1])
    d2 = move_cell(L3[i], rob_area)
    ds = d1 + d2
    
    tot_dist += ds
    init_rob = L3[i][-1]
lowest.append(tot_dist)
tot_dist = 0
for i in range(len(L4)-1):
    ds = 0
    d1 = dist_fn(init_rob, L4[i+1][1])
    d2 = move_cell(L4[i], rob_area)
    ds = d1 + d2
    
    tot_dist += ds
    init_rob = L4[i][-1]
lowest.append(tot_dist)
tot_dist = 0
for i in range(len(L5)-1):
    ds = 0
    d1 = dist_fn(init_rob, L5[i+1][1])
    d2 = move_cell(L5[i], rob_area)
    ds = d1 + d2
    
    tot_dist += ds
    init_rob = L5[i][-1]
lowest.append(tot_dist)
tot_dist = 0
for i in range(len(L6)-1):
    ds = 0
    d1 = dist_fn(init_rob, L6[i+1][1])
    d2 = move_cell(L6[i], rob_area)
    ds = d1 + d2
    
    tot_dist += ds
    init_rob = L6[i][-1]
lowest.append(tot_dist)
tot_dist = 0
for i in range(len(L7)-1):
    ds = 0
    d1 = dist_fn(init_rob, L7[i+1][1])
    d2 = move_cell(L7[i], rob_area)
    ds = d1 + d2
    
    tot_dist += ds
    init_rob = L7[i][-1]
lowest.append(tot_dist)
tot_dist = 0
for i in range(len(L8)-1):
    ds = 0
    d1 = dist_fn(init_rob, L[i+1][1])
    d2 = move_cell(L8[i], rob_area)
    ds = d1 + d2
    
    tot_dist += ds
    init_rob = L8[i][-1]
lowest.append(tot_dist)
    
print(lowest)
print(len(lowest))
def minimum(a, n):
 
    # inbuilt function to find the position of minimum
    minpos = a.index(min(a))
 
    
    
    return minpos + 1
 
 

minn = minimum(lowest, len(lowest))
print("cell for optimized distance",minn)
    

    


