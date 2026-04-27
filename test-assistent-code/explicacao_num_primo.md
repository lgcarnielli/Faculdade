# Explicação do Código: Verificador de Números Primos

## Função Principal

```python
def e_primo(n):
```

- **Definição**: Declara uma função chamada `e_primo` que recebe um parâmetro `n`
- **Propósito**: Verificar se o número `n` é primo

---

```python
    """Verifica se um número é primo."""
```

- **Docstring**: Documentação da função que descreve seu propósito
- **Utilidade**: Ajuda outros desenvolvedores a entender o que a função faz

---

```python
    if n < 2:
        return False
```

- **Condição**: Verifica se o número é menor que 2
- **Lógica**: Números menores que 2 (0 e 1) não são primos por definição
- **Retorno**: `False` — indica que não é primo

---

```python
    if n == 2:
        return True
```

- **Condição**: Verifica se o número é exatamente 2
- **Lógica**: 2 é o único número par que é primo
- **Retorno**: `True` — indica que é primo

---

```python
    if n % 2 == 0:
        return False
```

- **Operador**: `%` (módulo) retorna o resto da divisão
- **Condição**: Verifica se o número é divisível por 2 (é par)
- **Lógica**: Qualquer número par maior que 2 não é primo
- **Retorno**: `False`

---

```python
    for i in range(3, int(n**0.5) + 1, 2):
```

| Componente | Explicação |
|------------|------------|
| `range(3, ...)` | Começa em 3 e vai até o limite |
| `int(n**0.5) + 1` | Raiz quadrada de `n`, arredondada para cima |
| `, 2` | Incrementa de 2 em 2 (números ímpares) |

- **Otimização**: Só precisa testar divisores até a raiz quadrada de `n`
- **Justificativa**: Se `n` tem um divisor maior que sua raiz quadrada, o outro divisor correspondente será menor que a raiz quadrada

---

```python
        if n % i == 0:
            return False
```

- **Verificação**: Testa se `n` é divisível pelo número ímpar atual `i`
- **Se divisível**: Retorna `False` — encontrou um divisor, então não é primo

---

```python
    return True
```

- **Chega aqui**: Apenas se nenhum divisor foi encontrado
- **Conclusão**: O número é primo

---

## Bloco de Testes

```python
if __name__ == "__main__":
```

- **Propósito**: Garante que o código de teste só executa quando o arquivo é rodado diretamente
- **Boa prática**: Evita execução automática quando o arquivo é importado como módulo

---

```python
    numeros = [1, 2, 3, 4, 5, 17, 18, 19, 20, 21]
```

- **Lista**: Contém números para testar a função
- **Seleção**: Inclui primos (2, 3, 5, 17, 19) e não primos (1, 4, 18, 20, 21)

---

```python
    for num in numeros:
        print(f"{num} é primo? {e_primo(num)}")
```

- **Loop**: Itera sobre cada número da lista
- **f-string**: Formata a saída interpolando variáveis
- **Saída**: Exibe o resultado de cada teste

---

## Resultado Esperado

```
1 é primo? False
2 é primo? True
3 é primo? True
4 é primo? False
5 é primo? True
17 é primo? True
18 é primo? False
19 é primo? True
20 é primo? False
21 é primo? False
```

---

## Complexidade

- **Tempo**: O(√n) — devido à verificação apenas até a raiz quadrada
- **Espaço**: O(1) — usa apenas variáveis de tamanho fixo