import json


def calcfat(arquivo_json):
    with open(arquivo_json, 'r') as file:
        dados = json.load(file)

    faturamento = [dia['valor'] for dia in dados]

    menfat = min(faturamento)
    maifat = max(faturamento)

    # Resultados
    return {
        "menor_faturamento": menfat,
        "maior_faturamento": maifat,

    }


if __name__ == "__main__":
    resultado = calcfat('dados.json')
    print("Menor faturamento:", resultado["menor_faturamento"])
    print("Maior faturamento:", resultado["maior_faturamento"])
