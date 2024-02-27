class Graph:

    def __init__(self, graph_dict=None):
        """ initializes a graph object 
            If no dictionary or None is given, 
            an empty dictionary will be used
        """
        if graph_dict == None:
            graph_dict = {}
        self._graph_dict = graph_dict

    def edges(self, vertice):
        """ returns a list of all the edges of a vertice"""
        return [i for i in self._graph_dict[vertice]]

    def __generate_edges(self):
        """ A static method generating the edges of the 
            graph "graph". Edges are represented as sets 
            with one (a loop back to the vertex) or two 
            vertices 
        """
        edges = []
        for vertex in self._graph_dict:
            for neighbour in self._graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges
    
    def find_all_paths(self, start_vertex, end_vertex, path=[], sums=0):
        """ find all paths from start_vertex to 
            end_vertex in graph """
        graph = self._graph_dict 
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return path, sums
        if start_vertex not in graph:
            return []
        paths = []
        for vertex in graph[start_vertex]:
            if vertex[0] not in path:
                extended_paths = self.find_all_paths(vertex[0], 
                                                     end_vertex, 
                                                     path, sums + vertex[1])
                for p in extended_paths: 
                    paths.append(p)
                self.sums = 0
        return paths
    
    def total_mins(self, paths):
        records = {}
        for i in range(len(paths)):
            if type(paths[i]) == list:
                records[len(records)] = [paths[i],paths[i+1]]
        return records
    
    def fastest_way(self, aisles, total_min):
        table = [[0 for i in range(len(total_min))] for i in range(len(aisles))]            
        for i in range(len(aisles)):
          for j in range(len(total_min)):
            if aisles[i] in total_min[j][0]:
              table[i][j] += total_min[j][1]
        
        minimum_routes = []
        print(table)
        for i in table:
          smallest_time = min(num for num in i if num > 0)
          s = i.index(smallest_time)
          minimum_routes.append(s)

        return minimum_routes  
            
              
g = { "START" : [(1,0.1)],
        1 : [(3,0.2),(2,0.5),(6,1.5)],
        2 : [(1, 0.5), (5, 3.5), ("DROP OFF", 0.1)],
      3 :[[1, 0.2], (4, 1)],
      4 : [(3,1),(5, 0.5)],
      5 : [(2, 3.5),(6, 0.3)],
      6 : [(1, 1.5),(5,0.3)],
      "DROP OFF":[]
    }

aisles = [1, 2, 3, 4, 6]
graph = Graph(g)
path = graph.find_all_paths('START', 'DROP OFF')
dicxts = graph.total_mins(path)
print(dicxts)
print(graph.fastest_way(aisles, dicxts))

