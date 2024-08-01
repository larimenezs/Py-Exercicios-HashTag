#O governo criou um novo imposto que incide em 10% sobre o valor dos livros e agora você precisa alterar o registros dos preços dos livros da empresa para garantir que esse imposto vai ser repassado para o preço final do produto.

#Crie um código que recalcule o valor do livro da sua lista de produtos e ajuste na tabela.
#Além disso, calcule qual vai ser o impacto financeiro da criação desse imposto para a empresa (ou seja, quanto que o imposto vai aumentar de custo para a empresa)


produtos = ['computador', 'livro', 'tablet', 'celular', 'tv', 'ar condicionado', 
            'alexa', 'maquina de café', 'kindle']


produtos_ecommerce = [
  [10000, 2500],
  [50000, 40],
  [7000, 1200],
  [20000, 1500],
  [5800, 1300],
  [7200, 2500],
  [200, 800],
  [3300, 700],
  [1900, 400]
]


if 'livro' in produtos:
    i_index = produtos.index('livro')
    total_antigo = produtos_ecommerce[i_index][0] * produtos_ecommerce[i_index][1]
    produtos_ecommerce[i_index][1] = produtos_ecommerce[i_index][1] * 1.1
    total_novo = produtos_ecommerce[i_index][0] * produtos_ecommerce[i_index][1]
    print(f'Vamos pagar de imposto a mais: R${total_novo - total_antigo}')
