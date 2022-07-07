#Reto 4
#John Haver Herrera

from posixpath import split

def crearmatriz (fil,col):
    matriz=[]
    for i in range(fil):
        lstfila=[]
        for j in range (col):
            lstfila.append(int(0))
        matriz.append(lstfila)
    return matriz

def imprimematriz (fil,col, matriz):
    for i in range (fil):
        for j in range(col):
            print(f"{matriz[i][j]}", end="\t")
        print("")
    print("")
    
def asignavalor(fil, col, matriz, valor):
    matriz[fil][col]=valor
    return matriz

def medidas(sistolica, diastolica):
    if sistolica < 91 and diastolica < 63:
        return "Si"
    elif ((sistolica >= 91  and sistolica  <  134) and (diastolica>=63  and diastolica<77  )):
        return "No"
    elif ((sistolica >= 134 and sistolica  <  162) and (diastolica>=77  and diastolica<105 )):
        return "No"
    elif ((sistolica >= 162 and sistolica  <  188) and (diastolica>=105 and diastolica<119 )):
        return "Si"
    elif ((sistolica >= 188 and sistolica  <  201) and (diastolica>=119 and diastolica<126)):
        return "Si"
    elif ((sistolica >= 201 and sistolica  <  214) and (diastolica>=126 and diastolica<146)):
        return "Si"
    elif (sistolica  >= 214 and diastolica >= 146):
        return "Si"
    elif (sistolica  >= 152 and diastolica  <  79) :
        return "Si"

def mayor(sucursal,col,imprime):
    mayor=sucursal[0]
    medmayor=0
    for i in range(col):
        if sucursal[i]>mayor:
            mayor=sucursal[i] 
            medmayor=i
    
    if imprime==True:
       print(medmayor+1," ",mayor)
    else:
        return mayor

def menor(sucursal,col,imprime):
    menor=sucursal[0]
    medmenor=0
    for i in range(col):
        if sucursal[i]<menor:
            menor=sucursal[i] 
            medmenor=i
    if imprime==True:
        print(medmenor+1," ",menor)
    else:
        return menor

def suma (sucursal,col,imprime):
    suma=0
    for i in range(col):
        suma = suma + sucursal[i]
    if imprime==True:
        print(suma)
    else:
        return suma
   
def promedio (col,sucursal,imprime):
    suma=0
    prom=0
    pacientes=sucursal[col]
    for i in range(len(sucursal)-2):
        suma = suma + sucursal[i]
    if pacientes>0:
        prom=suma/pacientes
    if imprime==True:
        print(prom)
    else:
        return prom

def mayormatriz(fil,col,sucursal,imprime):
    mayor=sucursal[0][0]
    medmayor=0
    for i in range(fil):
        for j in range(col):
            if sucursal[i][j]>mayor:
                mayor=sucursal[i][j] 
                medmayor=i 
    if imprime==True:
       print(medmayor+1," ",mayor)
    else:
        return mayor

def menormatriz(fil,col,sucursal,imprime):
    menor=sucursal[0][0]
    medmenor=0
    for i in range(fil):
        for j in range(col):
            if sucursal[i][j]>0 and sucursal[i][j]<menor:
                menor=sucursal[i][j] 
                medmenor=i 
    if imprime==True:
       print(medmenor+1," ",menor)
    else:
        return menor

def mayormenor(matriz):
    mayor=matriz[0][0]
    menor=matriz[0][0]

    for fila in matriz:
        for valor in fila:
            if valor>mayor:
                mayor=valor
                sucmayor=fila
            if valor< menor:
                menor=valor
                sucmenor=fila
    print (sucmenor," ",menor)
    print (sucmayor," ",mayor)

def menormayortipo1(matriz):
    menorTipo1=matriz[0][0]
    mayorTipo1=matriz[0][0]
    menorTipo1Suc=0
    mayorTipo1Suc=0
    for fil in range(sucursales):
        if matriz[fil][0] < menorTipo1:
            menorTipo1 = matriz[fil][0]
            menorTipo1Suc=fil
        if matriz[fil][0] > mayorTipo1:
            mayorTipo1 = matriz[fil][0]
            mayorTipo1Suc=fil
            
    print(menorTipo1Suc+1," ",menorTipo1)
    print(mayorTipo1Suc+1," ",mayorTipo1)

entrada=input()
datos=entrada.split()

sucursales=int(datos[0])
tiposMed=int(datos[1])
pacientesTot=int(datos[2])

stockInicial=crearmatriz(sucursales,tiposMed)
stockFinal=crearmatriz(sucursales,tiposMed)
stockEntregas=crearmatriz(sucursales,tiposMed+2)

medicamentosSuc=0
while (medicamentosSuc<sucursales):
    entrada=input()
    datos=entrada.split()
    for i in range(tiposMed):
        asignavalor(medicamentosSuc,i,stockInicial,int(datos[i]))
    medicamentosSuc+=1

pacientes=0
while (pacientes<pacientesTot):
    entrada=input()
    datos=entrada.split()

    if int(datos[0]) <= sucursales:
        if medidas(int(datos[3]),int(datos[4])) == "Si":
            valor=stockEntregas[int(datos[0])-1][int(datos[1])-1]
            valor=valor+int(datos[2])
            asignavalor(int(datos[0])-1,int(datos[1])-1,stockEntregas,valor)

            valor=stockEntregas[int(datos[0])-1][tiposMed]
            valor+=1
            asignavalor(int(datos[0])-1,tiposMed,stockEntregas,valor)

        valor=stockEntregas[int(datos[0])-1][tiposMed+1]
        valor+=1
        asignavalor(int(datos[0])-1,tiposMed+1,stockEntregas,valor)

    pacientes+=1

imprimematriz(sucursales,tiposMed+2,stockEntregas)

for col in range(sucursales):
    for fil in range(tiposMed):
        valor=stockInicial[col][fil] - stockEntregas[col][fil]
        asignavalor(col,fil,stockFinal,valor)        


for i in range(sucursales):
    print(i+1)
    menor(stockFinal[i],tiposMed,True)
    mayor(stockFinal[i],tiposMed,True)
    menorVal=menor(stockEntregas[i],tiposMed,False)
    mayorVal=mayor(stockEntregas[i],tiposMed,False)
    promedioVal=suma(stockEntregas[i],tiposMed,False)/tiposMed 
    print("{0:.2f} {1:.2f} {2:.2f}".format(menorVal, promedioVal, mayorVal))
    pacientesSuc=stockEntregas[i][tiposMed+1]
    promedioSuc=0
    if pacientesSuc > 0:
        promedioSuc=suma(stockEntregas[i],tiposMed,False)/pacientesSuc
    print("{0:.2f}".format(promedioSuc))

menormayortipo1(stockEntregas)
