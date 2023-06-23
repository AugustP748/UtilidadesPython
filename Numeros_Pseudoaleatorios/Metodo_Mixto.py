def congruencial_mixto(semilla, a, c, m):
    while True:
        semilla = (a * semilla + c) % m
        yield semilla

if __name__ == '__main__':
    # Ejemplo de uso
    semilla_inicial = 1237
    constante_a = 4309
    constante_c = 2311
    modulo_m = 6031
    cantidad_numeros = 7

    generador_mixto = congruencial_mixto(semilla_inicial, constante_a, constante_c, modulo_m)

    numeros_pseudoaleatorios = [next(generador_mixto) for _ in range(cantidad_numeros)]

    print("Números pseudoaleatorios generados:", numeros_pseudoaleatorios)
