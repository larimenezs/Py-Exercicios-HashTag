#Quem foi o vendedor que vendeu mais?


meta = 10000
melhor_vendedor = ''
maior_venda = 0
vendas = [
    ['joão', 15000],
    ['julia', 27000],
    ['marcus', 9900],
    ['maria', 3750],
    ['ana', 10300],
    ['alon', 7870]
]


for venda in vendas:
    if venda[1] > maior_venda:
        maior_venda = venda[1]
        melhor_vendedor = venda[0]
print(f'O vendedor que mais vendeu foi {melhor_vendedor} com {maior_venda} vendas.')