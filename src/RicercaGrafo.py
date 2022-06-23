from igraph import *
import utils

vertex_values = []
for x in range(0, 36):
    vertex_values.append(str(x))


def bfs(graph, start, end):
    # maintain a queue of paths
    queue = [[start]]
    # push the first path into the queue
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        # path found
        if node == end:
            return path
        # enumerate all adjacent nodes, construct a
        # new path and push it into the queue
        for adjacent in graph.neighbors(node):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)


def path_cost(path):
    """
    returns cost of a path
    :param path: path to find cost of
    :return: cost of the path
    """
    total_cost = 0
    for (node, cost) in path:
        total_cost += cost
    return total_cost, path[-1][0]


def add_cost(graph, start, neighbours):
    """
    adds cost to neighbour list
    :param graph:
    :param start:
    :param neighbours:
    :return weighted_list: list of neighbours with costs added
    """
    weighted_list = []

    for node2 in neighbours:
        weighted_list.append([node2, graph.es.select(_source=start, _target=node2)['weight'][0]])

    return weighted_list


def lowest_cost_first(graph, start, end):
    """
    returns path to end node, starting from start node, using Lowest Cost First Search
    :param graph:
    :param start:
    :param end:
    :return path: path to end node
    """
    visited = []
    queue = [[(start, 0)]]

    while queue:
        queue.sort(key=path_cost)
        path = queue.pop(0)
        node = path[-1][0]
        visited.append(node)
        if node == end:
            return path

        else:
            adjacent_nodes = add_cost(graph, node, graph.neighbors(node))
            for (node2, cost) in adjacent_nodes:
                new_path = path.copy()
                new_path.append((node2, cost))
                queue.append(new_path)


def setup_graph():
    """
    Creates weighted graph
    :return graph: graph
    :return edges: list of edges of the graph
    :return weights: list of weights of the graph edges
    """
    a = [('0', '1', 4), ('0', '2', 5), ('2', '3', 1), ('3', '4', 4), ('2', '5', 2), ('2', '10', 3), ('9', '10', 2),
         ('27', '10', 2), ('10', '11', 3), ('13', '11', 1), ('9', '8', 1), ('5', '8', 1), ('5', '6', 4), ('6', '7', 2),
         ('8', '7', 2), ('6', '34', 6), ('34', '33', 2), ('30', '33', 3), ('7', '30', 3), ('34', '32', 5),
         ('33', '35', 2),
         ('28', '35', 2), ('30', '29', 2), ('29', '9', 2), ('35', '32', 2), ('29', '28', 1), ('27', '28', 2),
         ('32', '31', 2),
         ('27', '31', 4), ('13', '14', 2), ('13', '15', 4), ('13', '17', 1), ('11', '12', 2), ('20', '12', 1),
         ('27', '20', 2),
         ('12', '17', 3), ('17', '18', 1), ('18', '16', 4), ('19', '18', 5), ('19', '20', 5),
         ('20', '21', 2), ('21', '22', 1), ('21', '23', 2), ('23', '24', 4), ('25', '24', 2), ('25', '26', 1)]

    edge = []
    weights = []

    for i in range(46):

        for j in range(2):
            k = 2
            edge.append(a[i][j])

        weights.append(a[i][k])

    edges = [(i, j) for i, j in zip(edge[::2], edge[1::2])]
    list1 = []
    for i in range(len(edges)):
        list1.append((int(edges[i][0]), int(edges[i][1])))

    graph = Graph()
    for i in range(0, 36):
        graph.add_vertex(i)

    graph.add_edges(list1)
    graph.es['weight'] = weights
    edges = graph.get_edgelist()
    return graph, edges, weights


def find_solution(graph, start):
    """
    executes a search on the graph and returns the path in form of a list of nodes
    :param start: starting node
    :param graph: graph to search into
    :return solution: list of nodes representing the solution
    """
    goal = -1
    while goal < 0 or goal > 35:
        goal = int(input("Insert the node that you want to reach (0-35)\n"))

        if goal < 0 or goal > 35:
            print("Incorrect value")

    search_method = -1
    while search_method != 1 and search_method != 2:

        search_method = int(input("Insert the search method: \n1:Breadth-first-search\n2:Lowest-cost-first-search\n"))

        if search_method == 1:
            solution = bfs(graph, start, goal)
            print("Solution is:\n" + str(solution))
        elif search_method == 2:
            solution = lowest_cost_first(graph, 0, goal)
            print("Solution is:\n")
            print([x[0] for x in solution])
            print("Cost of solution is: ", path_cost(solution)[0])
        else:
            print("Incorrect answer")

    return solution


def print_solution(graph, solution, weights, color):
    """
    displays an image of the solution of the search on the graph
    :param color: color of the printed solution
    :param weights: list of graph weights
    :param graph: graph to print
    :param solution: solution to highlight on the image
    :return:
    """

    edges = graph.get_edgelist()
    g = Graph(edges)
    vertex_set = set(solution)
    g.vs["color"] = "yellow"
    g.es["label"] = weights
    try:
        sol_edges = g.vs.select(vertex_set)
    except TypeError:
        vertex_set = (x[0] for x in vertex_set)
        sol_edges = g.vs.select(vertex_set)

    sol_edges["color"] = color
    g.layout(layout='auto')
    plot(g, vertex_label=vertex_values)


def research(titles):
    """
    prints paths based on lowest-cost-first to find all movies in the shelves

    :param titles: movies to search for
    :return:
    """

    # setup and print graph
    graph, edges, weights = setup_graph()
    g = Graph(edges)
    plot(g, vertex_label=vertex_values)

    # print solutions on graph
    colors = ["red", "blue", "green", "brown", "purple"]
    racks = []
    for title in titles:
        # populate racks list with relative graph nodes
        racks.append(utils.get_nodes(utils.get_rack(utils.get_movie_id(title))))

    start_node = 0

    for rack, title, color in zip(racks, titles, colors):
        # print lowest-cost-first search path from movie to movie
        sol = lowest_cost_first(graph, start_node, rack)
        start_node = rack
        solution = [s[0] for s in sol]
        input("Press [enter] to print path to '{}'".format(title))
        print_solution(graph, solution, weights, color)
