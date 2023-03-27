from singly_linked_lists import LinkedList


class Graph:
    """

    An array of linked lists is used to store all the edges in the graph. 
    The size of the array is equal to the number of vertices in the graph. 
    Each index of the array contains a vertex. 
    This vertex points to a linked list that contains all the vertices connected to this one.

    Directed Graph: 
        Total Number of Possible Edges: vertices * (vertices - 1)
        Minimum Number of Edges to Connect to Every Other Vertex: vertex - 1
    UnDirected Graph:
        Total Number of Possible Edges: vertices * (vertices - 1) / 2 

    """

    def __init__(self, vertices):
        # Total number of vertices
        self.vertices = vertices
        # Defining a list which can hold multiple LinkedLists
        # equal to the number of vertices in the graph
        self.container = []

        # Creating a new LinkedList for each vertex/index of the list
        for i in range(vertices):
            # Appending a new LinkedList on each array index
            self.container.append(LinkedList())

    def add_edge(self, source, destination):
        if (source < self.vertices and destination < self.vertices):
            # directed graph
            self.container[source].insert_at_head(destination)
            # undirected graph
            # self.container[destination].insert_at_head(source)

        # If we were to implement an Undirected Graph i.e (1,0) == (0,1)
        # We would create an edge from destination towards source as well
        # i.e self.list[destination].insertAtHead(source)

    def print_graph(self):
        print(">>Adjacency List of Directed Graph<<")
        for i in range(self.vertices):
            print("[", i, "]", end="-> ")
            temp = self.container[i].get_head()
            while temp:
                print(temp.data, end=" --> ")
                temp = temp.next
            print('None')


g = Graph(4)
g.add_edge(0, 2)
g.add_edge(0, 1)
g.add_edge(1, 3)
g.add_edge(2, 3)

g.print_graph()
