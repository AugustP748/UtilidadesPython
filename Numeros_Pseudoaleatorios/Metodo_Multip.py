def congruencial_multiplicativo(semilla, a, m):
    while True:
        semilla = (a * semilla) % m
        yield semilla

if __name__ == '__main__':
    # Ejemplo de uso
    semilla_inicial = 1317
    constante_a = 5631
    modulo_m = 547
    cantidad_numeros = 7

    generador_multiplicativo = congruencial_multiplicativo(semilla_inicial, constante_a, modulo_m)

    numeros_pseudoaleatorios = [next(generador_multiplicativo) for _ in range(cantidad_numeros)]

    print("Números pseudoaleatorios generados:", numeros_pseudoaleatorios)
