#Crie uma lista com o top 3 valores de vendas do ano. 


meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]


vendas_1sem.extend(vendas_2sem)


top3 = list()
maior_valor = max(vendas_1sem)
top3.append(maior_valor)
vendas_1sem.remove(maior_valor)
maior_valor = max(vendas_1sem)
top3.append(maior_valor)
vendas_1sem.remove(maior_valor)
maior_valor = max(vendas_1sem)
top3.append(maior_valor)
vendas_1sem.remove(maior_valor)
print(f'Os 3 maiores valores são {top3}')