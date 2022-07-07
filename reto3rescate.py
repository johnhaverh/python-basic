#Reto 3 rescate
#John Haver Herrera

from posixpath import split

#sucursales=0
#while (sucursales==0):
entrada=input()
datos=entrada.split()

sucursales=int(datos[0])
pacientesSuc=int(datos[1])

medicamentos=[]
medSucursal=[]

indMed=0
while (indMed<sucursales):
    valor=int(input())
    if valor > 0:   
        medicamentos.append(valor)
        medSucursal.append(valor)
        indMed+=1

indPac=0
while (indPac<pacientesSuc):
    indPac+=1
    valor2=input()
    datos2=valor2.split()

    suc=int(datos2[0]) - 1 
    sistolica=int(datos2[1])
    diastolica = int(datos2[2])
    medSuc = 0

    if sistolica < 83 and diastolica < 48:
        medSuc=15
    elif ((sistolica >= 83  and sistolica  <  124) and (diastolica>=48  and diastolica<66 )):
        medSuc=0
    elif ((sistolica >= 124 and sistolica  <  141) and (diastolica>=66  and diastolica<83 )):
        medSuc=0
    elif ((sistolica >= 141 and sistolica  <  158) and (diastolica>=83  and diastolica<97 )):
        medSuc=3
    elif ((sistolica >= 158 and sistolica  <  186) and (diastolica>=97  and diastolica<112)):
        medSuc=6
    elif ((sistolica >= 186 and sistolica  <  197) and (diastolica>=112 and diastolica<128)):
        medSuc=18
    elif (sistolica  >= 197 and diastolica >= 128):
        medSuc=30
    elif (sistolica  >= 159 and diastolica  <  94) :
        medSuc=24


    for i in range(0, len(medicamentos)):
        if i==suc:
            valor=medicamentos[i] 
    valor-=medSuc
    if valor > 0:
        for i in range(0, len(medicamentos)):
            if i==suc:
                medicamentos[i] = valor

mayor=medicamentos[0]
sucMayor=0
for i in range(1, len(medicamentos)):
    if medicamentos[i]>mayor:
        mayor=medicamentos[i] 
        sucMayor=i
sucMayor+=1

menor=medicamentos[0]
sucMenor=0
for i in range(1, len(medicamentos)):
    if medicamentos[i]<menor:
        menor=medicamentos[i] 
        sucMenor=i
sucMenor+=1
print(sucMenor,menor)
print(sucMayor,mayor)

for i in range(0, len(medicamentos)):
    valor3=((medSucursal[i] - medicamentos[i])/medSucursal[i])*100
    print("{0} {1:.2f}%".format(i+1, valor3))
