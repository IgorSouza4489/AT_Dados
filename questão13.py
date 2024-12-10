#complexo 1
def exercicio_mochila(capacidade, pesos, valores, n):
    dp = [[0] * (capacidade + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, capacidade + 1):
            if pesos[i-1] <= w:
                #uma condicional que decide se inclui ou nao o item
                dp[i][w] = max(valores[i-1] + dp[i-1][w - pesos[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][capacidade]


def executar():
    pesos = [2, 3, 4, 5]
    valores = [3, 4, 5, 6]
    capacidade = 5
    n = len(pesos)
    resultado = exercicio_mochila(capacidade, pesos, valores, n)
    print(f"O valor máximo que pode ser carregado é {resultado}")

