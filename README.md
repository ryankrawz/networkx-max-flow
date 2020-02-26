# networkx-max-flow

`NetworkXDirectedGraph` objects can be created one of two ways. The constructor can be provided an adjacency matrix where a `1` at position `i, j` indicates an edge from node `i` to node `j` and a `0` does notL.
```
m = [
  [0, 1, 1, 0],
  [1, 1, 0, 0],
  [0, 0, 0, 1],
  [1, 0, 0, 1],
]

graph_matrix = NetworkXDirectedGraph(m)
```
The optional argument `from_edge_list` can also be set to `True`, in which case the constructor takes the file name of a NetworkX edge list.
```
graph_edge_list = NetworkXDirectedGraph('edge_list.txt', from_edge_list=True)
```
The maximum flows that implement both breadth-first search and Dijkstra's algorithm are automatically calculated for the graphs created from edge lists and can be accessed by `graph_edge_list.bfs_max_flow` and `graph_edge_list.dijkstra_max_flow`. However, these should not be calculated for matrix-based graphs as they are not properly formatted flow networks. The maximum flow can also be computed explicity as follows.
```
max_flow_bfs = graph_edge_list.max_flow(graph_edge_list.bfs)
max_flow_dijkstra = graph_edge_list.max_flow(networkx.dijkstra_path)
```
Any `NetworkXDirectedGraph` instance can be visualized through the Matplotlib interface by calling the `draw_graph` method.
```
graph_edge_list.draw_graph()
```
Lastly, the run time of the breadth-first search and Dijkstra's algorithm can be examined more closely with the `analyze_run_time` function. It's first positional argument is the top of the range of flow network sizes to test. For example, when this argument is equal to `10`, graphs with 2 nodes all the way up to 10 nodes will be tested. The second positional argument is the bucket size for averaging the run time on each graph. A bucket size of `5` would cause `analyze_run_time` to run the algorithms on each graph 5 times and average the run time. This function outputs a CSV file containing the average run times of both breadth-first search and Dijkstra's algorithm for each flow network size tested.
