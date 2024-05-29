Descripción ejercicio colisiones

Definición y Parámetro:

La función count_collisions tiene como objetivo calcular y devolver un conteo de colisiones para una secuencia dada de robots que se mueven hacia la derecha ('R') o hacia la izquierda ('L').

Uso de la Función count_collisions:

La función count_collisions está definida con un parámetro robots, que debe ser una cadena que contiene solo los caracteres 'R' y 'L'. Cada carácter representa un robot que se mueve en una dirección específica.

Funcionamiento Interno:

Inicialización: Al recibir la cadena de robots, la función inicializa varias estructuras de datos:

- n = len(robots): Calcula la cantidad de robots en la secuencia.
- collisions = [0] * n: Inicializa una lista collisions con ceros, donde cada índice representa la cantidad de colisiones que ha tenido el robot correspondiente.
- positions = [i * 2 for i in range(n)]: Inicializa las posiciones iniciales de los robots en incrementos de 2 metros, asegurando una distancia inicial entre ellos.

Simulación de Movimiento y Colisiones:

- La función entra en un bucle while True que simula el movimiento continuo de los robots y detecta las colisiones:
- new_positions = positions[:]: Copia las posiciones actuales de los robots.
- Actualiza las posiciones de los robots según su dirección ('R' para derecha, 'L' para izquierda).
- Detecta colisiones entre los robots adyacentes que se mueven en direcciones opuestas ('RL' o 'LR'). Cuando se detecta una colisión:
    - Incrementa los contadores de colisiones para los robots involucrados.
    - Intercambia sus direcciones para simular el cambio instantáneo de dirección tras una colisión.

Finalización del Proceso:

El bucle while continúa hasta que no se detecten más colisiones durante un ciclo completo de verificación.

Retorno del Resultado:

Una vez finalizada la simulación, la función convierte la lista collisions en una cadena de texto donde cada número representa la cantidad de colisiones que experimentó cada robot.

Ejemplo de Uso:

Para ejecutar el archivo desde la consola dirigise al directorio de colisiones y ejecute el comando python collisions.py
Seguido a esto solciitar ingresar una secuencia de robots: Ingrese la secuencia de robots (Ejemplo: RRL): RRL
Después de presionar Enter, la función calculará y mostrará el resultado: Resultado: 1 2 1

Se pueden realizar pruebas unitarias por medio del archivo test_collisions.py, en la cual por medio de la libreria unittest se realiza el testeo de los resultados esperados:

Se crea la clase class TestCountCollisions(unittest.TestCase) en donde internamente se crea una función la cual se encarga de comparar los valores recibidos con la salida esperada, ejemplo self.assertEqual(count_collisions('LR'), '0 0') al ser correcta la salida nos dara como resultado un ok en los test de lo contrario nos mostrara que la salida es difernente a los parametros ingresados.

Para ejecutar el test debe realizarlo con el comando python test_collisions.py dentro de la carpeta colisiones.

se pueden agregar mas test con la siguiente linea: self.assertEqual(count_collisions('LR'), '0 0') remplazando las entradas y las salidas esperadas.
