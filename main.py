open_list = []
closed_list = []

class Node:
    def __init__(self, name = None, neighbor_one = None, neighbor_two = None, neighbor_three = None):
        self.name = name
        self.neighbor_one = neighbor_one
        self.neighbor_two = neighbor_two
        self.neighbor_three = neighbor_three


def A_Star(node):

    open_list.append(node.name)

    while open_list != None:
