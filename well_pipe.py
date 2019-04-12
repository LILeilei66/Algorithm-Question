"""
Via google:
村庄有N户人家，每家都想要喝水。
自己建一口井的代价是well[i], 或者也可以拉一条水管去别人家，水管代价是pipe[i][j] = pipe[j][i]。
问整个村庄都能喝到水的最小代价

input:
double well[N];
double pipe[N][N];
"""

import numpy as np

def drink(well, pipe):
    """
    :param well: 建井的代价
    :param pipe:  拉水管的代价
    :return: min sum
    """
    N = len(well) # 村庄个数
    cost = [] # 每个村庄的cost
    well_place = [] # 哪些村庄打了井

    # 1. 先将所有连起来.
    well_place.append(np.argmin(well))

    cost = pipe[np.argmin(np.array(pipe).sum(0))]
    cost[well_place[0]] = well[well_place[0]]

    # 2. 遍历.
    # 取 接管子和打井 的最小值.
    for village in range(N):
        if village in well_place: # 若是已经打井, 肯定是打井cost小
            continue
        # 查看village 和所有村庄的min.
        village_pipe = pipe[village]
        cost[village] = min(min(village_pipe), well[village])

    return sum(cost)

if __name__ == '__main__':
    """
    如果有ABCD四个点，打井要花100，然后接水管A-B, C-D是10, B-C是20
    """
    well = [100,100,100,100]
    pipe = [[1000, 10,200,200], # sum = 1410
            [10, 1000, 20, 200], # sum = 1230
            [200, 20, 1000, 10], # sum = 1230
            [200, 200, 10, 1000]] # sum = 1410
    print(drink(well, pipe)) # 140

    """
    A.well = 5; B.well = 10;
    A-B = 1; C-B = 1; D-B = 1;
    """
    well = [5, 10, 100, 100]
    pipe = [[1000, 1, 100, 100],
            [1, 1000, 1, 1],
            [100, 1, 1000, 100],
            [100, 1, 100, 1000]]
    print(drink(well, pipe)) # 8