import random

print("========================================")
print("Bienvenido al Juego de Adinanza")
print("========================================")

numero_secreto = random.randrange(1, 101)

print("Selecciones nivel de dificultad")
print("========================================")
print("(1)Fácil (2)Medio (3)Difícil")
print("========================================")
nivel = int(input("Ingrese nivel de dificultad: "))
print("========================================")

print('Número secreto: ', numero_secreto)

if(nivel == 1):
  total_intentos = 20
elif(nivel == 2):
  total_intentos = 10
else:
  total_intentos= 5

for iteracion in range(1, total_intentos + 1): #se añade el + 1 para que tome los 3 intentos y no solo dos
  print('Intento: {} de {}' .format(iteracion, total_intentos))
  entrada = input("Digite un número entre el 1 y 100: ")
  entrada = int(entrada)
  print("Digitaste...", entrada)

  if(entrada < 1 or entrada > 100):
    print('Digite un número entre el 1 y 100: ')
    continue #Si cumple continuará con el proceso de iteración dentro del for

  acertaste = entrada == numero_secreto #iguales
  mayor = entrada > numero_secreto #entrada es MAYOR
  menor = entrada > numero_secreto #entrada es MENOR

  if(acertaste):
    print('Felicitaciones!!... Adivinaste el número')
    break
  elif(mayor):
    print('Losiento... El número que ingrasaste es mayor que el número secreto')
  else:
    print('Los siento... El número que ingresaste es menor que el número secreto')

  iteracion = iteracion+1

print('Fin del juego')