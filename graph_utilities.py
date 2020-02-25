import matplotlib.pyplot as plt
import networkx as nx


class NetworkXDirectedGraph:
    SOURCE_NODE = '1'
    TARGET_NODE = '2'

    def __init__(self, graph_info, from_edge_list=False):
        if not from_edge_list:
            self.g = self.produce_graph_matrix(graph_info)
            self.bfs_max_flow = 0
            self.dijkstra_max_flow = 0
        else:
            self.g = self.produce_graph_edge_list(graph_info)
            self.bfs_max_flow = self.max_flow(self.BFS)
            self.dijkstra_max_flow = self.max_flow(nx.dijkstra_path)

    @staticmethod
    # Accepts 2D array representing adjacency matrix, values can be 0 or 1
    def produce_graph_matrix(adjacency_matrix):
        directed_graph = nx.DiGraph()
        for i in range(len(adjacency_matrix)):
            # Create node for all nodes in matrix
            directed_graph.add_node(str(i + 1))
            for j in range(len(adjacency_matrix[i])):
                if adjacency_matrix[i][j] == 1:
                    # Create edge for all identified edges in matrix
                    directed_graph.add_edge(str(i + 1), str(j + 1))
        return directed_graph

    @staticmethod
    # Accepts file path for text file containing edge list
    def produce_graph_edge_list(file_path):
        return nx.read_edgelist(file_path, create_using=nx.DiGraph)

    # Applies given algorithm to find path from s to t
    def flow_path(self, g, path_alg):
        try:
            flow_path = path_alg(g, self.SOURCE_NODE, self.TARGET_NODE)
        except nx.NetworkXNoPath:
            flow_path = None
        return flow_path

    # Computes Ford Fulkerson max flow with configurable algorithm for finding path from s to t
    def max_flow(self, path_alg):
        current_graph = self.g.copy()
        # Start with flow of 0 on all edges
        max_flow = 0
        current_flow_path = self.flow_path(current_graph, path_alg)
        while current_flow_path:
            # Augment max flow
            max_flow += 1
            # Update residual graph based on flow path
            current_graph = self.residual_graph(current_graph, current_flow_path)
            current_flow_path = self.flow_path(current_graph, path_alg)
        return max_flow

    @staticmethod
    # Generates residual graph for a given flow
    def residual_graph(g, flow_path):
        for i in range(len(flow_path) - 1):
            # Decrement capacity of or remove forwards edge where flow occurs
            if g[flow_path[i]][flow_path[i + 1]]['capacity'] == 1:
                g.remove_edge(flow_path[i], flow_path[i + 1])
            else:
                g[flow_path[i]][flow_path[i + 1]]['capacity'] -= 1
            # Increment capacity of or create backwards edge where flow occurs
            if flow_path[i] in g[flow_path[i + 1]]:
                g[flow_path[i + 1]][flow_path[i]]['capacity'] += 1
            else:
                g.add_edges_from([(flow_path[i + 1], flow_path[i], {'capacity': 1})])
        return g

    # Renders image of graph using Matplotlib interface
    def draw_graph(self):
        pos = nx.spring_layout(self.g)
        nx.draw(self.g, pos, with_labels=True, font_weight='bold')
        plt.subplot(111)
        nx.draw_shell(self.g, with_labels=True, font_weight='bold')
        plt.show()

    @staticmethod
    # Implements BFS as in Note1
    def BFS(g, s, t):
        visited = [False] * (g.number_of_nodes() + 1)
        visited[int(s)] = True
        # maintain a queue of paths
        toExplore = []
        # push the first path into the queue
        toExplore.append([s])
        while toExplore:
            # get the first path from the queue
            path = toExplore.pop(0)
            # get the last node from the path
            node = path[-1]
            # path found
            if node == t:
                return path
            # enumerate all adjacent nodes, construct a new path and push it into the queue
            for neighbor in g.neighbors(node):
                if not visited[int(neighbor)]:
                    visited[int(neighbor)] = True
                    new_path = list(path)
                    new_path.append(neighbor)
                    toExplore.append(new_path)
        return None
