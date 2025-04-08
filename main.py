def calcular_media(numeros):
    """
    Calcula a média de uma lista de números
    """
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)

# Exemplo de uso
if __name__ == "__main__":
    # Lista de exemplo
    notas = [7.5, 8.0, 9.0, 6.5]
    
    # Calculando a média
    media = calcular_media(notas)
    
    # Mostrando o resultado
    print(f"As notas são: {notas}")
    print(f"A média é: {media:.2f}") 