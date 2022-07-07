#Reto 3
#John Haver Herrera

from posixpath import split
import os

os.system('clear') 

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
    indAyunas=datos2[1]
    if indAyunas.isspace == True or len(indAyunas)==0:
        continuar = False
        break
    else: 
        valGlucosaSangre = float(datos2[2])
        medSuc = 0
        if indAyunas == "si" or indAyunas == "no":
            if indAyunas == "si":
                if valGlucosaSangre < 4.4:
                    medSuc=1
                if valGlucosaSangre >= 4.4 and valGlucosaSangre < 6.1:
                    medSuc=0
                if valGlucosaSangre >= 6.1 and valGlucosaSangre < 7:
                    medSuc=2
                if valGlucosaSangre >= 7:
                    medSuc=7
            if indAyunas == "no":
                if valGlucosaSangre < 7.8:
                    medSuc=0
                if valGlucosaSangre >= 7.8 and valGlucosaSangre < 11:
                    medSuc=3
                if valGlucosaSangre >= 11:
                    medSuc=10

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
