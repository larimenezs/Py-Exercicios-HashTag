#Imagine que você trabalha no setor contábil de uma grande empresa.
#Crie uma function que calcule o % de carga tributária que está sendo aplicado sobre um determinado produto, dado o preço de venda, o "lucro" e os custos(com exceção do imposto) dele.
#Sua função deve calcular qual foi o % de imposto aplicado sobre o preço total.


def carga_tributaria(preço, custo, lucro):
    imposto = preço - custo - lucro
    carga = imposto / preço 
    return f'O produto incide {carga:.1%} de carga tributária.'


resultado = carga_tributaria(1500, 400, 800)
print(resultado)
