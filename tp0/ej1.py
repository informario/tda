'''
La Escuela Nacional 32 "Alan Turing" de Bragado tiene una forma particular de requerir que los alumnos formen fila. En vez del clásico "de menor a mayor altura", lo hacen primero con alumnos yendo con altura decreciente, hasta llegado un punto que empieza a ir de forma creciente, hasta terminar con todos los alumnos.

Por ejemplo las alturas podrían ser 1.2, 1.15, 1.14, 1.12, 1.02, 0.98, 1.18, 1.23.

    Implementar una función indice_mas_bajo que dado un arreglo/lista de alumnos(*) que represente dicha fila, devuelva el índice del alumno más bajo, en tiempo logarítmico. Se puede asumir que hay al menos 3 alumnos. En el ejemplo, el alumno más bajo es aquel con altura 0.98.

    Implementar una función validar_mas_bajo que dado un arreglo/lista de alumnos(*) y un índice, valide (devuelva True o False) si dicho índice corresponde al del alumno más bajo de la fila. (Aclaración: esto debería poder realizarse en tiempo constante)

(*)
Los alumnos son de la forma:

alumno {
    nombre (string)
    altura (float)
}

Se puede acceder a la altura de un alumno haciendo varible_tipo_alumno.altura.

Importante: considerar que si la prueba de volumen no pasa, es probable que sea porque no están cumpliendo con la complejidad requerida. 
'''
def indice_mas_bajo(alumnos):
    cant = len(alumnos)
    izq = 0
    der = cant-1
    piv = cant//2
    while der - izq > 1:
        if alumnos[piv].altura < alumnos[piv+1].altura:
            der = piv
            piv = (izq+der)//2
        elif alumnos[piv].altura < alumnos[piv-1].altura:
            izq = piv
            piv = (izq+der)//2

    if der - izq == 1:
        if alumnos[der].altura < alumnos[izq].altura:
            return der
        else:
            return izq
    elif der == izq:
        return der


def validar_mas_bajo(alumnos, indice):
    if len(alumnos) == 1:
        return True
    elif len(alumnos) == 2:
        return alumnos[indice].altura < alumnos[not indice].altura
    else:
        return alumnos[indice].altura < alumnos[indice+1].altura and alumnos[indice].altura < alumnos[indice-1].altura

