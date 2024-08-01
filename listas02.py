#Agora relacione as duas listas para printar 'O melhor mês do ano foi {} com {} vendas' e o mesmo para o pior mês do ano.

#Calcule também o faturamento total do Ano e quanto que o melhor mês representou do faturamento total. 


meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]


vendas_1sem.extend(vendas_2sem)
menor_valor = min(vendas_1sem)
maior_valor = max(vendas_1sem)


i_maior_valor = vendas_1sem.index(maior_valor)
print(f'O melhor mês do ano foi {meses[i_maior_valor]} com {maior_valor}')
i_menor_valor = vendas_1sem.index(menor_valor)
print(f'O pior mês do ano foi {meses[i_menor_valor]} com {menor_valor}')


fat_total = sum(vendas_1sem)
print(f'O faturamento total foi de R${fat_total:,}')


percentual = maior_valor / fat_total
print(f'O melhor mês representou {percentual:.1%} das vendas do ano todo.')

