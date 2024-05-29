def count_collisions(robots):
    n = len(robots)
    collisions = [0] * n
    positions = [i * 2 for i in range(n)]  # Distancia inicial de 2 metros
    
    while True:
        new_positions = positions[:]
        collision_detected = False
        
        for i in range(n):
            if robots[i] == 'R':
                new_positions[i] += 1
            elif robots[i] == 'L':
                new_positions[i] -= 1

        for i in range(n - 1):
            if new_positions[i] == new_positions[i + 1] and robots[i] == 'R' and robots[i + 1] == 'L':
                collisions[i] += 1
                collisions[i + 1] += 1
                robots = robots[:i] + 'L' + 'R' + robots[i + 2:]
                collision_detected = True
        
        positions = new_positions
        
        if not collision_detected:
            break
    
    return ' '.join(map(str, collisions))

if __name__ == '__main__':
    # Leer la entrada del usuario
    robots = input("Ingrese la secuencia de robots (Ejemplo: RRL): ")
    
    # Llamar a la función y mostrar el resultado
    resultado = count_collisions(robots)
    print(f"Resultado: {resultado}")
