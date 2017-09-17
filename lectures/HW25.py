from graphviz import Digraph

engines = ['dot', 'neato', 'fdp', 'twopi', 'circo'] # sfdp does not work in my laptop
for engine in engines:

    dot = Digraph(comment = "HW25", engine = engine)
    dot.attr('node', size = '7.5', color = 'green') # goldenrod2 is not a known color
    dot.node('A', "7th edition")
    dot.node('B', "32V")
    dot.node('C', "V7M")
    dot.node('D', "Xenixn")
    dot.node('E', "UniPlus+")
    dot.edges(["AB","AC","AD","AE"])

    dot.node("F", "8th edition")
    dot.node("G", "9th edition")
    dot.edges(["FG"])

    dot.node("H", "1 BSD")
    dot.node("I", "2 BSD")
    dot.edges(["HI"])

    dot.node("J", "2.8 BSD")
    dot.edges(["IJ"])

    dot.node("K", "Ultrix-11")
    dot.node("L", "2.9 BSD")
    dot.edges(["JK", "JL"])


    dot.node("M", "3 BSD")
    dot.edges(["BM"])

    dot.node("N", "4 BSD")
    dot.edges(["MN"])

    dot.node("O", "4.1 BSD")
    dot.edges(["NO"])

    dot.node("P", "4.2 BSD")
    dot.edges(["OP", "OJ", "OF"])


    dot.node("Q", "4.3 BSD")
    dot.node("R", "Ultrix-32")
    dot.edges(["PQ", "PR"])

    dot.render('HW25/{}.gv.pdf'.format(engine))