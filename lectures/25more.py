from graphviz import Digraph
from graphviz import Graph

g = Graph(name='G', engine = 'fdp') # sfdp is not called.
g.attr('node', shape = 'box')
g.node('e')

with g.subgraph(name = 'ClusterA') as a:
    a.edge('a', 'b')
    with a.subgraph(name = 'ClusterC') as c:
        c.edge('C', 'D')

with g.subgraph(name = "ClusterB") as b:
    b.edge('d', 'f')

g.edge('e', 'ClusterB')
g.edge('d', 'D')
g.edge('ClusterC', 'ClusterB')

g.render(view = True)
