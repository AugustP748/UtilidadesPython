def lehmer(semilla, a, m):
    while True:
        semilla = (a * semilla) % m
        yield semilla

if __name__ == '__main__':
    # Ejemplo de uso
    semilla_inicial = 4122
    constante_a = 48271
    modulo_m = 2**31 - 1
    cantidad_numeros = 10

    generador_lehmer = lehmer(semilla_inicial, constante_a, modulo_m)

    numeros_pseudoaleatorios = [next(generador_lehmer) for _ in range(cantidad_numeros)]

    print("Números pseudoaleatorios generados:", numeros_pseudoaleatorios)
