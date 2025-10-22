class Graph_ES:
    def __init__(self, V = None, E = None):
       self.Vs = set()
       self.Es = set()

       if V is not None:
            for v in V:
                self.add_vertex(v)
       if E is not None:
           for e in E:
               self.add_edge(e)
                       
 

    def add_vertex(self, v):
        self.Vs.add(v)

    def remove_vertex(self, v):
        self.Vs.remove(v)

    def add_edge(self, e):
        self.Es.add(e)

    def remove_edge(self,e):
        self.Es.add(e)

    def neighbors(self, v):
        nb = set()
        for e in self.Es:
            if e[0]==v:
                nb.add(e[1])
        return nb
    
    def __iter__(self):
        return iter(self.Vs)
    
    def __len__(self):
        return len(self.Vs)    


class Graph_AS:
    def __init__(self, V = None, E= None):
       self.Vs = set()
       self.nb = dict()
       
       if V is not None:
        for v in V: self.add_vertex(v)

        if E is not None:
            for e in E: self.add_edge(e)


    def add_vertex(self, v):
        self.Vs.add(v)
        if v not in self.nb:
            self.nb[v] = set()

    def remove_vertex(self, v):
        
        if v not in self.Vs:
            raise Exception(f"{v} not in graph")
        self.Vs.remove(v)
        self.nb.pop(v, None)
        
    def add_edge(self, e):
        u, v = e #e is tuple, tuple unpacking
        
        if u not in self.nb:
            self.nb[u] = {v}
        else:
            self.nb[u].add(v)

    def remove_edge(self,e):
        u, v = e #e is tuple, tuple unpacking
        
        self.nb[u].remove(v)

        if len(self.nb) == 0:
            self.nb.pop(u)


    def neighbors(self, v):
        return iter(self.nb[v])

    
    def __iter__(self):
        return iter(self.Vs)
    
    def __len__(self):
        return len(self.Vs) 
    


    


    
if __name__ == '__main__':
    g = Graph_ES()

    vs = {1,2,3,4}
    es = {(1,2),(1,3),(1,4),
          (2,1),(2,3),
          (3,1),(3,4),(3,2),
          (4,1),(4,3) }
    
    for v in vs:
        g.add_vertex(v)
    for e in es:
        g.add_edge(e)

 
    print(dir(tuple))
  
