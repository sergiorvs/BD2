from AVL import *

from shutil import copyfile
from random import randint, uniform,random

import linecache
import resource
import sys
import time

#sys.setrecursionlimit(100000)


def tablaNueva(nombre, columnas):
    ruta = 'BD/' + nombre + '.dbf'
    archivo = open(ruta, 'w')
    for cols in columnas:
        archivo.write(cols + '\n')
    archivo.write('------\n')
    archivo.close()
    print('tabla creada correctamente!')

def insertar(nombre, elementos):
    ruta = 'BD/' + nombre + '.dbf'
    archivo = open(ruta, 'a')
    for elemento in elementos:
        archivo.write(elemento + ' ')
    archivo.write('\n')
    archivo.close()
    # print("insertado!")

def insert_n(nombre, elementos, n):
    for i in range(1, n+1):
        elementos[0] = str(i)
        elementos[1] = "'nombre_" + str(i) + "'"
        elementos[2] = str(randint(0,100)) 
        insertar(nombre, elementos)  

def select(nombre, condicion):
    ruta = 'BD/' + nombre + '.dbf'
    archivo = open(ruta, 'r')
    lineas = archivo.readlines()

    aux = 0
    aux2 = 0
    cabecera = lineas[aux] 
    guia = ''   
    while cabecera != '------\n':
        datos = cabecera.split()
        aux2 += 1
        if datos[0] == condicion[0]:
            aux = aux2-1
        cabecera = lineas[aux2]

        guia += datos[0] + '|'
    
    print(guia)

    contLinea = 0
    for linea in lineas:
        if contLinea <= aux2:
            archivo.readline()
            contLinea += 1
        else:
            arrLinea = linea.split()
            if condicion[1] == '=':
                if arrLinea[aux] == condicion[2]:
                    print(linea[:-1])
            elif condicion[1] == '!=':
                if arrLinea[aux] != condicion[2]:
                    print(linea[:-1])
            elif condicion[1] == '<':
                if arrLinea[aux] < condicion[2]:
                    print(linea[:-1])
            elif condicion[1] == '>':
                if arrLinea[aux] > condicion[2]:
                    print(linea[:-1])
            elif condicion[1] == '<=':
                if arrLinea[aux] <= condicion[2]:
                    print(linea[:-1])
            elif condicion[1] == '>=':
                if arrLinea[aux] >= condicion[2]:
                    print(linea[:-1])
            
    archivo.close()

#create_idx [index_name] on [table_name] (parametro)
#create_idx idx_edad on estudiantes edad
#create_idx idx_id on estudiantes id
def create_index(index_name, table_name, param):
    table = 'BD/' + table_name + '.dbf'
    archivo = open(table, 'r')
    lineas = archivo.readlines()
    t = AVL()
    aux = 0
    aux2 = 0
    cabecera = lineas[aux] 
    flag = 0
    while cabecera != '------\n':
        datos = cabecera.split()
        aux2 += 1
        if datos[0] == param:
            aux = aux2-1
        if datos[1] == 'int':
            flag = 1
        else:
            flag = 0
        cabecera = lineas[aux2]
    contLinea = 0
    for linea in lineas:
        if contLinea <= aux2:
            archivo.readline()
        else:
            arrLinea = linea.split()
            if flag == 1:
                t.insert(int(arrLinea[aux]), contLinea + 1)
            else:
                t.insert(arrLinea[aux], contLinea + 1)
            # print("elemento insertado", arrLinea[aux])
            # print("the lines is: ",contLinea)
        contLinea += 1
    print("arbol creado!")
    # t.preShow(t.root)
    sys.setrecursionlimit(50000)
    afile = open(index_name + '.pkl', 'wb')
    pickle.dump(t, afile)
    afile.close()
    print("\n")

def selectWithIndex(index_name, table_name, condicion):
    afile = open(index_name+'.pkl', 'rb')
    t = pickle.load(afile)
    afile.close()
    table = 'BD/' + table_name + '.dbf'
    node = t.find(int(condicion))
    pointers = node.pointer
    for i in pointers:
        print(linecache.getline(table, i)[:-1])



if __name__ == '__main__':

    print("COMANDOS:")
    print("create table [nombre] (columna tipo)")
    print("for_insert [n] [nombre_tabla] [condicion]")
    print("insert [tabla] ([..elementos..])")
    print("create_idx [index_name] on [table_name] (parametro)")
    print("select_idx [index_name] [table_name] where [param]")
    print("select [tabla] where [condicion]")


    # elementos = []
    # elementos.append('0')
    # elementos.append('nombre_x')
    # elementos.append('0')
    # insert_n('estudiantes', elementos, 500)
    while(1):
        comando = input()
        comando = comando.split()
        size = len(comando)
        comando[size-1] = comando[size-1].replace(';', '')
        # create table [nombre] (columna tipo);
        if comando[0] == 'create' and comando[1] == 'table':
            nombreTabla = comando[2]
            cols = []
            comando[3] = comando[3][1:]  # borra (
            for i in range(3, size):
                if comando[i][len(comando[i])-1].find(',') >= 0 or comando[i][len(comando[i])-1].find(')') >= 0:
                    comando[i] = comando[i][:-1]
                    cols[len(cols)-1] = cols[len(cols)-1] + ' ' + comando[i]
                else:
                    cols.append(comando[i])
            tablaNueva(nombreTabla, cols)
        # for_insert [n] [nombre_tabla] [condicion]
        # for_insert 100 estudiantes (id, nombre, edad) 
        elif comando[0] == 'for_insert':
            n = int(comando[1])
            nombre = comando[2]
            elms = []
            comando[2] = comando[2][1:]
            for i in range(3, size):
                    elms.append(comando[i][:-1])
            insert_n(nombre, elms, n)
            print("insertado!")
        
        # insert [tabla] ([..elementos..]);
        elif comando[0] == 'insert':
            nombreTabla = comando[1]
            elms = []
            comando[2] = comando[2][1:]
            for i in range(2, size):
                    elms.append(comando[i][:-1])
            insertar(nombreTabla, elms)
        
        #create_idx [index_name] on [table_name] (parametro)
        elif comando[0] == 'create_idx':
            print("entro!!")
            index_name = comando[1]
            table_name = comando[3]
            param = comando[4]
            start = time.time()
            create_index(index_name, table_name, param)
            end = time.time()
            print("indice creado correctamente!")
            print("execution time: ", end - start)
        
        # select [tabla] where [condicion]
        elif comando[0] == 'select': #considerar que la condicion va separada por ' '
            nombreTabla = comando[1]
            cndn = []
            for i in range(3, size):
                cndn.append(comando[i])
            start = time.time()
            select(nombreTabla, cndn)
            end = time.time()
            print("execution time: ", end - start)

        #select_idx [index_name] [table_name] where [param]
        elif comando[0] == 'select_idx':
            index_name = comando[1]
            table_name = comando[2]
            cndn = comando[4]
            # cndn = []
            # for i in range(4, size):
            #     cndn.append(comando[i])
            start = time.time()
            selectWithIndex(index_name, table_name, cndn)
            end = time.time()
            print("execution time: ", end - start)

