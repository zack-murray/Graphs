from graph import Graph
from util import Stack, Queue

# Set up graph 
def build_graph(ancestors):
    graph = Graph()
    for parent, child in ancestors:
        # Create parent/child nodes
        graph.add_vertex(parent)
        graph.add_vertex(child)
        # Set edges to make directed graph (child->parent)
        graph.add_edge(child, parent)
    return graph

def earliest_ancestor(ancestors, starting_node):
    # Instantiate graph structure
    graph = build_graph(ancestors)
    # Instantiate empty queue
    q = Queue()
    # Put input node into the que
    q.enqueue([starting_node])
    # Set values to prep max path len and earliest ancestor
    max_path_len = 1
    earliest_ancestor = -1
    # While queue isnt empty 
    while q.size() > 0:
        # Setup the path and vertex pointer
        path = q.dequeue()
        v = path[-1]
        # If the path is equal or longer and the value is smaller, or if the path is longer
        if (len(path) >= max_path_len and v < earliest_ancestor) or (len(path) > max_path_len):
            earliest_ancestor = v
            max_path_len = len(path)
        for neighbor in graph.vertices[v]:
            # Copy the path
            path_copy = list(path)
            # Append the neighbor to the back of the queue
            path_copy.append(neighbor)
            q.enqueue(path_copy)
    
    return earliest_ancestor

# Nick's BFT Implementation

# import sys
# sys.path.append('../graph')
# from util import Queue
# from graph import Graph
# def earliest_ancestor(ancestors, starting_node):
#     # Create our graph
#     graph = Graph()
#     # Add vertices to graph
#     for parent, child in ancestors:
#         graph.add_vertex(parent)
#         graph.add_vertex(child)
#         # Add directions
#     for parent, child in ancestors:
#         # Since we want to traverse *up* the list we will point the child -> parent -> grandparent
#         graph.add_edge(child, parent)
#     qq = Queue()
#     qq.enqueue([starting_node])
#     if len(graph.get_neighbors(starting_node)) == 0:
#         return -1
#     else:
#         while qq.size() > 0:
#             path = qq.dequeue()
#             vertex = path[-1]
#             parents = graph.get_neighbors(vertex)
#             for parent in sorted(parents, reverse=True):
#                 copy_path = list(path)
#                 copy_path.append(parent)
#                 qq.enqueue(copy_path)
#         return vertex