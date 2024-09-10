def count_letter_a(s):
    # Conta a ocorrência de 'a' e 'A'
    count_a = s.count('a') + s.count('A')
    
    # Verifica se a letra 'a' existe na string
    if count_a > 0:
        return f"A letra 'a' aparece {count_a} vezes na string."
    else:
        return "A letra 'a' não aparece na string."

# Entrada da string
string = input("Informe uma string: ")

# Verifica e imprime a quantidade de vzs q a letra 'a' aparece 
resultado = count_letter_a(string)
print(resultado)
