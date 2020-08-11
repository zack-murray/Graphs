"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("nonexistent vertex")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue
        q = Queue()
        # Add starting vertex ID
        q.enqueue(starting_vertex)
        # Create set for visited verts
        visited = set()
        # While queue is not empty
        while q.size() > 0:
            # Dequeue a vert
            last_vert = q.dequeue()
            # If not visited
            if last_vert not in visited:
                # Visit it!
                # print(last_vert)
                # Mark as visited
                visited.add(last_vert)
                # Add all neighbors to the queue
                for neighbor in self.get_neighbors(last_vert):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack
        s = Stack()
        # Add starting vertex ID
        s.push(starting_vertex)
        # Create set for visited verts
        visited = set()
        # While the stack isn't empty
        while s.size() > 0:
            # Pop off the top element, this is the current vert
            last_vert = s.pop()
            # If we haven't visited this vert yet
            if last_vert not in visited:
                # Visit it!
                # print(last_vert)
                # Mark it as visited
                visited.add(last_vert)
                # Get its neighbors
                neighbors = self.get_neighbors(last_vert)
                # For each of the neighbors
                for neighbor in neighbors:
                    # Push it to the stack
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # Create set for visited verts
        visited = set()

        def dft_recurse(vertex):
            # Base case
            if vertex in visited:
                return
            else:
                # Mark it as visited
                visited.add(vertex)
            # Print it out
            # print(vertex)
            # Recurse through each neighbor
            for neighbor in self.get_neighbors(vertex):
                dft_recurse(neighbor)
        # Recurse from the starting vert
        dft_recurse(starting_vertex)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()
        q.enqueue([starting_vertex])
        # Create a Set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH
            path = q.dequeue()
            # Grab the last vertex from the PATH
            last_vert = path[-1]
            # If that vertex has not been visited...
            if last_vert not in visited:
                # Visit it!
                # print(last_vert)
                # CHECK IF IT'S THE TARGET
                if last_vert == destination_vertex:
                  # IF SO, RETURN PATH
                  return path
                # Mark it as visited...
                visited.add(last_vert)
                # Then add A PATH TO its neighbors to the back of the queue
                for neighbor in self.get_neighbors(last_vert):
                  # COPY THE PATH
                  next_path = path.copy()
                  # APPEND THE NEIGHOR TO THE BACK
                  next_path.append(neighbor)
                  q.enqueue(next_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty stack
        s = Stack()
        # Add starting vertex ID
        s.push([starting_vertex])
        # Create a Set to store visited vertices
        visited = set()
        # While the stack isn't empty
        while s.size() > 0:
            # Pop the first PATH
            path = s.pop()
            # Grab the last vertex from the PATH
            last_vert = path[-1]
            # If that vertex has not been visited...
            if last_vert not in visited:
                # Visit it!
                # print(last_vert)
                # Mark it as visited...
                visited.add(last_vert)
                # CHECK IF IT'S THE TARGET
                if last_vert == destination_vertex:
                    # IF SO, RETURN PATH
                    return path
                # Then add A PATH TO its neighbors to the top of the stack
                for neighbor in self.get_neighbors(last_vert):
                    # COPY THE PATH
                    next_path = path.copy()
                    # APPEND THE NEIGHOR TO THE TOP
                    next_path.append(neighbor)
                    s.push(next_path)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # Create a Set to store visited vertices
        visited = set()

        def dfs_recurse(path):
            # Grab the last vertex from the PATH
            last_vert = path[-1]
            # Base case
            if last_vert in visited:
                return None
            else:
                # Mark it as visited
                visited.add(last_vert)
            # CHECK IF IT'S THE TARGET
            if last_vert == destination_vertex:
                return path
            # Add A PATH TO its neighbors to the top of the stack
            for neighbor in self.get_neighbors(last_vert):
                # COPY THE PATH
                next_path = path.copy()
                # APPEND THE NEIGHOR TO THE TOP
                next_path.append(neighbor)
                # Recurse through each neighbor
                found = dfs_recurse(next_path)
                # Break if destination vert found
                if found:
                    return found
            
            return None
        # Recurse from the starting vert
        return dfs_recurse([starting_vertex])

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    print('bft')
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print('dft')
    graph.dft(1)
    print('dft recursive')
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print('bfs')
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print('dfs')
    print(graph.dfs(1, 6))
    print("dfs recursive")
    print(graph.dfs_recursive(1, 6))
