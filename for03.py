#Digamos que você está analisando as vendas dos produtos de um ecommerce e quer identificar quais produtos tiveram no ano 2020 mais vendas do que no ano de 2019, para reportar isso para a diretoria.


produtos = ['computador', 'livro', 'tablet', 'celular', 'tv', 'ar condicionado', 
            'alexa', 'maquina de café', 'kindle']
vendas2019 = [215688, 324589, 845698, 978546, 245698, 654897, 789546, 458975, 145698]
vendas2020 = [325469, 265875, 987564, 758945, 225456, 758469, 358758, 845755, 132546]


for i, produto in enumerate(produtos):
    if vendas2020[i] > vendas2019[i]:
        crescimento = vendas2020[i] / vendas2019[i] - 1
        print(f'{produto} vendeu R${vendas2019[i]:,} em 2019, R${vendas2020[1]:,} em 2020 e teve {crescimento:.1%} de crescimento.')





