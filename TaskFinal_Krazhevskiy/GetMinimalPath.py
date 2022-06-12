# functions for working with graph of cities and getting the best route

import sys
import itertools as it


def get_outgoing_edges(graph, node):
    """
    This function returns the outgoing edges of a node
    :param graph:
    :param node:
    :return:
    """
    connections = []
    for out_node in graph.keys():
        if graph[node].get(out_node, False):
            connections.append(out_node)
    return connections


def dijkstra(graph, start, end):
    """
    This function implements Dijkstra's algorithm for finding the shortest path
    :param graph: graph
    :param start: start point
    :param end: end point
    :return: list of points
    """
    unvisited_nodes = list(graph.keys())
    shortest_path = {}
    previous_nodes = {}

    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    shortest_path[start] = 0

    while unvisited_nodes:
        current_min_node = None
        for node in unvisited_nodes:
            if current_min_node is None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node

        neighbors = get_outgoing_edges(graph, current_min_node)
        # print("neighbours", neighbors)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph[current_min_node][neighbor]
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                previous_nodes[neighbor] = current_min_node

        unvisited_nodes.remove(current_min_node)

    return previous_nodes, shortest_path


def print_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node

    while node != start_node:
        path.append(node)
        node = previous_nodes[node]
    path.append(start_node)

    print(f"The best route with fuel consumption {shortest_path[target_node]} is:")
    print(" -> ".join(reversed(path)))


def get_results(graph, start_node, end_node):
    previous_nodes, shortest_path = dijkstra(graph, start_node, end_node)

    path = []
    node = end_node
    while node != start_node:
        path.append(node)
        node = previous_nodes[node]
        # print(node)
    path.append(start_node)

    return path[::-1], shortest_path[end_node]


def get_best_route(graph: dict, start_node: str, target_node: str, visit_cities: list) -> dict:
    """
    This function finds the best route
    :param graph: graph
    :param start_node: start point
    :param target_node: end point
    :param visit_cities: list of cities to visit
    :return: list of points
    """
    if not visit_cities:
        previous_nodes, shortest_path = dijkstra(graph, start_node, target_node)
        # print(previous_nodes)
        print_result(previous_nodes, shortest_path, start_node, target_node)
        return shortest_path[target_node]

    if len(visit_cities) == 1:
        path, cost = get_results(graph, start_node, visit_cities[0])
        path1, cost1 = get_results(graph, visit_cities[0], target_node)
        del path1[0]

        print(f"The best route with fuel consumption {cost + cost1} is:")
        print(" -> ".join(path), "->", " -> ".join(path1))
        return cost + cost1

    complete_paths = []
    complete_costs = []
    for mutation in it.permutations(visit_cities):
        city = start_node
        complete_cost = 0
        complete_path = [start_node]

        for node in mutation:
            path, cost = get_results(graph, city, node)
            del path[0]
            city = node
            complete_cost += cost
            complete_path += path

        path, cost = get_results(graph, city, target_node)
        del path[0]
        complete_path += path
        complete_cost += cost
        complete_costs.append(complete_cost)
        complete_paths.append(complete_path)

    final_cost = min(complete_costs)
    final_path = complete_paths[complete_costs.index(final_cost)]
    print(f"The best route with fuel consumption {final_cost} is:")
    print(" -> ".join(final_path))
