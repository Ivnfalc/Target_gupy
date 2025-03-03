import json

def calcular_faturamento(arquivo_json):
    with open(arquivo_json, 'r') as file:
        # Carrega os dados do arquivo JSON
        dados = json.load(file)


    faturamento = [dia['valor'] for dia in dados]


    menor_faturamento = min(faturamento)
    maior_faturamento = max(faturamento)

    # Calculando a média mensal, ignorando os dias com faturamento 0
    dias_validos = [valor for valor in faturamento if valor > 0]
    media_mensal = sum(dias_validos) / len(dias_validos) if dias_validos else 0

    
    dias_acima_media = sum(1 for valor in faturamento if valor > media_mensal)

    # Resultados
    return {
        "menor_faturamento": menor_faturamento,
        "maior_faturamento": maior_faturamento,
        "dias_acima_media": dias_acima_media
    }


if __name__ == "__main__":

    resultado = calcular_faturamento('dados.json')
    print("Menor faturamento:", resultado["menor_faturamento"])
    print("Maior faturamento:", resultado["maior_faturamento"])
    print("Dias acima da média mensal:", resultado["dias_acima_media"])