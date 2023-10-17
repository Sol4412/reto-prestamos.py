https://replit.com/join/juiskncotr-sol-veronicaver
#Calcular prestamos#
print("Te ayudaremos a calcular tu prestamo :)")
print("Por favor ingresa los datos que se te piden a continuacion:")
print("Cantidad del prestamo: ")
prestamo=float(input())
print("Tasa de interes anual (porcentaje): ")
interes=float(input())
print("Duracion del prestamo en años: ")
duracion=float(input())
if interes <=.05 == prestamo <=5:
  print("prestamo de bajo riesgo")
elif interes >.05 == prestamo >5:
  print("prestamo de riesgo moderado")
else :
  print("prestamo de alto riesgo")
