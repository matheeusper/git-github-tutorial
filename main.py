"""
Módulo de funções estatísticas básicas.
Este módulo fornece funções para calcular média, mediana, moda, variância e desvio padrão.
"""

def calcular_media(numeros):
    """
    Calcula a média de uma lista de números.
    
    Args:
        numeros (list): Lista de números
        
    Returns:
        float: Média dos números
    """
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)

def calcular_mediana(numeros):
    """
    Calcula a mediana de uma lista de números.
    
    Args:
        numeros (list): Lista de números
        
    Returns:
        float: Mediana dos números
    """
    if not numeros:
        return 0
    numeros_ordenados = sorted(numeros)
    meio = len(numeros_ordenados) // 2
    if len(numeros_ordenados) % 2 == 0:
        return (numeros_ordenados[meio - 1] + numeros_ordenados[meio]) / 2
    return numeros_ordenados[meio]

def calcular_moda(numeros):
    """
    Calcula a moda de uma lista de números.
    
    Args:
        numeros (list): Lista de números
        
    Returns:
        float: Moda dos números
    """
    if not numeros:
        return 0
    from collections import Counter
    contador = Counter(numeros)
    return max(contador.items(), key=lambda x: x[1])[0]

def calcular_variancia(numeros):
    """
    Calcula a variância de uma lista de números.
    
    Args:
        numeros (list): Lista de números
        
    Returns:
        float: Variância dos números
    """
    if not numeros:
        return 0
    media = calcular_media(numeros)
    diferencas_quadradas = [(x - media) ** 2 for x in numeros]
    return sum(diferencas_quadradas) / len(numeros)

def calcular_desvio_padrao(numeros):
    """
    Calcula o desvio padrão de uma lista de números.
    
    Args:
        numeros (list): Lista de números
        
    Returns:
        float: Desvio padrão dos números
    """
    if not numeros:
        return 0
    return calcular_variancia(numeros) ** 0.5

# Exemplo de uso
if __name__ == "__main__":
    # Lista de exemplo
    notas = [7.5, 8.0, 9.0, 6.5, 8.5]
    
    # Calculando todas as estatísticas
    print(f"Dados: {notas}")
    print(f"Média: {calcular_media(notas):.2f}")
    print(f"Mediana: {calcular_mediana(notas):.2f}")
    print(f"Moda: {calcular_moda(notas):.2f}")
    print(f"Variância: {calcular_variancia(notas):.2f}")
    print(f"Desvio Padrão: {calcular_desvio_padrao(notas):.2f}") 