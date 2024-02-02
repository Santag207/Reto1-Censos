1. Generación de Datos Aleatorios:
  Este proyecto incluye un generador de datos ficticios para censos de población. Cada censo cuenta con un identificador único (id), un nombre generado aleatoriamente, una edad y un indicador de si la persona paga impuestos.

3. Búsqueda Secuencial por ID:
  La función busqueda_secuencial realiza búsquedas secuenciales por ID en una lista de censos. Mide el tiempo de ejecución y presenta los resultados, incluyendo el censo encontrado y el tiempo de búsqueda.

5. Búsqueda Binaria por ID:
La función busqueda_binaria busca censos por ID utilizando un enfoque binario después de ordenar la lista por IDs. Mide el tiempo de ejecución y muestra los resultados, incluyendo el censo encontrado y el tiempo de búsqueda.

4. Búsqueda por Nombre:
La función busqueda_nombre realiza búsquedas por nombre, mostrando todos los datos asociados con el nombre buscado. Mide el tiempo de ejecución y presenta los resultados.

6. Función de Graficación:
La función Graficar utiliza matplotlib para crear gráficas que visualizan los tiempos de búsqueda en las iteraciones especificadas. La gráfica incluye tanto la búsqueda secuencial como la búsqueda binaria, si esta última se ejecuta.

6. Menú Principal:
La función main implementa un menú interactivo que permite al usuario seleccionar entre buscar por ID, buscar por nombre o salir del programa.

8. Bucle de Ejecución:
El programa está envuelto en un bucle que permite al usuario realizar múltiples búsquedas hasta que decide salir.

8. Ordenamiento Inicial:
La lista de censos se ordena inicialmente por identificador (id) para facilitar la búsqueda binaria.
