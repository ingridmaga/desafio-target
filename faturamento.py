import json

# Exemplo de dados de faturamento em JSON
dados_faturamento_json = '''
{
    "faturamento_diario": [1000, 2000, 0, 0, 1500, 1700, 0, 2100, 0, 3000, 2900, 0, 4000, 4500, 0, 2500, 0, 0, 5000, 5500, 0, 6000, 6200, 0, 7000, 0, 7200, 0, 8000, 0, 8500]
}
'''

# Carrega os dados de faturamento do JSON
dados_faturamento = json.loads(dados_faturamento_json)["faturamento_diario"]

# Filtra os dias com faturamento (ignorar os dias com faturamento 0)
faturamento_valido = [valor for valor in dados_faturamento if valor > 0]

# Calcula o menor valor de faturamento
menor_faturamento = min(faturamento_valido)

# Calcula o maior valor de faturamento
maior_faturamento = max(faturamento_valido)

# Calcula a média mensal de faturamento
media_faturamento = sum(faturamento_valido) / len(faturamento_valido)

# Conta os dias q o faturamento foi superior a média mensal
dias_acima_da_media = sum(1 for valor in faturamento_valido if valor > media_faturamento)

# Retorna os resultados
print(f"Menor faturamento: {menor_faturamento}")
print(f"Maior faturamento: {maior_faturamento}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
