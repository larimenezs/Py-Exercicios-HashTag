#Digamos que a gente tenha uma lista de vendedores e ao invés de saber todos os vendedores que bateram a meta, eu quero conseguir calcular o % de vendedores que bateram a meta.


meta = 10000
qnt_bateram_meta = []
vendedor_mais_vendeu = ''
vendas = [
    ['joão', 15000],
    ['julia', 27000],
    ['marcus', 9900],
    ['maria', 3750],
    ['ana', 10300],
    ['alon', 7870]
]


for vendedor in vendas:
    if vendedor[1] >= meta:
        qnt_bateram_meta.append(vendedor)
print(qnt_bateram_meta)
porcentagem = len(qnt_bateram_meta) / len(vendas)
print(f'{porcentagem:.1%} dos vendedores bateram a meta.')

