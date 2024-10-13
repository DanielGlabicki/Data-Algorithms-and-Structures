# Skończone
from Zad9_0 import AdjList, Vertex, printGraph, MST_prim
from graf_mst import graf


def main():
    
    graphList = AdjList()
    for i in graf:
        graphList.insert_edge(Vertex(i[0]), Vertex(i[1]), i[2])
        graphList.insert_edge(Vertex(i[1]), Vertex(i[0]), i[2])
    
    
    graphMST, height = MST_prim(graphList, Vertex("A"))
    
    printGraph(graphMST)
    
    return 0

main()
