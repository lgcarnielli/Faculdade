# Explicação do Código Refatorado

## Visão Geral

Este código calcula estatísticas básicas (total, média, máximo, mínimo) de uma lista de números.

---

## Linha a Linha

### Definição da Função

```python
def calcular_estatisticas(lista):
```

| Aspecto | Explicação |
|---------|------------|
| `def` | Palavra-chave para definir uma função |
| `calcular_estatisticas` | Nome da função (em português, snake_case) |
| `(lista)` | Parâmetro: a lista de números a ser processada |

---

### Docstring

```python
    """
    Calcula estatísticas básicas de uma lista de números.
    
    Args:
        lista: Lista de números inteiros ou floats.
        
    Returns:
        Tupla com: (total, média, máximo, mínimo).
    """
```

- **Aspas triplas**: Define uma string de múltiplas linhas
- **Propósito**: Documentar o que a função faz
- **Args**: Descreve os parâmetros de entrada
- **Returns**: Descreve o que a função retorna
- **Boa prática**: Essencial para documentação automática

---

### Cálculo do Total

```python
    total = sum(lista)
```

| Componente | Explicação |
|------------|------------|
| `sum()` | Função nativa do Python que soma todos os elementos |
| `lista` | Parâmetro passado para a função |
| `total` | Variável que armazena o resultado |

**Antes**: Loop manual `for i in range(len(l)): t = t + l[i]`
**Depois**: Uma única linha com `sum()`

---

### Cálculo da Média

```python
    media = total / len(lista)
```

| Componente | Explicação |
|------------|------------|
| `/` | Operador de divisão |
| `total` | Soma de todos os elementos |
| `len(lista)` | Retorna a quantidade de elementos |

**Fórmula**: média = soma / quantidade

---

### Cálculo do Máximo

```python
    maximo = max(lista)
```

- `max()`: Função nativa que retorna o maior valor
- Substitui o loop manual que verificava cada elemento

---

### Cálculo do Mínimo

```python
    minimo = min(lista)
```

- `min()`: Função nativa que retorna o menor valor
- Substitui o loop manual que verificava cada elemento

---

### Retorno da Função

```python
    return total, media, maximo, minimo
```

| Aspecto | Explicação |
|---------|------------|
| `return` | Keyword que especifica o valor de retorno |
| **Tupla** | Os 4 valores são retornados juntos como uma tupla |
| Desempacotamento | Permite atribuir cada valor a uma variável separada |

---

### Definição dos Dados

```python
numeros = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
```

| Aspecto | Explicação |
|---------|------------|
| `numeros` | Nome descritivo (antes era `x`) |
| `[...]` | Lista com 10 números inteiros |
| Vírgula + espaço | Formatação PEP 8 |

---

### Chamada da Função

```python
total, media, maximo, minimo = calcular_estatisticas(numeros)
```

| Aspecto | Explicação |
|---------|------------|
| **Desempacotamento** | Atribui cada elemento da tupla a uma variável |
| **Antes** | `a,b,c2,d=c(x)` — nomes confusos |
| **Depois** | Nomes claros que indicam o conteúdo |

---

### Impressão dos Resultados

```python
print("Total:", total)
print("Média:", media)
print("Maior:", maximo)
print("Menor:", minimo)
```

| Aspecto | Explicação |
|---------|------------|
| `print()` | Função para exibir saída no console |
| **f-string implícita** | Python concatena automaticamente com espaço |
| `"Total:"` | String fixa que serve como rótulo |
| `total` | Variável com o valor calculado |

---

## Comparação: Antes vs Depois

| Aspecto | Código Original | Código Refatorado |
|---------|------------------|-------------------|
| Nome da função | `c(l)` | `calcular_estatisticas(lista)` |
| Variáveis | `t, m, mx, mn, x, a, b, c2, d` | `total, media, maximo, minimo, numeros` |
| Soma | Loop manual | `sum()` |
| Máximo | Loop manual | `max()` |
| Mínimo | Loop manual | `min()` |
| Documentação | Ausente | Docstring completa |
| Formatação | Sem espaços | PEP 8 |

---

## Benefícios da Refatoração

1. **Legibilidade**: Nomes claros indicam o propósito
2. **Manutenção**: Easier de modificar no futuro
3. **Eficiência**: Funções nativas são otimizadas em C
4. **Documentação**: Docstring ajuda outros desenvolvedores
5. **Padrão**: Segue convenções Python (PEP 8)

---

## Saída Esperada

```
Total: 346
Média: 34.6
Maior: 89
Menor: 2
```

---

## Conceitos Python Utilizados

| Conceito | Onde Aplicado |
|----------|---------------|
| Função | `def calcular_estatisticas()` |
| Parâmetro | `lista` |
| Docstring | `"""..."""` |
| Função nativa | `sum()`, `max()`, `min()`, `len()` |
| Tupla | `(total, media, maximo, minimo)` |
| Desempacotamento | `total, media, ... = ...` |
| Tipagem dinâmica | Lista com inteiros |