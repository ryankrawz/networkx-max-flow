from graph_utilities import NetworkXDirectedGraph


class GraphTest:
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
           set(self.singleton.g.edges) != {(0, 0)} or
           set(self.small.g.edges) != {(0, 0), (1, 0)} or
           set(self.medium.g.edges) != {(0, 0), (0, 2), (0, 3), (2, 2), (2, 3), (3, 0), (1, 0), (1, 1)} or
           set(self.large.g.edges) != {(0, 0), (0, 2), (0, 4), (0, 7), (2, 0), (2, 2), (2, 4), (2, 5),
                                       (2, 7), (4, 0), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (7, 0),
                                       (7, 3), (7, 5), (1, 0), (1, 1), (1, 2), (1, 5), (1, 6), (1, 7),
                                       (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6), (6, 0), (6, 1),
                                       (6, 2), (6, 4), (6, 5), (6, 6), (6, 7), (3, 1), (3, 3), (3, 7)} or
           set(self.completely_connected.g.edges) != {(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1),
                                                      (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3),
                                                      (3, 0), (3, 1), (3, 2), (3, 3)} or
           bool(self.completely_disconnected.g.edges)):
            raise Exception('incorrect edges reported in GraphTest.test_edges')

    def test_nodes(self):
        if (bool(self.empty.g.nodes) or
           set(self.singleton.g.nodes) != {0} or
           set(self.small.g.nodes) != {0, 1} or
           set(self.medium.g.nodes) != {0, 2, 3, 1} or
           set(self.large.g.nodes) != {0, 2, 4, 7, 1, 5, 6, 3} or
           set(self.completely_connected.g.nodes) != {0, 1, 2, 3} or
           set(self.completely_disconnected.g.nodes) != {0, 1, 2, 3}):
            raise Exception('incorrect nodes reported in GraphTest.test_nodes')

    def sample_draw(self):
        self.large.draw_graph()

    def run_tests(self):
        self.test_edges()
        self.test_nodes()
        print('\nAll tests successful\n')
