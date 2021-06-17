"""
Nombre: invertirLista
Entradas: Una lista(lista)
Salidas: Una lista con sus valores invertidos.
Restrecciones: La entrada debe ser una lista.
"""
def invertirLista(lista):
    if isinstance(lista, list):
        if lista == []:
            return 0
        else:
            return invertirLista_Aux(lista,[])
    else:
        print ("Error: Porfavor ingrese una lista")
    
def invertirLista_aux(lista, listaInvertida):
    if lista == []:
        return listaInvertida
    else:
        return invertirLista_Aux(lista[:-1],listaInvertida + [lista[-1]])

#===========================================================================
"""
Nombre: extremos listas
Entradas: Una lista(lista)
Salidas: El numero mayor y el numero menor de la lista.
Restricciones: La entrada debe ser una lista.
"""
def extremosLista(lista) :
    if lista == [] :
        return 0
    else :
        if isinstance(lista, list) :
            mayor = numero_mayor(lista, lista[0])
            menor = numero_menor(lista, lista[0])
            if mayor == menor :
                return print([mayor])
            else :
                return print([menor, mayor])
        else :
            print('Error: la entrada no es una lista')

def numero_mayor(lista, numero) :
    if lista == [] :
        return numero
    elif numero >= lista[0] :
        return numero_mayor(lista[1:], numero)
    else :
        return numero_mayor(lista[1:], lista[0])

def numero_menor(lista, numero) :
    if lista == [] :
        return numero
    elif numero <= lista[0] :
        return numero_menor(lista[1:], numero)
    else :
        return numero_menor(lista[1:], lista[0])

#===========================================================================
"""
Nombre: eliminarDigito
Entradas: Dos entradas, num que es el numero al que se le borra los digitos, borrarNumero que es el numero que se debe eliminar.
Salidas: Devolver num sin los numeros introducidos en borrarNumero.
Restricciones: Tanto num como borrarNumero deben ser enteros.
"""
def eliminarDigito(num, borrarNumero) :
    if isinstance(num, int) and isinstance(borrarNumero, int) :
        if num == 0 :
            print('Error: debe introducir un digito que no sea cero')
        else :
            cantidadCaracteres = cuentaDigitos(borrarNumero, 0)
            return eliminarDigitoAux(str(num), str(borrarNumero), cantidadCaracteres, '')
    else :
        print('Error: las entradas Num y el borrarNumero deben ser enteros')

def cuentaDigitos(numero, cantidad) :
    if numero == 0 :
        return cantidad
    else :
        return cuentaDigitos(numero // 10, cantidad + 1)

def eliminarDigitoAux(num, borrarNumero, cantidad, nuevoNumero) :
    if num == '' :
        if nuevoNumero == '' :
            return 0
        else :
            return print(nuevoNumero)
    elif num[0:cantidad] == borrarNumero :
        return eliminarDigitoAux(num[cantidad:], borrarNumero, cantidad, nuevoNumero)
    else :
        return eliminarDigitoAux(num[1:], borrarNumero, cantidad, nuevoNumero + num[0])

#===========================================================================
def eliminarDigito_V2(num, borrarNumero) :
    if isinstance(num, int) and isinstance(borrarNumero, int) :
        if num == 0 :
            print('Error: debe introducir un digito que no sea cero')
        else :
            cantidadCaracteres = cuentaDigitos(borrarNumero, 0)
            return eliminarDigito_AuxV2(num, borrarNumero, 0, 0, cantidadCaracteres)
    else :
        print('Error: las entradas Num y el borrarNumero deben ser enteros') 

def eliminarDigito_AuxV2(numero, borrarNumero, potencia, nuevoNumero, cantidad) :
    if numero == 0 :
        return nuevoNumero
    elif numero % 10 ** cantidad == borrarNumero :
        return eliminarDigito_AuxV2(numero // 10 ** cantidad, borrarNumero, potencia, nuevoNumero, cantidad)
    else :
        return eliminarDigito_AuxV2(numero // 10, borrarNumero, potencia + 1, nuevoNumero + ((numero % 10) * 10 ** potencia), cantidad)

def cuentaDigitos(numero, cantidad) :
    if numero == 0 :
        return cantidad
    else :
        return cuentaDigitos(numero // 10, cantidad + 1)

#===========================================================================
"""
Nombre: nivelesLista.
Entradas: Una lista con sublista(lista)
Salidas: La cantidad de sublistas que posee cada índice.
Restricciones: La entradad lista debe ser una lista.
"""
def nivelesLista(lista) :
    if isinstance(lista, list) :
        return nivelesListaAux(lista, [])
    else :
        print('Debe ingresar una sublista')

def nivelesListaAux(lista, contenidoSublistas) :
    if lista == [] :
        return contenidoSublistas
    else :
        return nivelesListaAux2(lista, lista[0], contenidoSublistas, 0)

def nivelesListaAux2(lista, sublista, contenidoSublistas, cantidad) :
    if sublista == [] :
        return nivelesListaAux(lista[1:], contenidoSublistas + [cantidad + 1])
    elif isinstance(sublista, list) :
        if (not(isinstance(sublista[0], list))) :
            return nivelesListaAux2(lista, sublista[1:], contenidoSublistas, cantidad)
        else :
            return nivelesListaAux2(lista, sublista[0] + sublista[1:], contenidoSublistas, cantidad + 1)
    else:
        return nivelesListaAux2(lista, sublista[1:], contenidoSublistas, cantidad)

#===========================================================================
"""
Nombre: obtenerIndicesListaVectore
Entradas: Cualquier cantidad de vectores.
Salidas: Los índices en que se encuentran los ceros y los numeros negativos de cada vector.
Restricciones: Solo pueden introducirse vectores del mismo tamaño.
"""
def obtenerIndicesListaVectore(vectores) :
    if isinstance(vectores, list) :
        if comprobarEnteros(vectores) :
            if tamanoVectores(vectores, []) :
                return identificarCerosYNegativos(vectores,[])
            else :
                print('Los vectores deben de ser del mismo tamaño')
        else :
            print('Los elementos de los vectores deben ser enteros')
    else :
        print('Error: Los vectores deben estar en una lista.')

def identificarCerosYNegativos(lista, sumIndices) :
    if lista == [] :
        return sumIndices
    else :
        return identificarCerosYNegativosAux(lista, lista[0], sumIndices, 0, [])

def identificarCerosYNegativosAux(lista, sublista, sumIndices, indice, sumIndicesAux) :
    if sublista == [] :
        return identificarCerosYNegativos(lista[1:], sumIndices + [sumIndicesAux])
    elif sublista[0] <= 0 :
        return identificarCerosYNegativosAux(lista, sublista[1:], sumIndices, indice + 1, sumIndicesAux + [indice])
    else :
        return identificarCerosYNegativosAux(lista, sublista[1:], sumIndices, indice + 1, sumIndicesAux)

def comprobarEnteros(lista) :
    if lista == [] :
        return True
    else :
        return comprobarEnterosAux(lista, lista[0])

def comprobarEnterosAux(lista, sublista) :
    if sublista == [] :
        return comprobarEnteros(lista[1:])
    elif isinstance(sublista[0], int) :
        return comprobarEnterosAux(lista, sublista[1:])
    else :
        return False

def tamanoVectores(lista, cantidad) :
    if lista == [] :
        return comprobarIgualdad(cantidad, cantidad[0])
    else :
        return tamanoVectoresAux(lista, lista[0], cantidad, 0)

def tamanoVectoresAux(lista, sublista, cantidad, suma) :
    if sublista == [] :
        return tamanoVectores(lista[1:], cantidad + [suma])
    else :
        return tamanoVectoresAux(lista, sublista[1:], cantidad, suma + 1)

def comprobarIgualdad(cantidad, igual) :
    if cantidad == [] :
        return True
    elif igual == cantidad[0] :
        return comprobarIgualdad(cantidad[1:], igual)
    else :
        return False
