import matplotlib.pyplot as plt
import networkx as nx


class NetworkXDirectedGraph:
    def __init__(self, graph_info, from_edge_list=False):
        if not from_edge_list:
            self.g = self.produce_graph_matrix(graph_info)
        else:
            self.g = self.produce_graph_edge_list(graph_info)

    @staticmethod
    # Accepts 2D array representing adjacency matrix, values can be 0 or 1
    def produce_graph_matrix(adjacency_matrix):
        directed_graph = nx.DiGraph()
        for i in range(len(adjacency_matrix)):
            # Create node for all nodes in matrix
            directed_graph.add_node(i + 1)
            for j in range(len(adjacency_matrix[i])):
                if adjacency_matrix[i][j] == 1:
                    # Create edge for all identified edges in matrix
                    directed_graph.add_edge(i + 1, j + 1)
        return directed_graph

    @staticmethod
    # Accepts file path for text file containing edge list
    def produce_graph_edge_list(file_path):
        return nx.read_edgelist(file_path, create_using=nx.DiGraph)

    # Renders image of graph using Matplotlib interface
    def draw_graph(self):
        pos = nx.spring_layout(self.g)
        nx.draw(self.g, pos, with_labels=True, font_weight='bold')
        plt.subplot(111)
        nx.draw_shell(self.g, with_labels=True, font_weight='bold')
        plt.show()
