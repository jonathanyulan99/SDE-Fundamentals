from singly_linked_lists import LinkedList


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        # implement using an adjaceny List
        self.container = []

        for i in range(self.vertices):
            self.container.append(LinkedList())

    def add_edge(self, source, destination):
        if source < self.vertices and destination < self.vertices:
            self.container[source].insert_at_head(destination)
            # if it was undirected graph
            # self.container[destination].insert_at_head(source)

    def graph_print(self):
        print("Adjacency List")

        for i in range(self.vertices):
            print("[", i, "]", end="--> ")
            itr = self.container[i].get_head()
            while itr:
                print(itr.data, end=' --> ')
                itr = itr.next
            print("None")


g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(1, 2)
g.add_edge(1, 4)
g.add_edge(2, 3)
g.add_edge(3, 1)
g.add_edge(3, 2)
g.add_edge(3, 4)
g.add_edge(4, 0)

g.graph_print()
