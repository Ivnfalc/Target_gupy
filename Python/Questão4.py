faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}


fatotal = sum(faturamento.values())


print("Percentual de representação por estado:")
for estado, valor in faturamento.items():
    perc = (valor / fatotal) * 100
    print(f"{estado}: {perc:.2f}%")
