from graph_utilities import NetworkXDirectedGraph


class GraphTestMatrix:
    def __init__(self):
        self.empty = NetworkXDirectedGraph([])
        self.singleton = NetworkXDirectedGraph([[1]])
        self.small = NetworkXDirectedGraph(
            [[1, 0],
             [1, 0]]
        )
        self.medium = NetworkXDirectedGraph(
            [[1, 0, 1, 1],
             [1, 1, 0, 0],
             [0, 0, 1, 1],
             [1, 0, 0, 0]]
        )
        self.large = NetworkXDirectedGraph(
            [[1, 0, 1, 0, 1, 0, 0, 1],
             [1, 1, 1, 0, 0, 1, 1, 1],
             [1, 0, 1, 0, 1, 1, 0, 1],
             [0, 1, 0, 1, 0, 0, 0, 1],
             [1, 0, 0, 1, 1, 1, 1, 1],
             [1, 1, 1, 1, 1, 0, 1, 0],
             [1, 1, 1, 0, 1, 1, 1, 1],
             [1, 0, 0, 1, 0, 1, 0, 0]]
        )
        self.completely_connected = NetworkXDirectedGraph(
            [[1, 1, 1, 1],
             [1, 1, 1, 1],
             [1, 1, 1, 1],
             [1, 1, 1, 1]]
        )
        self.completely_disconnected = NetworkXDirectedGraph(
            [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]
        )

    def test_edges(self):
        if (bool(self.empty.g.edges) or
           set(self.singleton.g.edges) != {(1, 1)} or
           set(self.small.g.edges) != {(1, 1), (2, 1)} or
           set(self.medium.g.edges) != {(1, 1), (1, 3), (1, 4), (3, 3), (3, 4), (4, 1), (2, 1), (2, 2)} or
           set(self.large.g.edges) != {(1, 1), (1, 3), (1, 5), (1, 8), (3, 1), (3, 3), (3, 5), (3, 6),
                                       (3, 8), (5, 1), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (8, 1),
                                       (8, 4), (8, 6), (2, 1), (2, 2), (2, 3), (2, 6), (2, 7), (2, 8),
                                       (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 7), (7, 1), (7, 2),
                                       (7, 3), (7, 5), (7, 6), (7, 7), (7, 8), (4, 2), (4, 4), (4, 8)} or
           set(self.completely_connected.g.edges) != {(1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (2, 2),
                                                      (2, 3), (2, 4), (3, 1), (3, 2), (3, 3), (3, 4),
                                                      (4, 1), (4, 2), (4, 3), (4, 4)} or
           bool(self.completely_disconnected.g.edges)):
            raise Exception('incorrect edges reported in GraphTestMatrix.test_edges')

    def test_nodes(self):
        if (bool(self.empty.g.nodes) or
           set(self.singleton.g.nodes) != {1} or
           set(self.small.g.nodes) != {1, 2} or
           set(self.medium.g.nodes) != {1, 3, 4, 2} or
           set(self.large.g.nodes) != {1, 3, 5, 8, 2, 6, 7, 4} or
           set(self.completely_connected.g.nodes) != {1, 2, 3, 4} or
           set(self.completely_disconnected.g.nodes) != {1, 2, 3, 4}):
            raise Exception('incorrect nodes reported in GraphTestMatrix.test_nodes')

    def sample_draw(self):
        self.large.draw_graph()

    def run_tests(self):
        self.test_edges()
        self.test_nodes()
        print('\nAll tests successful\n')


class GraphTestEdgeList:
    def __init__(self):
        self.two_nodes = NetworkXDirectedGraph('edge_lists/2_nodes.txt', from_edge_list=True)
        self.four_nodes = NetworkXDirectedGraph('edge_lists/4_nodes.txt', from_edge_list=True)
        self.nine_nodes = NetworkXDirectedGraph('edge_lists/9_nodes.txt', from_edge_list=True)

    def test_edges(self):
        if (set(self.two_nodes.g.edges) != {('1', '2')} or
           set(self.four_nodes.g.edges) != {('4', '2'), ('1', '3'), ('1', '4'), ('3', '4'), ('3', '2')} or
           set(self.nine_nodes.g.edges) != {('3', '6'), ('7', '2'), ('1', '9'), ('3', '8'), ('9', '2'),
                                           ('8', '7'), ('4', '3'), ('6', '7'), ('5', '7'), ('3', '5'),
                                           ('1', '4')}):
            raise Exception('incorrect edges reported in GraphTestEdgeList.test_edges')

    def test_nodes(self):
        if (set(self.two_nodes.g.nodes) != {'1', '2'} or
           set(self.four_nodes.g.nodes) != {'1', '2', '3', '4'} or
           set(self.nine_nodes.g.nodes) != {'1', '2', '3', '4', '5', '6', '7', '8', '9'}):
            raise Exception('incorrect nodes reported in GraphTestEdgeList.test_nodes')

    def sample_draw(self):
        self.nine_nodes.draw_graph()

    def run_tests(self):
        self.test_edges()
        self.test_nodes()
        print('\nAll tests successful\n')
