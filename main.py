def calcular_media(numeros):
    """
    Calcula a média de uma lista de números
    """
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)

<<<<<<< HEAD
def calcular_mediana(numeros):
    """
    Calcula a mediana de uma lista de números
    """
    if not numeros:
        return 0
    numeros_ordenados = sorted(numeros)
    meio = len(numeros_ordenados) // 2
    if len(numeros_ordenados) % 2 == 0:
        return (numeros_ordenados[meio - 1] + numeros_ordenados[meio]) / 2
    return numeros_ordenados[meio]
=======
def calcular_moda(numeros):
    """
    Calcula a moda de uma lista de números
    """
    if not numeros:
        return 0
    from collections import Counter
    contador = Counter(numeros)
    return max(contador.items(), key=lambda x: x[1])[0]
>>>>>>> master

# Exemplo de uso
if __name__ == "__main__":
    # Lista de exemplo
    notas = [7.5, 8.0, 9.0, 6.5]
    
    # Calculando a média
    media = calcular_media(notas)
    
    # Mostrando o resultado
    print(f"As notas são: {notas}")
    print(f"A média é: {media:.2f}") 