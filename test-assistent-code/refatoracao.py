def calcular_estatisticas(lista):
    """
    Calcula estatísticas básicas de uma lista de números.
    
    Args:
        lista: Lista de números inteiros ou floats.
        
    Returns:
        Tupla com: (total, média, máximo, mínimo).
    """
    total = sum(lista)
    media = total / len(lista)
    maximo = max(lista)
    minimo = min(lista)
    
    return total, media, maximo, minimo


numeros = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]

total, media, maximo, minimo = calcular_estatisticas(numeros)

print("Total:", total)
print("Média:", media)
print("Maior:", maximo)
print("Menor:", minimo)