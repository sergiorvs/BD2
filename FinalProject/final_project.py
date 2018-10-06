from shutil import copyfile
"""
    para copiar archivos se usa esa libreria con el comando
    copyfile(fuente_origen, fuente_destino)
"""

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

def borrar(nombre, condicion):
    ruta = 'BD/' + nombre + '.dbf'
    archivo = open(ruta, 'r+')
    lineas = archivo.readlines()

    aux = 0
    aux2 = 0
    cabecera = lineas[aux]    
    while cabecera != '------\n':
        datos = cabecera.split()
        aux2 += 1
        if datos[0] == condicion[0]:
            aux = aux2-1
        cabecera = lineas[aux2]
    
    archivo.seek(0)
    contLinea = 0
    flag = True
    for linea in lineas:
        if contLinea <= aux2:
            archivo.write(linea)
            contLinea += 1
        else:
            arrLinea = linea.split()
            if condicion[1] == '=':
                if arrLinea[aux] != condicion[2]:
                    archivo.write(linea)
                else: 
                    flag = False
    archivo.truncate()
    archivo.close()
    if flag:
        print("no existe la fila")
    
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

def update(nombre, actualizacion, condicion):
    ruta = 'BD/' + nombre + '.dbf'
    archivo = open(ruta, 'r+')
    lineas = archivo.readlines()

    auxc = 0
    auxa = 0
    aux2 = 0
    cabecera = lineas[auxc]    
    while cabecera != '------\n':
        datos = cabecera.split()
        aux2 += 1
        if datos[0] == condicion[0]:
            auxc = aux2-1
        if datos[0] == actualizacion[0]:
            auxa = aux2-1
        cabecera = lineas[aux2]
    
    print("AUXA: ", auxa)
    print("AUXC: ", auxc)

    archivo.seek(0)
    contLinea = 0
    for linea in lineas:
        if contLinea <= aux2:
            archivo.write(linea)
            contLinea += 1
        else:
            arrLinea = linea.split()
            if condicion[1] == '=':
                if arrLinea[auxc] != condicion[2]:
                    archivo.write(linea)
                else:
                    arrLinea[auxa] = actualizacion[1]
                    nLinea = ' '.join(arrLinea)
                    archivo.write(nLinea + '\n')
            elif condicion[1] == '!=':
                if arrLinea[auxc] == condicion[2]:
                    archivo.write(linea)
                else:
                    arrLinea[auxa] = actualizacion[1]
                    nLinea = ' '.join(arrLinea)
                    archivo.write(nLinea + '\n')
            elif condicion[1] == '<':
                if arrLinea[auxc] >= condicion[2]:
                    archivo.write(linea)
                else:
                    arrLinea[auxa] = actualizacion[1]
                    nLinea = ' '.join(arrLinea)
                    archivo.write(nLinea + '\n')
            elif condicion[1] == '>':
                if arrLinea[auxc] <= condicion[2]:
                    archivo.write(linea)
                else:
                    arrLinea[auxa] = actualizacion[1]
                    nLinea = ' '.join(arrLinea)
                    archivo.write(nLinea + '\n')
            elif condicion[1] == '<=':
                if arrLinea[auxc] > condicion[2]:
                    archivo.write(linea)
                else:
                    arrLinea[auxa] = actualizacion[1]
                    nLinea = ' '.join(arrLinea)
                    archivo.write(nLinea + '\n')
            elif condicion[1] == '>=':
                if arrLinea[auxc] < condicion[2]:
                    archivo.write(linea)
                else:
                    arrLinea[auxa] = actualizacion[1]
                    nLinea = ' '.join(arrLinea)
                    archivo.write(nLinea + '\n')
                    
    archivo.truncate()
    archivo.close()


while(1):
    comando = input()
    comando = comando.split()
    size = len(comando)
    comando[size-1] = comando[size-1].replace(';', '')    
    # create table [nombre] (columna tipo);
    if comando[0] == 'create' and comando[1] == 'table':
        nombreTabla = comando[2]
        cols = []
        comando[3] = comando[3][1:] #borra ( 
        for i in range(3, size):
            if comando[i][len(comando[i])-1].find(',') >= 0 or comando[i][len(comando[i])-1].find(')') >= 0:
                comando[i] = comando[i][:-1]
                cols[len(cols)-1] = cols[len(cols)-1] + ' ' + comando[i]
            else:
                cols.append(comando[i])
        tablaNueva(nombreTabla, cols)

    # insert [tabla] ([..elementos..]);
    elif comando[0] == 'insert':
        nombreTabla = comando[1]
        elms = []
        comando[2] = comando[2][1:]
        for i in range(2, size):
                elms.append(comando[i][:-1])
        insertar(nombreTabla, elms)

    # delete [tabla] where [condicion]
    elif comando[0] == 'delete': #considerar que la condicion va separada por ' '
        nombreTabla = comando[1]
        cndn = []
        for i in range(3, size):
            cndn.append(comando[i])
        borrar(nombreTabla, cndn)
    
    # select [tabla] where [condicion]
    elif comando[0] == 'select': #considerar que la condicion va separada por ' '
        nombreTabla = comando[1]
        cndn = []
        for i in range(3, size):
            cndn.append(comando[i])
        select(nombreTabla, cndn)
    
    # update [tabla] set [a_actualizar] where [condicion]
    elif comando[0] == 'update':
        nombreTabla = comando[1]
        cndn = []
        actu = []
        actu.append(comando[3])
        actu.append(comando[5])
        for i in range(7, size):
            cndn.append(comando[i])
        print("lo que se acualizara es: ", actu)
        print("la condicon es: ", cndn)
        update(nombreTabla, actu, cndn)

    else:
        print("comando no encontrado, pruebe otra vez")


        

    print("el comando es ", comando)
