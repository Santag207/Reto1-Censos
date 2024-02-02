#Santiago Castro Zuluaga - Reto 1 (Censos)

import random
import time
import matplotlib.pyplot as plt
k = 100 #Numero de iteraciones tiempos y grafica
j = 100 #Numero de IDs random y de censos

def generar_nombre():  #Generador random de nombres (Usa letras aleatorias)
    letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    inicial_nombre = random.choice(letras)
    inicial_apellido1 = random.choice(letras)
    inicial_apellido2 = random.choice(letras)
    return f"{inicial_nombre}{inicial_apellido1}{inicial_apellido2}"

def generar_censo(): #Generador random de censos (No repite IDs)
    id_ = random.randint(1, j + 1)
    while id_ in ids_generados:
        id_ = random.randint(1, j + 1)

    nombre = generar_nombre()
    edad = random.randint(18, j - 1)
    paga_impuestos = random.choice([True, False])

    return {'id': id_, 'nombre': nombre, 'edad': edad, 'paga impuestos': paga_impuestos}

def busqueda_secuencial(lista, busqueda): #Busqueda ID secuencial
    for elemento in lista:
        if elemento['id'] == busqueda:
            return elemento
    return None

def busqueda_binaria(lista, busqueda): #Busqueda ID bin
    # La lista debe estar ordenada por IDs para realizar búsqueda binaria
    lista_ordenada = sorted(lista, key=lambda x: x['id'])
    inicio, fin = 0, len(lista_ordenada) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        elemento = lista_ordenada[medio]

        if elemento['id'] == busqueda:
            return elemento
        elif elemento['id'] < busqueda:
            inicio = medio + 1
        else:
            fin = medio - 1

    return None

def busqueda_id(lista, busqueda): #Busqueda ID
    tiempoSecuencial = []
    tiempoBinario = []
  
    # Búsqueda secuencial
    for _ in range(k):
      inicio_tiempoSecuencial = time.time()
      resultado_secuencial = busqueda_secuencial(lista, busqueda)
  
      fin_busqueda_secuencial = time.time()
      tiempo_tiempoSecuencial = fin_busqueda_secuencial - inicio_tiempoSecuencial
      tiempoSecuencial.append(tiempo_tiempoSecuencial)

    print("Búsqueda Secuencial:")
    print(resultado_secuencial)
    print("Este es el tiempo que tardó en buscar el ID: " + str(tiempo_tiempoSecuencial))
    print(" ")

    # Búsqueda binaria
    for _ in range(k):
      inicio_tiempoBinario = time.time()
      resultado_binario = busqueda_binaria(lista, busqueda)

      fin_busqueda_binaria = time.time()
      tiempo_tiempoBinario = fin_busqueda_binaria - inicio_tiempoBinario
      tiempoBinario.append(tiempo_tiempoBinario)

    print("Búsqueda Binaria:")
    print(resultado_binario)
    print("Este es el tiempo que tardó en buscar el ID: " + str(tiempo_tiempoBinario))
    print(" ")
    Graficar(tiempoSecuencial, tiempoBinario, k)

def busqueda_nombre(lista, busqueda):  # Busqueda nombre Secuencial
# Búsqueda secuencial
  tiempoSecuencial = []
  tiempoBinario = []
  busqueda = busqueda.upper()
  for _ in range(k):
      inicio_tiempoSecuencial = time.time()
      for elemento in lista:
          if elemento['nombre'] == busqueda:
              fin_busqueda_secuencial = time.time()
              tiempo_tiempoSecuencial = fin_busqueda_secuencial - inicio_tiempoSecuencial
              tiempoSecuencial.append(tiempo_tiempoSecuencial)

              print("Búsqueda Secuencial:")
              for clave, valor in elemento.items():
                print(f"{clave}: {valor}")
              print("Este es el tiempo que tardó en buscar el Nombre: " + str(tiempo_tiempoSecuencial))
              print(" ")
              #Graficar(tiempoSecuencial, tiempoBinario, k) #No muestra la grafca por problemas de replit
              return
              
  print("No se encontró el nombre")
    
def Graficar(tiempoSecuencial, tiempoBinario, k):
  # Crear una lista con números de iteración para el eje x
  iteraciones = list(range(1, k + 1))

  # Graficar los tiempos de búsqueda
  plt.plot(iteraciones, tiempoSecuencial, label='Búsqueda Secuencial')
  if (tiempoBinario != 0):
    plt.plot(iteraciones, tiempoBinario, label='Búsqueda Binaria')

  # Configurar la gráfica
  plt.title('Tiempos de Búsqueda')
  plt.xlabel('Iteración')
  plt.ylabel('Tiempo (segundos)')
  plt.legend()  # Agregar leyenda

  # Guardar la gráfica como una imagen
  nombre_archivo = f"grafica_{iteraciones[-1]}.png"
  plt.savefig(nombre_archivo)

  # Mostrar la gráfica
  plt.show()    #Si se quiere seguir en el menu se tiene que comentar ya que almostrar la grafica el programa se cierra para mostrarlos datos en vivo

def main():
  aux = 1
  while aux == 1:
      ultimo_censo = censos[-1]
      print(" ")
      print("Último censo registrado:", ultimo_censo)
      print("------------------------------------------")
      print("\nMenú:")
      print("1. Buscar por ID")
      print("2. Buscar por nombre")
      print("3. Salir")

      opcion = input("Selecciona una opción (1/2/3): ")

      if opcion == '1':
          # Búsqueda por ID
          id_busqueda = int(input("Introduce el ID que deseas buscar: "))
          print(" ")
          busqueda_id(censos, id_busqueda)
      elif opcion == '2':
          # Búsqueda por nombre
          nombre_busqueda = input("Introduce las dos iniciales del nombre que deseas buscar: ")
          print(" ")
          busqueda_nombre(censos, nombre_busqueda)
      elif opcion == '3':
          print("Gracias por usar el programa.")
          aux = 0  # Asigna 0 a aux para salir del bucle
      else:
          print("Opción no válida. Por favor, elige 1, 2 o 3.")


if __name__ == "__main__":
    n_censos = j
    ids_generados = set()
    censos = []

    for _ in range(n_censos):
        censo = generar_censo()
        ids_generados.add(censo['id'])
        censos.append(censo)

    # Ordenar la lista de censos por el ID
    censos = sorted(censos, key=lambda x: x['id'])

    main()