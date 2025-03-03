def inverter_string(s):
    return s[::-1]
# Impt
string_original = input("Digite a string a ser invertida: ")


string_invertida = inverter_string(string_original)

# Exibindo o resultado
print("String original:", string_original)
print("String invertida:", string_invertida)