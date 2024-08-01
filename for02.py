#Temos uma lista com os vendedores e os valores de vendas e queremos identificar (printar) quais os vendedores que bateram a meta e qual foi o valor que eles venderam.


meta = 10000
vendas = [
    ['joão', 15000],
    ['julia', 27000],
    ['marcus', 9900],
    ['maria', 3750],
    ['ana', 10300],
    ['alon', 7870]
]


for item in vendas:
    if item[1] >= meta:
        print(f'Vendedor {item[0]} bateu a meta. Fez {item[1]} vendas.')
