def inverter_string(s):
    # Cria lista pra armazenar os caracteres invertidos
    caracteres_invertidos = []
    
    # Itera pelos caracteres da string do final para o início
    for i in range(len(s) - 1, -1, -1):
        caracteres_invertidos.append(s[i])
    
    # Junta os caracteres em uma nova string
    string_invertida = ''.join(caracteres_invertidos)
    
    return string_invertida

# Exp
entrada = input("Digite uma string para inverter: ")
resultado = inverter_string(entrada)
print("String invertida:", resultado)
