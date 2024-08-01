#Transforme as listas abaixo em um único dicionário.


produtos = ['computador', 'livro', 'tablet', 'celular', 'tv', 'ar condicionado', 
            'alexa', 'maquina de café', 'kindle']
vendas2019 = [215688, 324589, 845698, 978546, 245698, 654897, 789546, 458975, 145698]
vendas2020 = [325469, 265875, 987564, 758945, 225456, 758469, 358758, 845755, 132546]


vendas = list(zip(vendas2019, vendas2020))
dict_produtos = dict(zip(produtos, vendas))
print(dict_produtos)
