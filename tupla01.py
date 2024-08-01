#Qual foi o faturamento do iphone no dia 20/08/2020?
#Qual foi o produto mais vendido (em unidades) no dia 21/08/2020?


vendas = [
    ('20/08/2020', 'iphone x', 'azul', '128gb', 350, 4000),
    ('20/08/2020', 'iphone x', 'prata', '128gb', 1500, 4000),
    ('20/08/2020', 'ipad', 'prata', '256gb', 127, 6000),
    ('20/08/2020', 'ipad', 'prata', '128gb', 981, 5000),
    ('21/08/2020', 'iphone x', 'azul', '128gb', 397, 4000),
    ('21/08/2020', 'iphone x', 'prata', '128gb', 1017, 4000),
    ('21/08/2020', 'ipad', 'prata', '256gb', 50, 6000),
    ('21/08/2020', 'ipad', 'prata', '128gb', 4000, 5000),
]


produto_mais_vendido = ''
qnt_produto_mais_vendido = 0
faturamento = 0
for item in vendas:
    data, produto, cor, armazenamento, qnt_vendas, preço = item
    if produto == 'iphone x' and data == '20/08/2020':
        faturamento += qnt_vendas * preço
    if data == '21/08/2020':
        if qnt_vendas > qnt_produto_mais_vendido:
            produto_mais_vendido = produto
            qnt_produto_mais_vendido = qnt_vendas
print(f'O faturamento total de iphone no dia 20/08/2020 foi de R${faturamento}')
print(f'O produto mais vendido foi {produto_mais_vendido} com {qnt_produto_mais_vendido} vendas.')

