#Reto 1
#John Haver Herrera
#Mision TIC 2022

indAyunas = str(input("Indique si está en ayunas <Si>/<No>: "))
valGlucosaSangre = float(input("Ingrese en valor de grlucosa en sangre mmol/l "))

if indAyunas == "si":
  if valGlucosaSangre < 4.4:
    print("Hipoglisemia")

  if valGlucosaSangre >= 4.4 and valGlucosaSangre < 6.1:
    print("Sin diabetes")

  if valGlucosaSangre >= 6.1 and valGlucosaSangre < 7:
    print("Pre diabetes")

  if valGlucosaSangre >= 7:
    print("Diabetes")

if indAyunas == "no":
  if valGlucosaSangre < 7.8:
    print("Sin diabetes")

  if valGlucosaSangre >= 7.8 and valGlucosaSangre < 11:
    print("Pre diabetes")

  if valGlucosaSangre >= 11:
    print("Diabetes")

if indAyunas != "si" and indAyunas != "no":
  print("error en los datos ingresados")