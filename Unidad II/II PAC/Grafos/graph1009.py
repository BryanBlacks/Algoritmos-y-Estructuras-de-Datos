#-*- coding: utf-8 -*-
"""
    Todo árbol es un grafo pero no todo grafo es un árbol

    El grafo se compone de:
    Nodos = vertices, vertex
    Arcos = aristas, edge

    Correspondencia donde el primero es por orden alfabetico
    El vertice A tiene aristas con: B y C
    El vertice B tiene aristas con: C y D
    El vertice C no tiene aristas
    El vertice D no tiene aristas
    C Es una ruta final 
    D Es una ruta final 
    
    Al tener dirección este grafo tiene restricciones
    Cada vertice será indice y cada elemento será un elemento en un arreglo
    de vertices como el valor de dicho indice

    Grafo Dirigido:
    Diccionario equivale a Json en un grafo Dirigido
    Una caracteristica de los grafos dirigidos, es posible producir ciclos(loops)
    pero también existen salidas naturales del grafo
"""
graphDir = {
    "A": ["B", "C"],
    "B": ["C", "D"],
    "C": ["E"],
    "D": [],
    "E": ["A"]
}
print(graphDir)

"""
    Grafo sin Dirección:
    Una de las caracteristicas de los grafos no dirigidos es que se debe establecer 
    un vertice de inicio y un vertice de fin.
    El objetivo de los grafos es buscar conexiones(rutas) entre los vertices, el 
    proposito de esas conexiones es conocer la ruta más corta.

    Las aristas que conectan vertices pueden tener un peso. El peso es una ponderación
    entre multiples caracteristicas (Definidas para el escenario especifico del grafo)
    Ej: Carreteras, Routers, Satelites etc.
"""
graph = {
    "A": ["B", "C", "E"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "E"],
    "D": ["B"],
    "E": ["A", "C"]
}
print(graph)