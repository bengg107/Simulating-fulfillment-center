import math
import random
import numpy as np


def generate_orderbook(N, M):
    omega = np.random.normal(0, 1, N)
    omega = abs(omega)
    nij = np.random.geometric(p=1 / (1 + omega), size=(M, N)) - 1

    wjlist = [sum([nij[i][j] for i in range(M)]) for j in range(N)]

    orderbook = []
    for i in range(M):
        orderbook.append(np.concatenate([[j] * nij[i, j] for j in range(N)]))

    return [orderbook, wjlist]

def find_item_index(given_list, p):
    """It finds the index of the closest element of given_list to point p"""
    dist_list = []
    for item in given_list:
        dist_list.append(math.dist(p, item))
    index = dist_list.index(min(dist_list))
    return index


def sort_fun(given_list):
    """Finds the path of the robot"""
    output_list = []
    index = find_item_index(given_list, [0, 0])
    output_list.append(given_list[index])
    given_list = given_list[0:index] + given_list[index + 1:]

    while given_list:
        index = find_item_index(given_list, output_list[-1])
        output_list.append(given_list[index])
        given_list = given_list[0:index] + given_list[index + 1:]

    return output_list


def robot_dist(given_list):
    """Computes the total distance travelled by the robot"""
    if not given_list:
        return 0
    seq = sort_fun(given_list)
    dist = math.dist([0, 0], seq[0])
    for i in range(len(seq) - 1):
        dist += math.dist(seq[i], seq[i + 1])
    return dist


# given N number of items, which is assumed to be divisible by 4, output a list of coordinates on the square
# this functions returns a list
def position_function(N):
    list = []
    intN = int(N/4)
    for i in range(intN):
        list.append([i+1,0])
        list.append([0, i+1])
    for i in range(intN):
        list.append([i+1, intN+1])
        list.append([intN+1, i+1])
    return list


def position_random_generator(N):
    positions = position_function(N)
    random.shuffle(positions)
    return positions


# given N number of items, return  which is assumed to be divisible by 4, return a list of randomised coordinates
def position_random_generator(N):
    positions = position_function(N)         # generate positions ordered in a certain manner
    random.shuffle(positions)                # shuffle the items in the list
    return positions

def dictionary_func(N):
# come up with a dictionary given N number of items. It assigns the item to a position in a naive way.
    a = position_function(N)
    diction = {i: a[i] for i in range(N)}
    return diction

def OrderToCoord(order, wjlist, N):
# given order and number of items, return the coordinates of these items in a list
    a = position_function(N)
    sorting_index = (np.argsort(wjlist))[::-1]
    #sorting_index = np.arange(N)
    diction = {i: a[sorting_index[i]] for i in range(N)}
    coord = [diction[item] for item in order]
    return coord

def TrivialOrderToCoord(order, wjlist, N):
# given order and number of items, return the coordinates of these items in a list
    a = position_function(N)
    #sorting_index = (np.argsort(wjlist))[::-1]
    sorting_index = np.arange(N)
    diction = {i: a[sorting_index[i]] for i in range(N)}
    coord = [diction[item] for item in order]
    return coord

def DistanceList1(N, M):
    [orderbook,wjlist] = generate_orderbook(N, M)
    arr_len = []
    for i in range(M): # item in order[0]:
        item0 = np.ndarray.tolist(orderbook[i])
        item0 = OrderToCoord(item0, wjlist, N)
        arr_len.append(robot_dist(item0))
    return arr_len

def DistanceList2(N, M):
    [orderbook,wjlist] = generate_orderbook(N, M)
    arr_len = []
    for i in range(M): # item in order[0]:
        item0 = np.ndarray.tolist(orderbook[i])
        item0 = TrivialOrderToCoord(item0, wjlist, N)
        arr_len.append(robot_dist(item0))
    return arr_len

# njlist = generate_orderbook(8,8)
# print(njlist[0])
# print(njlist[1])
# print((np.argsort(njlist[1]))[::-1])

arr_len = DistanceList(100,400)

print(arr_len)
import matplotlib.pyplot as plt
plt.hist(arr_len)
plt.show()

