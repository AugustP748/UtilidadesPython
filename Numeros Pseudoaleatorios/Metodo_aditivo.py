
def congruencial_aditivo(semillas, m):
    k = len(semillas)
    n = 0
    while True:
        nuevo_valor = sum(semillas) % m
        yield nuevo_valor
        semillas[n % k] = nuevo_valor
        n += 1



if __name__ == '__main__':
    # Ejemplo de uso
    #semillas_iniciales = [1942, 2372, 5131, 3317, 5147]
    semillas_iniciales = [5147, 3317, 5131, 2372,1942 ]
    modulo_m = 5147
    cantidad_numeros = 7

    generador_congruencial = congruencial_aditivo(semillas_iniciales, modulo_m)

    numeros_pseudoaleatorios = [next(generador_congruencial) for _ in range(cantidad_numeros)]

    print("Números pseudoaleatorios generados:", numeros_pseudoaleatorios)

