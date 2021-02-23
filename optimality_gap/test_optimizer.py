import networkx as nx
import random
from typing import Callable, List
from optimality_gap.subgraph_optimizer import optimize_subgraph_connectivity

def create_test_graph(n: int, seed: int) -> nx.Graph:
    internet: nx.Graph = nx.random_internet_as_graph(n, seed=seed)
    node_types: List[str] = ['source', 'destination']

    for i in range(n):
        internet.add_node(i, type=random.choice(node_types))

    return internet

def utility_function(G): return nx.wiener_index(G)


def test_utility():
    test_graph: nx.Graph = create_test_graph(50, 42)
    test_nodes = set(test_graph.nodes)
    result: tuple = optimize_subgraph_connectivity(graph=test_graph,
                                                   nodes=test_nodes,
                                                   utility_function=utility_function)
    print(f"Best subgraph: {result[0]}")
    print(f"Best score: {result[1]}")


if __name__ == '__main__':
    test_utility()

# def optimize_subgraph_connectivity(graph: nx.Graph,
                                   # nodes: set,
                                   # utility_function: Callable[[nx.Graph], float],
                                   # n_iter: int = 50,
                                   # **kwargs) -> Tuple[nx.Graph, float]:

