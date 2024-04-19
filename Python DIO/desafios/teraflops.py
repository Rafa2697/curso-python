capacidade_atual, aumento_percentual = map(int, input().split())


soma = capacidade_atual * (aumento_percentual/100) + capacidade_atual
print(f"{soma:.0f}")

