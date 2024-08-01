#Qual foi o valor de vendas do melhor mês do ano? E valor do pior mês do ano?


meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]


vendas_1sem.extend(vendas_2sem)
menor_valor = min(vendas_1sem)
print(menor_valor)
maior_valor = max(vendas_1sem)
print(maior_valor)



