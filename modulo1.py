__counter = 0
def lista(lista1, lista2):
    result = lista1 + lista2
    return result
lista1 = [5, 8, 10]
lista2 = [6, 3, 8]
print('numeros de las lista',lista(lista1,lista2)) 


def suma_elementos(lista):
    resultado = 0
    for i in lista:
        resultado += i
    return resultado

def promedio_elementos(lista):
    return suma_elementos(lista) / len(lista)

mi_lista = [1, 21, 11, 34, 89]
print("La suma de los elementos de la lista es:", suma_elementos(mi_lista))
print("El promedio de los elementos de la lista es:", promedio_elementos(mi_lista))

def valores (valor):
    if valor> 0:
        result = "positivo"
    else:
        result = "no positivo"

    if valor > 0:
        sign = "positivo"
    elif valor == 0:
        sign = "cero"
    else:
        sign = "negativo"
        
    return result, sign
valor = 0       
print(valores(valor))

#Modularizar la lógica de una fecha válida
def fecha_valida(dia, mes, ano):
    if ano % 4 == 0:
        bisiesto = True
    else:
        bisiesto = False

    if mes in [1, 3, 5, 7, 8, 10, 12]:
        mes_valido = True
    elif mes == 2:
        if bisiesto:
            if dia >= 1 and dia <= 29:
                mes_valido = True
            else:
                mes_valido = False
        else:
            if dia >= 1 and dia <= 28:
                mes_valido = True
            else:
                mes_valido = False
    else:
        if dia >= 1 and dia <= 31:
            mes_valido = True
        else:
            mes_valido = False

    return mes_valido

dia = 29
mes = 2
ano = 2022
if fecha_valida(dia, mes, ano):
    print("La fecha es válida")
else:
    print("La fecha no es válida")


# Modularización de una tarea compleja con listas
def promedio_notas(notas):
    suma = 0
    for nota in notas:
        suma += nota
    return suma / len(notas)

def aprobar_materia(notas, promedio_minimo=60):
    promedio = promedio_notas(notas)
    if promedio >= promedio_minimo:
        return True
    else:
        return False

notas = [10, 80, 90, 50]
if aprobar_materia(notas):
    print("Aprobó la materia")
else:
    print("No aprobó la materia")



if __name__ == "__main__":
    print("Yo prefiero ser un módulo")
else:
    print("Me gusta ser un módulo")





