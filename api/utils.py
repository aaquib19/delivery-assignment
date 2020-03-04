from collections import defaultdict
from itertools import permutations
graph = {

    'L1':{'C1':3,'C2':2.5,'C3':2},
    'C1':{'L1':3,'C2':4,'C3':5},
    'C2':{'L1':2.5,'C1':4,'C3':3},
    'C3':{'L1':2,'C1':5,'C2':3},
}

db={

    'A':{'loc':'C1','weight':3},
    'B':{'loc':'C1','weight':2},
    'C':{'loc':'C1','weight':8},
    'D':{'loc':'C2','weight':12},
    'E':{'loc':'C2','weight':25},
    'F':{'loc':'C2','weight':15},
    'G':{'loc':'C3','weight':.5},
    'H':{'loc':'C3','weight':1},
    'I':{'loc':'C3','weight':2},
}

paths = {
    #if c1 and c2 are there 
    'C1':[
        ['C1','L1']
    ],
    'C2':[
        ['C2','L1']
    ],
    'C3':[
        ['C3','L1']
    ],


    'C1C2':
        [
        ['C1','C2','L1'],
        ['C2','C1','L1'],
        ['C2','L1','C1','L1'],
        ['C1','L1','C2','L1'],
        ],
    'C1C3':[
        ['C1','L1','C3','L1'],
        ['C3','L1','C1','L1'],
        ],
    'C2C3':[
        ['C2','C3','L1'],
        ['C3','C2','L1'],
        ['C3','L1','C2','L1'],
        ['C2','L1','C3','L1'],
    ],
    'C1C2C3':[
        ['C1','C2','C3','L1'],
        ['C1','C2','L1','C3','L1'],
        ['C1','L1','C2','L1','C3','L1'],
        ['C1','L1','C2','C3','L1'],
        ['C2','C1','L1','C3','L1'],
        ['C2','C3','L1','C1'],
        ['C3','L1','C2','C1','L1'],
        ['C3','C2','C1','L1'],
        ['C3','L1','C2','L1','C1','L1'],
        ['C3','C2','L1','C1','L1']
    ]

    
}


def calculate_travel_cost(curr, warehouses,dropped, path):
    if curr == 'L1':
        return 10
    weight = warehouses[curr]

    res = 10
    weight = weight-5
    while(weight>0):
        res+=8

        weight -=5
    return res




def calculate_cost(order):
    center = set()
    warehouses = defaultdict(lambda : 0)
    for item in order:
        wgt = float(order[item])*db[item]['weight']
        center.add(db[item]['loc'])
        warehouses[db[item]['loc']] +=wgt
    # print(warehouses,center)

    center = sorted(center)
    # print(center)
    paths_ = paths["".join(center)]
    cost = []
    for path in paths_:
        res = 0
        dropped = []
        cost_=0
        for i in range(len(path)):
            if(i == len(path)-1):
                cost.append(res)
                break
            if path[i]=='L1':
                dropped.extend(path[:i])
                cost_ = 0
            cost_ =calculate_travel_cost(path[i],warehouses,dropped,path)
            res += cost_*graph[path[i]][path[i+1]]
      
            


    return {"cost":min(cost)}
 

# ans = calculate_cost({'A': '1','B':1,'C':'1'})