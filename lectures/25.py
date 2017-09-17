from graphviz import Digraph, Graph

dot = Digraph(comment = "The Round Table")
# Digraph: directed graph. dot variable has an instance which is generated from Digraph class
dot.node('A', 'King Arthur')
dot.node('B', 'Sir Dedevere the wise')
dot.node('L', 'Sir Lancelot the Brave')
dot.edges(["AB", "AL"]) # edges' list. A -> B, A -> L because Digraph is directed graph.
dot.edge("B", "L", constraint = 'False')

dot.render('test_output/round_table.gv.pdf', view = True)
