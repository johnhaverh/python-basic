#Reto 2
#John Haver Herrera
#Mision TIC 2022

valor1=int(input())
valor2=int(input())

medicamento1=valor1
medicamento2=valor2
pacientesatendidos=0
porcentajepacientes1=0
porcentajepacientes2=0
pacientes1=0
pacientes2=0
ninguno=0
#print(medicamento1,medicamento2)
continuar = True
while continuar:
    try:
        #indAyunas = str(input(""))
        valor1=str(input(""))
    except EOFError:
            break
    indAyunas=valor1
    if indAyunas.isspace == True or len(indAyunas)==0:
        continuar = False
        break
    else: 
        valGlucosaSangre = float(input())
        pacientesatendidos+=1
        if indAyunas == "si":
            if valGlucosaSangre < 4.4:
                pacientes2+=1
            if valGlucosaSangre >= 4.4 and valGlucosaSangre < 6.1:
                ninguno+=1
            if valGlucosaSangre >= 6.1 and valGlucosaSangre < 7:
                pacientes1+=1
            if valGlucosaSangre >= 7:
                pacientes1+=1
        if indAyunas == "no":
            if valGlucosaSangre < 7.8:
                ninguno+=1
            if valGlucosaSangre >= 7.8 and valGlucosaSangre < 11:
                pacientes1+=1
            if valGlucosaSangre >= 11:
                pacientes1+=1


if pacientesatendidos !=0:
    print("{0}".format(pacientesatendidos))
    porcentajepacientes1=(float(pacientes1)/pacientesatendidos)*100
    print("{0} {1:.2f}%".format(pacientes1, porcentajepacientes1))
    porcentajepacientes2=(float(pacientes2)/pacientesatendidos)*100
    print("{0} {1:.2f}%".format(pacientes2, porcentajepacientes2))
else:
    print(pacientesatendidos)
    print("{0} {1:.2f}%".format(0,0)) 
    print("{0} {1:.2f}%".format(0,0)) 