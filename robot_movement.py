import math


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
    seq = sort_fun(given_list)
    dist = math.dist([0, 0], seq[0])
    for i in range(len(seq) - 1):
        dist += math.dist(seq[i], seq[i + 1])
    return dist
