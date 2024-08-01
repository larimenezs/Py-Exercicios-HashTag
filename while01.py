#Nosso programa deve registrar os produtos e as quantidades e adicionar em uma lista.
#O programa deve continuar rodando até o input estar vazio, ou seja, o usuário apertar "enter" sem digitar nenhum produto ou quantidade.


vendas = []
while True:
    produto = str(input('Digite o nome do produto: '))
    if not produto:
        break
    qnt = int(input(f'Qual a quantidade do produto: '))
    vendas.append([produto, qnt])
print(vendas)