class Node:
    def __init__(self, value):
        self.value = value
        self.edges = []

class Edge:
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to

class Graph:
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    def insert_node(self, new_node_val):
        node = Node(new_node_val)
        self.nodes.append(node)
        
    def insert_edge(self, new_edge_val, node_from_val, node_to_val):
        from_node = self.linear_search(self.nodes, node_from_val)
        to_node = self.linear_search(self.nodes, node_to_val)

        if not to_node:
            to_node = Node(node_to_val)
            self.nodes.append(to_node)
        if not from_node:
            from_node = Node(node_from_val)
            self.nodes.append(from_node)
        
        new_edge = Edge(new_edge_val, node_from_val, node_to_val)
        self.edges.append(new_edge)
        from_node.edges.append(new_edge)
        to_node.edges.append(new_edge)
    
    def linear_search(self, items_lst, find_val):
        """ Linear search algorithm.
        """
        for item in items_lst:
            if item.value == find_val:
                return item
        return None

    def get_edge_list(self):
        """Don't return a list of edge objects!
        Return a list of triples that looks like this:
        (Edge Value, From Node Value, To Node Value)"""
        edge_lst = []
        for edge in self.edges:
            edge_lst.append(tuple((edge.value, edge.node_from, edge.node_to)))
        return edge_lst

    def get_adjacency_list(self):
        """Don't return any Node or Edge objects!
        You'll return a list of lists.
        The indecies of the outer list represent
        "from" nodes.
        Each section in the list will store a list
        of tuples that looks like this:
        (To Node, Edge Value)"""
        max_node_value = self.find_max_node_value()
        outer_lst = [None,] * (max_node_value + 1)
        for edge in self.edges:
            if not outer_lst[edge.node_from]:
                outer_lst[edge.node_from] = []
            outer_lst[edge.node_from].append((edge.node_to, edge.value))
        return outer_lst
    
    def find_max_node_value(self):
        # there is a possibility for a node to have value = 0
        max_node = -1
        if len(self.nodes):
            for node in self.nodes:
                if node.value > max_node:
                    max_node = node.value
        return max_node

    def get_adjacency_matrix(self):
        """Return a matrix, or 2D list.
        Row numbers represent from nodes,
        column numbers represent to nodes.
        Store the edge values in each spot,
        and a 0 if no edge exists."""
        max_node_value = self.find_max_node_value()
        list_2D = [[0 for i in range(max_node_value + 1)] for j in range(max_node_value + 1)]
        for edge in self.edges:
            list_2D[edge.node_from][edge.node_to] = edge.value
        return list_2D

if __name__ == "__main__":
    graph = Graph()
    graph.insert_edge(100, 1, 2)
    graph.insert_edge(101, 1, 3)
    graph.insert_edge(102, 1, 4)
    graph.insert_edge(103, 3, 4)
    # Should be [(100, 1, 2), (101, 1, 3), (102, 1, 4), (103, 3, 4)]
    print(graph.get_edge_list())
    # Should be [None, [(2, 100), (3, 101), (4, 102)], None, [(4, 103)], None]
    print(graph.get_adjacency_list())
    # Should be [[0, 0, 0, 0, 0], [0, 0, 100, 101, 102], [0, 0, 0, 0, 0], [0, 0, 0, 0, 103], [0, 0, 0, 0, 0]]
    print(graph.get_adjacency_matrix())