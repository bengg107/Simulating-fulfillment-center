import math
import random
import numpy as np


def generate_orderbook(N, M):
    omega = np.random.normal(0, 1, N)
    omega = abs(omega)
    nij = np.random.geometric(p=1 / (1 + omega), size=(M, N)) - 1

    orderbook = []
    for i in range(M):
        orderbook.append(np.concatenate([[j] * nij[i, j] for j in range(N)]))

    return orderbook

def find_item_index(given_list, p):
    """It finds the index of the closest element of give_list to point p"""
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
    intN = int(N/4)
    a1 =  [(i+1 , 0) for i in range(intN)]    # bottom side
    a2 = [(intN+1, i+1) for i in range(intN)]   # right side
    a3 = [(0, i+1) for i in range(intN)]      # left side
    a4 = [(i+1, intN+1) for i in range(intN)] # top side
    a = [*a1, *a2, *a3, *a4]                   # concat the sides together
    return a


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

def OrderToCoord(order, N):
# given order and number of items, return the coordinates of these items in a list
    diction_tr = dictionary_func(N)
    coord = [diction_tr[item] for item in order]
    return coord

def DistanceList(N, M):
    order = generate_orderbook(N, M)
    arr_len = []
    for item in order:
        item0 = np.ndarray.tolist(item)
        item0 = OrderToCoord(item0, N)
        arr_len.append(robot_dist(item0))
    return arr_len


print(DistanceList(100,400))

#print(arr_len)
# import matplotlib.pyplot as plt
# plt.hist(arr_len)
# plt.show()

