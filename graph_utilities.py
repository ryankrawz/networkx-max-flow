import matplotlib.pyplot as plt
import networkx as nx


class NetworkXDirectedGraph:
    def __init__(self, adjacency_matrix):
        self.g = self.produce_graph(adjacency_matrix)

    @staticmethod
    # Accepts 2D array representing adjacency matrix, values can be 0 or 1
    def produce_graph(adjacency_matrix):
        directed_graph = nx.DiGraph()
        for i in range(len(adjacency_matrix)):
            # Create node for all nodes in matrix
            directed_graph.add_node(i)
            for j in range(len(adjacency_matrix[i])):
                if adjacency_matrix[i][j] == 1:
                    # Create edge for all identified edges in matrix
                    directed_graph.add_edge(i, j)
        return directed_graph

    # Renders image of graph using Matplotlib interface
    def draw_graph(self):
        nx.draw(self.g, with_labels=True, font_weight='bold')
        plt.subplot(111)
        nx.draw_shell(self.g, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')
        plt.show()

    # Implements BFS as in Note1
    def BFS(self, u):
        # Mark all the vertices as not visited (line 1-2 in pseudo-code)
        visited = [False] * (len(adjacency_matrix))

        # Create a queue for BFS (line 3 in pseudo-code)
        toExplore = []
        S = []

        # Mark the source node as visited and enqueue it
        toExplore.append(u)
        S.append(u)
        visited[u] = True

        while toExplore:

            # Dequeue a vertex from queue and print it
            s = queue.pop(0)

            for i in self.g.neighbors(u):
                if visited[i] == False:
                    visited[i] = True
                    toExplore.append(i)
                    S.append(i)
