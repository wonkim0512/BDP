
from graphviz import Graph



g = Graph(name='G', engine = 'sfdp')
g.edge('a', 'b')
g.edge('2','3')
g.edge('3','4')
g.edge('4','5')
g.edge('5','6')
g.edge('5','7')
g.edge('5','8')
g.edge('7','9')
g.edge('9','10')
g.edge('10','11')
g.edge('10','12')
print(g)
g.view()
