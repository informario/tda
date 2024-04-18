'''Implementar un algoritmo que reciba un grafo y determine si el mismo es un grafo bipartito, o no. Es decir, la función es_bipartito debe devolver True si el grafo recibido por parámetro es efectivamente bipartito, False en caso contrario. Que un grafo sea Bipartito implica que puede separarse los vértices en dos grupos S y T, tal que para cada par de vértices de S no exista arista entre sí (lo mismo para T), que la intersección entre S y T sea vacía y que la unión sea igual al conjunto de todos los vértices del grafo.

A fines del ejercicio, considerar que se pueden ver todos los vértices del grafo en un orden aleatorio con for v in grafo, y el grafo cuenta con la primitivas hay_arista(origen, destino) (devuelve bool), adyacentes(vertice) que devuelve una lista de vértices adyacentes al indicado, y vertices() que nos devuelve todos los vértices (lista).

El grafo internamente se encuentra implementado con listas de adyacencia (en su versión de diccionario de diccionarios), a considerar para la complejidad.'''

import sys
# Para el caso de querer implementar un DFS, 
# para que no hayan problemas en la prueba de volumen
sys.setrecursionlimit(10000)

def es_bipartito(grafo):
    color_dict = {}
    color = 0
    l_vertices = grafo.vertices()
    if (len(l_vertices)==0):
        return True
    
    for v in grafo:
        if(color_dict.get(v) == None):
            color_dict[v] = color
            resultado = colorear_adyacentes(grafo, v, (1 - color), color_dict)
            if (resultado==False):
                return resultado
    return True


def colorear_adyacentes(grafo, v, color, color_dict):
    adyacentes = grafo.adyacentes(v)
    for v in adyacentes:
        if (color_dict.get(v) == (1 - color)):
            return False
        elif(color_dict.get(v) == None):
            color_dict[v] = color
            resultado = colorear_adyacentes(grafo, v, (1 - color), color_dict)
            if (resultado==False):
                return resultado
    return True
